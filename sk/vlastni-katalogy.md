---
slug: vlastni-katalogy
lang: sk
title: Vlastné katalógy
products: [kodi, ha, stremio]
priority: 3
templates:
  kodi: |
    Ahoj, od verzie 10.0 si katalóg poskladáš sám a Nokturno ti v ňom môže nechať len tituly, ku ktorým je stream podľa tvojich požiadaviek.
    1. Filmy alebo Seriály → Vlastné katalógy → Nový katalóg.
    2. Zvoľ Nastaviť cez mobil (odporúčame), naskenuj QR kód a vyber šablónu, napríklad Filmy v 4K s CZ dabingom.
    3. Režim Len tituly so streamom overuje tituly na pozadí, prvá dávka preverí 40 titulov hneď.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/vlastni-katalogy
    Tím Nokturno
  stremio: |
    Ahoj, vlastné katalógy (až 20) sú v nastaveniach doplnku, karta Vlastné katalógy → Pridať katalóg. Začať sa dá zo šablóny.
    Po zmene katalógov doplnok v Stremiu pridaj znova, nech ich aplikácia načíta.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/vlastni-katalogy
    Tím Nokturno
---

# Vlastné katalógy

Vlastný katalóg je zoznam filmov alebo seriálov, ktorý si poskladáš sám: podľa žánrov, tém, krajiny pôvodu, rokov a radenia.
Od verzie 10.0 vie katalóg navyše **overovať streamy** – ukáže len tituly, ku ktorým Nokturno našlo stream
v požadovanej kvalite, s dabingom alebo titulkami a napríklad s 5.1. Tituly vyberá server Nokturna, vlastný kľúč TMDB
na to nepotrebuješ. Keď ho máš (od verzie 10.0.1), katalógy sa berú priamo z TMDB a server je len záloha:
fungujú aj pri jeho výpadku a server nevidí tvoje filtre.

