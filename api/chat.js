/**
 * AZSCO Assistant — server-side proxy for the Gemini API.
 *
 * The API key lives here, in the GEMINI_API_KEY environment variable, and never
 * reaches the browser. The static site posts {lang, messages} to this endpoint.
 *
 * Deploy target: any host that runs a Node serverless function with the Web
 * Request/Response API (Vercel, Netlify Functions v2, Deno Deploy). A Cloudflare
 * Workers variant is in workers/chat-worker.js.
 *
 * Required environment variable:
 *   GEMINI_API_KEY    your key from https://aistudio.google.com/apikey
 *                      (no payment method required for the free tier)
 * Optional:
 *   GEMINI_MODEL      defaults to gemini-2.5-flash
 *   ALLOWED_ORIGIN    comma-separated origins allowed to call this endpoint
 *
 * Why Gemini and not Mistral: Mistral's free tier rate-limits far too
 * aggressively for live visitor traffic (a single test message could exhaust
 * it). Google AI Studio's free tier is meant for exactly this kind of light,
 * ongoing production use -- see https://ai.google.dev/gemini-api/docs/models
 * for current rate limits if the model ever needs bumping to a newer one.
 */

const MODEL = process.env.GEMINI_MODEL || 'gemini-2.5-flash';
const GEMINI_URL = `https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent`;

const MAX_CHARS = 1000;     // per message
const MAX_MESSAGES = 40;    // per request
const MAX_TOKENS = 500;     // per reply

/* What the assistant is allowed to say about AZSCO. Keeping the facts here,
   rather than relying on the model's own knowledge, is what stops it inventing
   services, prices or coverage.

   This is a duplicate of CHAT_FACTS / CHAT_RULES in tools/build.py (which
   feeds the "direct" mode config at assets/js/chat-config.js) and of
   workers/chat-worker.js — the three must be kept in sync by hand whenever
   the business facts change, since a static site has no way to share this at
   build time with an edge function deployed separately. */
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
  if (!process.env.GEMINI_API_KEY) {
    // Configuration problem, not the visitor's fault — do not leak details.
    console.error('GEMINI_API_KEY is not set');
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
  // Gemini uses "model" where the client (and Mistral's shape) says
  // "assistant" -- translate roles and wrap each turn's text in "parts".
  const contents = incoming
    .slice(-MAX_MESSAGES)
    .filter(m => m && (m.role === 'user' || m.role === 'assistant') && typeof m.content === 'string')
    .map(m => ({
      role: m.role === 'assistant' ? 'model' : 'user',
      parts: [{ text: m.content.slice(0, MAX_CHARS) }],
    }));

  if (!contents.length) return json({ error: 'No usable messages' }, 400, origin);

  try {
    const res = await fetch(GEMINI_URL, {
      method: 'POST',
      headers: {
        'x-goog-api-key': process.env.GEMINI_API_KEY,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        contents,
        systemInstruction: { parts: [{ text: systemPrompt(lang) }] },
        generationConfig: { temperature: 0.3, maxOutputTokens: MAX_TOKENS },
      }),
    });

    if (!res.ok) {
      const detail = await res.text();
      console.error('Gemini API error', res.status, detail.slice(0, 500));
      return json({ error: 'Assistant unavailable' }, 502, origin);
    }

    const data = await res.json();
    const reply = data?.candidates?.[0]?.content?.parts?.map(p => p.text || '').join('').trim();
    if (!reply) return json({ error: 'Empty reply' }, 502, origin);

    return json({ reply }, 200, origin);
  } catch (err) {
    console.error('Proxy failure', err);
    return json({ error: 'Assistant unavailable' }, 502, origin);
  }
}

export const config = { runtime: 'edge' };
