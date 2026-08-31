/**
 * AZSCO Assistant — server-side proxy for the Mistral API.
 *
 * The API key lives here, in the MISTRAL_API_KEY environment variable, and never
 * reaches the browser. The static site posts {lang, messages} to this endpoint.
 *
 * Deploy target: any host that runs a Node serverless function with the Web
 * Request/Response API (Vercel, Netlify Functions v2, Deno Deploy). A Cloudflare
 * Workers variant is in workers/chat-worker.js.
 *
 * Required environment variable:
 *   MISTRAL_API_KEY   your key from console.mistral.ai
 * Optional:
 *   MISTRAL_MODEL     defaults to mistral-small-latest
 *   ALLOWED_ORIGIN    comma-separated origins allowed to call this endpoint
 */

const MISTRAL_URL = 'https://api.mistral.ai/v1/chat/completions';
const MODEL = process.env.MISTRAL_MODEL || 'mistral-small-latest';

const MAX_CHARS = 1000;     // per message
const MAX_MESSAGES = 40;    // per request
const MAX_TOKENS = 500;     // per reply

/* What the assistant is allowed to say about AZSCO. Keeping the facts here,
   rather than relying on the model's own knowledge, is what stops it inventing
   services, prices or coverage. */
const FACTS = `
COMPANY
- AZSCO for Facility Guard Services (AZSCO), established 2008, headquartered in
  Qibla, Kuwait. Part of Almail Group.
- Office: Floor 27, Kuwait Building Tower, Fahad Al Salem St., Qibla, Kuwait.
- Telephone: (+965) 1808606. Email: info@azsco.com.
- Office hours: Sunday to Thursday, 8:00-17:00. Emergency response 24/7.

WHAT AZSCO DOES
AZSCO provides security manpower only. It does NOT sell, install or maintain
security systems (no fire alarm, intrusion, CCTV, access control or smart home
installation). Services:
- Manned Guarding: static security officers for apartments, malls, banks,
  stores, offices, compounds and industrial sites.
- Mobile Patrols: scheduled and random patrols, perimeter checks,
  lock-and-unlock, key holding, alarm response.
- Event & VIP Security: crowd management, access screening, stewarding,
  close protection.
- Reception & Concierge: front-of-house officers, visitor management,
  contractor and delivery control.
- Security Consulting: site surveys, risk assessments, post orders,
  deployment planning.
- Supervision & Reporting: field supervisors, shift audits, incident reporting.

OTHER FACTS
- Officers are screened, licensed, uniformed, trained and supervised.
- Technology partners: Ajax, Hikvision, Rasilient.
- Clients include Xcite, Millennium Hotels and Resorts, and Alnasser.
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
- ${arabic
      ? 'Reply in Arabic (Modern Standard Arabic), in a professional tone.'
      : 'Reply in English, in a professional tone.'}
- If a visitor appears to have an urgent security incident, tell them to call
  (+965) 1808606 immediately rather than continuing to chat.`;
}

function corsHeaders(origin) {
  const allowed = (process.env.ALLOWED_ORIGIN || '').split(',').map(s => s.trim()).filter(Boolean);
  const ok = !allowed.length || (origin && allowed.includes(origin));
  return {
    'Access-Control-Allow-Origin': ok ? (origin || '*') : 'null',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Content-Type': 'application/json',
  };
}

function json(body, status, origin) {
  return new Response(JSON.stringify(body), { status, headers: corsHeaders(origin) });
}

export default async function handler(request) {
  const origin = request.headers.get('origin');

  if (request.method === 'OPTIONS') {
    return new Response(null, { status: 204, headers: corsHeaders(origin) });
  }
  if (request.method !== 'POST') {
    return json({ error: 'Method not allowed' }, 405, origin);
  }
  if (!process.env.MISTRAL_API_KEY) {
    // Configuration problem, not the visitor's fault — do not leak details.
    console.error('MISTRAL_API_KEY is not set');
    return json({ error: 'Assistant unavailable' }, 503, origin);
  }

  let payload;
  try {
    payload = await request.json();
  } catch {
    return json({ error: 'Invalid JSON' }, 400, origin);
  }

  const lang = payload && payload.lang === 'ar' ? 'ar' : 'en';
  const incoming = Array.isArray(payload && payload.messages) ? payload.messages : [];
  if (!incoming.length) return json({ error: 'No messages' }, 400, origin);

  // Accept only the shape we expect; drop anything else the client sent.
  const messages = incoming
    .slice(-MAX_MESSAGES)
    .filter(m => m && (m.role === 'user' || m.role === 'assistant') && typeof m.content === 'string')
    .map(m => ({ role: m.role, content: m.content.slice(0, MAX_CHARS) }));

  if (!messages.length) return json({ error: 'No usable messages' }, 400, origin);

  try {
    const res = await fetch(MISTRAL_URL, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.MISTRAL_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: MODEL,
        temperature: 0.3,
        max_tokens: MAX_TOKENS,
        messages: [{ role: 'system', content: systemPrompt(lang) }, ...messages],
      }),
    });

    if (!res.ok) {
      const detail = await res.text();
      console.error('Mistral API error', res.status, detail.slice(0, 500));
      return json({ error: 'Assistant unavailable' }, 502, origin);
    }

    const data = await res.json();
    const reply = data?.choices?.[0]?.message?.content?.trim();
    if (!reply) return json({ error: 'Empty reply' }, 502, origin);

    return json({ reply }, 200, origin);
  } catch (err) {
    console.error('Proxy failure', err);
    return json({ error: 'Assistant unavailable' }, 502, origin);
  }
}

export const config = { runtime: 'edge' };
