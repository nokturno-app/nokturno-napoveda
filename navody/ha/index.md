# Nokturno pro Home Assistant

Integrace a karta **Nokturno** pro Home Assistant. Je to především přehrávač **vlastního úložiště** (WebDAV – NAS, Nextcloud, server). Volitelně umí hledat i u vyhledávačů třetích stran (WebShare, Sosáč, Luna, HellSpy, Sledujteto, FastShare, CZtor, Přehraj.to). Titul pustí v Kodi nebo na jiném přehrávači, stáhne ho i s titulky do Home Assistantu, pošle odkaz do mobilu a hlídá nové díly seriálů i filmy, které zatím nikde nejsou.

![Výsledky hledání v kartě](images/karta-vysledky.png)

## V kostce

- **Vlastní úložiště** – až tři WebDAV složky. Soubory, které k titulu patří, jsou mezi streamy první a pustí se v Kodi i na jiném přehrávači. Viz [Nastavení](nastaveni.md#vlastni-uloziste) a [Používání](pouzivani.md#soubory-z-vlastniho-uloziste).
- **Karta na dashboardu** – hledání, výběr streamu, přehrání, stažení a poslání do mobilu bez dálkového ovladače.
- **Stahování do Home Assistantu** i s titulky a **odkazy do mobilu**.
- **Hlídané** – kontrola nových dílů hlídaných seriálů (každých 6 hodin) a dostupnosti hlídaných titulů (jednou denně). Oznámení přijde, až se dá opravdu dívat. Kontrola je společná s Kodi, takže se na každém zařízení neopakuje. Podrobně v nápovědě: [Hlídané: nové díly a Kontrolovat dál](../../cs/hlidane.md).
- **Stav zdrojů** – senzor, který hlásí, který zdroj potřebuje zásah; hodí se na automatizaci.
- **Synchronizace s Kodi** – zhlédnuté, rozkoukané, Můj seznam, historie hledání a Hlídané, doma přes klíč a kdekoli přes skupinu.
- **Česky, slovensky i anglicky** podle jazyka Home Assistantu.

Integrace sdílí zdroje i logiku s [doplňkem Nokturno pro Kodi](../kodi/index.md). Co který zdroj dělá a co potřebuje, je podrobně v [návodu pro Kodi, stránka Zdroje a účty](../kodi/zdroje-a-ucty.md) – platí i tady.

## Právní upozornění

Nokturno je především přehrávač **vlastního úložiště** – obsahu, který si nahraješ a zpřístupníš (třeba přes WebDAV). Vyhledávače třetích stran jsou jen volitelná doplňková služba, Nokturno samo žádný obsah nehostuje. Plné znění podmínek je na [nokturno.stream/terms](https://nokturno.stream/terms).

## Pomoc

Když něco nejde, najdi hlášku v **[nápovědě](../../index.md)**. Kam napsat, když nepomůže: [Kde hledat pomoc](../../cs/kde-hledat-pomoc.md), nejrychleji [Discord](https://discord.gg/ChmMPmDDEj).
