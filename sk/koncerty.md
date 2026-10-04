---
slug: koncerty
lang: sk
title: Koncerty
products: [kodi, stremio]
priority: 3
templates:
  kodi: |
    Ahoj, Koncerty sú od verzie 10.0 v hlavnom menu Nokturna. Potrebujú vlastný API kľúč Last.fm, je zadarmo.
    1. Kľúč si založ na https://www.last.fm/api/account/create (stačí účet na Last.fm, názov aplikácie ľubovoľný) a skopíruj API key.
    2. V Kodi otvor Koncerty → Nastaviť koncerty, vlož kľúč a vyber hudobné žánre.
    3. Hľadanie beží na pozadí a zoznam sa plní postupne, prvá dávka prehľadá 40 interpretov hneď.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/koncerty
    Tím Nokturno
  stremio: |
    Ahoj, Koncerty zapneš v nastaveniach doplnku, karta Koncerty: zaškrtni hudobné žánre a vlož Last.fm API kľúč (zadarmo na https://www.last.fm/api/account/create).
    Potom daj Uložiť zmeny a doplnok v Stremiu pridaj znova. Zoznam sa plní postupne, kým aplikácia beží.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/koncerty
    Tím Nokturno
---

# Koncerty

Koncerty sú záznamy koncertov interpretov z hudobných žánrov, ktoré si vyberieš. Nokturno si od verzie 10.0 skladá
zoznam samo: z [Last.fm](https://www.last.fm) zoberie najpočúvanejších interpretov tvojich žánrov a pri každom hľadá
záznamy koncertov na tvojich zdrojoch (WebShare, HellSpy, FastShare). Zoznam sa plní na pozadí a stále rastie.

Funguje v Kodi a v Stremiu. Home Assistant koncerty sám nezobrazuje, ale s vyplneným kľúčom Last.fm (Nastavenie integrácie → Ostatné) ich hľadá na pozadí a zdieľajú sa so skupinou.

## Kľúč Last.fm
Koncerty potrebujú vlastný **API kľúč Last.fm**. Je zadarmo a patrí len tebe.

1. Prihlás sa na [last.fm](https://www.last.fm) (alebo si založ účet).
2. Otvor [last.fm/api/account/create](https://www.last.fm/api/account/create).
3. Vyplň **Application name** (napríklad „Nokturno“) a krátky popis. Ostatné polia nechaj prázdne.
4. Skopíruj **API key** (nie „Shared secret“).

## Kodi
### Nastavenie
1. V hlavnom menu otvor **Koncerty → Nastaviť koncerty**.
2. Keď kľúč ešte nemáš, Nokturno sa na neho opýta. Vlož **Last.fm API kľúč** a Nokturno ho hneď overí.
3. V dialógu **Hudobné žánre katalógu** vyber jeden alebo viac žánrov: Česká scéna, Slovenská scéna, Český rock,
   Classic rock, Hard rock, Metal, Rock, Pop, Punk, Hip-hop, Jazz, Elektronika, Folk, Klasika, Reggae, World.
4. Na otázku **„Spustiť hľadanie koncertov teraz?“** daj **Áno**. Prvá dávka hneď prehľadá 40 interpretov.

Kľúč nájdeš aj v **Nastavenia → Zdroje a účty**, skupina **Last.fm**. Tlačidlo **Overiť kľúč** skontroluje, že ho
Last.fm prijíma. Kľúč sa dá vyplniť aj cez Nastaviť z mobilu a so zapnutou synchronizáciou účtov sa dostane aj do
ostatných Kodi v skupine.

### Čo je v menu Koncerty
| Položka | Čo ukáže |
|---|---|
| **Novo pridané** | 50 naposledy nájdených koncertov |
| **Podľa žánru** | žánre, v ktorých už je nejaký nález → interpreti s počtom koncertov |
| **Podľa abecedy** | písmená (čísla a ostatné znaky pod „#“) → interpreti |
| **Prehľadané X interpretov, ďalší pribúdajú – načítať teraz** | priebeh. Klik prehľadá hneď ďalších 20 interpretov. |
| **Hľadať interpreta** | napíšeš meno a vyberieš interpreta z výsledkov (s kľúčom Last.fm aj podobné mená: Lucie → Lucie, Lucie Bílá). Výber ho hneď prehľadá vo tvojich zdrojoch a pridá do zoznamu – aj bez žánrov. |
| **Nastaviť koncerty** | zmena žánrov alebo kľúča |

Pri interpretovi sú koncerty od najnovšieho roku. Koncert má náhľad zo zdroja, dĺžku a veľkosť súboru. Na konci je **Znovu prehľadať** s dátumom posledného hľadania.
Klik ho prehrá. Keď prvý súbor nejde, Nokturno skúsi ďalšiu kópiu.

### Ako zoznam rastie
- Interpreti prichádzajú z rebríčka Last.fm. Ďalšia strana rebríčka pribudne, hneď ako sú skoro všetci doterajší
  prehľadaní (najviac raz za hodinu). Zoznam teda nie je obmedzený na 200 interpretov, rastie až do 3000.
- Na pozadí sa prehľadá 8 interpretov za 10 minút, pri prehrávaní len 1. Striedajú sa s
  [vlastnými katalógmi](vlastni-katalogy.md), ktoré sa overujú.
- Interpret s nálezom sa kontroluje každý týždeň, bez nálezu za 3 dni. Kto nemá nič ani na tretí pokus, skúsi sa
  znova až za 30 dní.
- Staré odkazy sa overujú. Zmazaný súbor zo zoznamu zmizne.

### Synchronizácia
So zapnutým okruhom **Synchronizovať koncerty** (Nastavenia → Synchronizácia) sa nájdené koncerty zdieľajú so skupinou, teda s ďalšími Kodi
aj s Home Assistantom. Každé zariadenie ukáže len súbory zo zdrojov, ktoré má samo zapnuté. Zariadenia s rovnakými zdrojmi
rovnakého interpreta znova neprehľadávajú.

### Zmena žánrov
Žánre zmeníš cez **Nastaviť koncerty**. Keď žáner **pridáš**, interpreti, ktorých už máš, zostanú a pribudnú noví.
Keď žáner **odoberieš**, zmiznú interpreti, ktorí nepatria do žiadneho z vybraných žánrov.

## Stremio
1. Otvor nastavenia doplnku (**Doplnky → Nokturno → Konfigurovať**, alebo `http://<IP zariadenia s aplikáciou>:7140/configure`).
2. V karte **Koncerty** zaškrtni hudobné žánre a vyplň **Last.fm API kľúč**.
3. Daj **Uložiť zmeny** a doplnok v Stremiu **pridaj znova**, nech Stremio načíta nové katalógy.

V Stremiu pribudne druh **Koncerty** so zoznamami **Nové pridané** a **Podľa abecedy** (s výberom žánru). Interpret
je plagát, jeho koncerty sú ako diely. V zozname **Podľa abecedy** sa dá hľadať menom interpreta, neznámeho doplnok prehľadá v zdrojoch a pridá. Hľadá aplikácia na pozadí, kým beží, takže sa zoznam zapĺňa postupne.

## Keď niečo nejde
| Čo vidíš | Čo urobiť |
|---|---|
| „Kľúč Last.fm neplatí.“ | preklep, alebo skopírovaný „Shared secret“ namiesto API key. Skopíruj kľúč znova. |
| „Last.fm sa nepodarilo opýtať. Skús to neskôr.“ | Last.fm práve neodpovedá, skús to o chvíľu. |
| „Katalóg sa pripravuje – interpreti sa prehľadávajú na pozadí.“ | hľadanie ešte beží. Daj **načítať teraz** alebo počkaj. |
| interpret v zozname chýba | ešte naňho neprišiel rad, alebo na tvojich zdrojoch žiadny koncert nie je. |
| málo nálezov | zapni viac zdrojov (WebShare, HellSpy, FastShare). FastShare bez kreditu sa na pozadí preskakuje. |

---
[Všetky návody](./) · [Česky](../cs/koncerty)
