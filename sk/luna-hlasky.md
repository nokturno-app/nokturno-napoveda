---
slug: luna-hlasky
lang: sk
title: Čo znamenajú hlásenia z Overiť nastavenie Luny
products: [kodi]
priority: 0
---

# Čo znamenajú hlásenia z Overiť nastavenie Luny

Tlačidlo **Overiť nastavenie Luny** nájdeš v **Nokturno → Nastavenia → Zdroje a účty**, v skupine **Luna**.
Najprv sa spýta na adresu (predvyplnená je uložená, stačí OK), potom prejde celú cestu od servera po streamy
a napíše, kde to viazne. Pri chybe ponúkne zadanie inej adresy a **Poslať log**.

Hore v hlavnom menu a vo výpise **Stav zdrojov** sa zobrazuje skrátená podoba toho istého hlásenia (stĺpec „V menu“).

| Hlásenie pri overení | V menu | Čo to znamená | Čo urobiť |
|---|---|---|---|
| Luna … odpovedá a vracia streamy. Nastavenie je v poriadku. | – | všetko funguje | nič |
| Nie je vyplnená adresa Luny ani token. | chýba adresa aj token | polia sú prázdne | [Luna: „beží, ale chýba token“](luna-token.md), alebo Lunu vypni |
| Adresa … nemá očakávaný tvar. | adresa nedáva zmysel | preklep v adrese | tvar `http://192.168.1.10:7126` |
| Na adrese … sa nikto neozval. | server neodpovedá | na adrese nič nebeží | [Luna: „server neodpovedá“](luna-neodpovida.md) |
| Na adrese … niečo odpovedá, ale nie je to Luna. | na tej adrese nebeží Luna | iné zariadenie alebo port | Luna má port 7126 |
| Luna … beží, ale chýba token. | beží, ale chýba token | chýba adresa doplnku zo `/setup` | [Luna: „beží, ale chýba token“](luna-token.md) |
| V poli Token nie je token. | v poli Token nie je token | vložený len kus adresy | skopíruj celú adresu doplnku |
| Luna … beží, ale tento token neprijala. | token Luna neprijala | token z inej alebo preinštalovanej Luny | vygeneruj adresu znova na `/setup` tejto Luny |
| … hľadanie na WebShare funguje, ale jej hlavný zdroj nič nevracia. | hlavný zdroj nič nevracia – účet WebShare v Lune? | token z inej Luny alebo chýba WebShare | na `/setup` skontroluj WebShare a token |
| … beží, ale nenašla streamy ani pri známych filmoch. | nenašla žiadne streamy – účet WebShare v Lune? | v Lune nie je prihlásený WebShare alebo nemá VIP | na `/setup` sa znova prihlás do WebShare |
| V tejto sieti sa Luna nenašla. (po Nájsť Lunu v sieti) | – | hľadanie v sieti nič nenašlo | Luna nebeží, je v inej sieti alebo má iný port; adresu vyplň ručne |

Home Assistant pre Lunu potrebný nie je. Luna beží aj priamo na Android TV boxe (adresa `http://127.0.0.1:7126`),
na počítači alebo na NAS. Vždy potrebuje účet WebShare VIP.

Celý návod (po česky): [Nastavení Luny](../navody/kodi/nastaveni-luny.md).

---
[Všetky návody](./) · [Česky](../cs/luna-hlasky)
