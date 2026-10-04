---
slug: prihlaseni
lang: sk
title: "Zdroj hlási „nesedí meno alebo heslo“"
products: [kodi, ha, stremio]
priority: 1
when: {webshare: [bad_login], fastshare: [bad_login], sledujteto: [bad_login], prehrajto: [bad_login], storage: [bad_login]}
templates:
  kodi: |
    Ahoj, {zdroj} odmieta prihlásenie: nesedí meno alebo heslo.
    1. Prihlás sa rovnakými údajmi na webe zdroja. Keď to nejde ani tam, obnov si heslo na webe.
    2. Nokturno → Nastavenia → Zdroje a účty, v skupine {zdroj} vyplň meno a heslo znova (bez medzery na konci).
    3. Potom daj Nastavenia → Pokročilé → Overiť zdroje (v starších verziách Otestovať zdroje).
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/prihlaseni
    Tím Nokturno
---

# Zdroj hlási „nesedí meno alebo heslo“

## Čo to znamená
Zdroj odmietol meno alebo heslo, ktoré má Nokturno uložené. Hlásenie sa zobrazí:
- hore v menu a vo výpise **Stav zdrojov**: „<zdroj>: nesedí meno alebo heslo“ (v menu skrátene „nesedí prihlásenie“),
- v **Overiť zdroje** alebo pri prehrávaní: „<zdroj>: přihlášení se nepovedlo…“ (zatiaľ po česky), pri WebShare
  anglicky zo servera (napríklad „login: …“).

Pri Sledujteto, Přehraj.to a FastShare / Sdilej.cz Nokturno po odmietnutom prihlásení zdroj s rovnakými údajmi
**hodinu neskúša**, aby účet nezablokoval. Keď heslo opravíš, skúsi ho hneď.

## Čo urobiť
1. **Over údaje na webe zdroja.** Pri vlastnom úložisku sa prihlás priamo k NAS alebo Nextcloudu. Pri zdrojoch tretích
   strán sa prihlás na webe (webshare.cz, sledujteto.cz, fastshare.cz alebo sdilej.cz,
   prehraj.to) rovnakým menom a heslom. Keď nejde ani tam, obnov si heslo na webe.
2. **Vyplň ich v Nokturne znova.**
   - **Kodi:** vlastné úložisko v **Nokturno → Nastavenia → Vlastné úložisko**, zdroje tretích strán
     v **Nokturno → Nastavenia → Zdroje a účty**, skupina zdroja. Pozor na medzeru na konci
     a na veľké písmená. Pohodlnejšie to ide z mobilu: **Nastaviť z mobilu a prenos → Nastaviť z mobilu**.
   - **Stremio:** v nastavení doplnku (ozubené koliesko pri Nokturne v Stremiu) oprav údaje, daj **Overiť účet**
     a ulož zmeny. S profilom platia hneď. V starom režime bez profilov je zmenené nastavenie nová adresa:
     doplnok pridaj znova a starý v Stremiu odinštaluj.
   - **Home Assistant:** **Nastavenia → Zariadenia a služby → Nokturno → Konfigurovať**, krok **Vlastné úložisko**
     alebo **Zdroje a účty**.
     Formulár hlási chybu prihlásenia.
3. **Over.** V Kodi **Nastavenia → Pokročilé → Overiť zdroje** (v starších verziách **Otestovať zdroje**),
   v Stremiu **Overiť účet**.

## Tipy k jednotlivým zdrojom
- **Vlastné úložisko:** meno a heslo sú k tvojmu úložisku, nie k Nokturnu.
- **WebShare:** namiesto hesla sa dá vložiť aj 40-znakový „salted hash“, Nokturno ho spozná samo.
- **FastShare / Sdilej.cz:** účty sú oddelené. Kto má účet na Sdilej.cz, zvolí v Kodi pri FastShare
  **Účet z: Sdilej.cz** (v Stremiu a HA rovnaká voľba).
- **Sosáč** sa prihlasuje účtom **Streamuj.tv**, nie WebShare. Streamuj prihlásenie dopredu neoverí,
  zlé heslo sa spozná až pri prehrávaní.
- **CZtor** heslo nechce vôbec, zariadenie sa páruje PIN kódom, pozri [CZtor](cztor.md).

---
[Všetky návody](./) · [Česky](../cs/prihlaseni)
