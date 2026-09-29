---
slug: poslat-log
lang: sk
title: Ako poslať log a zistiť ID inštalácie
products: [kodi]
priority: 1
templates:
  kodi: |
    Ahoj, ďakujeme za log. Pozrieme sa naň a odpoveď ti pošleme sem do Kodi.
    Tím Nokturno
---

# Ako poslať log a zistiť ID inštalácie

Log je záznam toho, čo Kodi a Nokturno robili. Podľa neho väčšinou hneď spoznáme, kde je problém.
Týka sa doplnku pre Kodi.

## Poslať log
1. Zopakuj to, čo nefunguje (nech je chyba v logu čerstvá).
2. Otvor **Nokturno → Nastavenia → Pokročilé** a klikni na **Odoslať log Kodi**.
3. Potvrď „Naozaj odoslať log?“. Zobrazí sa „Log odoslaný“.

Keď overenie Luny skončí chybou, ponúkne tlačidlo **Poslať log** rovno v okne.

Čo sa posiela: posledných zhruba 500 kB súboru `kodi.log`. Heslá, tokeny, e-maily a IP adresy doplnok
pred odoslaním vymaže. Log sa dá poslať aj s vypnutými štatistikami.

## Zistiť ID inštalácie
**Nokturno → Nastavenia → Pokročilé**, v skupine **Keď niečo nefunguje** klikni na **Verzia a ID tejto inštalácie**.
ID je náhodný kód, ktorý nič neprezradí o tebe ani o zariadení. Podľa neho ale nájdeme tvoj log a môžeme
ti poslať odpoveď priamo do Kodi.

## Čo ďalej
Napíš nám na [Discord](https://discord.gg/ChmMPmDDEj) do fóra #pomoc alebo na fórum,
čo nefunguje, kedy bol log odoslaný a ID inštalácie. Pozri [Kde hľadať pomoc](kde-hledat-pomoc.md).

Odpoveď príde do Kodi ako okno so správou. Zobrazí sa, keď sa doplnok nabudúce spojí so serverom Nokturna
(najneskôr do niekoľkých hodín) a keď práve nič neprehrávaš.

Správy dostanú len verzie 7.9.3 a novšie. Staršie verzie nepoznajú novú adresu servera, najprv
[aktualizuj](aktualizace.md).

---
[Všetky návody](./) · [Česky](../cs/poslat-log)
