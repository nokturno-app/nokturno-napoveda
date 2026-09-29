---
slug: soukromi
lang: sk
title: Súkromie a dáta
products: [kodi, ha, stremio]
priority: 3
templates:
  kodi: |
    Ahoj, Nokturno posiela na náš server len anonymné štatistiky (náhodné ID inštalácie, verzia, zapnuté zdroje, tituly, pri ktorých sa otvorili streamy) a hlásenia o chybách. Heslá, účty a adresy úložísk neodchádzajú nikdy.
    Vypnúť sa dá v Nokturno → Nastavenia → Štatistiky → Odosielať anonymné štatistiky.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/soukromi
    Tím Nokturno
---

# Súkromie a dáta

Nokturno používaš u seba a pre seba. Heslá a účty k zdrojom zostávajú v tvojom zariadení, na náš server
(`nokturno.stream`) posielajú doplnky len anonymné údaje o používaní. Tu je prehľad, čo presne to je a ako to vypneš.
Úplné znenie je na stránke [Spracovanie osobných údajov](https://nokturno.stream/privacy).

## Čo doplnky posielajú na server
- **Anonymné štatistiky**, najviac raz za 6 hodín: náhodné ID inštalácie, verzia doplnku, platforma a jazyk,
  ktoré zdroje máš zapnuté (len prepínače, žiadne účty) a tituly, pri ktorých sa otvorili streamy. Kodi k tomu pridá
  technické údaje o spoľahlivosti (skin, architektúra, spôsob aktualizácie, počty prehraní, doba načítania).
- **Aplikácia Nokturno pre Stremio** od verzie 9.0.6 pridá aj údaje o serveri, na ktorom beží: náhodné ID servera,
  ako beží (počítač, Android, Home Assistant, VPS), systém a počet nastavení. Žiadnu adresu, doménu ani meno.
- **Hlásenia o pádoch**, keď v doplnku nastane chyba v kóde (Kodi a aplikácia pre Stremio): typ chyby, miesto v kóde,
  verzia a pár riadkov logu. Adresy, účty, heslá a IP sa vopred vymažú. Výpadky zdrojov sa neposielajú.
- **Log** len na vyžiadanie, keď ho sám pošleš tlačidlom **Odoslať log Kodi**. Heslá, tokeny, e-maily a IP adresy
  doplnok pred odoslaním vymaže. Pozri [Ako poslať log](poslat-log.md).
- **Synchronizácia, prenos nastavení a SyncWatch** len keď ich použiješ. Dáta zašifruje tvoje zariadenie kódom skupiny,
  server ich neprečíta.

Po vypnutí štatistík sa ďalej posiela len údaj, že inštalácia žije: náhodné ID a verzia (Kodi aj spôsob aktualizácie).
Tituly ani zdroje nie.

## Čo sa neposiela nikdy
- heslá, tokeny ani mená k účtom k zdrojom,
- adresa doplnku pre Stremio (sú v nej tvoje účty),
- adresy tvojich úložísk a obsah vyhľadávania.

K štatistikám sa neukladá IP adresa. Server si ako každý web vedie technické záznamy o požiadavkách aj s IP adresou
a drží ich 14 dní kvôli prevádzke a ochrane pred zneužitím.

## Kde sú heslá
Len v tvojom zariadení: v nastavení doplnku v Kodi, v integrácii v Home Assistante, alebo pri aplikácii Nokturno pre Stremio
na tvojom vlastnom serveri. Doplnok pre Stremio, ktorý beží **na cudzom serveri**, ale tvoje prihlasovacie údaje vidí,
pretože sú v adrese doplnku. Preto ho spúšťaj len u seba, pozri [Nokturno pre Stremio – aplikácia](stremio-aplikace.md).

## Ako zber vypnúť
| Kde | Ako |
|---|---|
| Kodi | **Nokturno → Nastavenia → Štatistiky → Odosielať anonymné štatistiky**. Hlásenia o pádoch vypneš zvlášť voľbou **Posielať hlásenia o chybách**, s vypnutými štatistikami sa neposielajú vôbec. |
| Home Assistant | **Nastavenia → Zariadenia a služby → Nokturno → Konfigurovať → Ostatné → Posielať anonymné štatistiky** |
| Aplikácia pre Stremio | v súbore `nokturno.json` voľby `"stats": false` a `"crash_reports": false`, pri spustení zo zdrojového kódu premenné `NOKTURNO_STATS=0` a `NOKTURNO_CRASH_REPORTS=0`. V doplnku Home Assistantu sú obe voľby v záložke **Konfigurácia**. |

## Ako dlho sa dáta držia
| Čo | Ako dlho |
|---|---|
| profil inštalácie (ID, verzia, platforma, zapnuté zdroje) | 90 dní od posledného hlásenia |
| log, ktorý pošleš | 30 dní |
| hlásenie o páde | 90 dní od posledného výskytu chyby |
| správa, ktorú ti pošleme do doplnku | 90 dní |
| synchronizácia | 90 dní od posledného použitia |
| prenos nastavení | 15 minút, alebo do vyzdvihnutia |
| technické záznamy servera | 14 dní |

Zálohy databázy servera sa mažú do 30 dní. Podrobnosti, súhrnné štatistiky a tvoje práva (prístup, výmaz, námietka)
sú na stránke [Spracovanie osobných údajov](https://nokturno.stream/privacy). O údaje alebo ich výmaz si povieš
na privacy@nokturno.stream, uveď ID inštalácie (Kodi: **Nastavenia → Pokročilé → Verzia a ID tejto inštalácie**).

---
[Všetky návody](./) · [Česky](../cs/soukromi)
