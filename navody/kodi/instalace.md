# Instalace

Doplněk běží na Kodi 20 Nexus a novějším, testujeme ho na Kodi 21 Omega (Android TV, CoreELEC, Windows). Rozhraní je česky, slovensky, anglicky a maďarsky.

## 1. Povolit neznámé zdroje

**Nastavení → Systém → Doplňky → Neznámé zdroje** – zapnout. Bez toho Kodi odmítne nainstalovat cokoli mimo oficiální repozitář Kodi.

## 2. Doporučený způsob – přes repozitář (automatické aktualizace)

Přímo v Kodi, bez počítače a prohlížeče (funguje i na TV a set-top boxech bez klávesnice):

1. **Nastavení → Správce souborů → Přidat zdroj**, jako adresu zadej
   `https://nokturno.stream/repo/` a pojmenuj ji třeba `Nokturno`.
2. **Doplňky → Instalovat ze souboru ZIP → Nokturno → repository.nokturno → repository.nokturno.zip**.
3. **Doplňky → Instalovat z repozitáře → Nokturno repozitář → Video doplňky → Nokturno → Instalovat**.

Odtud už Kodi nové verze stahuje samo – podle nastavení aktualizací je rovnou nainstaluje, nebo jen nabídne. Adresa `nokturno.stream/repo/` slouží jen k první instalaci; aktualizace pak jdou přímo z GitHubu.

Alternativa: ZIP repozitáře stáhnout v prohlížeči (`repository.nokturno.zip`) a přenést do zařízení s Kodi přes USB nebo síť, pak pokračovat od kroku 2.

### Aktualizace hned, ne až za den

Kodi kontroluje repozitáře jednou denně. Když víš o nové verzi, **Nastavení doplňku → Pokročilé → Zkontrolovat aktualizace doplňků** vyžádá kontrolu okamžitě. Totéž udělá místní nabídka (podržet OK nebo pravé tlačítko) na **Nokturno repozitář → Zkontrolovat aktualizace**.

### Beta verze

Novinky dřív, ale můžou obsahovat chyby: **Doplňky → Instalovat z repozitáře → Nokturno repozitář → Repozitáře doplňků → Nokturno repozitář (beta) → Instalovat**. Kodi pak nabízí stabilní verze i bety a vždy nainstaluje tu nejnovější; po vydání stabilní verze se beta sama nahradí stabilní. Zpět jen na stabilní verze: beta repozitář odinstaluj a v Informacích o doplňku vyber poslední stabilní verzi.

## 3. Ruční instalace bez repozitáře (bez automatických aktualizací)

Stáhni konkrétní verzi `plugin.video.nokturno-x.y.z.zip` ze sekce [Releases](https://github.com/nokturno-app/plugin.video.nokturno/releases), pak v Kodi **Doplňky → Instalovat ze souboru ZIP**. Nové verze se pak stahují a instalují ručně.

## Návrat na starší verzi

Místní nabídka na doplňku **Nokturno → Informace → Verze** – repozitář nabízí i předchozí vydání.

## Souhlas s podmínkami použití

Při prvním otevření se doplněk zeptá na souhlas s podmínkami použití (**Souhlasím** / **Nesouhlasím**). Bez souhlasu se menu neotevře. Podmínky si kdykoli přečteš v *Nastavení → Podmínky použití → Zobrazit podmínky*, případně na <https://nokturno.stream/terms>.

## Průvodce prvním nastavením

Po souhlasu se nabídne **průvodce nastavením** se třemi možnostmi:

- **Z mobilu** – na TV se ukáže QR kód, v mobilu vyplníš účty v pohodlném formuláři (viz [Nastavit z mobilu](nastaveni.md#nastavit-z-mobilu)).
- **Průvodce ovladačem** – série otázek ano/ne: WebShare, Sosáč (účet Streamuj.tv), Luna, HellSpy, Sledujteto, FastShare nebo Sdilej.cz, CZtor, klíč TMDB. Kde je potřeba účet, vyplníš jméno a heslo.
- **Přeskočit** – všechno jde doplnit později v nastavení.

Na konci se průvodce zeptá, jestli **změřit rychlost internetu** a podle ní nastavit nejvyšší datový tok. Když máš doplněk **TMDb Helper**, nabídne i nastavení Nokturna jako přehrávače pro tlačítko Přehrát v detailu filmu a **přepnutí jazyka TMDb Helperu** na jazyk Kodi (TMDb Helper ho z Kodi nepřebírá, detail filmu by jinak byl anglicky).

**Lunu průvodce najde v síti sám** a rovnou ukáže, kde si vyzvednout token. Podrobný postup je na stránce [Nastavení Luny krok za krokem](nastaveni-luny.md).

Po aktualizaci ze starší verze se průvodce sám nenabídne, pokud už máš nějaký zdroj zapnutý. Ručně ho spustíš v **Nastavení → Pokročilé → Průvodce nastavením**. Dokud nemáš nastavený žádný zdroj, je průvodce v hlavním menu jako první položka.

## Co dál

Katalog a hledání fungují hned i bez nastavení. K přehrání potřebuješ vlastní úložiště nebo aspoň jeden volitelný zdroj: pokračuj na [Vlastní úložiště](vlastni-uloziste.md) nebo [Zdroje a účty](zdroje-a-ucty.md). Nastavení z jednoho Kodi do dalšího přeneseš podle stránky [Synchronizace a přenos](synchronizace.md#prenos-nastaveni-do-dalsiho-kodi).
