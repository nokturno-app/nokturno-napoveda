---
slug: prihlaseni
lang: cs
title: "Zdroj hlásí „nesedí jméno nebo heslo“"
products: [kodi, ha, stremio]
priority: 1
when: {webshare: [bad_login], fastshare: [bad_login], sledujteto: [bad_login], prehrajto: [bad_login], storage: [bad_login]}
templates:
  kodi: |
    Ahoj, {zdroj} odmítá přihlášení: nesedí jméno nebo heslo.
    1. Přihlas se stejnými údaji na webu zdroje. Když to nejde ani tam, obnov si heslo na webu.
    2. Nokturno → Nastavení → Zdroje a účty, ve skupině {zdroj} vyplň jméno a heslo znovu (bez mezery na konci).
    3. Pak dej Nastavení → Pokročilé → Ověřit zdroje (ve starších verzích Otestovat zdroje).
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/prihlaseni
    Tým Nokturno
---

# Zdroj hlásí „nesedí jméno nebo heslo“

## Co to znamená
Zdroj odmítl jméno nebo heslo, které má Nokturno uložené. Hláška se ukáže:
- nahoře v menu a ve výpisu **Stav zdrojů**: „<zdroj>: nesedí jméno nebo heslo“ (v menu zkráceně „nesedí přihlášení“),
- v **Ověřit zdroje** nebo při přehrání: „<zdroj>: přihlášení se nepovedlo…“, u WebShare anglicky od serveru (například „login: …“).

U Sledujteto, Přehraj.to a FastShare / Sdilej.cz Nokturno po odmítnutém přihlášení zdroj se stejnými údaji
**hodinu nezkouší**, aby účet nezablokoval. Když heslo opravíš, zkusí ho hned.

## Co udělat
1. **Ověř údaje na webu zdroje.** U vlastního úložiště se přihlas přímo k NAS nebo Nextcloudu. U zdrojů třetích
   stran se přihlas na webu (webshare.cz, sledujteto.cz, fastshare.cz nebo sdilej.cz,
   prehraj.to) stejným jménem a heslem. Když nejde ani tam, obnov si heslo na webu.
2. **Vyplň je v Nokturnu znovu.**
   - **Kodi:** vlastní úložiště v **Nokturno → Nastavení → Vlastní úložiště**, zdroje třetích stran
     v **Nokturno → Nastavení → Zdroje a účty**, skupina zdroje. Pozor na mezeru na konci
     a na velká písmena. Pohodlněji to jde z mobilu: **Nastavit z mobilu a přenos → Nastavit z mobilu**.
   - **Stremio:** v nastavení doplňku (ozubené kolo u Nokturna ve Stremiu) oprav údaje, dej **Ověřit účet**
     a ulož změny. S profilem platí hned. Ve starém režimu bez profilů je změněné nastavení nová adresa:
     doplněk přidej znovu a starý ve Stremiu odinstaluj.
   - **Home Assistant:** **Nastavení → Zařízení a služby → Nokturno → Konfigurovat**, krok **Vlastní úložiště**
     nebo **Zdroje a účty**.
     Formulář hlásí „Špatný e-mail nebo heslo.“
3. **Ověř.** V Kodi **Nastavení → Pokročilé → Ověřit zdroje** (ve starších verzích **Otestovat zdroje**),
   ve Stremiu **Ověřit účet**.

## Tipy k jednotlivým zdrojům
- **Vlastní úložiště:** jméno a heslo jsou k tvému úložišti, ne k Nokturnu.
- **WebShare:** místo hesla jde vložit i 40znakový „salted hash“, Nokturno ho pozná samo.
- **FastShare / Sdilej.cz:** účty jsou oddělené. Kdo má účet na Sdilej.cz, zvolí v Kodi u FastShare
  **Účet z: Sdilej.cz** (ve Stremiu a HA stejná volba).
- **Sosáč** se přihlašuje účtem **Streamuj.tv**, ne WebShare. Streamuj přihlášení dopředu neověří,
  špatné heslo se pozná až při přehrání.
- **CZtor** heslo nechce vůbec, zařízení se páruje PINem, viz [CZtor](cztor.md).

---
[Všechny návody](../) · [Slovensky](../sk/prihlaseni)
