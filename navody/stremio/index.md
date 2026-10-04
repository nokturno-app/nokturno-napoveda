# Nokturno pro Stremio

!!! danger "Doplněk na cizím serveru dostává tvoje přihlašovací údaje"
    Každý doplněk pro Stremio, který běží na cizím serveru, dostává tvoje přihlašovací údaje ke zdrojům
    (vlastní úložiště, WebShare, FastShare…). Jsou v adrese doplňku, provozovatel serveru je proto může vidět
    a uložit a musíš mu věřit. Jistotu máš jen s doplňkem, který běží u tebe.

**Nokturno pro Stremio** je aplikace, která běží u tebe – na počítači, NASu, Android TV boxu nebo jako doplněk Home Assistantu – a přidá k filmům
a seriálům ve Stremiu (i v Nuviu a dalších přehrávačích s doplňky Stremia) streamy z tvého **vlastního úložiště** (WebDAV)
a volitelně i z vyhledávačů třetích stran, které si zapneš – **WebShare, Sosáč, Sledujteto, FastShare / Sdilej.cz, HellSpy,
Přehraj.to a CZtor**. Tituly hledáš ve Stremiu jako obvykle, streamy Nokturna se objeví v detailu filmu nebo dílu mezi ostatními.

## V kostce

- **Běží u tebe.** Aplikaci stáhneš z [vydání na GitHubu](https://github.com/nokturno-app/nokturno-stremio-app/releases/latest)
  pro Windows, macOS, Linux nebo Android a sama se aktualizuje. Doplněk funguje, jen když aplikace běží. Viz [Nokturno pro Stremio – aplikace](../../cs/stremio-aplikace.md).
- **Vlastní úložiště** – až tři WebDAV složky s vlastními soubory, mezi streamy jako první. Viz [Zdroje a nastavení](zdroje-a-nastaveni.md#vlastni-uloziste).
- **Volitelně i další zdroje.** K titulu, který si otevřeš, Nokturno dohledá soubory i u zdrojů, které si zapneš.
  Názvy, plakáty a popisy má Stremio samo; Nokturno volitelně přidá vlastní [katalogy](zdroje-a-nastaveni.md#vlastni-katalogy).
- **Každý má vlastní nastavení.** Od verze 9.6.0 je uložené v aplikaci jako pojmenovaný profil a adresa doplňku nese jen jeho klíč. Změny platí bez nového přidání doplňku, viz [Jak přidat Nokturno do Stremia nebo Nuvia](../../cs/stremio-instalace.md).
  Adresu proto nikomu neposílej.
- **Bere se jen to, co k titulu patří.** Soubory se filtrují podle názvu, roku a dílu; podobné, ale jiné filmy
  (pokračování, stejnojmenné tituly) se vynechají.
- **Výpadek zdroje nevadí.** Když jeden zdroj neodpovídá, doplněk ho přeskočí a vrátí streamy z ostatních.
- **Většina dat teče přímo.** WebShare, HellSpy, Přehraj.to, CZtor, Sledujteto a Sosáč se přehrávají přímo ze zdroje.
  Soubory z vlastního úložiště a FastShare (i Sdilej.cz) přehrávači od verze 9.6.1 předává aplikace Nokturno a data tečou přes ni.
  Ve webovém přehrávači v prohlížeči záleží na formátu souboru: `.mkv`, `.avi` a podobné nepřehraje, v aplikaci (Stremio, Nuvio) hrají.
- **Česky i slovensky.** Formulář je v obou jazycích. Nastavení uložené ve slovenském formuláři má slovensky i hlášky doplňku mezi streamy.

## Podmínky použití

Nokturno je přehrávač a vyhledávač nad tvým vlastním úložištěm a volitelně i nad úložišti třetích stran, které si zapneš. Samo žádný obsah
nehostuje a neověřuje, jestli je soubor na cizím úložišti legální. Používej ho jen k obsahu, ke kterému máš právo.
Plné znění podmínek je na [nokturno.stream/terms](https://nokturno.stream/terms).

## Pomoc

Když něco nejde, najdi hlášku v **[nápovědě](../../index.md)**. Kam napsat, když nepomůže: [Kde hledat pomoc](../../cs/kde-hledat-pomoc.md), nejrychleji [Discord](https://discord.gg/ChmMPmDDEj).
