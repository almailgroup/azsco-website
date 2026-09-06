/**
 * AZSCO Assistant — Cloudflare Workers proxy for the Mistral API.
 *
 * Self-contained on purpose: this file has no imports, so it can be pasted
 * directly into the Cloudflare dashboard's Worker editor (Workers & Pages ->
 * Create -> Create Worker -> Edit code), with no CLI, build step or account
 * beyond a free Cloudflare sign-up. It is a Workers-native rewrite of
 * api/chat.js (same logic, "env" instead of "process.env") for anyone who
 * prefers deploying with Wrangler instead:
 *
 *   npx wrangler deploy workers/chat-worker.js --name azsco-chat
 *   npx wrangler secret put MISTRAL_API_KEY --name azsco-chat
 *
 * Either way, once deployed:
 *   1. Add the MISTRAL_API_KEY secret (Settings -> Variables and Secrets in
 *      the dashboard, or the wrangler command above).
 *   2. Optionally add ALLOWED_ORIGIN as a plain variable, e.g.
 *      "https://www.azsco.com,https://azsco.com" -- without it, any site can
 *      call this worker and spend your Mistral quota.
 *   3. Set CHAT_ENDPOINT in tools/build.py to this worker's URL (shown at
 *      the top of its dashboard page, e.g. https://azsco-chat.<subdomain>.workers.dev),
 *      set CHAT_MODE = "proxy", and run `python3 tools/build.py`.
 *
 * IMPORTANT: keep this file's FACTS in sync with CHAT_FACTS / CHAT_RULES in
 * tools/build.py (and with api/chat.js) by hand whenever the business facts
 * change -- a deployed worker has no way to read the static site's source at
 * build time.
 */

const MISTRAL_URL = 'https://api.mistral.ai/v1/chat/completions';

const MAX_CHARS = 1000;     // per message
const MAX_MESSAGES = 40;    // per request
const MAX_TOKENS = 500;     // per reply

const FACTS = `
COMPANY
- AZSCO Security Services Company (formerly Almail Zone Security Services),
  established 2014, headquartered in Qibla, Kuwait.
- Office: Floor 27B, Kuwait Building Tower, Fahad Al Salem St., Qibla, Kuwait.
- Telephone: (+965) 1808606.
- Email: info@azsco.com for general enquiries, sales@azsco.com for sales
  and quotations.
- Office hours: Sunday to Thursday, 8:00-17:00. Emergency response 24/7.
- CEO: Dr. Abdulaziz Almail.
- Certified ISO 9001:2015 for quality management, and compliant with
  Anti-Money Laundering standards.

WHAT AZSCO DOES
AZSCO provides security manpower only. It does NOT sell, install or maintain
security systems (no fire alarm, intrusion, CCTV or access control
installation). Services:
- Facility Guarding: trained, uniformed officers guarding apartments, malls,
  banks, stores, offices, compounds, industrial sites and events.
- VIP Protection & Rapid Intervention: physically and technically qualified
  personal guards for individuals needing a high level of security, plus
  rapid-intervention response to critical sites.
- Central Operations Room: a 24/7 monitoring and communications room that
  keeps continuous contact with every AZSCO-guarded site and dispatches a
  rapid response to any incident.
- Security Patrols: scheduled patrols by trained officers equipped with the
  necessary tools, reinforcing the security of guarded sites and areas.

OTHER FACTS
- Officers are screened, licensed, uniformed, trained (first aid,
  fire-fighting, dealing with the public, dealing with accidents,
  self-defense) and supervised.
- Officers come from a range of nationalities: Kuwaiti, Indian, Egyptian,
  Chadian, Nigerian, Nepalese and stateless individuals.
- Serves government, commercial, financial, industrial, residential and many
  other sectors across Kuwait.
- Technology partners whose equipment feeds AZSCO's Central Operations Room
  monitoring: Ajax, Rasilient, Avigilon, Teltonika, Inrico, Hikvision, Pelco
  and Motorola. AZSCO does not itself sell or install this equipment.
- Clients include Radisson Blu Hotel Kuwait, Alnasser, Millennium Hotels and
  Resorts, and Kuwait Ports Authority, among others.
- A free site survey is the normal first step for a new enquiry.
`;

