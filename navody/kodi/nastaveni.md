# Nastavení

Nastavení otevřeš položkou **Nastavení** na konci hlavního menu doplňku, nebo v Kodi přes místní nabídku na doplňku (podržet OK nebo pravé tlačítko) → **Nastavení**. Vlevo jsou kategorie, vpravo jejich volby. U každé volby je dole v okně krátká nápověda.

![Nastavení Nokturna: vlevo kategorie, vpravo volby](images/kodi-nastaveni.jpg)

| Kategorie | Co v ní je |
|---|---|
| **Vlastní úložiště** | až tři WebDAV složky s tvými soubory, viz [Vlastní úložiště](../../cs/vlastni-uloziste.md) |
| **Zdroje a účty** | volitelné zdroje, OpenSubtitles, TMDB a Trakt.tv, viz [Zdroje a účty](zdroje-a-ucty.md) |
| **Nastavit z mobilu a přenos** | vyplnění nastavení v telefonu a přenos do dalšího Kodi |
| **Přehrávání** | jazyk, titulky, kvalita, řazení streamů, stahování |
| **Výběr streamu** | co se u streamu v dialogu ukazuje a v jakém pořadí |
| **Synchronizace** | sdílení zhlédnutého, Mého seznamu a Hlídaných mezi tvými Kodi, viz [Synchronizace a přenos](synchronizace.md) |
| **Statistiky** | anonymní statistiky a hlášení o chybách |
| **Pokročilé** | průvodce, údržba, odeslání logu, informace o doplňku |
| **Podmínky použití** | souhlas s podmínkami a jejich plné znění |

## Nastavit z mobilu

Na TV se ukáže QR kód. Otevři ho mobilem připojeným ke stejné Wi-Fi a vyplň nastavení v prohlížeči – účty, hesla i ostatní volby, bez psaní ovladačem. Funguje jen v místní síti a adresa platí 30 minut. Hesla se na stránku v mobilu nikdy neposílají zpět, prázdné pole heslo nemění.

Na stránce z mobilu jdou rovnou i tlačítka **Najít Lunu v síti** a **Ověřit nastavení Luny**. Na Androidu jde adresu pod QR kódem i ťuknout a otevřít v prohlížeči.

