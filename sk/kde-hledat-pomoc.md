---
slug: kde-hledat-pomoc
lang: sk
title: Kde hľadať pomoc
products: [kodi, ha, stremio]
priority: 1
templates:
  kodi: |
    Ahoj, Nokturno má vlastný Discord server: discord.gg/ChmMPmDDEj
    Otázky píš do fóra #pomoc, novinky a vydania nájdeš v #novinky.
    Nápoveda k najčastejším problémom: https://nokturno-app.github.io/nokturno-napoveda/sk/
    Tím Nokturno
  stremio: |
    Niečo nefunguje? Nápoveda k najčastejším problémom je na odkaze.
    Na otázky odpovedáme na Discorde: discord.gg/ChmMPmDDEj
---

# Kde hľadať pomoc

## 1. Skús to vyriešiť na mieste
- **Kodi:** keď je úplne hore v hlavnom menu riadok s menom zdroja (napríklad „Luna: server neodpovedá“), klikni naň.
  Ukáže, ktorý zdroj nefunguje a prečo, a každý riadok vedie tam, kde sa to opravuje.
  Pozri [Hore v menu je riadok so zdrojom](stav-zdroju.md).
- **Kodi:** **Nokturno → Nastavenia → Pokročilé → Overiť zdroje** (v starších verziách **Otestovať zdroje**) overí
  všetky zapnuté zdroje naraz.
- **Stremio:** v nastavení doplnku daj pri každom zdroji **Overiť účet**.
- **Home Assistant:** senzor **Stav zdrojov** ukáže počet zdrojov, ktoré potrebujú zásah.

## 2. Nájdi svoj problém v nápovede
Návody sú zoradené podľa toho, čo vidíš na obrazovke: [všetky návody](./).

## 3. Opýtaj sa nás
- **Discord server Nokturno:** [discord.gg/ChmMPmDDEj](https://discord.gg/ChmMPmDDEj) – hlavné miesto na otázky
  a hlásenie problémov (fórum #pomoc), novinky v #novinky.
  Pozri [Discord server Nokturno](discord.md).
- Fórum pre Kodi: vlákno Nokturno na [xbmc-kodi.cz](https://www.xbmc-kodi.cz/prispevek-nokturno-webshare-sosac-hellspy-sledujteto-a-vlastni-uloziste-%E2%80%93-kodi-i-stremio).
- Fórum pre Stremio: [stremio.cz/d/240](https://stremio.cz/d/240).

Napíš, na čom Nokturno používaš (Kodi, Stremio, Home Assistant, aké zariadenie), čo presne sa stalo a aké hlásenie vidíš.

**Pri Kodi nám pomôže log.** Pošli ho z doplnku a do správy napíš ID inštalácie, pozri
[Ako poslať log a zistiť ID inštalácie](poslat-log.md). Odpoveď potom môžeme poslať priamo do tvojho Kodi.

## 4. Chyba v kóde doplnku
Keď vieš, že ide o chybu v programe (napríklad doplnok spadne a vždy rovnako), môžeš ju nahlásiť na GitHube:
[Kodi](https://github.com/nokturno-app/plugin.video.nokturno/issues) ·
[Home Assistant](https://github.com/nokturno-app/nokturno-ha/issues).
Na otázky k nastaveniu a zdrojom tam neodpovedáme, na tie je Discord.

Neočakávané chyby v kóde doplnok pre Kodi hlási sám (dá sa vypnúť v **Nastavenia → Štatistiky → Posielať hlásenia o chybách**).

---
[Všetky návody](./) · [Česky](../cs/kde-hledat-pomoc)
