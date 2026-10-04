---
slug: stav-zdroju
lang: sk
title: "Hore v menu je riadok so zdrojom („Stav zdrojov“)"
products: [kodi, ha]
priority: 1
---

# Hore v menu je riadok so zdrojom („Stav zdrojov“)

## Čo to znamená
Keď niektorý zapnutý zdroj potrebuje zásah, zobrazí sa **úplne hore v hlavnom menu** Nokturna riadok s menom
zdroja a krátkym popisom, napríklad „Úložisko: neodpovedá“ alebo „WebShare: zostáva dní: 3“. Keď je problémov viac,
za textom je „+1“, „+2“…

Keď je všetko v poriadku, riadok v menu vôbec nie je.

## Čo urobiť
1. Klikni na riadok. Otvorí sa výpis **Stav zdrojov**, každý zdroj má vlastný riadok s plným popisom.
2. Klikni na riadok zdroja. Vedie rovno tam, kde sa to opravuje: pri Lune na **Overiť nastavenie Luny**,
   pri CZtore na **Spárovať PIN kódom**, pri predplatnom WebShare na **Stav predplatného WebShare**, inak do nastavení.
3. Pod zdrojmi je **Overiť zdroje** (v starších verziách **Otestovať zdroje**). Skúsi všetky zdroje znova a stav prepíše.

Zdroj, s ktorým teraz nič urobiť nejde (napríklad výpadok na jeho strane), môžeš **uspať**: podrž OK alebo klikni
pravým tlačidlom na jeho riadok a zvoľ **Uspať zdroj** (10 minút, 1 hodina, 12 hodín). Počas toho sa v ňom nehľadá.

## Čo jednotlivé stavy znamenajú
| Vo výpise | Čo to znamená | Návod |
|---|---|---|
| Úložisko: neodpovedá | vlastné úložisko | [Ako pripojiť vlastné úložisko](vlastni-uloziste.md) |
| neodpovedá | zdroj alebo server nie je dosiahnuteľný | [„<Zdroj> neodpovedá“](zdroj-neodpovida.md) |
| nesedí meno alebo heslo | zdroj odmietol prihlásenie | [Zdroj hlási „nesedí meno alebo heslo“](prihlaseni.md) |
| predplatné vypršalo, do konca predplatného zostáva dní: N | WebShare, CZtor alebo Přehraj.to | [Premium, VIP a kredit](premium-a-kredit.md) |
| účet bez VIP – sťahovanie pár kB/s | WebShare bez VIP | [Premium, VIP a kredit](premium-a-kredit.md) |
| účet bez Premium – prehrávanie nepôjde | Sledujteto bez Premium | [Premium, VIP a kredit](premium-a-kredit.md) |
| minul sa kredit | FastShare / Sdilej.cz | [Premium, VIP a kredit](premium-a-kredit.md) |
| zariadenie nie je spárované | CZtor | klikni na riadok a spáruj PIN kódom, pozri [CZtor](cztor.md) |
| odmieta túto sieť (HTTP 429) – VPN alebo mobilné dáta? | HellSpy odmieta tvoju sieť, typicky VPN alebo mobilné dáta | [„Odmieta túto sieť (HTTP 429)“](sit-odmitnuta-429.md) |
| server neodpovedá, beží, ale chýba token… | Luna | [Čo znamenajú hlásenia Luny](luna-hlasky.md) |

## Stav sa po oprave nezmenil
Stav sa obnovuje na pozadí po niekoľkých hodinách. Hneď ho prepíše **Overiť zdroje** vo výpise
alebo v **Nastavenia → Pokročilé**.

Na telefóne alebo tablete s Androidom nemá Kodi na pozadí prístup k sieti. Stav potom môže chvíľu ukazovať
„neodpovedá“, aj keď zdroj funguje. Po otvorení menu sa sám obnoví.

## Home Assistant
Rovnaký prehľad ukazuje senzor **Stav zdrojov**: hodnota je počet zdrojov, ktoré potrebujú zásah
(0 = všetko v poriadku), podrobnosti sú v jeho atribútoch.

---
[Všetky návody](./) · [Česky](../cs/stav-zdroju)
