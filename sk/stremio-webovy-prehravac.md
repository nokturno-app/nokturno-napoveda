---
slug: stremio-webovy-prehravac
lang: sk
title: „⚠️ Vo webovom prehrávači sa neprehrá“
products: [stremio]
priority: 2
templates:
  stremio: |
    Stream s riadkom „⚠️ Vo webovom prehrávači sa neprehrá“ (vlastné úložisko, FastShare) prehrá len aplikácia Stremio alebo Nuvio.
    Stremio v prehliadači (web.stremio.com) ho odmietne.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/stremio-webovy-prehravac
---

# „⚠️ Vo webovom prehrávači sa neprehrá“

## Čo to znamená
Streamy z **vlastného úložiska** a z **FastShare** potrebujú prihlásenie. Prehrávač si súbor sťahuje priamo
zo zdroja a prihlasovacie údaje posiela sám. To vie **aplikácia** Stremio (Android, Windows, Mac, Linux)
a **Nuvio**. Stremio v prehliadači to nevie a taký stream odmietne.

Doplnok nespozná, či pozeráš v prehliadači, preto má stream v popise riadok
**„⚠️ Vo webovom prehrávači sa neprehrá – len v aplikácii“** (pri niektorých adresách doplnku po česky
„⚠️ Ve webovém přehrávači se nepřehraje – jen v aplikaci“).

## Čo urobiť
- Spusti stream v aplikácii Stremio alebo Nuvio.
- V prehliadači vyber iný stream, napríklad z WebShare alebo HellSpy.

## Webový prehrávač neprehrá ani niektoré iné súbory
Súbory `.mkv`, `.avi` a podobné webový prehrávač často neprehrá ani z iných zdrojov. V aplikácii hrajú.

## Vlastné úložisko nehrá ani v aplikácii
Úložisko musí byť dosiahnuteľné zo servera doplnku (ten ho prechádza) **aj** zo zariadenia, kde prehrávaš.
Adresa len z domácej siete (`192.168.…`) nestačí. Pozri [Ako pripojiť vlastné úložisko](vlastni-uloziste.md).

---
[Všetky návody](./) · [Česky](../cs/stremio-webovy-prehravac)
