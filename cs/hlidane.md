---
slug: hlidane
lang: cs
title: "Hlídané: nové díly a Kontrolovat dál"
products: [kodi, ha]
priority: 2
templates:
  kodi: |
    Ahoj, na to jsou v Nokturnu Hlídané. Nokturno se samo ozve, až půjde titul pustit.
    1. Seriál: v kontextovém menu seriálu dej Hlídat nové díly.
    2. Film nebo seriál, který zatím nikde není: v kontextovém menu dej Hlídat, až bude k dispozici.
    3. Díl má streamy, ale ne takové, jaké chceš (třeba bez CZ titulků): v kontextovém menu dílu dej Kontrolovat dál. Nokturno se ozve, až streamů přibude.
    Seznam je v hlavním menu pod Pokračovat ve sledování, položka Hlídané.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/hlidane
    Tým Nokturno
---

# Hlídané: nové díly a Kontrolovat dál

Hlídané si pamatují, na co čekáš. Nokturno se samo ozve, až to půjde pustit:
- **nový díl** seriálu, který sleduješ,
- **film nebo seriál, který zatím nikde není**,
- titul nebo díl, který streamy má, ale **ne takové, jaké chceš** (třeba bez CZ titulků nebo bez 5.1).
  Na to je **Kontrolovat dál**: Nokturno ho hlídá dál a ozve se, až streamů přibude.

Hlídané jsou v Kodi a v Home Assistantu. Ve Stremiu nejsou.

## Kodi

### Jak něco přidat
| Na co čekáš | Kde |
|---|---|
| nové díly seriálu | kontextové menu seriálu → **Hlídat nové díly** |
| film nebo seriál, který zatím nikde není | kontextové menu titulu → **Hlídat, až bude k dispozici** |
| díl, který streamy má, ale ne takové, jaké chceš | kontextové menu dílu → **Kontrolovat dál 2x02** (s číslem toho dílu) |
| film, který streamy má, ale ne takové, jaké chceš | **Hlídat, až bude k dispozici**, po první kontrole v Hlídaných kontextové menu → **Kontrolovat dál** |

Když se u titulu nenajde žádný stream, Nokturno se zeptá samo: „Ozvat se, až bude k dispozici?“ Stačí potvrdit.
U dílu seriálu se tím začne hlídat celý seriál.

Z Hlídaných titul odebereš v kontextovém menu: **Přestat hlídat nové díly**, **Přestat hlídat** nebo **Nekontrolovat dál**.
Zhlédnutý film nebo díl zmizí z Hlídaných sám, díl i tehdy, když už máš zhlédnutý některý další.

### Seznam Hlídané
Položka **Hlídané** je v hlavním menu hned pod **Pokračovat ve sledování**. Ukáže se, jakmile v ní něco je.
Když přibyl nový díl, je to vidět rovnou v menu („Hlídané · 1 nový díl“).

- **Seriály** jsou nahoře, s novým dílem první: „Zrádci · nový díl 3x02“. Bez nového dílu je u seriálu poslední díl,
  který jde pustit. Kliknutím seriál otevřeš a nový díl tím zhasne. V kontextovém menu je navíc
  **Označit nový díl jako viděný** a **Kontrolovat dál** u posledního dílu. U seriálu i u hlídaného dílu je v kontextovém menu
  **Seznam dílů** a **Všechny série**.
- **Tituly** jsou pod seriály a mají stav:

| Stav | Co znamená |
|---|---|
| lze pustit | titul má streamy, kliknutím otevřeš výběr streamu |
| kontrolovat dál | streamy má, ale Nokturno ho hlídá dál, dokud jich nepřibude |
| zatím ne | titul je známý, ale žádný zdroj ho zatím nemá |
| hlídá se | titul zatím žádný zdroj nezná, Nokturno ho hledá podle názvu |

Díl s **Kontrolovat dál** u seriálu, který hlídáš, je přímo na řádku seriálu („Cizinka · 2x02 · kontrolovat dál“).

