---
slug: soukromi
lang: cs
title: Soukromí a data
products: [kodi, ha, stremio]
priority: 3
templates:
  kodi: |
    Ahoj, Nokturno posílá na náš server jen anonymní statistiky (náhodné ID instalace, verze, zapnuté zdroje, tituly, u kterých se otevřely streamy) a hlášení o chybách. Hesla, účty a adresy úložišť neodcházejí nikdy.
    Vypnout jde v Nokturno → Nastavení → Statistiky → Odesílat anonymní statistiky.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/soukromi
    Tým Nokturno
---

# Soukromí a data

Nokturno používáš u sebe a pro sebe. Hesla a účty ke zdrojům zůstávají ve tvém zařízení, na náš server
(`nokturno.stream`) posílají doplňky jen anonymní údaje o používání. Tady je přehled, co přesně to je a jak to vypneš.
Úplné znění je na stránce [Zpracování osobních údajů](https://nokturno.stream/privacy).

## Co doplňky posílají na server
- **Anonymní statistiky**, nejvýš jednou za 6 hodin: náhodné ID instalace, verze doplňku, platforma a jazyk,
  které zdroje máš zapnuté (jen přepínače, žádné účty) a tituly, u kterých se otevřely streamy. Kodi k tomu přidá
  technické údaje o spolehlivosti (skin, architektura, způsob aktualizace, počty přehrání, doba načítání).
- **Aplikace Nokturno pro Stremio** od verze 9.0.6 přidá i údaje o serveru, na kterém běží: náhodné ID serveru,
  jak běží (počítač, Android, Home Assistant, VPS), systém a počet nastavení. Žádnou adresu, doménu ani jméno.
- **Hlášení o pádech**, když v doplňku nastane chyba v kódu (Kodi a aplikace pro Stremio): typ chyby, místo v kódu,
  verze a pár řádků logu. Adresy, účty, hesla a IP se předem vymažou. Výpadky zdrojů se neposílají.
- **Log** jen na vyžádání, když ho sám pošleš tlačítkem **Odeslat log Kodi**. Hesla, tokeny, e-maily a IP adresy
  doplněk před odesláním vymaže. Viz [Jak poslat log](poslat-log.md).
- **Synchronizace, přenos nastavení a SyncWatch** jen když je použiješ. Data zašifruje tvoje zařízení kódem skupiny,
  server je nepřečte.

Po vypnutí statistik se dál posílá jen údaj, že instalace žije: náhodné ID a verze (Kodi i způsob aktualizace).
Tituly ani zdroje ne.

## Co se neposílá nikdy
- hesla, tokeny ani jména k účtům ke zdrojům,
- adresa doplňku pro Stremio (jsou v ní tvoje účty),
- adresy tvých úložišť a obsah hledání.

Ke statistikám se neukládá IP adresa. Server si jako každý web vede technické záznamy o požadavcích i s IP adresou
a drží je 14 dní kvůli provozu a ochraně před zneužitím.

## Kde jsou hesla
Jen ve tvém zařízení: v nastavení doplňku v Kodi, v integraci v Home Assistantu, nebo u aplikace Nokturno pro Stremio
na tvém vlastním serveru. Doplněk pro Stremio, který běží **na cizím serveru**, ale tvoje přihlašovací údaje vidí,
protože jsou v adrese doplňku. Proto ho pouštěj jen u sebe, viz [Nokturno pro Stremio – aplikace](stremio-aplikace.md).

## Jak sběr vypnout
| Kde | Jak |
|---|---|
| Kodi | **Nokturno → Nastavení → Statistiky → Odesílat anonymní statistiky**. Hlášení o pádech vypneš zvlášť volbou **Posílat hlášení o chybách**, s vypnutými statistikami se neposílají vůbec. |
| Home Assistant | **Nastavení → Zařízení a služby → Nokturno → Konfigurovat → Ostatní → Posílat anonymní statistiky** |
| Aplikace pro Stremio | v souboru `nokturno.json` volby `"stats": false` a `"crash_reports": false`, při spuštění ze zdrojového kódu proměnné `NOKTURNO_STATS=0` a `NOKTURNO_CRASH_REPORTS=0`. V doplňku Home Assistantu jsou obě volby v záložce **Konfigurace**. |

## Jak dlouho se data drží
| Co | Jak dlouho |
|---|---|
| profil instalace (ID, verze, platforma, zapnuté zdroje) | 90 dní od posledního hlášení |
| zhlédnuté tituly u náhodného ID instalace | bez časového omezení |
| log, který pošleš | 30 dní |
| hlášení o pádu | 90 dní od posledního výskytu chyby |
| zpráva, kterou ti pošleme do doplňku | 90 dní |
| synchronizace | 90 dní od posledního použití |
| přenos nastavení | 15 minut, nebo do vyzvednutí |
| technické záznamy serveru | 14 dní |

Zálohy databáze serveru se mažou do 30 dnů. Podrobnosti, souhrnné statistiky a tvoje práva (přístup, výmaz, námitka)
jsou na stránce [Zpracování osobních údajů](https://nokturno.stream/privacy). O údaje nebo jejich výmaz si řekneš
na privacy@nokturno.stream, uveď ID instalace (Kodi: **Nastavení → Pokročilé → Verze a ID této instalace**).

---
[Všechny návody](../) · [Slovensky](../sk/soukromi)
