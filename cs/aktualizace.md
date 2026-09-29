---
slug: aktualizace
lang: cs
title: Jak zjistit verzi a aktualizovat
products: [kodi, ha, stremio]
priority: 1
templates:
  kodi: |
    Ahoj, máš starší verzi Nokturna ({verze}). Nejnovější je {nejnovejsi}, opravuje řadu chyb.
    1. Nokturno → Nastavení → Pokročilé → Zkontrolovat aktualizace doplňků.
    2. Aby příště přišla aktualizace sama: v Kodi Nastavení → Systém → Doplňky → Aktualizace a zvol automatickou instalaci.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/aktualizace
    Tým Nokturno
---

# Jak zjistit verzi a aktualizovat

## Kodi

### Jakou verzi mám
**Nokturno → Nastavení → Pokročilé**, ve skupině **Když něco nefunguje** klikni na **Verze a ID této instalace**.
Nejnovější verze je vždy na [GitHubu](https://github.com/nokturno-app/plugin.video.nokturno/releases/latest).

### Aktualizovat hned
**Nokturno → Nastavení → Pokročilé → Zkontrolovat aktualizace doplňků.** Kodi zkontroluje repozitáře a novou
verzi nainstaluje. Jinak to dělá samo jednou denně.

### Aby aktualizace chodily samy
V Kodi otevři **Nastavení → Systém → Doplňky → Aktualizace** a zvol automatickou instalaci aktualizací.

### Aktualizace nechodí vůbec
- **Doplněk máš nainstalovaný ze zipu bez repozitáře.** Pak se neaktualizuje nikdy. Nainstaluj repozitář Nokturna
  podle [Jak nainstalovat Nokturno do Kodi](instalace-kodi.md). Nastavení zůstane.
- **Ve Správci souborů máš starou adresu** `nokturno.tailf0014.ts.net`. Ta od září 2026 nefunguje, zdroj smaž.
  Aktualizace ale chodí z GitHubu a na této adrese nezávisí.
- **Verze starší než 7.9.3** neznají novou adresu serveru Nokturna. Nefungují v nich žebříčky, katalogy,
  synchronizace ani zprávy od nás. Aktualizace doplňku přitom chodí dál, stačí ji spustit.

## Home Assistant
HACS kontroluje nové verze jen jednou za 48 hodin. Když novou verzi nevidíš:
1. **HACS → Nokturno → tři tečky → Update information.**
2. **Aktualizovat**, pak restartuj Home Assistant.
3. V mobilní aplikaci Home Assistant aplikaci úplně zavři a znovu otevři, ať se načte nová karta.

## Stremio
Aplikace Nokturno pro Stremio se aktualizuje sama, při startu a pak každých 6 hodin. Dělat nemusíš nic,
jen ji nech běžet. Verzi ukazuje stránka nastavení doplňku. Podrobnosti v článku
[Nokturno pro Stremio – aplikace](stremio-aplikace.md#aktualizace).

---
[Všechny návody](../) · [Slovensky](../sk/aktualizace)
