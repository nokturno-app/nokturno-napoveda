---
slug: vlastni-katalogy
lang: cs
title: Vlastní katalogy
products: [kodi, ha, stremio]
priority: 3
templates:
  kodi: |
    Ahoj, od verze 10.0 si katalog poskládáš sám a Nokturno ti v něm může nechat jen tituly, ke kterým je stream podle tvých požadavků.
    1. Filmy nebo Seriály → Vlastní katalogy → Nový katalog.
    2. Zvol Nastavit přes mobil (doporučujeme), naskenuj QR kód a vyber šablonu, třeba Filmy ve 4K s CZ dabingem.
    3. Režim Jen tituly se streamem ověřuje tituly na pozadí, první dávka prověří 40 titulů hned.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/vlastni-katalogy
    Tým Nokturno
  stremio: |
    Ahoj, vlastní katalogy (až 20) jsou v nastavení doplňku, karta Vlastní katalogy → Přidat katalog. Začít jde ze šablony.
    Po změně katalogů doplněk ve Stremiu přidej znovu, ať je aplikace načte.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/vlastni-katalogy
    Tým Nokturno
---

# Vlastní katalogy

Vlastní katalog je seznam filmů nebo seriálů, který si poskládáš sám: podle žánrů, témat, země původu, let a řazení.
Od verze 10.0 umí katalog navíc **ověřovat streamy** – ukáže jen tituly, ke kterým Nokturno našlo stream
v požadované kvalitě, s dabingem nebo titulky a třeba s 5.1. Tituly vybírá server Nokturna, vlastní klíč TMDB
k tomu nepotřebuješ. Když ho máš (od verze 10.0.1), katalogy se berou přímo z TMDB a server je jen záloha:
fungují i při jeho výpadku a server nevidí tvoje filtry.

