---
slug: luna-neodpovida
lang: sk
title: "Luna: „server neodpovedá“"
products: [kodi]
priority: 0
when: {luna: [unreachable, not_luna, bad_url, no_url]}
templates:
  kodi: |
    Ahoj, Nokturno sa nemôže spojiť so serverom Luna, preto sa z nej nič nenačíta.
    1. Lunu nepoužívaš? Nokturno → Nastavenia → Zdroje a účty, v skupine Luna vypni Používať Lunu. Ostatné zdroje fungujú ďalej.
    2. Používaš ju? Zariadenie, kde Luna beží, musí byť zapnuté a v rovnakej sieti ako Kodi. Home Assistant nie je potrebný: Luna beží aj priamo na Android TV boxe (adresa http://127.0.0.1:7126), na počítači alebo na NAS. Potrebuje WebShare VIP.
    3. V skupine Luna klikni na Nájsť Lunu v sieti a potom na Overiť nastavenie Luny. Overenie napíše, čo presne nesedí.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/luna-neodpovida
    Tím Nokturno
---

# Luna: „server neodpovedá“

## Čo to znamená
Nokturno sa nedostalo na adresu, ktorú má pri Lune vyplnenú. Hlásenie sa zobrazuje na niekoľkých miestach:

- hore v hlavnom menu: „Luna: server neodpovedá“,
- po kliknutí na **Overiť nastavenie Luny**: „Na adrese … sa nikto neozval.“ alebo „Na adrese … niečo odpovedá, ale nie je to Luna.“,
- po kliknutí na **Nájsť Lunu v sieti**: „V tejto sieti sa Luna nenašla.“,
- pri hľadaní: „Luna neodpovídá“ (toto hlásenie je zatiaľ po česky).

Ostatné zdroje na Lune nezávisia a fungujú ďalej.

## Prečo sa to stáva
Od najčastejšieho:

1. **Lunu nemáš a nikdy nebola nastavená.** Vo verziách do 8.2 je prepínač Luny zapnutý a adresa predvyplnená
   aj u ľudí, ktorí Lunu nikdy nemali. Je to najčastejší dôvod hlásenia.
2. **Zariadenie s Lunou je vypnuté** alebo je v inej sieti (sieť pre hostí, VPN, iná Wi-Fi).
3. **Adresa ukazuje inam**: na iné zariadenie, alebo je v nej iný port ako 7126.
4. **Luna na tvojom televízore bežať nemôže.** Napríklad na televízore LG (webOS) alebo Samsung (Tizen) musí Luna
   bežať na inom zariadení v sieti.

## Čo urobiť
Cesta v Kodi: **Nokturno → Nastavenia → Zdroje a účty**, skupina **Luna**.

1. **Lunu nepoužívaš?** Vypni **Používať Lunu** a daj OK. Hlásenie zmizne, všetko ostatné ide ďalej.
2. **Používaš ju?** Skontroluj, že zariadenie s Lunou je zapnuté a že je v rovnakej sieti ako Kodi.
   Home Assistant potrebný nie je. Luna beží:
   - priamo na Android TV boxe s Kodi, adresa je potom `http://127.0.0.1:7126`,
   - na počítači s Windows, Linuxom alebo macOS, na NAS alebo Raspberry Pi,
   - alebo ako doplnok Home Assistantu.

   Vždy potrebuje účet **WebShare VIP**.
3. Klikni na **Nájsť Lunu v sieti**. Nokturno prejde domácu sieť a adresu vyplní samo.
4. Klikni na **Overiť nastavenie Luny** a riaď sa hlásením. Čo ktoré znamená, nájdeš v článku
   [Čo znamenajú hlásenia z Overiť nastavenie Luny](luna-hlasky.md).

Celý návod na sprevádzkovanie Luny krok za krokom je v návode (po česky):
[Nastavení Luny](../navody/kodi/nastaveni-luny.md).

## Stále to nejde?
V okne overenia klikni na **Poslať log** a napíš nám, pozri [Kde hľadať pomoc](kde-hledat-pomoc.md).

---
[Všetky návody](./) · [Česky](../cs/luna-neodpovida)
