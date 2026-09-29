---
slug: stremio-webovy-prehravac
lang: cs
title: „⚠️ Ve webovém přehrávači se nepřehraje“
products: [stremio]
priority: 2
templates:
  stremio: |
    Stream s řádkem „⚠️ Ve webovém přehrávači se nepřehraje“ (vlastní úložiště, FastShare) přehraje jen aplikace Stremio nebo Nuvio.
    Stremio v prohlížeči (web.stremio.com) ho odmítne.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/stremio-webovy-prehravac
---

# „⚠️ Ve webovém přehrávači se nepřehraje“

## Co to znamená
Streamy z **vlastního úložiště** a z **FastShare** potřebují přihlášení. Přehrávač si soubor stahuje přímo
ze zdroje a přihlašovací údaje posílá sám. To umí **aplikace** Stremio (Android, Windows, Mac, Linux)
a **Nuvio**. Stremio v prohlížeči to neumí a takový stream odmítne.

Doplněk nepozná, jestli se díváš v prohlížeči, proto má stream v popisu řádek
**„⚠️ Ve webovém přehrávači se nepřehraje – jen v aplikaci“**.

## Co udělat
- Pusť stream v aplikaci Stremio nebo Nuvio.
- V prohlížeči vyber jiný stream, třeba z WebShare nebo HellSpy.

## Webový přehrávač nepřehraje ani některé jiné soubory
Soubory `.mkv`, `.avi` a podobné webový přehrávač často nepřehraje ani z jiných zdrojů. V aplikaci hrají.

## Vlastní úložiště nehraje ani v aplikaci
Úložiště musí být dosažitelné ze zařízení, kde běží aplikace Nokturno (ta v něm hledá soubory), **i** ze zařízení,
kde přehráváš. Když je aplikace i přehrávač doma, stačí adresa z domácí sítě (`192.168.…`).
Viz [Jak připojit vlastní úložiště](vlastni-uloziste.md).

---
[Všechny návody](../) · [Slovensky](../sk/stremio-webovy-prehravac)
