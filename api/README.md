# AZSCO Assistant — API proxy

> Calling Mistral directly from the browser (`CHAT_MODE = "direct"`) turned out
> not to work reliably in production — Mistral's API does not support being
> called from an arbitrary website's browser (no CORS), so the widget opens
> but every reply fails. This proxy is the fix: it holds the key server-side
> and the browser talks to it instead, on a domain that can send the right
> headers. Deploy one of the functions below, then set `CHAT_MODE = "proxy"`
> and `CHAT_ENDPOINT` in `tools/build.py` and rebuild.

This proxy adds the API key server-side, so it never reaches the browser.

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

`workers/chat-worker.js` has no imports, so it can be deployed straight from
the dashboard with no CLI or Node install:

1. Sign up free at <https://dash.cloudflare.com/sign-up> if you don't have an
   account.
2. **Workers & Pages → Create → Create Worker.** Give it a name (e.g.
   `azsco-chat`) and deploy the default template.
3. **Edit code**, delete the placeholder, paste in the full contents of
   `workers/chat-worker.js`, then **Save and deploy**.
4. **Settings → Variables and Secrets → Add.** Add `MISTRAL_API_KEY` as a
   *secret* with your key from <https://console.mistral.ai>. Optionally add
   `ALLOWED_ORIGIN` as a plain variable set to
   `https://www.azsco.com,https://azsco.com`. Save and deploy again.
5. Copy the worker's URL from the top of its dashboard page (looks like
   `https://azsco-chat.<your-subdomain>.workers.dev`).
6. Set `CHAT_ENDPOINT` to that URL and `CHAT_MODE = "proxy"` in
   `tools/build.py`, then run `python3 tools/build.py`.

Prefer the command line instead:

```bash
npx wrangler deploy workers/chat-worker.js --name azsco-chat
npx wrangler secret put MISTRAL_API_KEY --name azsco-chat
```

Either way, keep this file's `FACTS` in sync by hand with `CHAT_FACTS` /
`CHAT_RULES` in `tools/build.py` and with `api/chat.js` whenever the business
facts change — a deployed worker cannot read the static site's source.

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
