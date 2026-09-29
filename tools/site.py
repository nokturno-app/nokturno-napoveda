#!/usr/bin/env python3
"""Složí zdroj webu nápovědy do `_src/` a vygeneruje `_mkdocs.yml` s menu.

    python3 tools/site.py                                    # web do site/
    python3 tools/site.py --serve                            # náhled (hledání jen s diakritikou)

Český web je v kořeni, slovenský pod `/sk/`, jazyk se přepíná v hlavičce.
Menu se nikde ručně nevede: bere se ze sekcí `## …` (`## Kodi › Funkce` = záložka Kodi) a odkazů `- [..](..md)` v rozcestnících
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

import build

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "_src"
LIST_RE = re.compile(r"^( *)([-*]|\d+\.) ")
LINK_RE = re.compile(r"^- \[(.+?)\]\((.+?\.md)\)")


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
# Návody, které se sloučily do článku nápovědy; stará adresa koluje v příspěvcích, proto přesměruje.
REDIRECTS = {"navody/kodi/vlastni-uloziste.md": "cs/vlastni-uloziste.md",
             "navody/kodi/hlidane.md": "cs/hlidane.md"}


def guide(d):
    """Stránky návodu v pořadí z `navody/<d>/_nav.md` (převzatý postranní panel bývalé wiki),
    jako [(popisek, cesta od kořene zdroje)]."""
    items = []
    for line in (ROOT / "navody" / d / "_nav.md").read_text(encoding="utf-8").splitlines():
        if m := LINK_RE.match(line):
            target = (ROOT / "navody" / d / m.group(2)).resolve()
            items.append((m.group(1), target.relative_to(ROOT).as_posix()))
    return items


def site_nav(index, lang):
    """Záložky webu ze sekcí rozcestníku (`## Kodi › Funkce`, bez záložky = Nápověda). Na konec
    záložky produktu přidá stránky návodu, které v rozcestníku nejsou. Slovenský web návody nemá,
    odkazuje na české s označením „(po česky)“."""
    home = "Nápověda" if lang == "cs" else "Nápoveda"
    tabs = {None: ["index.md"], **{name: [] for name in GUIDES.values()}}
    listed = set()
    for tab, section, items in build.menu(index):
        entries = []
        for label, link in items:
            path = (index.parent / link).resolve().relative_to(ROOT).as_posix()
            listed.add(path)
            entries.append({label: link})
        if entries:
            tabs[tab].append({section: entries})
    for d, name in GUIDES.items():
        rest = [(label, path) for label, path in guide(d) if path not in listed]
        if lang == "cs":
            rest = [{label: path} for label, path in rest]
            title = "Podrobné návody"
        else:
            rest = [{f"{label} (po česky)": KB + path[:-3] + ".html"}
                    for label, path in rest if path.startswith("navody/")]
            title = "Podrobné návody (po česky)"
        if rest:
            tabs[name].append({title: rest})
    return [{home: tabs.pop(None)}, *({name: items} for name, items in tabs.items() if items)]


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
    for old, new in REDIRECTS.items():
        url = pathlib.PurePosixPath(*[".."] * old.count("/"), new[:-3] + ".html")
        (cs / old).write_text(
            f'---\nsearch:\n  exclude: true\n---\n<meta http-equiv="refresh" content="0; url={url}">\n'
            f'<script>location.replace("{url}" + location.hash)</script>\n\n'
            f"Stránka se přesunula: [{new}](../../{new})\n", encoding="utf-8")
    # slovenské články leží v kořeni slovenského webu; odkazy na české návody míří do jiného webu,
    # MkDocs je nepřeloží, proto rovnou na .html
    copy_md(ROOT / "sk", sk, lambda t: NAVODY_MD.sub(r"\1.html", t))
    for docs, lang in ((cs, "cs"), (sk, "sk")):
        shutil.copytree(ROOT / "assets", docs / "assets")

    cs_cfg = config_for("cs", cs, site_nav(ROOT / "index.md", "cs"))
    sk_cfg = config_for("sk", sk, site_nav(ROOT / "sk" / "index.md", "sk"))
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
