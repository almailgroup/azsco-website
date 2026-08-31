/**
 * AZSCO Assistant — Cloudflare Workers variant of api/chat.js.
 *
 * Deploy:
 *   npx wrangler deploy workers/chat-worker.js --name azsco-chat
 *   npx wrangler secret put MISTRAL_API_KEY --name azsco-chat
 *
 * Then point the site at it by setting CHAT_ENDPOINT in tools/build.py to the
 * worker URL (e.g. https://azsco-chat.<subdomain>.workers.dev) and rebuilding.
 *
 * The logic is identical to api/chat.js; only the way the environment is passed
 * differs — Workers hand it to fetch() rather than exposing process.env.
 */
import handler from '../api/chat.js';

export default {
  async fetch(request, env) {
    // Bridge Workers' env bindings onto the shape api/chat.js expects.
    globalThis.process = globalThis.process || {};
    globalThis.process.env = { ...(globalThis.process.env || {}), ...env };
    return handler(request);
  },
};
