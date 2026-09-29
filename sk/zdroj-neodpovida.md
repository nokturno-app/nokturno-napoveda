---
slug: zdroj-neodpovida
lang: sk
title: "„<Zdroj> neodpovedá“"
products: [kodi, ha, stremio]
priority: 2
when: {webshare: [unreachable], sledujteto: [unreachable], fastshare: [unreachable], prehrajto: [unreachable], cztor: [unreachable]}
templates:
  kodi: |
    Ahoj, Nokturno sa nemôže spojiť so zdrojom {zdroj}. Ostatné zdroje fungujú ďalej.
    1. Skús to o chvíľu, zdroj mohol mať výpadok.
    2. Máš zapnutú VPN, rodičovskú kontrolu alebo blokovanie reklám v DNS (Pi-hole, AdGuard)? Skús ich vypnúť, alebo v routeri nastav DNS 1.1.1.1.
    3. Potom daj Nokturno → Nastavenia → Pokročilé → Overiť zdroje (v starších verziách Otestovať zdroje).
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/zdroj-neodpovida
    Tím Nokturno
---

# „<Zdroj> neodpovedá“

## Čo to znamená
Nokturno sa ku zdroju nedostalo: server neodpovedal včas alebo spojenie skončilo chybou siete. Hlásenie sa zobrazuje:
- hore v menu a vo výpise **Stav zdrojov**: „<zdroj>: neodpovedá“,
- pri hľadaní ako upozornenie „<zdroj> neodpovídá“ (zatiaľ po česky), vo výpise hľadania ako položka „Zdroj neodpovedal“,
- v **Overiť zdroje**.

Zdroj, ktorý sa neozve do 20 sekúnd, Nokturno pri hľadaní preskočí a ukáže streamy z ostatných.

## Prečo sa to stáva
- **Výpadok na strane zdroja.** O chvíľu to zvyčajne prejde.
- **DNS blokuje adresu zdroja.** Pi-hole, AdGuard, rodičovská kontrola alebo filter operátora.
- **VPN alebo firemná sieť** spojenie so zdrojom nepustí.
- **Telefón alebo tablet s Androidom:** na pozadí nemá Kodi prístup k sieti. Stav potom chvíľu ukazuje „neodpovedá“,
  po otvorení menu sa sám obnoví.
- **Luna a vlastné úložisko** majú vlastné návody: [Luna: „server neodpovedá“](luna-neodpovida.md),
  [Ako pripojiť vlastné úložisko](vlastni-uloziste.md).

## Čo urobiť
1. Skús to o pár minút.
2. Otvor web zdroja v prehliadači **v rovnakej sieti**. Keď nejde ani tam, je problém v sieti alebo pri zdroji.
3. Vypni VPN alebo blokovanie v DNS, prípadne v routeri nastav iné DNS (napríklad `1.1.1.1`).
4. Potom daj **Nokturno → Nastavenia → Pokročilé → Overiť zdroje** (v starších verziách **Otestovať zdroje**).

Zdroj, ktorý teraz nechceš skúšať, môžeš uspať: vo výpise **Stav zdrojov** podrž OK na jeho riadku a zvoľ
**Uspať zdroj** (10 minút, 1 hodina, 12 hodín).

## HellSpy alebo Přehraj.to a HTTP 429
To nie je výpadok, ale odmietnutá sieť. Pozri [„Odmieta túto sieť (HTTP 429)“](sit-odmitnuta-429.md).

---
[Všetky návody](./) · [Česky](../cs/zdroj-neodpovida)
