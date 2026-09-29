# Synchronizace a přenos

Máš Kodi na televizi, v telefonu a v set-top boxu? **Synchronizace** průběžně sdílí mezi všemi, co máš zhlédnuté, kde sledování skončilo, co máš v Mém seznamu a co hlídáš. **Přenos nastavení** jednorázově zkopíruje účty a volby na další Kodi, ať se nemusí zadávat znovu.

## Synchronizace mezi Kodi

Všechno je v *Nastavení → Synchronizace*.

### Středisko synchronizace

Data si Kodi vyměňují přes jedno ze dvou středisek:

- **Dashboard Nokturna** – funguje odkudkoli a nepotřebuje Home Assistant. Tuto volbu chce většina lidí.
- **Home Assistant** – Kodi v domácí síti se spojí s integrací Nokturno v Home Assistantu přes adresu a klíč.

Ve výchozím stavu je vybraný **Dashboard Nokturna**. Kdo už synchronizuje přes Home Assistant, tomu volba zůstane na Home Assistantu. Tlačítka pro skupinu jsou dostupná jen se zapnutou synchronizací a se střediskem Dashboard Nokturna.

### Dashboard Nokturna: skupina zařízení

1. Na prvním Kodi zapni **Synchronizovat mezi více Kodi**, zkontroluj, že **Středisko synchronizace** je **Dashboard Nokturna**, a zvol **Založit skupinu / otevřít připojení**. Ukáže se kód ve tvaru `NKT-XXXX-XXXX-XXXX-XXXX` – opiš si ho a uschovej.
2. Na dalších Kodi stejné nastavení, ale **Připojit se ke skupině** a zadej kód.
3. Hotovo. Synchronizace běží na pozadí.

Kód pustí nové zařízení do skupiny jen **30 minut** po založení. Stejným tlačítkem **Založit skupinu / otevřít připojení** se skupina znovu otevře, když chceš přidat další zařízení – na dalších 30 minut, kód zůstane stejný.

**Odejít ze skupiny** přestane toto Kodi synchronizovat, nic se nesmaže. Ostatním zařízením kód zůstává; zařízení, které nemá mít přístup, se dá odříznout jen založením nové skupiny a připojením ostatních novým kódem.

**Soukromí:** kód je zároveň klíč. Server drží jen zapečetěná data, která sám nepřečte, a kód ze zařízení nikdy neodchází. Bez kódu data nikdo nepřečte ani neobnoví.

### Home Assistant

- **Home Assistant jako středisko** – vyplň **Adresa Home Assistantu** a **Klíč (z nastavení integrace Nokturno)**. Klíč najdeš v nastavení integrace v Home Assistantu.
- **Home Assistant ve skupině Dashboardu** – když používáš Dashboard Nokturna, zadej týž kód skupiny i v nastavení integrace v Home Assistantu. Home Assistant se stane dalším členem skupiny a karta v něm zůstane aktuální, i když žádné Kodi zrovna neběží. Viz [návod pro Home Assistant](../ha/nastaveni.md).

### Co se synchronizuje

Každý okruh jde zapnout zvlášť:

- **Synchronizovat zhlédnuté a rozkoukané**
- **Synchronizovat Můj seznam**
- **Synchronizovat historii hledání**
- **Synchronizovat Hlídané** – viz [Hlídané](../../cs/hlidane.md)
- **Synchronizovat nastavení doplňku** (výchozí vypnuto) – preferovaný jazyk, řazení streamů, zapnuté zdroje a podobně.
- **Synchronizovat účty ke zdrojům** (výchozí vypnuto) – přihlášení ke zdrojům, vlastnímu úložišti a klíč TMDB. Hesla jdou zašifrovaná a server je nepřečte, ale kdo má kód skupiny, přečte je – kód patří jen tvým zařízením.

Nikdy se nesdílí složka pro stahování, samotné nastavení synchronizace a přihlášení k CZtoru a Traktu – ta se párují na každém zařízení zvlášť.

**Synchronizovat teď** (v nastavení a v Mém seznamu) spustí výměnu hned. Na telefonu s Androidem se synchronizuje hlavně ve chvíli, kdy je Kodi otevřené – na pozadí mu systém často vypne připojení.

## Přenos nastavení do dalšího Kodi

*Nastavení → Nastavit z mobilu a přenos → Přenos nastavení.* Jednorázově zkopíruje účty a volby. Hodí se, když si pořizuješ další zařízení.

**Přes internet:**

1. Na původním Kodi zvol **Odeslat do jiného Kodi**. Ukáže se kód ve tvaru `NKT-XXXX-XXXX`, platí 15 minut a použije se jednou.
2. Na novém Kodi zvol **Načíst z jiného Kodi** a kód zadej.
3. Doplněk ukáže, co se změní, a teprve pak nastavení zapíše. Kopie původního nastavení zůstane v profilu doplňku.

**Přes soubor** (třeba na USB): **Uložit do souboru** vytvoří soubor a ukáže kód, bez kterého soubor nikdo nepřečte. Na druhém Kodi **Načíst ze souboru** a zadej kód.

Co se nepřenáší: přihlášení k **CZtoru** a **Traktu** (nové Kodi hned nabídne spárování), složka pro stahování, nastavení synchronizace a ID instalace. Přenesená data jsou zašifrovaná kódem a server je nepřečte.
