---
slug: stahovani
lang: cs
title: Stahování selhalo
products: [kodi, ha]
priority: 2
templates:
  kodi: |
    Ahoj, stahování se nepovedlo.
    1. Aktualizuj Nokturno na nejnovější verzi, starší verze některé zdroje a síťové složky stahovat neuměly.
    2. Nokturno → Nastavení → Přehrávání → Stahování: Složka pro stahování musí být zapisovatelná, třeba USB disk nebo síťová složka.
    3. V menu Stažené dej u položky Zkusit znovu. Přerušené stahování naváže, kde skončilo.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/stahovani
    Tým Nokturno
---

# Stahování selhalo

## Kodi
Stáhnout jde z kontextového menu titulu (**Stáhnout**): otevře se výběr streamu a vybraný stream jde do fronty.
Hotová a rozstahovaná videa jsou v menu **Stažené**.

### „Nejdřív nastav složku pro stahování v nastavení.“
**Nokturno → Nastavení → Přehrávání → Stahování → Složka pro stahování.** Bez ní se stahovat nedá a položka
**Stažené** v menu není.

### „Stahování selhalo: …“
1. **Aktualizuj Nokturno.** Starší verze nestahovaly z CZtoru (do 6.0.3), z Přehraj.to (do 7.0.3)
   a do síťové složky (do 7.9.6).
2. **Zkontroluj složku.** Musí být zapisovatelná a musí na ní být místo. Na televizích bez vlastního úložiště
   použij USB disk nebo síťovou složku (`smb://…`).
3. **Zkontroluj zdroj.** Stahování potřebuje stejný účet jako přehrávání (Premium, VIP, kredit).
   Viz [Premium, VIP a kredit](premium-a-kredit.md).
4. V menu **Stažené** dej u položky **Zkusit znovu**.

### Stahování se přerušilo
Po výpadku sítě, restartu Kodi nebo vypnutí boxu stahování **naváže tam, kde skončilo** (u nedokončené položky
**Zkusit znovu**). Do síťové složky se nenavazuje, začne znovu.

Hotové stahování jde v kontextovém menu **Smazat** (smaže soubor z disku).

## Home Assistant
Integrace stahuje do **Složky pro stahování** ze sekce **Stahování a odkazy**. Složka musí na disku Home Assistantu
existovat a být zapisovatelná. Oznámení o dokončení chodí do služby `notify.`
z pole **Oznámení o stažení a nových dílech**. Prázdné pole pošle oznámení jen do Home Assistantu.

---
[Všechny návody](../) · [Slovensky](../sk/stahovani)