Funguje v Kodi a ve Stremiu. Home Assistant katalogy nezakládá, ale umí je [ověřovat za ostatní](#home-assistant).

## Dva režimy katalogu
| Režim | Co ukáže | Kdy se hodí |
|---|---|---|
| **Katalog z TMDB** | hned všechny tituly podle filtrů, po 20 na stránku | procházení, tipy na filmy. U titulu bez streamu si zapni [hlídání](hlidane.md) – Hlídané dají vědět, až stream bude. |
| **Jen tituly se streamem** | jen tituly, které jdou přehrát podle tvých požadavků | „chci 4K s CZ dabingem a nechci klikat naprázdno“ |

V režimu **Jen tituly se streamem** se katalog plní postupně. Nokturno na pozadí prochází kandidáty (zhruba 200
nejoblíbenějších titulů podle filtrů) a u každého hledá stream. Co vyhoví, se v katalogu objeví.

## Šablony
Šablona je hotový katalog, který si můžeš upravit. Nabízí ji stránka v mobilu a formulář Stremia.

| Šablona | Co dělá |
|---|---|
| Populární filmy, Populární seriály | co se teď na TMDB nejvíc sleduje |
| Nejlépe hodnocené filmy, Nejlépe hodnocené seriály | nejlépe hodnocené na TMDB |
| Nové filmy s CZ dabingem, Nové seriály s CZ dabingem | posledních 2 roky, jen tituly se streamem s českým zvukem |
| Filmy ve 4K s CZ dabingem | jen filmy se streamem ve 4K a s českým zvukem |
| České filmy, České seriály | země původu Česko |
| Pohádky s CZ dabingem | téma Pohádky, jen tituly se streamem s českým zvukem |

**Kde jsou Populární a Nejlépe hodnocené z menu?** Od verze 10.0 nejsou pevnou položkou v menu Filmy a Seriály.
Když je chceš, založ si je ze šablony – a můžeš si je rovnou upravit, třeba jen na posledních 5 let.

## Kodi: založení katalogu
1. **Filmy** nebo **Seriály → Vlastní katalogy → Nový katalog**. Druh katalogu (filmy, nebo seriály) se řídí tím,
   kde jsi.
2. Nokturno nabídne dvě cesty:
   - **Nastavit přes mobil (doporučujeme)** – na televizi se ukáže QR kód, celý katalog vyplníš v telefonu
     a můžeš začít ze šablony. Postup je níž v části [Nastavení přes mobil](#nastaveni-pres-mobil).
   - **Pokračovat v nastavení v Kodi** – projdeš dialogy ovladačem (bez šablon).
3. Katalog se objeví ve **Vlastních katalozích**. Kliknutím ho otevřeš.

### Dialogy v Kodi, v tomto pořadí
| Dialog | Co vybrat |
|---|---|
| **Režim katalogu** | **Katalog z TMDB**, nebo **Jen tituly se streamem** |
| **Žánry (nic = všechny)** | jeden nebo víc žánrů. Seriály mají jiný seznam (třeba **Sci-fi a fantasy**, **Dětský**). |
| **Témata (stačí jedno, nejvýš 3)** | Pohádky, Vánoce, Halloween, Silvestr, Podle skutečné události, Podle knihy, Životopisný, Superhrdinové, Sériový vrah, 2. světová válka, Bojová umění, Sport, Mimozemšťané, Cestování časem, Zombie, Duchové, Upíři, Postapokalypsa, Loupež, Špionáž, Přežití, Psi, Dinosauři |
| **Tituly musí mít** | jen při dvou a víc žánrech: **všechny vybrané žánry**, nebo **aspoň jeden vybraný žánr** |
| **Země původu (nejvýš 5)** | Česko, Slovensko, USA, Velká Británie, Francie, Německo, Itálie, Španělsko, Polsko, Maďarsko, Jižní Korea, Japonsko, Dánsko, Švédsko, Norsko |
| **Roky** | **Bez omezení**, **Od–do** (rok od a do, prázdné = bez omezení), nebo **Posledních X let** (1–50, výchozí 5) |
| **Řadit podle** | **Oblíbenosti**, **Hodnocení na TMDB** (jen tituly s dost hlasy), **Data vydání** (nejnovější první), **Abecedy** (oblíbené tituly podle názvu) |
| **Jazyk zvuku** * | Libovolné, Čeština, Slovenština, Čeština nebo slovenština, Angličtina, Maďarština |
| **Titulky** * | stejné možnosti jako jazyk zvuku |
| **Minimální kvalita** * | Libovolná, Full HD, 2K, 4K |
| **Kanály zvuku** * | Libovolné, nebo **5.1 a víc** |
| **Zobrazit seřazené podle** * | **Nově nalezené**, **Stejně jako výběr**, nebo **Nejnovější vydání** |
| **Ikona katalogu** | Filmy, Seriály, Seznam, Hvězda, Žebříček, Žánr, Rok, Země, Sbírka, Novinky, Herci, Studia |
| **Název katalogu** | předvyplní se z voleb (třeba „Pohádky · Česko · CZ dabing · posledních 5 let“), můžeš ho přepsat |

\* jen v režimu **Jen tituly se streamem**.

Téma a žánr se kombinují: s žánrem **Komedie** a tématem **Vánoce** dostaneš vánoční komedie. Z vybraných témat
stačí, když titul má jedno. Zrušení kteréhokoli dialogu tlačítkem Zpět zruší celé zakládání.

Po uložení katalogu v režimu **Jen tituly se streamem** se Nokturno zeptá **„Spustit ověření streamů nyní?“**. **Ano** spustí první
dávku – ta hned prověří 40 titulů, ať je v katalogu co ukázat.

### Úprava a smazání
Místní nabídka katalogu (dlouhý stisk OK, nebo tlačítko menu na ovladači):
- **Upravit katalog** – projde stejné dialogy, předvybrané jsou uložené volby. Název, který jsi přepsal, zůstane.
- **Upravit na mobilu** – QR kód jako při zakládání.
- **Smazat katalog** – ještě se zeptá „Smazat katalog …?“.
- **Zobrazit v hlavním menu** – katalog se ukáže přímo ve Filmech nebo Seriálech, nad položkou Vlastní katalogy (od verze 10.1). **Odebrat z hlavního menu** ho vrátí jen pod Vlastní katalogy.

## Nastavení přes mobil
1. Na televizi zvol **Nastavit přes mobil (doporučujeme)** (u nového katalogu), nebo **Upravit na mobilu**
   (v místní nabídce katalogu).
2. Připoj telefon ke stejné Wi-Fi jako Kodi a naskenuj QR kód. Adresa platí 30 minut a pro jedno uložení.
3. Na stránce **Nokturno – Vlastní katalogy**:
   - nahoře vyber **Šablonu** a dej **Načíst šablonu** – pole se vyplní,
   - uprav, co potřebuješ. Pole pro ověřování (jazyk zvuku, titulky, kvalita, 5.1, řazení zobrazení) jsou
     aktivní jen v režimu **Jen tituly se streamem**,
   - **Hned spustit první dávku** spustí po uložení ověření prvních 40 titulů bez dalšího dotazu.
4. Dej **Uložit do Kodi**. Na televizi přijde oznámení „Katalog uložen.“

Když se QR kód neukáže a přijde hláška o místní síti, Kodi nezná svoji adresu ve Wi-Fi. Pokračuj ovladačem
přes **Pokračovat v nastavení v Kodi**.

## Ověřování streamů
Platí pro katalogy v režimu **Jen tituly se streamem**.

**Uvnitř katalogu** je nahoře řádek **„Ověřeno X z Y – spustit dávku nyní“**. Klik spustí ruční dávku 20 titulů.
Průběh ukazuje ukazatel v rohu („Ověřuji …“) a na konci přijde „Dávka hotová – ověřeno …, vyhovuje …“.
Pod řádkem jsou jen vyhovující tituly. Prázdný katalog hlásí „Katalog se připravuje – tituly se ověřují na pozadí.“

**Na pozadí** Kodi ověřuje samo, dokud běží:
- jednou za 10 minut dávku 8 titulů, poprvé asi 2 minuty po startu Kodi,
- při přehrávání jen 1 titul za kolo, ať se nic neseká,
- katalogy (a [Koncerty](koncerty.md)) se střídají dokola, takže první naplnění víc katalogů trvá hodiny,
- titul, který nevyhověl, se zkusí znovu za 3 dny; vyhovující se kontroluje každý týden. Když stream zmizí,
  zmizí i titul z katalogu,
- u seriálu se hledá stream k poslednímu odvysílanému dílu,
- seznam kandidátů se obnovuje po 6 hodinách, takže nové tituly přibývají samy.

Ověřuje se přes zdroje zapnuté v tomto zařízení. Na pozadí se vynechá FastShare bez kreditu, Přehraj.to bez Premium
a HellSpy v pauze po chybě 429 – ověřování by jim jen ubíralo kredit nebo limit.

Ověřovaných katalogů může být nejvýš 20. Když je jich víc, Kodi nový katalog uloží jako **Katalog z TMDB**
a ohlásí „Ověřovat jde nejvýš 20 katalogů.“

## Synchronizace mezi zařízeními
Se zapnutou [synchronizací](synchronizace.md) se katalogy sdílí ve skupině: **Nastavení → Synchronizace →
Co se synchronizuje → Synchronizovat vlastní katalogy**.
- Přenáší se definice katalogů, smazání i výsledky ověření.
- Výsledky si převezme jen zařízení se **stejnými zapnutými zdroji**. Mobil bez Luny nebo bez WebShare by
  s cizími výsledky ukazoval tituly, které sám nepřehraje, a tak si katalog ověří sám.
- Zařízení ve skupině neověřují stejné tituly naráz, každé začne jinde. Katalog se tak naplní rychleji.
- Když je ve skupině Home Assistant, ověřuje on a ostatní zařízení jen zobrazují. Kodi, které má od Home Assistantu
  výsledky mladší než 2 hodiny, samo na pozadí neověřuje. Ruční dávka funguje vždy.

## Home Assistant
Home Assistant katalogy dostává synchronizací z Kodi (bez nastavení, okruh je vždy zapnutý). Běží pořád, a tak je
na ověřování ideální: každou minutu ověří jeden titul a výsledky pošle zpátky do Kodi.

| Co | K čemu |
|---|---|
| akce **Stav vlastních katalogů** (`nokturno.catalogs`) | vrátí ověřované katalogy a jejich stav |
| akce **Ověřit katalog hned** (`nokturno.catalog_verify`) | ověří hned **Počet titulů** (1–50, výchozí 10). **ID katalogu** prázdné = další v pořadí. |
| akce **Pozastavit ověřování katalogů** (`nokturno.catalog_pause`) | zastaví nebo pustí ověřování na tomto Home Assistantu |
| senzor **Katalogy** (`sensor.nokturno_katalogy`) | počet ověřovaných katalogů; v atributech u každého ověřeno, vyhovuje, celkem a čas poslední kontroly |

Podrobně v návodu [Služby a senzory](../navody/ha/sluzby-a-senzory.md).

## Stremio
Ve Stremiu se katalogy skládají ve formuláři nastavení doplňku.

1. Otevři nastavení doplňku: ve Stremiu **Doplňky → Nokturno → Konfigurovat**, nebo stránku
   `http://<IP zařízení s aplikací>:7140/configure`.
2. Najdi kartu **Vlastní katalogy** a dej **Přidat katalog**. Každý katalog má vlastní záložku („1. Název“).
3. Vyplň:
   - **Druh** (Filmy nebo Seriály) a případně **Ze šablony**,
   - režim **Katalog z TMDB** nebo **Jen tituly se streamem**,
   - **Žánry**, **Témata**, **Země původu**, **Roky** a **Řadit podle**,
   - u ověřovaného režimu **Jazyk zvuku**, **Titulky**, **Minimální kvalita**, **5.1 a víc** a **Zobrazit seřazené podle**,
   - **Název** (do 40 znaků, doplní se sám).
4. Dej **Uložit změny** a **doplněk ve Stremiu přidej znovu**. Stremio si seznam katalogů pamatuje, takže změnu
   katalogů pozná jen po novém přidání. U účtů a předvoleb to potřeba není.

- Katalogů může být až 20. Ukážou se na domovské stránce Stremia hned za katalogy Nokturna.
- Ověřuje aplikace na pozadí, dokud běží: jeden titul za minutu, dokola napříč všemi ověřovanými katalogy.
  Nový katalog dostane úvodní dávku 40 titulů.
- Profily se stejnými účty a stejným katalogem sdílí jedno ověřování. Výsledky Stremia se s Kodi nesynchronizují.

## Tipy
| Chceš | Nastav |
|---|---|
| české a slovenské pohádky, které jdou pustit | Filmy, téma **Pohádky**, země **Česko** a **Slovensko**, režim **Jen tituly se streamem** |
| 4K filmy s dabingem (místo dřívějších Filmů ve vysoké kvalitě) | šablona **Filmy ve 4K s CZ dabingem** |
| novinky posledního roku s titulky | **Posledních X let** = 1, **Titulky** Čeština nebo slovenština, **Zobrazit seřazené podle** Nejnovější vydání |
| vánoční komedie | žánr **Komedie**, téma **Vánoce** |
| korejské thrillery | žánr **Thriller**, země **Jižní Korea** |
| nejlepší horory 80. let | žánr **Horor**, **Od–do** 1980–1989, **Řadit podle** Hodnocení na TMDB |

## Když něco nejde
| Co vidíš | Co udělat |
|---|---|
| „Katalog se nepodařilo načíst. Zkus to později.“ | server Nokturna zrovna neodpovídá. Zkus to za chvíli. |
| katalog z TMDB je prázdný | filtry nic nenechaly. Uber žánr nebo téma, zvol **aspoň jeden vybraný žánr**, nebo rozšiř roky. |
| „Katalog se připravuje – tituly se ověřují na pozadí.“ | ověřování teprve běží. Otevři katalog a dej **spustit dávku nyní**, nebo počkej. |
| ověřený katalog má málo titulů | požadavky jsou přísné (třeba 4K + 5.1 + slovenský zvuk). Uvolni kvalitu nebo jazyk, nebo zapni další zdroj. |
| na mobilu je katalog jiný než na televizi | mobil má jiné zdroje, a tak si katalog ověřuje sám. Je to v pořádku. |
| ve Stremiu se změna katalogu neprojevila | doplněk ve Stremiu odinstaluj a přidej znovu. |

---
[Všechny návody](../) · [Slovensky](../sk/vlastni-katalogy)
