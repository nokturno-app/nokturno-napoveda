#!/usr/bin/env python3
"""Složí zdroj webu nápovědy do `_src/` a vygeneruje `_mkdocs.yml` s menu.

    python3 tools/site.py                                    # web do site/
    python3 tools/site.py --serve                            # náhled (hledání jen s diakritikou)

Český web je v kořeni, slovenský pod `/sk/`, jazyk se přepíná v hlavičce.
Menu se nikde ručně nevede: bere se ze sekcí `## …` a odkazů `- [..](..md)` v rozcestnících
(`index.md` česky, `sk/index.md` slovensky). Články zůstávají v `cs/` a `sk/` (čte je i Eliška), návody k doplňkům
(bývalá wiki na GitHubu) v `navody/<kodi|ha|stremio>/`, jejich menu v `_nav.md`.
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys
import unicodedata

import hashlib
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "_src"
LIST_RE = re.compile(r"^( *)([-*]|\d+\.) ")
LINK_RE = re.compile(r"^- \[(.+?)\]\((.+?\.md)\)")


def sections(index, prefix):
    nav, current = [], None
    for line in index.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            current = []
            nav.append({line[3:].strip(): current})
        elif current is not None and (m := LINK_RE.match(line)):
            current.append({m.group(1): prefix + m.group(2).split("/")[-1]})
    return nav


def fix_lists(text):
    """Seznamy psané pro Jekyll (kramdown) převede na Python-Markdown: prázdný řádek před
    seznamem hned za odstavcem a vnořené odrážky odsazené o 4 mezery místo 2–3."""
    out, prev = [], ""
    for line in text.splitlines():
        m = LIST_RE.match(line)
        if m:
            if 0 < len(m.group(1)) < 4:
                line = "    " + line.lstrip(" ")
            elif not m.group(1) and prev.strip() and not LIST_RE.match(prev) \
                    and not prev.startswith(("#", "---", ">")) and not prev.startswith(" "):
                out.append("")
        out.append(line)
        prev = line
    return "\n".join(out) + "\n"


def fold(text):
    return "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))


def fold_search_index(path):
    """Hledání bez diakritiky: ke každé stránce do indexu přidá její text bez háčků a čárek
    („hlidane“ najde „Hlídané“). Dotaz s diakritikou dál míří na původní text."""
    index = json.loads(path.read_text(encoding="utf-8"))
    for doc in index["docs"]:
        extra = fold(doc["title"] + " " + doc["text"])
        if extra != doc["title"] + " " + doc["text"]:
            doc["text"] += " " + extra
    path.write_text(json.dumps(index, ensure_ascii=False), encoding="utf-8")


GUIDES = {"kodi": "Kodi", "ha": "Home Assistant", "stremio": "Stremio"}


def guide(d):
    """Menu návodu z `navody/<d>/_nav.md` (převzatý postranní panel bývalé wiki)."""
    items = []
    for line in (ROOT / "navody" / d / "_nav.md").read_text(encoding="utf-8").splitlines():
        if m := LINK_RE.match(line):
            items.append({m.group(1): f"navody/{d}/{m.group(2)}"})
    return items


KB = "https://nokturno-app.github.io/nokturno-napoveda/"
PATICKA_CLANKU = re.compile(r"\n---\n\[Všet?(?:ky|chny) návody\]\([^)]*\) · \[[^\]]+\]\([^)]*\)\s*\Z")
NAVODY_MD = re.compile(r"(\]\(\.\./navody/[^)#\s]+)\.md")


def copy_md(src, dst, fix=lambda t: t):
    """Zkopíruje strom a Markdown cestou upraví (seznamy, případně odkazy)."""
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("_nav.md"))
    for md in dst.rglob("*.md"):
        text = PATICKA_CLANKU.sub("\n", md.read_text(encoding="utf-8"))  # jazyk a úvod řeší hlavička webu
        md.write_text(fix(fix_lists(text)), encoding="utf-8")


COPYRIGHT = {
    "cs": ('<a href="https://nokturno.stream/">nokturno.stream</a> · '
           '<a href="https://nokturno.stream/terms">Podmínky použití</a> · '
           '<a href="https://discord.gg/ChmMPmDDEj">Discord</a>'),
    "sk": ('<a href="https://nokturno.stream/?lang=sk">nokturno.stream</a> · '
           '<a href="https://nokturno.stream/terms">Podmienky použitia</a> · '
           '<a href="https://discord.gg/ChmMPmDDEj">Discord</a>'),
}


def config_for(lang, docs, nav):
    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    config["docs_dir"] = str(docs.relative_to(ROOT))
    config["nav"] = nav
    config["theme"]["language"] = lang
    config["extra"]["alternate"] = [
        {"name": "Česky", "link": KB, "lang": "cs"},
        {"name": "Slovensky", "link": KB + "sk/", "lang": "sk"},
    ]
    # otisk obsahu v adrese, jinak prohlížeč drží starou kopii ještě 10 minut po nasazení
    def v(p):
        return p + "?v=" + hashlib.sha1((ROOT / p).read_bytes()).hexdigest()[:8]
    config["extra_css"] = [v(p) for p in config["extra_css"]]
    config["extra_javascript"] = [v("assets/jazyk.js")]
    config["copyright"] = COPYRIGHT[lang]
    config["extra"]["generator"] = False
    if lang == "sk":
        config["site_name"] = "Nokturno – nápoveda"
        config["site_url"] = KB + "sk/"
    path = ROOT / f"_mkdocs.{lang}.yml"
    path.write_text(yaml.safe_dump(config, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return path


def main():
    """Dva weby: český v kořeni (nápověda + návody k doplňkům) a slovenský pod /sk/.
    Jazyk se přepíná v hlavičce, záložky jsou podle obsahu."""
    shutil.rmtree(SRC, ignore_errors=True)
    cs, sk = SRC / "cs", SRC / "sk"
    copy_md(ROOT / "cs", cs / "cs")
    copy_md(ROOT / "navody", cs / "navody")
    # rozcestník /cs/ je teď hlavní stránka; stará adresa koluje v příspěvcích, proto jen přesměruje
    (cs / "cs" / "index.md").write_text(
        '---\nsearch:\n  exclude: true\n---\n<meta http-equiv="refresh" content="0; url=../">\n\n'
        "[Nápověda Nokturna](../index.md)\n", encoding="utf-8")
    shutil.copy(ROOT / "index.md", cs / "index.md")
    (cs / "index.md").write_text(fix_lists((cs / "index.md").read_text(encoding="utf-8")), encoding="utf-8")
    shutil.copy(ROOT / "templates.json", cs / "templates.json")
    # slovenské články leží v kořeni slovenského webu; odkazy na české návody míří do jiného webu,
    # MkDocs je nepřeloží, proto rovnou na .html
    copy_md(ROOT / "sk", sk, lambda t: NAVODY_MD.sub(r"\1.html", t))
    for docs, lang in ((cs, "cs"), (sk, "sk")):
        shutil.copytree(ROOT / "assets", docs / "assets")

    cs_cfg = config_for("cs", cs, [
        {"Nápověda": ["index.md", *sections(ROOT / "index.md", "cs/")]},
        *({name: guide(d)} for d, name in GUIDES.items()),
    ])
    sk_cfg = config_for("sk", sk, [
        {"Nápoveda": ["index.md", *sections(ROOT / "sk" / "index.md", "")]},
        *({f"{name}": f"{KB}navody/{d}/"} for d, name in GUIDES.items()),
    ])
    return cs_cfg, sk_cfg


if __name__ == "__main__":
    cs_cfg, sk_cfg = main()
    if "--serve" in sys.argv:
        subprocess.run(["mkdocs", "serve", "-f", cs_cfg.name], cwd=ROOT, check=True)
    else:
        subprocess.run(["mkdocs", "build", "-q", "-f", cs_cfg.name, "-d", "site"], cwd=ROOT, check=True)
        subprocess.run(["mkdocs", "build", "-q", "-f", sk_cfg.name, "-d", "site/sk"], cwd=ROOT, check=True)
        for index in ("site", "site/sk"):
            fold_search_index(ROOT / index / "search" / "search_index.json")
