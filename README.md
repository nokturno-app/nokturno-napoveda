# Nokturno – nápověda

Nápověda k Nokturnu pro Kodi, Home Assistant a Stremio, česky a slovensky.

**Čti ji tady:** https://nokturno-app.github.io/nokturno-napoveda/ · slovensky https://nokturno-app.github.io/nokturno-napoveda/sk/

Nokturno je přehrávač a vyhledávač nad tvým vlastním úložištěm (WebDAV, NAS) i úložišti třetích stran. Samo žádný
obsah nehostuje a za to, co přehráváš, odpovídáš ty.

## Pro autory
- Článek: `cs/<slug>.md` a `sk/<slug>.md` se stejným slugem. Slug se nikdy nemění.
- Šablony odpovědí pro dashboard jsou v hlavičce článku (`templates:`). Po změně spusť `python3 tools/build.py`
  a commitni i `templates.json`. CI pouští `python3 tools/build.py --check`.
- Web staví MkDocs Material (`mkdocs.yml`, `tools/site.py`), menu se bere ze sekcí rozcestníků `index.md`
  a `sk/index.md`. Nový článek tedy stačí přidat do rozcestníku. Náhled: `pip install "mkdocs<2" mkdocs-material`,
  pak `python3 tools/site.py --serve`. Nasazuje workflow `pages.yml` po každém pushi do `main`.
- Styl: tykání, za autora množné číslo, cesty v menu přesně podle aktuálního doplňku.
