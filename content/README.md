# Content

Everything in this folder is **data, not code**. It is the only part of the
site that is edited without touching Python, and it is what the content editor
at <https://azsco.com/admin/> writes to.

## How a product reaches the live site

```
  /admin/  ──commit──▶  content/products/<slug>.json
                              │
                   "Build site" workflow runs tools/build.py
                              │
                   tools/verify.py checks the result
                              │
              commits the regenerated HTML ──▶ GitHub Pages
```

A save takes a minute or two to appear. That delay is the cost of the pages
being static files rather than database queries — which is also why they load
as fast as they do and why Google indexes them properly.

If the workflow fails, **nothing is published**: the live site stays on its
last good version and the Actions tab shows what was wrong.

## products/

One JSON file per product. The filename is the slug, and the slug is the URL:
`surveillance-cameras.json` becomes `/products/surveillance-cameras/` and
`/ar/products/surveillance-cameras/`.

| Field | Required | Notes |
| --- | --- | --- |
| `slug` | yes | lowercase, digits, single hyphens. Changing it changes the URL. |
| `published` | — | `false` hides the product without deleting it |
| `order` | — | lower sorts first; default 50 |
| `category` | yes | one of the values in `PRODUCT_CATEGORIES` in `tools/build.py` |
| `brands` | — | list of strings, shown on the card |
| `image` | — | site-root path, e.g. `/assets/img/products/x.jpg` |
| `image_alt_en` / `_ar` | — | describes the photo for screen readers and search |
| `name_en` / `name_ar` | yes | |
| `summary_en` / `summary_ar` | yes | card text, and the search-result description |
| `description_en` / `description_ar` | — | the body of the product page |
| `features` | — | list of `{"en": "...", "ar": "..."}` |
| `specs` | — | list of `{"label_en","label_ar","value_en","value_ar"}` |
| `featured` | — | `true` lists the product before all others, whatever its order |
| `badge_en` / `_ar` | — | short label in the card's corner, e.g. New (24 chars max) |
| `model` | — | model or part number; always rendered left-to-right |
| `gallery` | — | list of `{"image","alt_en","alt_ar"}`; the first stands in as the main photo if `image` is empty |
| `datasheet` | — | path to a PDF under `/assets/docs/`; adds a download button |
| `applications` | — | list of `{"en","ar"}`, shown as tags under "Where it is used" |
| `faqs` | — | list of `{"q_en","q_ar","a_en","a_ar"}`, shown as an expandable list |
| `seo_title_en` / `_ar` | — | overrides the browser/search title; keep under ~60 chars |
| `seo_desc_en` / `_ar` | — | overrides the search description; keep under ~155 chars |

Arabic is not optional. A product with no Arabic falls back to English on the
Arabic site, which looks broken to half the audience.

## Adding a category

Categories live in `PRODUCT_CATEGORIES` in `tools/build.py`, because the site
has to know how to render one. Add it there and run `python3 tools/build.py`:
the dropdown in the content editor is **generated** from that list, so the two
cannot drift apart.
