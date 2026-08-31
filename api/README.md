# AZSCO Assistant — API proxy

The chat widget in the website never holds the Mistral API key. It posts to this
proxy, which adds the key server-side. **Putting the key in the site's JavaScript
would publish it** — anyone could read it from the page source and spend against
your account.

## What to deploy

| File | For |
| --- | --- |
| `api/chat.js` | Vercel, Netlify Functions, Deno Deploy — anything running a Node/Edge function |
| `workers/chat-worker.js` | Cloudflare Workers |

## Environment variables

| Name | Required | Notes |
| --- | --- | --- |
| `MISTRAL_API_KEY` | yes | From <https://console.mistral.ai>. Set it as a secret, never in a file. |
| `MISTRAL_MODEL` | no | Defaults to `mistral-small-latest`. |
| `ALLOWED_ORIGIN` | recommended | Comma-separated origins, e.g. `https://www.azsco.com`. Without it any site can call your endpoint and spend your quota. |

## Deploying on Vercel

```bash
vercel deploy
vercel env add MISTRAL_API_KEY        # paste the key when prompted
vercel env add ALLOWED_ORIGIN         # https://www.azsco.com
```

The function is then served at `/api/chat`, which is the site's default endpoint —
no change needed in the site itself.

## Deploying on Cloudflare Workers

```bash
npx wrangler deploy workers/chat-worker.js --name azsco-chat
npx wrangler secret put MISTRAL_API_KEY
```

Then set `CHAT_ENDPOINT` in `tools/build.py` to the worker's URL and run
`python3 tools/build.py`.

## Checking it works

```bash
curl -X POST https://<your-deployment>/api/chat \
  -H 'Content-Type: application/json' \
  -d '{"lang":"en","messages":[{"role":"user","content":"What services do you offer?"}]}'
```

A healthy response is `{"reply":"..."}`. If you get `{"error":"Assistant unavailable"}`,
check the function logs — the proxy deliberately does not return API errors to the
browser, so that key or quota problems are not exposed to visitors.

## Limits enforced by the proxy

- 1000 characters per message, 40 messages per request, 500 tokens per reply.
- Only `user` and `assistant` roles are accepted from the browser; the system
  prompt is added server-side and cannot be overridden by a visitor.

These are a first line of defence, not rate limiting. For a public site, also put
your host's rate limiting or WAF in front of the endpoint.
