---
slug: stara-adresa-repozitare
lang: sk
title: Kodi hlási chybu pri starej adrese Nokturna
products: [kodi]
priority: 2
templates:
  kodi: |
    Ahoj, v Správcovi súborov máš starú adresu Nokturna nokturno.tailf0014.ts.net. Od septembra 2026 nefunguje a Kodi pri nej hlási chybu.
    1. Nastavenia → Správca súborov, na zdroji so starou adresou podrž OK a zvoľ Odstrániť zdroj.
    2. Aktualizácie doplnku od tej adresy nezávisia, chodia z GitHubu ďalej.
    3. Na novú inštaláciu slúži adresa https://nokturno.stream/repo/
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/stara-adresa-repozitare
    Tím Nokturno
---

# Kodi hlási chybu pri starej adrese Nokturna

## Čo to znamená
V **Správcovi súborov** Kodi máš zdroj s adresou `https://nokturno.tailf0014.ts.net/repo/`. Táto adresa od septembra 2026
nefunguje. Kodi pri nej pri prechádzaní hlási, že sa nemôže pripojiť.

## Čo urobiť
1. **Nastavenia → Správca súborov**, na zdroji so starou adresou podrž OK (alebo pravé tlačidlo) a zvoľ **Odstrániť zdroj**.
2. Keď zdroj ešte potrebuješ na inštaláciu na ďalšom zariadení, pridaj novú adresu:
   `https://nokturno.stream/repo/`. Návod: [Ako nainštalovať Nokturno do Kodi](instalace-kodi.md).

## Prídem o aktualizácie?
Nie. Adresa v Správcovi súborov slúži len na prvú inštaláciu repozitára. Nainštalovaný **Nokturno repozitár**
berie aktualizácie z GitHubu a od tejto adresy nezávisí.

Verzie doplnku **staršie ako 7.9.3** ale starú adresu používajú aj pre server Nokturna (rebríčky, katalógy,
synchronizácia, správy). Aktualizuj, pozri [Ako zistiť verziu a aktualizovať](aktualizace.md).

---
[Všetky návody](./) · [Česky](../cs/stara-adresa-repozitare)
