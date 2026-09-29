---
slug: ha-karta
lang: cs
title: "Home Assistant: karta a přehrání v Kodi"
products: [ha]
priority: 3
---

# Home Assistant: karta a přehrání v Kodi

## Přehrání v Kodi nic nedělá
- V nastavení integrace, sekce **Přehrávání**, musí být ve **Výchozích přehrávačích (Kodi)** zařízení,
  kde je nainstalovaný doplněk Nokturno pro Kodi. Karta přehrává přes něj.
- Entita Kodi (`media_player.…`) musí být v Home Assistantu dostupná.
- V Kodi zapni ovládání přes webový server: **Nastavení → Služby → Ovládání**.
- Když se přehrání spustí, ale v Kodi se nic neděje, pošli nám log z Kodi, viz [Jak poslat log](poslat-log.md).

## Karta nereaguje nebo vypadá zaseklá
- Spusť akci **Vymazat cache API** (`nokturno.clear_cache`) v **Nástroje pro vývojáře → Akce**.
- Po aktualizaci integrace obnov stránku úplně (Ctrl+Shift+R). Prohlížeč si drží starou verzi karty.

## „Pokračovat ve sledování“ je prázdné
Karta ukazuje poslední známý stav i ve chvíli, kdy Kodi neběží. Když je prázdné i tak, zkontroluj,
že Home Assistant vidí Kodi: entita `media_player.…` musí existovat a aspoň jednou být dostupná.

## Oznámení nechodí
- V sekci **Stahování a odkazy** vyplň **Oznámení o stažení a nových dílech** službou `notify.`,
  třeba `notify.mobile_app_telefon`. Prázdné pole pošle oznámení jen do Home Assistantu, ne do mobilu.
- Nové díly se kontrolují každých 6 hodin, hlídané tituly jednou denně. Oznámení přijde při nejbližší kontrole.
- Hned zkontrolovat jde akcí **Zkontrolovat nové díly** (`nokturno.check_series`).
- Díl bez data vydání se nehlídá, dokud datum nemá.

## Odkaz do mobilu nefunguje mimo domácí síť
V sekci **Stahování a odkazy** vyplň **Adresu mimo domácí síť**. Bez ní odkaz vede na adresu v domácí síti.

## Senzory se jmenují jinak než v návodu
Názvy senzorů se řídí jazykem Home Assistantu. Starší instalace si nechávají původní `entity_id`.
Skutečné názvy najdeš v **Nastavení → Zařízení a služby → Entity**.

## Další problémy
- Integrace hlásí „vyžaduje opravu“: [Zdroj hlásí „nesedí jméno nebo heslo“](prihlaseni.md).
- HACS nenabízí novou verzi: [Jak zjistit verzi a aktualizovat](aktualizace.md).
- Synchronizace s Kodi: [Synchronizace mezi zařízeními nefunguje](synchronizace.md).
- CZtor: [CZtor: „zařízení není spárované“](cztor.md).
- Podrobnosti: [Nokturno pro Home Assistant](../navody/ha/index.md).

---
[Všechny návody](../) · [Slovensky](../sk/ha-karta)
