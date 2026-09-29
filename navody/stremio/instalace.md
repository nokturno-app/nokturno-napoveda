# Instalace

Doplněk se přidává adresou, kterou vyrobí **formulář nastavení** – **[nokturno.stream/configure](https://nokturno.stream/configure)**. Formulář provede třemi kroky: zdroje a účty, předvolby a přidání do aplikace.

![Formulář nastavení doplňku, karta Vlastní úložiště](images/stremio-formular.jpg)

## 1. Vyplň zdroje

Stačí jeden zdroj, víc zdrojů najde víc streamů. U každého je rozbalovací návod (registrace, co vyplnit) a tlačítko, které účet rovnou ověří – **Ověřit účet**, u vlastního úložiště **Ověřit úložiště**, u CZtoru **Spárovat CZtor**. Řekne, jestli přihlášení prošlo a jestli máš VIP, Premium nebo kredit, bez kterého se nedá plynule přehrávat. Podrobnosti ke zdrojům jsou na stránce [Zdroje a nastavení](zdroje-a-nastaveni.md).

## 2. Předvolby (nepovinné)

Jazyk zvuku (čeština, slovenština, angličtina, maďarština), řazení streamů, skrytí SD, upřednostnění zvuku 5.1 a [katalogy](zdroje-a-nastaveni.md#katalogy). Výchozí nastavení sedí většině lidí.

## 3. Přidat do aplikace

- **Počítač** – klikni na **Přidat do Stremia**, prohlížeč se zeptá, jestli otevřít Stremio, a ve Stremiu potvrď **Instalovat**.
- **Telefon** – otevři formulář v telefonu, kde máš Stremio, a postupuj stejně. Když se aplikace neotevře, použij **Zkopírovat adresu** a vlož ji ručně: *Doplňky → pole nahoře → Instalovat*.
- **Nuvio** (telefon i TV) – klikni na **Přidat do Nuvia**. Nuvio na TV bez prohlížeče: **Zkopírovat adresu** a vlož ji v Nuviu mezi doplňky.
- **Streamlet** – odkaz pro přidání doplňku nemá. Použij **Zkopírovat adresu** a vlož ji ve Streamletu jako doplněk Stremia.
- **Televize** – nainstaluj doplněk na počítači nebo telefonu **pod stejným účtem Stremio**. Doplňky se mezi zařízeními synchronizují samy a na TV se objeví do minuty.

Soubory z vlastního úložiště a FastShare se přehrávají přímo ze zdroje, takže je webový přehrávač Stremia v prohlížeči nepustí – použij aplikaci Stremio nebo Nuvio.

> Adresa doplňku obsahuje tvoje účty. Není zašifrovaná, jen zakódovaná – kdo ji má, přehrává přes tvoje účty. Nikomu ji neposílej.

## Změna nastavení

Ve Stremiu **Doplňky → Nokturno → ozubené kolo (Konfigurovat)** otevře formulář s tvým současným nastavením. Po úpravě znovu klikni na **Přidat do Stremia** (nebo Nuvia). Změněné nastavení je nová adresa – starou verzi doplňku pak odinstaluj, ať nemáš Nokturno dvakrát.

## Doplněk přidaný ze staré adresy

Doplněk dnes běží na `nokturno.stream`. Kdo ho přidal dřív ze staré adresy, tomu přestal fungovat a musí ho přidat znovu:

1. Ve Stremiu doplněk Nokturno odinstaluj.
2. Otevři **[nokturno.stream/configure](https://nokturno.stream/configure)**, vyplň účty a předvolby znovu.
3. Přidej doplněk do aplikace podle kroku 3 výš.

Stará adresa nese nastavení, proto se nedá na novou převést automaticky.

## Identita v adrese

Formulář do adresy vkládá podepsanou **identitu**. Získá se krátkým výpočtem přímo v prohlížeči (na počítači kolem sekundy, na telefonu pár sekund) – stránka mezitím funguje a identita se do adresy dopíše po dokončení. Identita je jen náhodné číslo podepsané serverem, nenese žádné osobní údaje. Adresa bez identity a bez účtů se nepřijímá. Místo streamů pak uvidíš položku **⚠️ Nokturno** s textem „Adresa doplňku je zastaralá.“ Otevři nastavení doplňku (ozubené kolo), vytvoří se nová adresa. Pak starý doplněk odeber a nový přidej.
