# Nokturno pro Stremio

Doplněk **Nokturno** přidá k filmům a seriálům ve Stremiu (i v Nuviu a dalších přehrávačích s doplňky Stremia) streamy z tvého **vlastního úložiště** (WebDAV) a volitelně i z vyhledávačů třetích stran – **WebShare, Sosáč, Sledujteto, FastShare / Sdilej.cz, HellSpy, Přehraj.to a CZtor**, často s českým dabingem nebo titulky. Tituly hledáš ve Stremiu jako obvykle, streamy Nokturna se objeví v detailu filmu nebo dílu mezi ostatními.

## V kostce

- **Vlastní úložiště** – až tři WebDAV složky s vlastními soubory, mezi streamy jako první. Viz [Zdroje a nastavení](zdroje-a-nastaveni.md#vlastni-uloziste).
- **Volitelně i další zdroje.** K titulu, který si otevřeš, Nokturno dohledá soubory i v českých a slovenských úschovnách. Názvy, plakáty a popisy má Stremio samo; Nokturno volitelně přidá vlastní [katalogy](zdroje-a-nastaveni.md#katalogy) (žebříček Nejsledovanější, nově přidané s CZ/SK dabingem a titulky). Sezónní a tematické katalogy, které připravujeme my, jsou v doplňku vždy.
- **Každý má vlastní nastavení.** Účty se neukládají na server – jsou zakódované v adrese doplňku, kterou ti vyrobí formulář nastavení. Adresu proto nikomu neposílej. Výjimkou je [CZtor](zdroje-a-nastaveni.md#cztor): do adresy jde jen náhodný klíč a přihlášení zůstává na serveru zapečetěné tímto klíčem. V adrese je i podepsaná **identita**, kterou formulář vydá po krátkém výpočtu v prohlížeči.
- **Bere se jen to, co k titulu patří.** Soubory se filtrují podle názvu, roku a dílu; podobné, ale jiné filmy (pokračování, stejnojmenné tituly) se vynechají.
- **Výpadek zdroje nevadí.** Když jeden zdroj neodpovídá, doplněk ho přeskočí a vrátí streamy z ostatních.
- **Data tečou přímo.** Soubory z vlastního úložiště a FastShare se přehrávají přímo ze zdroje, ne přes server doplňku. Přehrají se proto **jen v aplikaci** (Stremio, Nuvio), ne ve webovém přehrávači v prohlížeči. Přehraj.to a CZtor hrají i v prohlížeči.
- **Zprávy.** Občas se mezi streamy objeví položka **📢 Nokturno** s krátkou zprávou od nás. Když na ni klepneš, přestane se ti ukazovat.
- **Česky i slovensky.** Formulář je v obou jazycích. Nastavení uložené ve slovenském formuláři má slovensky i hlášky doplňku mezi streamy.

## Adresa doplňku se změnila

Doplněk běží na **[nokturno.stream](https://nokturno.stream/)**. Kdo ho přidal před 23. 9. 2026 ze staré adresy, musí ho přidat znovu z formuláře **[nokturno.stream/configure](https://nokturno.stream/configure)** – adresa nese nastavení a na novou se převést nedá. Postup je na stránce [Instalace](instalace.md).

## Právní upozornění

Nokturno je především přehrávač **vlastního úložiště** – obsahu, který si nahraješ a zpřístupníš (třeba přes WebDAV). Vyhledávače třetích stran jsou jen volitelná doplňková služba, Nokturno samo žádný obsah nehostuje. Plné znění podmínek je na [nokturno.stream/terms](https://nokturno.stream/terms).

## Pomoc

Když něco nejde, najdi hlášku v **[nápovědě](../../index.md)**. Kam napsat, když nepomůže: [Kde hledat pomoc](../../cs/kde-hledat-pomoc.md), nejrychleji [Discord](https://discord.gg/ChmMPmDDEj).
