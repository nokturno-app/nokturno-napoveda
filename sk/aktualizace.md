---
slug: aktualizace
lang: sk
title: Ako zistiť verziu a aktualizovať
products: [kodi, ha, stremio]
priority: 1
templates:
  kodi: |
    Ahoj, máš staršiu verziu Nokturna ({verze}). Najnovšia je {nejnovejsi}, opravuje množstvo chýb.
    1. Nokturno → Nastavenia → Pokročilé → Skontrolovať aktualizácie doplnkov.
    2. Aby nabudúce prišla aktualizácia sama: v Kodi Nastavenia → Systém → Doplnky → Aktualizácie a zvoľ automatickú inštaláciu.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/aktualizace
    Tím Nokturno
---

# Ako zistiť verziu a aktualizovať

## Kodi

### Akú verziu mám
**Nokturno → Nastavenia → Pokročilé**, v skupine **Keď niečo nefunguje** klikni na **Verzia a ID tejto inštalácie**.
Najnovšia verzia je vždy na [GitHube](https://github.com/nokturno-app/plugin.video.nokturno/releases/latest).

### Aktualizovať hneď
**Nokturno → Nastavenia → Pokročilé → Skontrolovať aktualizácie doplnkov.** Kodi skontroluje repozitáre a novú
verziu nainštaluje. Inak to robí samo raz denne.

### Aby aktualizácie chodili samy
V Kodi otvor **Nastavenia → Systém → Doplnky → Aktualizácie** a zvoľ automatickú inštaláciu aktualizácií.

### Aktualizácie nechodia vôbec
- **Doplnok máš nainštalovaný zo zipu bez repozitára.** Potom sa neaktualizuje nikdy. Nainštaluj repozitár Nokturna
  podľa [Ako nainštalovať Nokturno do Kodi](instalace-kodi.md). Nastavenie zostane.
- **V Správcovi súborov máš starú adresu** `nokturno.tailf0014.ts.net`. Tá od septembra 2026 nefunguje, zdroj zmaž.
  Aktualizácie ale chodia z GitHubu a na tejto adrese nezávisia.
- **Verzie staršie ako 7.9.3** nepoznajú novú adresu servera Nokturna. Nefungujú v nich rebríčky, katalógy,
  synchronizácia ani správy od nás. Aktualizácia doplnku pritom chodí ďalej, stačí ju spustiť.

## Home Assistant
HACS kontroluje nové verzie len raz za 48 hodín. Keď novú verziu nevidíš:
1. **HACS → Nokturno → tri bodky → Update information.**
2. **Aktualizovať**, potom reštartuj Home Assistant.
3. V mobilnej aplikácii Home Assistant aplikáciu úplne zavri a znova otvor, nech sa načíta nová karta.

## Stremio
Aplikácia Nokturno pre Stremio sa aktualizuje sama, pri štarte a potom každých 6 hodín. Robiť nemusíš nič,
len ju nechaj bežať. Verziu ukazuje stránka nastavenia doplnku. Podrobnosti v článku
[Nokturno pre Stremio – aplikácia](stremio-aplikace.md#aktualizacie).

Doplnok s adresou `nokturno.stream` od 30. 9. 2026 nefunguje, pozri
[Stremio: doplnok z nokturno.stream nefunguje](stremio-stara-adresa.md).

---
[Všetky návody](./) · [Česky](../cs/aktualizace)