Ve stejné kategorii je **Přenos nastavení** (Odeslat do jiného Kodi, Načíst z jiného Kodi, Uložit do souboru, Načíst ze souboru) – popsaný na stránce [Synchronizace a přenos](synchronizace.md#prenos-nastaveni-do-dalsiho-kodi).

## Přehrávání

- **Preferovaný jazyk zvuku** – Libovolný / Čeština / Slovenština / Angličtina / Maďarština. Streamy s tímto jazykem zvuku jsou vždy nahoře, ostatní pod nimi. Nic se neschovává, jen se to přeřadí.
- **Preferovat prostorový zvuk (5.1 a víc)** – při stejné kvalitě jde nahoru stream s prostorovým zvukem.
- **Automaticky přepnout zvuk na preferovaný jazyk** – po spuštění se vybere zvuková stopa v preferovaném jazyce, i když má soubor jako výchozí jinou.
- **Titulky** – *Nechat na Kodi* / *Když chybí zvuk v preferovaném jazyce* / *Vždy v preferovaném jazyce*. Ve výchozím stavu se titulky zapnou, když zvuk v preferovaném jazyce není (čeština a slovenština se navzájem zastoupí), a vypnou se, když zvuk v preferovaném jazyce je.
- **Skrýt SD streamy** – streamy pod 720p se ze seznamu úplně vyřadí.
- **Skrýt 3D streamy** – 3D soubory (podle názvu nebo hlavičky souboru) se nezobrazí nikdy, ani když jiný stream není. Podrobně v nápovědě: [Výběr streamu: filtry, 3D a poslední filtr](../../cs/vyber-streamu.md).
- **Max. datový tok (Mb/s, 0 = bez omezení)** – přepočítá se na velikost souboru podle stopáže otevřeného titulu. Tlačítko **Změřit rychlost a nastavit datový tok** změří připojení a limit nastaví samo.
- **Řazení streamů** – *Jak přišly* / *Nejdřív nejlepší kvalita* / *Nejdřív největší* / *Nejdřív nejmenší*.
- **Zjišťovat zvuk ze souboru (kolik streamů)** – u kolika streamů od začátku seznamu doplněk přečte začátek souboru a zjistí jazyk a počet kanálů tam, kde je zdroj neřekl. Výsledek si pamatuje měsíc. 0 = nezjišťovat.
- **TV program: ukázat i dnes už skončené pořady**

Stejné verze souboru (kvalita, zvuk, titulky a velikost do 10 %) doplněk vždy sloučí do jednoho řádku, viz [Používání](pouzivani.md#vyber-streamu).

### Stahování

**Složka pro stahování** – kam se ukládají stažená videa a jejich titulky. Může to být i síťová složka (například `smb://`); do ní se ale přerušené stahování nenavazuje a začne znovu. Bez nastavené složky se v menu neukáže položka **Stažené**.

## Výběr streamu

Co se u každého streamu v dialogu výběru ukazuje a v jakém pořadí:

- **Nastavit z mobilu** – položky přesouváš šipkami mezi horním a dolním řádkem. Pohodlnější než psát pořadí ručně.
- **Co a v jakém pořadí ukazovat u streamu** – položky oddělené čárkou, svislítko dělí horní a dolní řádek. Možnosti: `langs` (jazyky zvuku), `size` (velikost), `video` (rozlišení a kodek), `audio` (zvukové stopy), `bitrate` (datový tok), `length` (délka), `subs` (titulky), `source` (zdroj), `file` (název souboru). Co chybí, se nezobrazí. Kvalita je vždy obrázek vlevo.
- **Výchozí pořadí** – vrátí výchozí položky.
- **Automaticky použít poslední filtr** – dialog se otevře rovnou s naposledy použitým filtrem. Když by u titulu nenechal žádný stream, ukážou se všechny.

## Synchronizace

Středisko, skupina a co se sdílí – celé na stránce [Synchronizace a přenos](synchronizace.md).

## Statistiky

- **Odesílat anonymní statistiky** – náhodné id instalace, verze, platforma a počty zobrazení titulů. Žádné účty, hesla ani IP. Po vypnutí se posílá jen id instalace a verze, aby bylo vidět, že instalace žije.
- **Odeslat statistiky teď**
- **Posílat hlášení o chybách** – když v doplňku nastane chyba v kódu, pošle se krátké hlášení (typ chyby, místo v kódu, verze a pár řádků logu Nokturna). Adresy, účty, hesla a IP se předem vymažou, výpadky zdrojů se neposílají.

Co přesně se posílá, popisuje [README repozitáře](https://github.com/nokturno-app/plugin.video.nokturno#anonymní-statistiky).

## Pokročilé

**Údržba**

- **Průvodce nastavením** – spustí [průvodce prvním nastavením](instalace.md#pruvodce-prvnim-nastavenim) znovu.
- **Vymazat cache (katalogy, hledání, streamy)** (ve starších verzích Vymazat cache API) – doplněk si pamatuje katalogy, výsledky hledání a seznamy streamů; po vymazání je načte znovu.
- **Ověřit zdroje** (ve starších verzích Otestovat zdroje) – ověří všechny zapnuté zdroje i klíč TMDB naráz a řekne, co konkrétně nefunguje.
- **Přidat Nokturno do TMDb Helperu (Přehrát v detailu filmu)** – viz [Používání](pouzivani.md#prehrat-z-detailu-filmu-tmdb-helper).
- **Zkontrolovat aktualizace doplňků** – nová verze se nabídne hned, ne až při denní kontrole Kodi.
- **Odeslat log Kodi** – pošle posledních ~500 KB `kodi.log`, abychom mohli nahlášený problém dohledat. Tokeny, hesla, e-maily a IP se z logu předem vymažou. Funguje i s vypnutými statistikami. Viz [Řešení problémů](../../index.md).

**Informace** – web `nokturno.stream`, rodina doplňků (Kodi, Stremio, Home Assistant), **Verze a ID této instalace** (ID se hodí, když nám hlásíš chybu), fóra (xbmc-kodi.cz, stremio.cz) a **Právní upozornění**.

## Podmínky použití

- **Souhlasím s podmínkami použití** – bez souhlasu se menu doplňku neotevře. Poprvé se doplněk zeptá sám dialogem, viz [Instalace](instalace.md#souhlas-s-podminkami-pouziti).
- **Zobrazit podmínky** – plné znění. Najdeš ho i na <https://nokturno.stream/terms>.
