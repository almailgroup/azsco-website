#!/usr/bin/env python3
"""Checks the generated site before it is published.

Run after tools/build.py. Exits non-zero on any problem, which is what stops
the build workflow from committing a broken page over a working one -- the CMS
lets people edit content without review, so this is the only gate between a
malformed product and the live site.

Checks:
  * every content/products/*.json parses and has the fields the build needs
  * every generated page's tags are balanced
  * every internal link and srcset candidate resolves to a file that exists
"""
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}
SKIP_DIRS = {".git", ".github", "node_modules", "content", "tools", "backend"}


class Balance(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errors = [], []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append(f"stray </{tag}>")
        elif self.stack[-1] != tag:
            self.errors.append(f"</{tag}> closes <{self.stack[-1]}>")
        else:
            self.stack.pop()


def check_products():
    """The CMS writes these files, so they are the least trusted input here."""
    problems = []
    directory = os.path.join(ROOT, "content", "products")
    if not os.path.isdir(directory):
        return problems
    slugs = {}
    for name in sorted(os.listdir(directory)):
        if not name.endswith(".json"):
            continue
        path = os.path.join(directory, name)
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        except ValueError as err:
            problems.append(f"{name}: not valid JSON ({err})")
            continue
        if not isinstance(data, dict):
            problems.append(f"{name}: expected an object at the top level")
            continue
        if not data.get("published", True):
            continue
        slug = data.get("slug") or os.path.splitext(name)[0]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            problems.append(f"{name}: slug {slug!r} must be lowercase letters, "
                            f"digits and single hyphens — it becomes the URL")
        if slug in slugs:
            problems.append(f"{name}: slug {slug!r} already used by {slugs[slug]}")
        slugs[slug] = name
        for field in ("name_en", "name_ar", "summary_en", "summary_ar"):
            if not str(data.get(field, "")).strip():
                problems.append(f"{name}: {field} is empty")
        for key in ("features", "specs"):
            if key in data and not isinstance(data[key], list):
                problems.append(f"{name}: {key} must be a list")
        image = data.get("image") or ""
        if image and not os.path.exists(os.path.join(ROOT, image.lstrip("/"))):
            problems.append(f"{name}: image {image} does not exist")
    return problems


def pages():
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if name.endswith(".html"):
                yield os.path.join(base, name)


def check_pages():
    problems = []
    count = 0
    for path in pages():
        count += 1
        rel = os.path.relpath(path, ROOT)
        with open(path, encoding="utf-8") as fh:
            html = fh.read()

        parser = Balance()
        parser.feed(html)
        for err in parser.errors[:3]:
            problems.append(f"{rel}: {err}")
        if parser.stack:
            problems.append(f"{rel}: unclosed {parser.stack[:3]}")

        urls = re.findall(r'(?:href|src)="([^"]+)"', html)
        for match in re.finditer(r'srcset="([^"]+)"', html):
            urls += [c.strip().split()[0] for c in match.group(1).split(",") if c.strip()]
        for url in urls:
            if url.startswith(("http", "mailto:", "tel:", "#", "data:", "//")):
                continue
            clean = url.split("#")[0].split("?")[0]
            if not clean:
                continue
            # root-relative resolves from the site root, otherwise from the page
            base_dir = ROOT if clean.startswith("/") else os.path.dirname(path)
            target = os.path.normpath(os.path.join(base_dir, clean.lstrip("/")))
            if os.path.isdir(target):
                target = os.path.join(target, "index.html")
            if not os.path.exists(target):
                problems.append(f"{rel}: broken link {url}")
    return count, problems


def main():
    product_problems = check_products()
    count, page_problems = check_pages()
    problems = product_problems + page_problems

    print(f"checked {len(os.listdir(os.path.join(ROOT, 'content', 'products')))} "
          f"product files and {count} pages")
    if not problems:
        print("OK — tags balanced, every link resolves, products valid")
        return 0
    print(f"\n{len(problems)} problem(s):")
    for problem in problems[:40]:
        print(f"  {problem}")
    if len(problems) > 40:
        print(f"  ... and {len(problems) - 40} more")
    return 1


if __name__ == "__main__":
    sys.exit(main())
