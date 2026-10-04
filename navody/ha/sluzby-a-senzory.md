# Služby a senzory

Integrace vytváří čtyři senzory a řadu služeb, na které jde navázat automatizace. Názvy senzorů se překládají podle jazyka Home Assistantu; skutečné `entity_id` najdeš v *Nastavení → Zařízení a služby → Entity* (starší instalace si ponechávají původní, třeba `sensor.nokturno_k_zhlednuti`).

## Senzory

| Senzor | Hodnota | Hlavní atributy |
|---|---|---|
| **Stahování** | počet běžících a čekajících stahování | seznam stahování s průběhem, historie hledání, nastavené přehrávače |
| **Nové díly** | počet hlídaných seriálů s novým dílem | `series` – hlídané seriály, poslední dostupný a nový díl |
| **Hlídané** | počet hlídaných titulů, které už mají stream | `items` – hlídané tituly a jejich stav, `favourites` – Můj seznam |
| **Stav zdrojů** | počet zdrojů, které potřebují zásah (`0` = vše v pořádku) | `sources`, `problems` |
| **Katalogy** | počet ověřovaných vlastních katalogů | `paused`, `catalogs` – u každého `name`, `kind`, `verified`, `matched`, `total`, `last_check` |

### Stav zdrojů

Senzor hlásí, které zdroje potřebují zásah: nedostupné vlastní úložiště, a u volitelných zdrojů třetích stran vypršelé předplatné WebShare, účet bez VIP nebo Premium, HellSpy, který odmítá síť, Luna, která neběží, došlý kredit FastShare, nespárovaný CZtor nebo omezení Přehraj.to.

- Hodnota je počet takových zdrojů. Na automatizaci stačí jedno porovnání: stav > 0.
- Atribut `sources` má u každého zapnutého zdroje úroveň (`ok` / `warn` / `fail`), kód příčiny a podrobnosti; `problems` je seznam zdrojů s problémem.
- Senzor se neptá po síti, čte uložený stav. Ten se obnovuje každých 6 hodin.

Příklad automatizace – oznámení, když některý zdroj přestane fungovat:

```yaml
automation:
  - alias: Nokturno – zdroj potřebuje zásah
    triggers:
      - trigger: numeric_state
        entity_id: sensor.nokturno_stav_zdroju
        above: 0
    actions:
      - action: notify.mobile_app_telefon
        data:
          title: Nokturno
          message: "Zdroje k řešení: {{ state_attr('sensor.nokturno_stav_zdroju', 'problems') | join(', ') }}"
```

## Události

| Událost | Kdy | Data |
|---|---|---|
| `nokturno_new_episode` | nový díl hlídaného seriálu má stream | `id`, `title` (díl), `season`, `episode`, `series_id`, `series_title` |
| `nokturno_trakt_available` | hlídaný titul má poprvé stream, nebo mu přibyly streamy | `id`, `title`, `type`, `streams` |
| `nokturno_download_done` | stahování doběhlo | `name`, `path`, `size` |

## Služby

Všechny služby najdeš v *Nástroje pro vývojáře → Akce* pod doménou `nokturno`, s popisem každého pole.

**Hledání a přehrání**

| Služba | Co dělá |
|---|---|
| `nokturno.search` | vyhledá film nebo seriál |
| `nokturno.streams` | seřazené streamy titulu z hledání |
| `nokturno.episodes` | díly a série seriálu |
| `nokturno.detail` | popis, plakát a hodnocení titulu podle IMDb id |
| `nokturno.play` | pustí titul v Kodi nebo jiném přehrávači; místo ID jde zadat dotaz. Bez zadané entity hraje na všech nastavených přehrávačích. |
| `nokturno.resolve` | vrátí přímý odkaz na stream (VLC, mobil, Cast) |
| `nokturno.fulltext_search` | uvolněné fulltextové hledání (WebShare, HellSpy, Sledujteto, FastShare) |
| `nokturno.continue_watching`, `nokturno.remove_progress` | rozkoukané tituly z Kodi; odebrání z Pokračovat ve sledování |

**Stahování a odkazy**

| Služba | Co dělá |
|---|---|
| `nokturno.download` | stáhne stream do složky Home Assistantu |
| `nokturno.start_download`, `nokturno.cancel_download` | spustí čekající stahování hned / zruší stahování |
| `nokturno.send_link` | pošle odkaz na stream do mobilu |
| `nokturno.share_file` | pošle do mobilu dočasný odkaz na stažený soubor (jen správce) |
| `nokturno.delete_file` | smaže stažený soubor (jen správce) |

**Hlídané a Můj seznam**

| Služba | Co dělá |
|---|---|
| `nokturno.watch_series` | začne (nebo s `remove` přestane) hlídat nové díly seriálu |
| `nokturno.check_series` | hned zkontroluje hlídané seriály |
| `nokturno.mark_seen` | zhasne označení nového dílu |
| `nokturno.want_to_watch` | přidá titul do Hlídaných; bez ID stačí název, s `flag` rovnou s příznakem Kontrolovat dál |
| `nokturno.trakt_watchlist` | hned zkontroluje hlídané tituly (Watchlist z Trakt.tv je od 10.0 v Mém seznamu) |
| `nokturno.trakt_flag` | přepne příznak Kontrolovat dál |
| `nokturno.favourite_toggle`, `nokturno.favourite_add` | přidá nebo odebere titul v Mém seznamu; přesune ho z hlídaných |

**Vlastní katalogy**

Katalogy zakládáš v Kodi, do Home Assistantu přijdou synchronizací. Home Assistant je pak ověřuje (1 titul za minutu, katalogy se střídají) a výsledky posílá zpátky – Kodi samo neověřuje, dokud má od něj čerstvé výsledky. Viz [Vlastní katalogy](../../cs/vlastni-katalogy.md).

| Služba | Co dělá |
|---|---|
| `nokturno.catalogs` | vrátí stav ověřovaných katalogů |
| `nokturno.catalog_verify` | hned ověří `count` titulů (1–50, výchozí 10) katalogu `id`; bez `id` další v pořadí |
| `nokturno.catalog_pause` | `paused: true` zastaví ověřování na tomto Home Assistantu, `false` ho pustí |

**Trakt.tv a údržba**

| Služba | Co dělá |
|---|---|
| `nokturno.trakt_auth` | propojí Trakt.tv: kód přijde do oznámení, zadáš ho na `trakt.tv/activate` |
| `nokturno.trakt_watched` | zapíše titul do historie Trakt.tv |
| `nokturno.clear_history` | smaže historii hledání |
| `nokturno.clear_cache` | vymaže cache hledání, streamů a katalogů (ne historii ani Můj seznam) |

Služby `nokturno.delete_file` a `nokturno.share_file` smí spustit jen správce Home Assistantu. Volání z automatizace nebo skriptu (bez přihlášeného uživatele) projde.
