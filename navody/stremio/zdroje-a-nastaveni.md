# Zdroje a nastavení

Hlavní funkcí je [vlastní úložiště](#vlastni-uloziste). Ostatní zdroje jsou **volitelné vyhledávače třetích stran** – zapneš si je jen ty, se svým účtem, doplněk sám žádný obsah nehostuje.

| Zdroj | Co dává | Co potřebuje |
|---|---|---|
| **Vlastní úložiště** | tvoje soubory z NAS, Nextcloudu nebo serveru, vždy první mezi streamy | adresa WebDAV složky, případně jméno a heslo |
| **WebShare** | největší výběr souborů, všechny kvality až po 4K; přehrává se přímo z WebShare | účet WebShare, pro plynulé přehrávání **VIP** |
| **Sosáč** | české filmy a seriály s dabingem a titulky, po dílech | účet **Streamuj.tv** (přehrává se odtamtud) |
| **Sledujteto** | velký výběr filmů a seriálů, rozlišení a zvuk posílá přímo jejich rozhraní | účet Sledujteto, k přehrání **Premium** |
| **FastShare / Sdilej.cz** | velký výběr filmů a seriálů, rozlišení posílá přímo jejich rozhraní | hledání nic, k přehrání účet s **kreditem** nebo neomezeným stahováním |
| **HellSpy** | veřejné původní soubory zdarma | nic – stačí ho zapnout (v novém profilu je vypnutý) |
| **Přehraj.to** | velký výběr, hraje v prohlížeči i v aplikaci | účet Přehraj.to, s **Premium** původní soubor |
| **CZtor** | placený katalog, plná kvalita včetně 4K a dabingu, hraje i v prohlížeči | předplatné cztor.com, spárování PINem |

## Vlastní úložiště

Sekce **Vlastní úložiště a zdroje** ve formuláři, první karta **Vlastní úložiště** – až tři složky s vlastními soubory na WebDAV (NAS, Nextcloud, server). U každého: **název** (ukáže se u streamu), **adresa složky**, **uživatelské jméno** a **heslo**. Tlačítko **Ověřit úložiště** zkusí přečíst kořen složky a řekne, kolik v něm je položek, nebo proč to nejde.

- Soubory, které k filmu nebo dílu patří, jsou ve Stremiu **mezi streamy první**; místo zdroje je u nich název úložiště.
- **Soubor přehrávači předává aplikace Nokturno** (od verze 9.6.1), přihlášení k úložišti do Stremia neodchází a data tečou přes aplikaci. Ve webovém přehrávači Stremia v prohlížeči záleží na formátu souboru (`.mkv`, `.avi` a podobné nepřehraje), v aplikaci (Stremio, Nuvio) hrají.
- Úložiště musí být dosažitelné **ze zařízení, kde běží aplikace Nokturno** (ta v něm hledá soubory a předává je přehrávači). Přehrávač potřebuje dosáhnout jen na aplikaci. Když je aplikace doma, stačí adresa z domácí sítě.
- Jak soubory pojmenovat (rok u filmu, `S01E02` u dílu, **složka s originálním názvem** u filmů s odlišným českým názvem – Stremio zná tituly často jen anglicky) je podrobně v [článku Jak připojit vlastní úložiště](../../cs/vlastni-uloziste.md#jak-pojmenovat-soubory).
- Nový soubor se objeví nejpozději do hodiny.

## Volitelné zdroje

Zdroje třetích stran jsou na dalších kartách sekce **Vlastní úložiště a zdroje**. Všechny jsou volitelné a v novém
profilu vypnuté.

### WebShare

Vyplň uživatelské jméno (nebo e-mail) a heslo z webshare.cz. Bez **VIP** WebShare stahování zpomalí natolik, že se film nedá plynule přehrávat. **Ověřit účet** ukáže, jestli přihlášení prošlo a kolik dní VIP zbývá.

Nechceš mít heslo v nastavení čitelné? Místo hesla jde vložit 40znakový „salted hash“, který používají i jiné doplňky WebShare.

### Sosáč (přes Streamuj.tv)

Katalog Sosáče je veřejný, streamy se ale přehrávají ze Streamuj.tv – proto jméno a heslo odtamtud. Streamuj neumí přihlášení ověřit dopředu, **Zkontrolovat** ověří jen tvar údajů; špatné heslo se pozná až při prvním přehrání. Místo hesla jde vložit i jeho 32znakový otisk, jaký ukládá doplněk Nokturno pro Kodi.

### Sledujteto

Vyplň e-mail a heslo ze sledujteto.cz. Hledá se s jakýmkoli účtem, **přehrát jde jen s Premium** – bez něj se streamy ukážou, ale nepustí se. **Ověřit účet** ukáže, jestli je Premium aktivní.

Rozlišení, počet kanálů a kodek zvuku se berou přímo z rozhraní Sledujteto. Podle podmínek Sledujteto nesmí jeden účet používat lidé z různých domácností.

### FastShare / Sdilej.cz

Vyplň uživatelské jméno a heslo z fastshare.cz. Účet ze **Sdilej.cz** funguje taky – soubory jsou stejné, jen přepni **Účet z** na *Sdilej.cz* ([FastShare s účtem ze Sdilej.cz](../../cs/sdilej-cz.md)). Hledá se i bez účtu, **přehrání jde z kreditu** (podle přenesených dat) nebo s neomezeným stahováním. **Ověřit účet** ukáže zbývající kredit.

Soubor přehrávači předává **aplikace Nokturno** (od verze 9.6.1), přihlášení do Stremia neodchází. Ve webovém přehrávači v prohlížeči záleží na formátu souboru. Zvukové stopy se z hlavičky souboru čtou jen s neomezeným stahováním; na kredit je jazyk jen odhadem z názvu.

### HellSpy

Veřejná úschovna, žádný účet, nic nestojí. Volba **Používat HellSpy** je v novém profilu vypnutá, zapni ji, když ho chceš používat.

### Přehraj.to

Do formuláře zadáš **svůj účet Přehraj.to** (e-mail a heslo). **Ověřit účet** zkontroluje, že přihlášení funguje a jestli je účet Premium.

Účet je tu **povinný**, bez vyplněného účtu se zdroj nenabídne. Doplněk pro Kodi a integrace pro Home Assistant umí Přehraj.to i bez přihlášení, jen s nižší kvalitou.

S **Premium** účtem se přehrává původní soubor včetně 4K, bez Premia jen překódovaná verze (nižší kvalita). Soubor hraje **v prohlížeči i v aplikaci** – jde o přímou adresu, která nepotřebuje přihlašovací hlavičky.

### CZtor

Placený katalog [cztor.com](https://cztor.com) se streamy v plné kvalitě včetně 4K a dabingu. Heslo se nikam nezadává, zařízení se páruje PINem:

1. Na cztor.com si založ účet a aktivuj předplatné.
2. Ve formuláři klikni na **Spárovat CZtor**. Ukáže se PIN a odkaz na `cztor.com/activate`.
3. Tam se přihlas a PIN zadej. Formulář to za pár vteřin sám pozná.
4. Adresa doplňku se tím změní – doplněk pak přidej do aplikace znovu.

Do adresy doplňku jde jen náhodný klíč. Aplikace tvoje přihlášení drží zapečetěné tímto klíčem, takže ho bez adresy nikdo nepřečte. **Zrušit párování** ho zruší. CZtor hraje i ve webovém přehrávači.

Podrobně v nápovědě: [CZtor: „zařízení není spárované“](../../cs/cztor.md).

### OpenSubtitles a Luna

Titulky z **OpenSubtitles** má zatím jen doplněk pro Kodi.

**Luna** má vlastní doplněk do Stremia; Nokturno ji nepoužívá. Klidně můžeš mít nainstalované oba – některé soubory z WebShare pak uvidíš dvakrát, jednou od Luny, jednou od Nokturna.

## Předvolby

- **Preferovaný jazyk zvuku** – čeština, slovenština, angličtina, maďarština, nebo *nezáleží*. Streamy s touto řečí jdou nahoru.
- **Řazení streamů** – nejlepší kvalita / největší / nejmenší soubory nahoře / podle zdroje. Ve Stremiu je bez posouvání vidět jen pár prvních řádků, proto na řazení záleží.
- **Skrýt streamy v SD kvalitě** – vynechá nahrávky pod 720p.
- **Skrýt Dolby Vision bez záložní vrstvy (profil 5)** – vynechá streamy, které televize bez Dolby Vision ukáže zeleně a fialově. Poznáme je z hlavičky souboru (u prvních streamů výpisu), u ostatních jen podle označení P5 v názvu.
- **Skrýt AV1** – vynechá streamy s kodekem AV1, pro přehrávače, které ho neumí (starší Shield, Apple TV).
- **Upřednostnit prostorový zvuk 5.1**
- **Nejvyšší datový tok (Mb/s)** – pro pomalejší internet; orientačně Full HD 8–15 Mb/s, 4K 25–60 Mb/s.

## Co se u streamu zobrazuje

Vlevo kvalita (a značky jako HDR10, DV nebo DV only, které poznáváme z hlavičky souboru u prvních streamů výpisu, jinak podle názvu), vpravo název souboru, jazyky zvuku jako vlaječky s počtem kanálů a kodekem (např. `🇨🇿 5.1 AC3`), titulky, velikost, datový tok, délka a zdroj. Vlnovka (`~Full HD`) znamená odhad, ne údaj ze zdroje nebo ze souboru.

## Vlastní katalogy

Karta **Vlastní katalogy** – až 20 seznamů filmů a seriálů na domovské stránce Stremia (a v Nuviu). **Přidat katalog** založí nový, každý má vlastní záložku.

- **Ze šablony** – Populární, Nejlépe hodnocené, Nové s CZ dabingem, Filmy ve 4K s CZ dabingem, České filmy a seriály, Pohádky s CZ dabingem. Šablonu jde dál upravit.
- **Katalog z TMDB** ukáže hned všechny tituly podle filtrů. **Jen tituly se streamem** ověřuje na pozadí, dokud aplikace běží, a ukáže jen to, co jde přehrát v požadované kvalitě, jazyce zvuku a titulků a s 5.1.
- Filtry: žánry, témata (Pohádky, Vánoce, Podle skutečné události… nejvýš 3), země původu (nejvýš 5), roky (od–do, posledních X let) a řazení.
- **Název** do 40 znaků se vyplní sám, přepsat ho jde.

Ověřuje se 1 titul za minutu napříč všemi ověřovanými katalogy, nový katalog dostane úvodní dávku 40 titulů. Podrobně v nápovědě: [Vlastní katalogy](../../cs/vlastni-katalogy.md).

Dřívější karta Katalogy (Populární, Nejlépe hodnocené) zmizela, zapnuté katalogy se samy převedly na vlastní katalogy.

## Koncerty

Koncerty se hledají ve tvém vlastním úložišti a volitelně v úložištích třetích stran, která máš povolená a nastavená. Karta **Koncerty** – zaškrtni hudební žánry a vyplň **Last.fm API klíč** (zdarma na [last.fm/api/account/create](https://www.last.fm/api/account/create)). Ve Stremiu přibude druh **Koncerty** se seznamy **Nově přidané** a **Podle abecedy** (s výběrem žánru). Hledá se na pozadí, dokud aplikace běží. Podrobně: [Koncerty](../../cs/koncerty.md).

## Po změně katalogů

Stremio si seznam katalogů pamatuje – po změně vlastních katalogů nebo koncertů dej **Uložit změny** a doplněk ve Stremiu odinstaluj a přidej znovu. Účty a předvolby platí hned i bez toho.

**Sezónní a tematické katalogy** (třeba vánoční filmy nebo Film pro dnešní den) přidáváme sami. Nezapínají se ve formuláři – jsou v doplňku vždy, na začátku seznamu katalogů, a sezónní po sezóně zase zmizí. Stremio si seznam katalogů pamatuje, nový katalog proto někdy uvidíš až po obnovení doplňku.

## Statistiky

Aplikace posílá anonymní statistiky: náhodný identifikátor nastavení, verzi, které zdroje máš zapnuté a u kterých titulů se otevřely streamy – nejvýš jednou za 6 hodin. Žádné účty, hesla ani adresa doplňku. Vypneš je v souboru `nokturno.json` volbou `"stats": false`, hlášení o pádech volbou `"crash_reports": false`, viz [Nokturno pro Stremio – aplikace](../../cs/stremio-aplikace.md).
