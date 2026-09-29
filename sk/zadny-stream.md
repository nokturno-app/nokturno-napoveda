---
slug: zadny-stream
lang: sk
title: "Nedá sa nájsť žiadny film („Nenašiel sa žiadny stream“)"
products: [kodi]
priority: 1
templates:
  kodi: |
    Ahoj, Nokturno k titulu nenašlo žiadny stream.
    1. Nokturno → Nastavenia → Pokročilé → Overiť zdroje (v starších verziách Otestovať zdroje). Ukáže, ktoré zdroje fungujú. Keď žiadny, začni pri ňom.
    2. V Nastavenia → Zdroje a účty musí byť zapnutý a prihlásený aspoň jeden zdroj, alebo nastavené vlastné úložisko.
    3. Keď zdroje fungujú, titul na nich nemusí byť. Skús dole v dialógu streamov hľadať voľnejšie podľa názvu súboru.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/zadny-stream
    Tím Nokturno
---

# Nedá sa nájsť žiadny film („Nenašiel sa žiadny stream“)

## Čo to znamená
Katalóg a hľadanie fungujú, ale pri titule sa nezobrazí žiadny stream. Kodi hlási „Nenašiel sa žiadny stream“,
prípadne „Zdroj nie je zapnutý alebo nastavený – skontroluj v nastaveniach Zdroje a účty a Vlastné úložisko“.

Katalóg a hľadanie bežia aj bez účtov. Streamy ale prichádzajú len zo zdrojov, ktoré máš zapnuté a nastavené.

## Čo urobiť
1. **Over zdroje.** **Nokturno → Nastavenia → Pokročilé → Overiť zdroje** (v starších verziách **Otestovať zdroje**).
   Pri každom zdroji ukáže „v poriadku“, „nie je nastavené“ alebo dôvod chyby.
2. **Zapni aspoň jeden zdroj.** Keď výsledok hlási pri všetkom „nie je nastavené“, otvor **Nastavenia → Zdroje a účty**
   a vyplň účet (WebShare potrebuje VIP), alebo nastav [vlastné úložisko](vlastni-uloziste.md).
   Najpohodlnejšie to ide z mobilu: **Nastavenia → Nastaviť z mobilu a prenos → Nastaviť z mobilu**.
3. **Zdroj hlási chybu?** Pokračuj návodom k tomu hláseniu:
   [prihlásenie](prihlaseni.md), [Premium a kredit](premium-a-kredit.md), [Luna](luna-hlasky.md).
4. **Zdroje fungujú, len tento titul nič nemá.** Titul na zdrojoch nemusí vôbec byť, hlavne úplné novinky.
   - Dole v dialógu streamov skús **Hľadať voľnejšie podľa názvu súboru** (v starších verziách **Skúsiť uvoľnený fulltext**).
   - Po neúspešnom hľadaní sa doplnok spýta „Skúsiť hľadať pod iným názvom?“. Zadaj slovenský, český alebo originálny názov.

## Prečo Nokturno neponúkne súbor, ktorý na zdroji vidím
Nokturno berie len súbory, ktoré k titulu naozaj patria (názov, rok, pri seriáli číslo série a dielu).
Podobný, ale iný film zámerne vynechá. Uvoľnené hľadanie (bod 4) ukáže aj súbory, ktoré týmto sitom neprešli.

---
[Všetky návody](./) · [Česky](../cs/zadny-stream)
