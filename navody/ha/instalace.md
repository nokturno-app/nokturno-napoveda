# Instalace

## 1. HACS

1. Home Assistant → **HACS** → tři tečky vpravo nahoře → **Vlastní repozitáře**.
2. Adresa: `https://github.com/nokturno-app/nokturno-ha`, kategorie **Integrace** → Přidat.
3. Vyhledej **Nokturno** v HACS → Stáhnout.
4. Restartuj Home Assistant.

## 2. Přidat integraci

**Nastavení → Zařízení a služby → Přidat integraci → Nokturno.**

Průvodce jde krok po kroku:

1. **Právní upozornění** – bez souhlasu integraci přidat nejde.
2. **Přehrávání** – přehrávače Kodi a předvolby streamů.
3. **Vlastní úložiště** – adresa WebDAV složky (NAS, Nextcloud), jméno a heslo. Krok jde přeskočit a úložiště doplnit později.
4. **Volitelné zdroje** – výběr zdrojů třetích stran. Ve výchozím stavu není vybraný žádný.
5. **Údaje vybraných zdrojů** – jen pro zdroje vybrané v předchozím kroku.
6. **CZtor – spárování** – jen když vybereš CZtor, viz [Nastavení](nastaveni.md#cztor).

Katalog a hledání fungují i bez úložiště a bez jediného zdroje. Stahování, synchronizace a další úložiště se nastavují až v Nastavení integrace, jednotlivá pole popisuje [Nastavení](nastaveni.md).

Po dokončení integrace zaregistruje kartu `custom:nokturno-card` do zdrojů Lovelace sama (když dashboard běží v režimu UI, ne v YAML).

## 3. Přidat kartu na dashboard

Úprava dashboardu → Přidat kartu → vyhledej **Nokturno** (nebo ručně `type: custom:nokturno-card`). Senzor stahování, se kterým karta pracuje, se při přidání přes editor doplní sám.

## 4. Propojit s Kodi

Integrace pouští tituly v Kodi přes `plugin://plugin.video.nokturno/…`. Na zařízení, kde se má přehrávat, proto potřebuješ **nainstalovaný [doplněk Nokturno pro Kodi](../kodi/instalace.md)** a Kodi musí být v Home Assistantu jako entita `media_player` (standardní integrace Kodi). Které přehrávače karta nabízí, nastavíš v [Nastavení → Přehrávání](nastaveni.md#prehravani).

## Aktualizace

HACS nabídne aktualizaci integrace i karty sám. Seznam vydání je v sekci [Releases](https://github.com/nokturno-app/nokturno-ha/releases). Po aktualizaci restartuj Home Assistant a mobilní aplikaci úplně zavři a otevři znovu, ať si stáhne novou verzi karty.

**Aktualizace se v HACS neukázala?** HACS obnovuje data ručně přidaných repozitářů jen jednou za 48 hodin. Vynutíš to v HACS → Nokturno → tři tečky → **Update information** (Aktualizovat informace); pak se nabídne **Aktualizovat**.

**Formulář po aktualizaci ukazuje místo popisků anglické klíče** (`pref_surround`, `kodi_entity`)? Prohlížeč drží staré překlady. Restartuj Home Assistant a stránku obnov i s vyprázdněním cache (Ctrl+Shift+R).

Pokračuj na [Nastavení](nastaveni.md).
