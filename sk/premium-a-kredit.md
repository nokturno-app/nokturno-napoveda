---
slug: premium-a-kredit
lang: sk
title: "„Účet bez Premium“, „účet bez VIP“, „minul sa kredit“"
products: [kodi, stremio]
priority: 1
when: {webshare: [free, expired], sledujteto: [no_premium], fastshare: [no_credit], prehrajto: [no_premium], cztor: [expired]}
templates:
  kodi: |
    Ahoj, {zdroj} u teba nemá aktívne predplatné alebo kredit, preto z neho prehrávanie nejde alebo je pomalé.
    1. Na webe zdroja skontroluj predplatné (WebShare VIP, Sledujteto a Přehraj.to Premium, FastShare / Sdilej.cz kredit).
    2. Keď ho mať nechceš, v Nokturno → Nastavenia → Zdroje a účty zdroj vypni. Ostatné zdroje fungujú ďalej.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/premium-a-kredit
    Tím Nokturno
---

# „Účet bez Premium“, „účet bez VIP“, „minul sa kredit“

## Čo to znamená
Prihlásenie prešlo, ale účet nemá predplatné alebo kredit, ktoré zdroj na prehrávanie chce. Nokturno to hlási
hore v menu, vo výpise **Stav zdrojov** a v **Overiť zdroje**.

| Zdroj | Hlásenie | Čo sa deje | Čo urobiť |
|---|---|---|---|
| WebShare | účet bez VIP – sťahovanie pár kB/s | bez VIP WebShare sťahovanie spomalí, film sa plynulo neprehrá | kúp VIP na webshare.cz |
| WebShare | predplatné vypršalo; do konca predplatného zostáva dní: N | VIP skončilo alebo čoskoro skončí | predĺž VIP; koľko zostáva, ukáže **Stav predplatného WebShare** |
| Sledujteto | účet bez Premium – prehrávanie nepôjde | bez Premium Sledujteto odkaz na súbor nevydá | Premium na sledujteto.cz, alebo zdroj vypni |
| Přehraj.to | účet bez Premium – menej výsledkov a len 1080p | bez Premium len časť výsledkov a prekódované súbory | Premium na prehraj.to; funguje to aj bez neho |
| Přehraj.to | bez účtu – len prvá strana výsledkov | účet nie je vyplnený | vyplň účet, keď ho máš |
| FastShare / Sdilej.cz | minul sa kredit; zostáva N GB kreditu | prehrávanie sa odpočítava z kreditu | dobi kredit, alebo vyber menší súbor |
| CZtor | predplatné vypršalo | predplatné na cztor.com skončilo | predĺž predplatné |

Nokturno žiadne účty nepredáva a k predplatnému zdrojov nemá prístup. Kupuje sa vždy na webe daného zdroja.

## Nechcem platiť
Zdroj vypni: v Kodi **Nokturno → Nastavenia → Zdroje a účty**, prepínač **Používať …** v skupine zdroja.
V Stremiu nechaj jeho kartu prázdnu a doplnok pridaj znova. Ostatné zdroje a [vlastné úložisko](vlastni-uloziste.md)
fungujú ďalej.

## Stremio
V Stremiu ukáže stav účtu tlačidlo **Overiť účet** pri každom zdroji v nastavení doplnku.
WebShare bez VIP sa bude sekať rovnako ako v Kodi.

---
[Všetky návody](./) · [Česky](../cs/premium-a-kredit)
