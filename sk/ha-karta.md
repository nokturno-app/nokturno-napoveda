---
slug: ha-karta
lang: sk
title: "Home Assistant: karta a prehrávanie v Kodi"
products: [ha]
priority: 3
---

# Home Assistant: karta a prehrávanie v Kodi

## Prehrávanie v Kodi nič nerobí
- V nastaveniach integrácie, sekcia **Prehrávanie**, musí byť v **Predvolených prehrávačoch (Kodi)** zariadenie,
  kde je nainštalovaný doplnok Nokturno pre Kodi. Karta prehráva cez neho.
- Entita Kodi (`media_player.…`) musí byť v Home Assistante dostupná.
- V Kodi zapni ovládanie cez webový server: **Nastavenia → Služby → Ovládanie**.
- Keď sa prehrávanie spustí, ale v Kodi sa nič nedeje, pošli nám log z Kodi, pozri [Ako poslať log](poslat-log.md).

## Karta nereaguje alebo vyzerá zaseknutá
- Spusti akciu **Vymazať cache API** (`nokturno.clear_cache`) v **Nástroje pre vývojárov → Akcie**.
- Po aktualizácii integrácie obnov stránku úplne (Ctrl+Shift+R). Prehliadač si drží starú verziu karty.

## „Pokračovať v sledovaní“ je prázdne
Karta ukazuje posledný známy stav aj vtedy, keď Kodi nebeží. Keď je prázdne aj tak, skontroluj,
že Home Assistant vidí Kodi: entita `media_player.…` musí existovať a aspoň raz byť dostupná.

## Upozornenia nechodia
- V sekcii **Sťahovanie a odkazy** vyplň **Upozornenia na stiahnutie a nové diely** službou `notify.`,
  napríklad `notify.mobile_app_telefon`. Prázdne pole pošle upozornenie len do Home Assistantu, nie do mobilu.
- Nové diely sa kontrolujú každých 6 hodín, sledované tituly raz denne. Upozornenie príde pri najbližšej kontrole.
- Hneď skontrolovať sa dá akciou **Skontrolovať nové diely** (`nokturno.check_series`).
- Diel bez dátumu vydania sa nesleduje, kým dátum nemá.

## Odkaz do mobilu nefunguje mimo domácej siete
V sekcii **Sťahovanie a odkazy** vyplň **Adresu mimo domácej siete**. Bez nej odkaz vedie na adresu v domácej sieti.

## Senzory sa volajú inak ako v návode
Názvy senzorov sa riadia jazykom Home Assistantu. Staršie inštalácie si nechávajú pôvodné `entity_id`.
Skutočné názvy nájdeš v **Nastavenia → Zariadenia a služby → Entity**.

## Ďalšie problémy
- Integrácia hlási „vyžaduje opravu“: [Zdroj hlási „nesedí meno alebo heslo“](prihlaseni.md).
- HACS neponúka novú verziu: [Ako zistiť verziu a aktualizovať](aktualizace.md).
- Synchronizácia s Kodi: [Synchronizácia medzi zariadeniami nefunguje](synchronizace.md).
- CZtor: [CZtor: „zariadenie nie je spárované“](cztor.md).
- Podrobnosti (po česky): [Nokturno pro Home Assistant](../navody/ha/index.md).

---
[Všetky návody](./) · [Česky](../cs/ha-karta)
