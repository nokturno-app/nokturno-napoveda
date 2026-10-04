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
    2. Najprv skontroluj vlastné úložisko: Nastavenia → Vlastné úložisko (adresa, meno, heslo, úložisko zapnuté). Zdroje tretích strán v Nastavenia → Zdroje a účty sú voliteľné, pri novej inštalácii sú vypnuté.
    3. Keď zdroje fungujú, titul na nich nemusí byť. Skús dole v dialógu streamov hľadať voľnejšie podľa názvu súboru.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/zadny-stream
    Tím Nokturno
---

# Nedá sa nájsť žiadny film („Nenašiel sa žiadny stream“)

## Čo to znamená
Katalóg a hľadanie fungujú, ale pri titule sa nezobrazí žiadny stream. Kodi hlási „Nenašiel sa žiadny stream“,
prípadne „Zdroj nie je zapnutý alebo nastavený – skontroluj v nastaveniach Zdroje a účty a Vlastné úložisko“.

Katalóg a hľadanie bežia aj bez účtov. Streamy ale prichádzajú len z tvojho vlastného úložiska a zo zdrojov tretích strán,
ktoré máš zapnuté a nastavené. Zdroje tretích strán sú voliteľné a pri novej inštalácii sú všetky vypnuté.

## Čo urobiť
1. **Over zdroje.** **Nokturno → Nastavenia → Pokročilé → Overiť zdroje** (v starších verziách **Otestovať zdroje**).
   Pri každom zdroji ukáže „v poriadku“, „nie je nastavené“ alebo dôvod chyby.
2. **Nastav vlastné úložisko.** Keď výsledok hlási pri všetkom „nie je nastavené“, začni [vlastným úložiskom](vlastni-uloziste.md)
   (**Nastavenia → Vlastné úložisko**). Voliteľne môžeš v **Nastavenia → Zdroje a účty** zapnúť aj zdroj tretej strany
   a vyplniť jeho účet (WebShare potrebuje VIP).
   Najpohodlnejšie to ide z mobilu: **Nastavenia → Nastaviť z mobilu a prenos → Nastaviť z mobilu**.
3. **Zdroj hlási chybu?** Pokračuj návodom k tomu hláseniu:
   [prihlásenie](prihlaseni.md), [Premium a kredit](premium-a-kredit.md), [Luna](luna-hlasky.md).
4. **Zdroje fungujú, len tento titul nič nemá.** Titul na zdrojoch nemusí vôbec byť, hlavne úplné novinky.
   Vo vlastnom úložisku pomôže, keď názov súboru alebo priečinka obsahuje názov titulu a rok.
   - Dole v dialógu streamov skús **Hľadať voľnejšie podľa názvu súboru** (v starších verziách **Skúsiť uvoľnený fulltext**).
   - Po neúspešnom hľadaní sa doplnok spýta „Skúsiť hľadať pod iným názvom?“. Zadaj slovenský, český alebo originálny názov.

## Prečo Nokturno neponúkne súbor, ktorý na zdroji vidím
Nokturno berie len súbory, ktoré k titulu naozaj patria (názov, rok, pri seriáli číslo série a dielu).
Podobný, ale iný film zámerne vynechá. Uvoľnené hľadanie (bod 4) ukáže aj súbory, ktoré týmto sitom neprešli.

---
[Všetky návody](./) · [Česky](../cs/zadny-stream)
