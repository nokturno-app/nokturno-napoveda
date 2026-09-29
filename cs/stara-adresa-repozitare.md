---
slug: stara-adresa-repozitare
lang: cs
title: Kodi hlásí chybu u staré adresy Nokturna
products: [kodi]
priority: 2
templates:
  kodi: |
    Ahoj, ve Správci souborů máš starou adresu Nokturna nokturno.tailf0014.ts.net. Od září 2026 nefunguje a Kodi u ní hlásí chybu.
    1. Nastavení → Správce souborů, na zdroji se starou adresou podrž OK a zvol Odstranit zdroj.
    2. Aktualizace doplňku na té adrese nezávisí, chodí z GitHubu dál.
    3. Pro novou instalaci slouží adresa https://nokturno.stream/repo/
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/stara-adresa-repozitare
    Tým Nokturno
---

# Kodi hlásí chybu u staré adresy Nokturna

## Co to znamená
Ve **Správci souborů** Kodi máš zdroj s adresou `https://nokturno.tailf0014.ts.net/repo/`. Tato adresa od září 2026
nefunguje. Kodi u ní při procházení hlásí, že se nemůže připojit.

## Co udělat
1. **Nastavení → Správce souborů**, na zdroji se starou adresou podrž OK (nebo pravé tlačítko) a zvol **Odstranit zdroj**.
2. Když zdroj ještě potřebuješ pro instalaci na dalším zařízení, přidej novou adresu:
   `https://nokturno.stream/repo/`. Návod: [Jak nainstalovat Nokturno do Kodi](instalace-kodi.md).

## Přijdu o aktualizace?
Ne. Adresa ve Správci souborů slouží jen k první instalaci repozitáře. Nainstalovaný **Nokturno repozitář**
bere aktualizace z GitHubu a na této adrese nezávisí.

Verze doplňku **starší než 7.9.3** ale starou adresu používají i pro server Nokturna (žebříčky, katalogy,
synchronizace, zprávy). Aktualizuj, viz [Jak zjistit verzi a aktualizovat](aktualizace.md).

---
[Všechny návody](../) · [Slovensky](../sk/stara-adresa-repozitare)
