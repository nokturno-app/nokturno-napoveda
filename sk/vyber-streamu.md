---
slug: vyber-streamu
lang: sk
title: "Výber streamu: filtre, 3D a posledný filter"
products: [kodi]
priority: 3
templates:
  kodi: |
    Ahoj, 3D verzie sa dajú skryť.
    1. Nokturno → Nastavenia → Prehrávanie: zapni Skryť 3D streamy. 3D súbory sa potom nezobrazia nikdy, ani keď iný stream nie je.
    2. Chceš mať výber rovno s filtrom (napríklad len CZ zvuk)? V Nastavenia → Výber streamu zapni Automaticky použiť posledný filter.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/vyber-streamu
    Tím Nokturno
---

# Výber streamu: filtre, 3D a posledný filter

Po kliknutí na film alebo diel (aj po **Prehrať** v detaile) sa otvorí dialóg **Vyber stream**. Kedykoľvek ho vyvoláš
aj z kontextového menu filmu alebo dielu: **Vybrať stream**.

## Čo je v dialógu
- Každý stream má dva riadky, vľavo obrázok kvality. Čo a v akom poradí sa ukazuje, sa dá nastaviť (nižšie).
- Jazyk s vlnovkou (`~CZ`) je len odhad z názvu súboru. Bez vlnovky ho potvrdil zdroj alebo hlavička súboru.
- `×3` za streamom znamená tri rovnaké verzie súboru zlúčené do jedného riadku. Keď jedna nejde prehrať, skúsi sa ďalšia.
- Hore je **Filter streamov** s počtom streamov, **Zrušiť filter** a **Použiť posledný filter**.
- Dole je **Zobraziť všetky streamy** (rozbalí zlúčené verzie) a pri niektorých tituloch **Hľadať voľnejšie podľa názvu súboru**.

## Filter streamov
**Filter streamov** ponúkne len to, čo sa pri titule naozaj našlo: **Kvalita**, **Zvuk**, **Kanály**, **Kodek**,
**Titulky** a **Zdroj**.
- V jednej skupine stačí ktorákoľvek vybraná hodnota: Zvuk CZ a Zvuk SK = český alebo slovenský zvuk.
- Medzi skupinami musí platiť všetko: Zvuk SK a Kvalita 1080p = len slovenský zvuk v 1080p.
- Zvuk, kanály a kodek sa hľadajú na rovnakej zvukovej stope: Zvuk SK a Kanály 5.1 = slovenská stopa v 5.1.

Nokturno si posledný filter pamätá (v každom Kodi zvlášť). **Použiť posledný filter** ho vráti jedným klikom,
v zátvorke je počet streamov, ktoré nechá.

| Hlásenie | Čo znamená |
|---|---|
| „Filter nič nenechal, zobrazené sú všetky streamy“ | taký stream pri titule nie je, ukazuje sa celý zoznam |
| „Nie je podľa čoho filtrovať“ | streamy o sebe nič nevedia (kvalitu, zvuk ani zdroj) |

## Nastavenia
**Nokturno → Nastavenia → Prehrávanie:**

| Voľba | Čo robí |
|---|---|
| **Preferovaný jazyk zvuku** | streamy s týmto jazykom sú hore; nič sa neskrýva |
| **Preferovať priestorový zvuk (5.1 a viac)** | pri rovnakej kvalite ide vyššie stream s 5.1 a viac |
| **Skryť SD streamy** | streamy pod 720p sa vyradia. Keby nezostal žiadny, zobrazia sa všetky |
| **Skryť 3D streamy** | 3D súbory sa nezobrazia nikdy, ani keď iný stream nie je |
| **Max. dátový tok (Mb/s, 0 = bez obmedzenia)** | streamy s vyšším tokom sa vyradia. Keď sa nezmestí žiadny, zostane najmenší súbor. Hodnotu nastaví aj **Zmerať rýchlosť a nastaviť dátový tok** |
| **Radenie streamov** | **Ako prišli**, **Najprv najlepšia kvalita**, **Najprv najväčšie**, **Najprv najmenšie** |

**Nokturno → Nastavenia → Výber streamu:**

| Voľba | Čo robí |
|---|---|
| **Čo a v akom poradí ukazovať pri streame** | údaje v hornom a dolnom riadku. Pohodlnejšie cez **Nastaviť z mobilu**, kde sa údaje presúvajú šípkami. **Predvolené poradie** vráti pôvodný stav |
| **Automaticky použiť posledný filter** | dialóg sa otvorí rovno s posledným filtrom. Keby pri titule nenechal žiadny stream, zobrazia sa všetky |

## 3D streamy
3D verzie sú na bežnom televízore dva obrazy vedľa seba alebo nad sebou. Nokturno ich spozná podľa názvu súboru
(3D, H-SBS, Half-OU, MVC a podobne) alebo podľa hlavičky súboru MKV. So zapnutým **Skryť 3D streamy**
sa nezobrazia vôbec, ani medzi zlúčenými verziami.

Hlavička súboru sa pri otvorení zoznamu číta len pri niekoľkých streamoch, zvyšok sa dočíta na pozadí. 3D súbor bez značky
v názve sa preto môže zobraziť prvýkrát a zmizne pri ďalšom otvorení.

---
[Všetky návody](./) · [Česky](../cs/vyber-streamu)