function systemPrompt(lang) {
  const arabic = lang === 'ar';
  return `You are the AZSCO Assistant, the virtual assistant on the website of AZSCO,
a security manpower company in Kuwait.

${FACTS}

RULES
- Answer ONLY questions about AZSCO, its security manpower services, and how to
  get in touch. For anything else, politely say it is outside what you can help
  with and offer to put the visitor in touch with the team.
- Use ONLY the facts above. If you do not know something — pricing, guard
  numbers, availability, contract terms, staff names — say so plainly and point
  the visitor to (+965) 1808606 or info@azsco.com. Never guess or invent.
- AZSCO does not install or maintain security systems. If asked for CCTV, alarm
  or access control installation, say AZSCO provides security personnel and
  suggest contacting the team to discuss what they need.
- Never quote a price, promise a response time, or commit AZSCO to anything.
- Be brief: two or three short paragraphs at most. Plain text, no markdown
  headings or bullet lists.
- If a visitor appears to have an urgent security incident, tell them to call
  (+965) 1808606 immediately rather than continuing to chat.
- ${arabic
      ? 'Reply in Arabic (Modern Standard Arabic), in a professional tone.'
      : 'Reply in English, in a professional tone.'}`;
}

function corsHeaders(origin, env) {
  const allowed = (env.ALLOWED_ORIGIN || '').split(',').map(s => s.trim()).filter(Boolean);
  const ok = !allowed.length || (origin && allowed.includes(origin));
  return {
    'Access-Control-Allow-Origin': ok ? (origin || '*') : 'null',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Content-Type': 'application/json',
  };
}

function json(body, status, origin, env) {
  return new Response(JSON.stringify(body), { status, headers: corsHeaders(origin, env) });
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get('origin');

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: corsHeaders(origin, env) });
    }
    if (request.method !== 'POST') {
      return json({ error: 'Method not allowed' }, 405, origin, env);
    }
    if (!env.MISTRAL_API_KEY) {
      // Configuration problem, not the visitor's fault — do not leak details.
      console.error('MISTRAL_API_KEY is not set');
      return json({ error: 'Assistant unavailable' }, 503, origin, env);
    }

    let payload;
    try {
      payload = await request.json();
    } catch {
      return json({ error: 'Invalid JSON' }, 400, origin, env);
    }

    const lang = payload && payload.lang === 'ar' ? 'ar' : 'en';
    const incoming = Array.isArray(payload && payload.messages) ? payload.messages : [];
    if (!incoming.length) return json({ error: 'No messages' }, 400, origin, env);

    // Accept only the shape we expect; drop anything else the client sent.
    const messages = incoming
      .slice(-MAX_MESSAGES)
      .filter(m => m && (m.role === 'user' || m.role === 'assistant') && typeof m.content === 'string')
      .map(m => ({ role: m.role, content: m.content.slice(0, MAX_CHARS) }));

    if (!messages.length) return json({ error: 'No usable messages' }, 400, origin, env);

    try {
      const res = await fetch(MISTRAL_URL, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${env.MISTRAL_API_KEY}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: env.MISTRAL_MODEL || 'mistral-small-latest',
          temperature: 0.3,
          max_tokens: MAX_TOKENS,
          messages: [{ role: 'system', content: systemPrompt(lang) }, ...messages],
        }),
      });

      if (!res.ok) {
        const detail = await res.text();
        console.error('Mistral API error', res.status, detail.slice(0, 500));
        return json({ error: 'Assistant unavailable' }, 502, origin, env);
      }

      const data = await res.json();
      const reply = data?.choices?.[0]?.message?.content?.trim();
      if (!reply) return json({ error: 'Empty reply' }, 502, origin, env);

      return json({ reply }, 200, origin, env);
    } catch (err) {
      console.error('Proxy failure', err);
      return json({ error: 'Assistant unavailable' }, 502, origin, env);
    }
  },
};
