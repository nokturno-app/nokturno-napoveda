#!/usr/bin/env python3
"""Z hlaviček článků (`cs/*.md`, `sk/*.md`) vygeneruje `templates.json` — šablony odpovědí pro dashboard.

    python3 tools/build.py           # zapíše templates.json
    python3 tools/build.py --check   # jen zkontroluje (limity, dvojice cs/sk, aktuálnost souboru)

Formát popisuje `kanon/sablony-format.md` v koordinační složce, stručně: jeden záznam na
(id, jazyk, produkt), text z `templates.<produkt>` v hlavičce článku.
"""
import json
import pathlib
import re
import sys
import time

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE_URL = "https://nokturno-app.github.io/nokturno-napoveda"
LANGS = ("cs", "sk")
PRODUCTS = ("kodi", "stremio", "ha")
LIMITS = {"kodi": 1200, "stremio": 600, "ha": 1200}
STREMIO_MAX_LINES = 5
VARS = {
    "verze": "verze doplňku u instalace (installs.version)",
    "nejnovejsi": "nejnovější stabilní verze Kodi (obrazovka Rodina)",
    "zdroj": "název zdroje, vyplní autor ručně",
}
VAR_RE = re.compile(r"\{([^{}]*)\}")


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    head = text[4:text.index("\n---", 4)]
    return yaml.safe_load(head) or {}


def build():
    errors, records, seen = [], [], {}
    for lang in LANGS:
        for path in sorted((ROOT / lang).glob("*.md")):
            if path.stem == "index":
                continue
            fm = front_matter(path)
            where = f"{lang}/{path.name}"
            if fm is None:
                errors.append(f"{where}: chybí hlavička")
                continue
            slug = fm.get("slug")
            if slug != path.stem:
                errors.append(f"{where}: slug {slug!r} nesedí s názvem souboru")
            if fm.get("lang") != lang:
                errors.append(f"{where}: lang {fm.get('lang')!r} nesedí se složkou")
            templates = fm.get("templates") or {}
            seen.setdefault(slug, {})[lang] = set(templates)
            for product, text in templates.items():
                if product not in PRODUCTS:
                    errors.append(f"{where}: neznámý produkt {product!r}")
                    continue
                text = (text or "").strip()
                if len(text) > LIMITS[product]:
                    errors.append(f"{where}: šablona {product} má {len(text)} znaků, limit {LIMITS[product]}")
                if product == "stremio" and len(text.splitlines()) > STREMIO_MAX_LINES:
                    errors.append(f"{where}: šablona stremio má víc než {STREMIO_MAX_LINES} řádků")
                for var in VAR_RE.findall(text):
                    if var not in VARS:
                        errors.append(f"{where}: neznámá proměnná {{{var}}} v šabloně {product}")
                records.append({
                    "id": slug,
                    "lang": lang,
                    "product": product,
                    "title": fm.get("title", slug),
                    "text": text,
                    "link": f"{BASE_URL}/{lang}/{slug}",
                    "when": fm.get("when") or {},
                    "priority": int(fm.get("priority", 3)),
                })
    for slug, by_lang in seen.items():
        if set(by_lang) != set(LANGS):
            errors.append(f"{slug}: chybí jazyk {sorted(set(LANGS) - set(by_lang))}")
        elif by_lang["cs"] != by_lang["sk"]:
            errors.append(f"{slug}: šablony cs {sorted(by_lang['cs'])} a sk {sorted(by_lang['sk'])} se liší")
    records.sort(key=lambda r: (r["priority"], r["id"], r["product"], r["lang"]))
    return errors, records


LINK_RE = re.compile(r"\]\(([^)\s#]+)(?:#[^)]*)?\)")


def broken_links():
    """Relativní odkazy mezi stránkami (`x.md`, `../sk/x`, `./`), které nikam nevedou."""
    errors = []
    for path in sorted(ROOT.glob("*.md")) + sorted(p for lang in LANGS for p in (ROOT / lang).glob("*.md")):
        if path.name == "README.md":
            continue
        for link in LINK_RE.findall(path.read_text(encoding="utf-8")):
            if re.match(r"[a-z]+:", link):
                continue
            target = (path.parent / link).resolve()
            ok = ((target / "index.md").exists() if link.endswith("/") or target.is_dir()
                  else target.exists() or target.with_suffix(".md").exists())
            if not ok:
                errors.append(f"{path.relative_to(ROOT)}: odkaz {link!r} nikam nevede")
    return errors


def main():
    check = "--check" in sys.argv[1:]
    errors, records = build()
    errors += broken_links()
    out = ROOT / "templates.json"
    data = {"version": 1, "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "base_url": BASE_URL, "vars": VARS, "templates": records}
    if check and out.exists():
        old = json.loads(out.read_text(encoding="utf-8"))
        old.pop("generated", None)
        new = dict(data)
        new.pop("generated")
        if old != new:
            errors.append("templates.json není aktuální — spusť python3 tools/build.py")
    for e in errors:
        print("CHYBA", e, file=sys.stderr)
    if errors:
        return 1
    if not check:
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"šablon: {len(records)}, článků: {len({r['id'] for r in records})}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