Funguje v Kodi a v Stremiu. Home Assistant katalógy nezakladá, ale vie ich [overovať za ostatných](#home-assistant).

## Dva režimy katalógu
| Režim | Čo ukáže | Kedy sa hodí |
|---|---|---|
| **Katalóg z TMDB** | hneď všetky tituly podľa filtrov, po 20 na stranu | prechádzanie, tipy na filmy. Pri titule bez streamu si zapni [stráženie](hlidane.md) – Sledované dajú vedieť, keď stream bude. |
| **Len tituly so streamom** | len tituly, ktoré sa dajú prehrať podľa tvojich požiadaviek | „chcem 4K s CZ dabingom a nechcem klikať naprázdno“ |

V režime **Len tituly so streamom** sa katalóg plní postupne. Nokturno na pozadí prechádza kandidátov (zhruba 200
najobľúbenejších titulov podľa filtrov) a pri každom hľadá stream. Čo vyhovie, sa v katalógu objaví.

## Šablóny
Šablóna je hotový katalóg, ktorý si môžeš upraviť. Ponúka ju stránka v mobile a formulár Stremia.

| Šablóna | Čo robí |
|---|---|
| Populárne filmy, Populárne seriály | čo sa teraz na TMDB najviac sleduje |
| Najlepšie hodnotené filmy, Najlepšie hodnotené seriály | najlepšie hodnotené na TMDB |
| Nové filmy s CZ dabingom, Nové seriály s CZ dabingom | posledné 2 roky, len tituly so streamom s českým zvukom |
| Filmy v 4K s CZ dabingom | len filmy so streamom v 4K a s českým zvukom |
| České filmy, České seriály | krajina pôvodu Česko |
| Rozprávky s CZ dabingom | téma Rozprávky, len tituly so streamom s českým zvukom |

**Kde sú Populárne a Najlepšie hodnotené z menu?** Od verzie 10.0 nie sú pevnou položkou v menu Filmy a Seriály.
Keď ich chceš, založ si ich zo šablóny – a môžeš si ich rovno upraviť, napríklad len na posledných 5 rokov.

## Kodi: založenie katalógu
1. **Filmy** alebo **Seriály → Vlastné katalógy → Nový katalóg**. Druh katalógu (filmy, alebo seriály) sa riadi tým,
   kde si.
2. Nokturno ponúkne dve cesty:
   - **Nastaviť cez mobil (odporúčame)** – na televízore sa ukáže QR kód, celý katalóg vyplníš v telefóne
     a môžeš začať zo šablóny. Postup je nižšie v časti [Nastavenie cez mobil](#nastavenie-cez-mobil).
   - **Pokračovať v nastavení v Kodi** – prejdeš dialógy ovládačom (bez šablón).
3. Katalóg sa objaví vo **Vlastných katalógoch**. Kliknutím ho otvoríš.

### Dialógy v Kodi, v tomto poradí
| Dialóg | Čo vybrať |
|---|---|
| **Režim katalógu** | **Katalóg z TMDB**, alebo **Len tituly so streamom** |
| **Žánre (nič = všetky)** | jeden alebo viac žánrov. Seriály majú iný zoznam (napríklad **Sci-fi a fantasy**, **Dětský**). |
| **Témy (stačí jedna, najviac 3)** | Rozprávky, Vianoce, Halloween, Silvester, Podľa skutočnej udalosti, Podľa knihy, Životopisný, Superhrdinovia, Sériový vrah, 2. svetová vojna, Bojové umenia, Šport, Mimozemšťania, Cestovanie v čase, Zombie, Duchovia, Upíri, Postapokalypsa, Lúpež, Špionáž, Prežitie, Psy, Dinosaury |
| **Tituly musia mať** | len pri dvoch a viac žánroch: **všetky vybrané žánre**, alebo **aspoň jeden vybraný žáner** |
| **Krajiny pôvodu (najviac 5)** | Česko, Slovensko, USA, Veľká Británia, Francúzsko, Nemecko, Taliansko, Španielsko, Poľsko, Maďarsko, Južná Kórea, Japonsko, Dánsko, Švédsko, Nórsko |
| **Roky** | **Bez obmedzenia**, **Od–do** (rok od a do, prázdne = bez obmedzenia), alebo **Posledných X rokov** (1–50, predvolené 5) |
| **Radiť podľa** | **Obľúbenosti**, **Hodnotenia na TMDB** (len tituly s dosť hlasmi), **Dátumu vydania** (najnovšie prvé), **Abecedy** (obľúbené tituly podľa názvu) |
| **Jazyk zvuku** * | Ľubovoľné, Čeština, Slovenčina, Čeština alebo slovenčina, Angličtina, Maďarčina |
| **Titulky** * | rovnaké možnosti ako jazyk zvuku |
| **Minimálna kvalita** * | Ľubovoľná, Full HD, 2K, 4K |
| **Kanály zvuku** * | Ľubovoľné, alebo **5.1 a viac** |
| **Zobraziť zoradené podľa** * | **Novo nájdené**, **Rovnako ako výber**, alebo **Najnovšie vydanie** |
| **Ikona katalógu** | Filmy, Seriály, Zoznam, Hviezda, Rebríček, Žáner, Rok, Krajina, Zbierka, Novinky, Herci, Štúdiá |
| **Názov katalógu** | predvyplní sa z volieb (napríklad „Rozprávky · Česko · CZ dabing · posledných 5 rokov“), môžeš ho prepísať |

\* len v režime **Len tituly so streamom**.

Téma a žáner sa kombinujú: so žánrom **Komedie** a témou **Vianoce** dostaneš vianočné komédie. Z vybraných tém
stačí, keď titul má jednu. Zrušenie ktoréhokoľvek dialógu tlačidlom Späť zruší celé zakladanie.

Po uložení katalógu v režime **Len tituly so streamom** sa Nokturno opýta **„Spustiť overenie streamov teraz?“**. **Áno** spustí prvú
dávku – tá hneď preverí 40 titulov, nech je v katalógu čo ukázať.

### Úprava a zmazanie
Miestna ponuka katalógu (dlhé podržanie OK, alebo tlačidlo menu na ovládači):
- **Upraviť katalóg** – prejde rovnaké dialógy, predvybrané sú uložené voľby. Názov, ktorý si prepísal, zostane.
- **Upraviť na mobile** – QR kód ako pri zakladaní.
- **Zmazať katalóg** – ešte sa opýta „Zmazať katalóg …?“.
- **Zobraziť v hlavnom menu** – katalóg sa ukáže priamo vo Filmoch alebo Seriáloch, nad položkou Vlastné katalógy (od verzie 10.1). **Odobrať z hlavného menu** ho vráti len pod Vlastné katalógy.

## Nastavenie cez mobil
1. Na televízore zvoľ **Nastaviť cez mobil (odporúčame)** (pri novom katalógu), alebo **Upraviť na mobile**
   (v miestnej ponuke katalógu).
2. Pripoj telefón k rovnakej Wi-Fi ako Kodi a naskenuj QR kód. Adresa platí 30 minút a pre jedno uloženie.
3. Na stránke **Nokturno – Vlastné katalógy**:
   - hore vyber **Šablónu** a daj **Načítať šablónu** – polia sa vyplnia,
   - uprav, čo potrebuješ. Polia na overovanie (jazyk zvuku, titulky, kvalita, 5.1, radenie zobrazenia) sú
     aktívne len v režime **Len tituly so streamom**,
   - **Hneď spustiť prvú dávku** spustí po uložení overenie prvých 40 titulov bez ďalšej otázky.
4. Daj **Uložiť do Kodi**. Na televízore príde oznámenie „Katalóg uložený.“

Keď sa QR kód neukáže a príde hlásenie o miestnej sieti, Kodi nepozná svoju adresu vo Wi-Fi. Pokračuj ovládačom
cez **Pokračovať v nastavení v Kodi**.

## Overovanie streamov
Platí pre katalógy v režime **Len tituly so streamom**.

**Vnútri katalógu** je hore riadok **„Overené X z Y – spustiť dávku teraz“**. Klik spustí ručnú dávku 20 titulov.
Priebeh ukazuje ukazovateľ v rohu („Overujem …“) a na konci príde „Dávka hotová – overených …, vyhovuje …“.
Pod riadkom sú len vyhovujúce tituly. Prázdny katalóg hlási „Katalóg sa pripravuje – tituly sa overujú na pozadí.“

**Na pozadí** Kodi overuje samo, kým beží:
- raz za 10 minút dávku 8 titulov, prvýkrát asi 2 minúty po štarte Kodi,
- pri prehrávaní len 1 titul za kolo, nech sa nič nesekáva,
- katalógy (a [Koncerty](koncerty.md)) sa striedajú dokola, takže prvé naplnenie viacerých katalógov trvá hodiny,
- titul, ktorý nevyhovel, sa skúsi znova za 3 dni; vyhovujúce sa kontrolujú každý týždeň. Keď stream zmizne,
  zmizne aj titul z katalógu,
- pri seriáli sa hľadá stream k poslednému odvysielanému dielu,
- zoznam kandidátov sa obnovuje po 6 hodinách, takže nové tituly pribúdajú samy.

Overuje sa cez zdroje zapnuté v tomto zariadení. Na pozadí sa vynechá FastShare bez kreditu, Prehraj.to bez Premium
a HellSpy v pauze po chybe 429 – overovanie by im len uberalo kredit alebo limit.

Overovaných katalógov môže byť najviac 20. Keď je ich viac, Kodi nový katalóg uloží ako **Katalóg z TMDB**
a ohlási „Overovať ide najviac 20 katalógov.“

## Synchronizácia medzi zariadeniami
So zapnutou [synchronizáciou](synchronizace.md) sa katalógy zdieľajú v skupine: **Nastavenia → Synchronizácia →
Čo sa synchronizuje → Synchronizovať vlastné katalógy**.
- Prenáša sa definícia katalógov, zmazanie aj výsledky overenia.
- Výsledky si prevezme len zariadenie s **rovnakými zapnutými zdrojmi**. Mobil bez Luny alebo bez WebShare by
  s cudzími výsledkami ukazoval tituly, ktoré sám neprehrá, a tak si katalóg overí sám.
- Zariadenia v skupine neoverujú rovnaké tituly naraz, každé začne inde. Katalóg sa tak naplní rýchlejšie.
- Keď je v skupine Home Assistant, overuje on a ostatné zariadenia len zobrazujú. Kodi, ktoré má od Home Assistantu
  výsledky mladšie ako 2 hodiny, samo na pozadí neoveruje. Ručná dávka funguje vždy.

## Home Assistant
Home Assistant katalógy dostáva synchronizáciou z Kodi (bez nastavenia, okruh je vždy zapnutý). Beží stále, a tak je
na overovanie ideálny: každú minútu overí jeden titul a výsledky pošle späť do Kodi.

| Čo | Na čo |
|---|---|
| akcia **Stav vlastných katalógov** (`nokturno.catalogs`) | vráti overované katalógy a ich stav |
| akcia **Overiť katalóg hneď** (`nokturno.catalog_verify`) | overí hneď **Počet titulov** (1–50, predvolené 10). **ID katalógu** prázdne = ďalší v poradí. |
| akcia **Pozastaviť overovanie katalógov** (`nokturno.catalog_pause`) | zastaví alebo pustí overovanie na tomto Home Assistante |
| senzor **Katalógy** (`sensor.nokturno_katalogy`) | počet overovaných katalógov; v atribútoch pri každom overené, vyhovuje, celkom a čas poslednej kontroly |

Podrobne v návode [Služby a senzory](../navody/ha/sluzby-a-senzory.md).

## Stremio
V Stremiu sa katalógy skladajú vo formulári nastavení doplnku.

1. Otvor nastavenia doplnku: v Stremiu **Doplnky → Nokturno → Konfigurovať**, alebo stránku
   `http://<IP zariadenia s aplikáciou>:7140/configure`.
2. Nájdi kartu **Vlastné katalógy** a daj **Pridať katalóg**. Každý katalóg má vlastnú záložku („1. Názov“).
3. Vyplň:
   - **Druh** (Filmy alebo Seriály) a prípadne **Zo šablóny**,
   - režim **Katalóg z TMDB** alebo **Len tituly so streamom**,
   - **Žánre**, **Témy**, **Krajina pôvodu**, **Roky** a **Zoradiť podľa**,
   - pri overovanom režime **Jazyk zvuku**, **Titulky**, **Minimálna kvalita**, **5.1 a viac** a **Zobraziť zoradené podľa**,
   - **Názov** (do 40 znakov, doplní sa sám).
4. Daj **Uložiť zmeny** a **doplnok v Stremiu pridaj znova**. Stremio si zoznam katalógov pamätá, takže zmenu
   katalógov pozná len po novom pridaní. Pri účtoch a predvoľbách to nie je potrebné.

- Katalógov môže byť až 20. Ukážu sa na domovskej stránke Stremia hneď za katalógmi Nokturna.
- Overuje aplikácia na pozadí, kým beží: jeden titul za minútu, dokola naprieč všetkými overovanými katalógmi.
  Nový katalóg dostane úvodnú dávku 40 titulov.
- Profily s rovnakými účtami a rovnakým katalógom zdieľajú jedno overovanie. Výsledky Stremia sa s Kodi nesynchronizujú.

## Tipy
| Chceš | Nastav |
|---|---|
| české a slovenské rozprávky, ktoré sa dajú pustiť | Filmy, téma **Rozprávky**, krajina **Česko** a **Slovensko**, režim **Len tituly so streamom** |
| 4K filmy s dabingom (namiesto doterajších Filmov vo vysokej kvalite) | šablóna **Filmy v 4K s CZ dabingom** |
| novinky posledného roka s titulkami | **Posledných X rokov** = 1, **Titulky** Čeština alebo slovenčina, **Zobraziť zoradené podľa** Najnovšie vydanie |
| vianočné komédie | žáner **Komedie**, téma **Vianoce** |
| kórejské thrillery | žáner **Thriller**, krajina **Južná Kórea** |
| najlepšie horory 80. rokov | žáner **Horor**, **Od–do** 1980–1989, **Radiť podľa** Hodnotenia na TMDB |

## Keď niečo nejde
| Čo vidíš | Čo urobiť |
|---|---|
| „Katalóg sa nepodarilo načítať. Skús to neskôr.“ | server Nokturna práve neodpovedá. Skús to o chvíľu. |
| katalóg z TMDB je prázdny | filtre nič nenechali. Uber žáner alebo tému, zvoľ **aspoň jeden vybraný žáner**, alebo rozšír roky. |
| „Katalóg sa pripravuje – tituly sa overujú na pozadí.“ | overovanie ešte beží. Otvor katalóg a daj **spustiť dávku teraz**, alebo počkaj. |
| overený katalóg má málo titulov | požiadavky sú prísne (napríklad 4K + 5.1 + slovenský zvuk). Uvoľni kvalitu alebo jazyk, alebo zapni ďalší zdroj. |
| na mobile je katalóg iný ako na televízore | mobil má iné zdroje, a tak si katalóg overuje sám. Je to v poriadku. |
| v Stremiu sa zmena katalógu neprejavila | doplnok v Stremiu odinštaluj a pridaj znova. |

---
[Všetky návody](./) · [Česky](../cs/vlastni-katalogy)
