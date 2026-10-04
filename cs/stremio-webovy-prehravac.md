---
slug: stremio-webovy-prehravac
lang: cs
title: „⚠️ Ve webovém přehrávači se nepřehraje“
products: [stremio]
priority: 2
templates:
  stremio: |
    Od verze 9.6.1 řádek „⚠️ Ve webovém přehrávači se nepřehraje“ u streamů není. Když ho vidíš, máš starší aplikaci Nokturno, aktualizuj ji.
    Soubory z vlastního úložiště a FastShare teď přehrávači předává aplikace Nokturno.
    Stremio v prohlížeči (web.stremio.com) nepřehraje soubory .mkv, .avi a podobné, v aplikaci Stremio nebo Nuvio hrají.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/stremio-webovy-prehravac
---

# „⚠️ Ve webovém přehrávači se nepřehraje“

## Co to znamená
Od verze 9.6.1 tenhle řádek u streamů **není**. Soubory z **vlastního úložiště** a z **FastShare** (i Sdilej.cz)
teď přehrávači předává aplikace Nokturno, přihlášení do Stremia neodchází.

Když řádek u streamu pořád vidíš, máš **starší aplikaci** (do verze 9.6.0). Aplikace se aktualizuje sama,
nebo ji stáhni znovu, viz [Aplikace Nokturno](stremio-aplikace.md).

## Webový přehrávač a formát souboru
Stremio v prohlížeči (web.stremio.com) nepřehraje soubory `.mkv`, `.avi`, `.ts`, `.m2ts`, `.wmv` a `.flv`
(označí je, že nejsou pro web). V aplikaci Stremio nebo Nuvio hrají. O přehrání ve webovém přehrávači
tedy rozhoduje formát souboru, ne zdroj.

## Co udělat
- Pusť stream v aplikaci Stremio nebo Nuvio.
- V prohlížeči vyber jiný stream, třeba soubor `.mp4` z vlastního úložiště, nebo z volitelného zdroje (WebShare, HellSpy).

## Vlastní úložiště nehraje ani v aplikaci
Úložiště musí být dosažitelné ze zařízení, kde běží aplikace Nokturno (ta v něm hledá soubory a předává je přehrávači).
Přehrávač potřebuje dosáhnout jen na aplikaci. Když je aplikace doma, stačí adresa z domácí sítě (`192.168.…`).
Viz [Jak připojit vlastní úložiště](vlastni-uloziste.md).

---
[Všechny návody](../) · [Slovensky](../sk/stremio-webovy-prehravac)