Watchlist z [Trakt.tv](trakt.md) je od verze 10.0 v **Mém seznamu**, ne v Hlídaných. Titul z něj, na který chceš čekat, si přidej do Hlídaných ručně.

### Kdy Nokturno kontroluje
- Seriál nejvýš jednou za 6 hodin, titul jednou denně. Hned to spustí **Zkontrolovat teď**
  (poslední položka Hlídaných, je i v kontextovém menu).
- Kontroluje se na pozadí, jen když má Kodi síť, a nikdy během přehrávání. Na telefonu s Androidem
  hlavně ve chvíli, kdy je Kodi otevřené.
- Nový díl se ohlásí, až když ho jde pustit, ne hned, jak vyšel. Díl bez data vydání se nehlídá, dokud datum nemá.
- Oznámení je krátká zpráva v rohu obrazovky: „Nový díl ke sledování“, „Už je k dispozici: …“ nebo „Přibyl zdroj: …“.
  Během přehrávání počká na konec.

### Synchronizace
Když synchronizuješ víc Kodi, zapni **Nokturno → Nastavení → Synchronizace → Synchronizovat Hlídané** (ve výchozím
stavu zapnuté). Hlídané se pak sdílí mezi všemi Kodi i s Home Assistantem. Co jedno zařízení zkontrolovalo,
další už znovu nekontroluje, a oznámení přijde na každé. Nastavení synchronizace:
[Synchronizace mezi zařízeními nefunguje](synchronizace.md).

## Home Assistant
V kartě Nokturno je **Hlídané** řada plakátů na úvodní obrazovce, vedle Pokračovat ve sledování, Mého seznamu a Katalogů.
Ukáže 12 titulů, zbytek je za dlaždicí **Zobrazit vše**. Dokud v ní nic není, řada se nezobrazí.

- **Seriály** jsou první. Na plakátu s novým dílem je štítek „nový díl 1x03“.
- **Tituly** jsou za seriály. Plakát titulu, který zatím žádný stream nemá, je ztlumený. U hlídaného dílu je na plakátu číslo dílu (1x02).
- Klepnutím na plakát se otevře dialog titulu. Je v něm stav titulu (lze pustit, kontrolovat dál, hlídá se, zatím ne), u seriálu nový díl, díl ke sledování, nebo „zatím bez streamu“, a dole volby:
  - seriál: **Otevřít**, **Označit nový díl jako viděný** (když je nový díl), **Kontrolovat dál díl 1x02 (streamy nevyhovují)**
    nebo **Přestat kontrolovat díl 1x02** (jen když je nějaký díl ke sledování) a **Přestat hlídat**,
  - titul se streamy: **Vybrat stream**, **Přesunout do Mého seznamu** (jen když se nekontroluje dál), **Kontrolovat dál (streamy nevyhovují)**
    nebo **Přestat kontrolovat dál** a **Odebrat z Hlídaných**,
  - titul bez streamů: **Vybrat stream** (u dílu **Otevřít**) a **Odebrat z Hlídaných**.
- Do Hlídaných přidáš titul z dialogu kterékoli řady nebo výsledků hledání: **Přidat do Hlídaných**, u seriálu **Hlídat nové díly**.
  V detailu titulu je totéž zvoneček, u seriálu ve výpisu dílů oko.

Když máš v editoru karty zapnuté **Klik na plakát rovnou přehraje (dlouhý stisk = nabídka)**, dialog otevře dlouhý stisk.

Oznámení do mobilu: v nastavení integrace, sekce **Stahování a odkazy**, vyplň **Oznámení o stažení a nových dílech**
(třeba `notify.mobile_app_telefon`). Prázdné pole = oznámení jen v Home Assistantu.

Hned zkontrolovat jde v **Nástroje pro vývojáře → Akce**: seriály akcí **Zkontrolovat nové díly** (`nokturno.check_series`),
hlídané tituly akcí **Hlídané – zkontrolovat teď** (`nokturno.trakt_watchlist`).

Synchronizace s Kodi: sekce **Synchronizace s Kodi → Synchronizovat Hlídané**.

---
[Všechny návody](../) · [Slovensky](../sk/hlidane)
