---
slug: premium-a-kredit
lang: cs
title: "„Účet bez Premium“, „účet bez VIP“, „došel kredit“"
products: [kodi, stremio]
priority: 1
when: {webshare: [free, expired], sledujteto: [no_premium], fastshare: [no_credit], prehrajto: [no_premium], cztor: [expired]}
templates:
  kodi: |
    Ahoj, {zdroj} u tebe nemá aktivní předplatné nebo kredit, proto z něj přehrávání nejde nebo je pomalé.
    1. Na webu zdroje zkontroluj předplatné (WebShare VIP, Sledujteto a Přehraj.to Premium, FastShare / Sdilej.cz kredit).
    2. Když ho mít nechceš, v Nokturno → Nastavení → Zdroje a účty zdroj vypni. Zdroje třetích stran jsou volitelné, vlastní úložiště a ostatní zdroje fungují dál.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/premium-a-kredit
    Tým Nokturno
---

# „Účet bez Premium“, „účet bez VIP“, „došel kredit“

## Co to znamená
Přihlášení prošlo, ale účet nemá předplatné nebo kredit, které zdroj k přehrávání chce. Nokturno to hlásí
nahoře v menu, ve výpisu **Stav zdrojů** a v **Ověřit zdroje**.

| Zdroj | Hláška | Co se děje | Co udělat |
|---|---|---|---|
| WebShare | účet bez VIP – stahování pár kB/s | bez VIP WebShare stahování zpomalí, film se plynule nepřehraje | kup VIP na webshare.cz |
| WebShare | předplatné vypršelo; do konce předplatného zbývá dní: N | VIP skončilo nebo brzy skončí | prodluž VIP; kolik zbývá, ukáže **Stav předplatného WebShare** |
| Sledujteto | účet bez Premium – přehrávání nepůjde | bez Premium Sledujteto odkaz na soubor nevydá | Premium na sledujteto.cz, nebo zdroj vypni |
| Přehraj.to | účet bez Premium – méně výsledků a jen 1080p | bez Premium jen část výsledků a překódované soubory | Premium na prehraj.to; funguje to i bez něj |
| Přehraj.to | bez účtu – jen první strana výsledků | účet není vyplněný | vyplň účet, když ho máš |
| FastShare / Sdilej.cz | došel kredit; zbývá N GB kreditu | přehrání se odečítá z kreditu | dobij kredit, nebo vyber menší soubor |
| CZtor | předplatné vypršelo | předplatné na cztor.com skončilo | prodluž předplatné |

Nokturno žádné účty neprodává a k předplatnému zdrojů nemá přístup. Kupuje se vždy na webu daného zdroje.

## Nechci platit
Zdroje třetích stran jsou volitelné. Hlavní je tvoje [vlastní úložiště](vlastni-uloziste.md), které nic nestojí
a funguje dál. Zdroj vypni: v Kodi **Nokturno → Nastavení → Zdroje a účty**, přepínač **Používat …** ve skupině
zdroje. Ve Stremiu nech jeho kartu prázdnou a ulož změny. Ostatní zdroje fungují dál.

## Stremio
Ve Stremiu ukáže stav účtu tlačítko **Ověřit účet** u každého zdroje v nastavení doplňku.
WebShare bez VIP se bude sekat stejně jako v Kodi.

---
[Všechny návody](../) · [Slovensky](../sk/premium-a-kredit)
