---
slug: kde-hledat-pomoc
lang: cs
title: Kde hledat pomoc
products: [kodi, ha, stremio]
priority: 1
templates:
  kodi: |
    Ahoj, Nokturno má vlastní Discord server: discord.gg/ChmMPmDDEj
    Dotazy piš do fóra #pomoc, novinky a vydání najdeš v #novinky.
    Nápověda k nejčastějším problémům: https://nokturno-app.github.io/nokturno-napoveda
    Tým Nokturno
  stremio: |
    Něco nefunguje? Nápověda k nejčastějším problémům je na odkazu.
    Na dotazy odpovídáme na Discordu: discord.gg/ChmMPmDDEj
---

# Kde hledat pomoc

## 1. Zkus to vyřešit na místě
- **Kodi:** když je úplně nahoře v hlavním menu řádek se jménem zdroje (například „Luna: server neodpovídá“), klikni na něj.
  Ukáže, který zdroj nefunguje a proč, a každý řádek vede tam, kde se to opravuje.
  Viz [Nahoře v menu je řádek se zdrojem](stav-zdroju.md).
- **Kodi:** **Nokturno → Nastavení → Pokročilé → Ověřit zdroje** (ve starších verzích **Otestovat zdroje**) ověří všechny zapnuté zdroje najednou.
- **Stremio:** v nastavení doplňku dej u každého zdroje **Ověřit účet**.
- **Home Assistant:** senzor **Stav zdrojů** ukáže počet zdrojů, které potřebují zásah.

## 2. Najdi svůj problém v nápovědě
Návody jsou seřazené podle toho, co vidíš na obrazovce: [všechny návody](../).

## 3. Zeptej se nás
- **Discord server Nokturno:** [discord.gg/ChmMPmDDEj](https://discord.gg/ChmMPmDDEj) – hlavní místo pro dotazy
  a hlášení problémů (fórum #pomoc), novinky v #novinky.
  Viz [Discord server Nokturno](discord.md).
- Fórum pro Kodi: vlákno Nokturno na [xbmc-kodi.cz](https://www.xbmc-kodi.cz/prispevek-nokturno-webshare-sosac-hellspy-sledujteto-a-vlastni-uloziste-%E2%80%93-kodi-i-stremio).
- Fórum pro Stremio: [stremio.cz/d/240](https://stremio.cz/d/240).

Napiš, na čem Nokturno používáš (Kodi, Stremio, Home Assistant, jaké zařízení), co přesně se stalo a jakou hlášku vidíš.

**U Kodi nám pomůže log.** Pošli ho z doplňku a do zprávy napiš ID instalace, viz
[Jak poslat log a zjistit ID instalace](poslat-log.md). Odpověď pak můžeme poslat přímo do tvého Kodi.

## 4. Chyba v kódu doplňku
Když víš, že jde o chybu v programu (například doplněk spadne a vždy stejně), můžeš ji nahlásit na GitHubu:
[Kodi](https://github.com/nokturno-app/plugin.video.nokturno/issues) ·
[Home Assistant](https://github.com/nokturno-app/nokturno-ha/issues).
Na dotazy k nastavení a zdrojům tam neodpovídáme, na ty je Discord.

Neočekávané chyby v kódu doplněk pro Kodi hlásí sám (lze vypnout v **Nastavení → Statistiky → Posílat hlášení o chybách**).

---
[Všechny návody](../) · [Slovensky](../sk/kde-hledat-pomoc)
