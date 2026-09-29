---
slug: hlidane
lang: sk
title: "Sledované: nové diely a Kontrolovať ďalej"
products: [kodi, ha]
priority: 2
templates:
  kodi: |
    Ahoj, na toto sú v Nokturne Sledované. Nokturno sa samo ozve, keď sa titul bude dať pustiť.
    1. Seriál: v kontextovom menu seriálu daj Sledovať nové diely.
    2. Film alebo seriál, ktorý zatiaľ nikde nie je: v kontextovom menu daj Sledovať, kým bude dostupné.
    3. Diel má streamy, ale nie také, aké chceš (napríklad bez CZ titulkov): v kontextovom menu dielu daj Kontrolovať ďalej. Nokturno sa ozve, keď streamov pribudne.
    Zoznam je v hlavnom menu pod Pokračovať v sledovaní, položka Sledované.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/hlidane
    Tím Nokturno
---

# Sledované: nové diely a Kontrolovať ďalej

Sledované si pamätajú, na čo čakáš. Nokturno sa samo ozve, keď sa to bude dať pustiť:
- **nový diel** seriálu, ktorý sleduješ,
- **film alebo seriál, ktorý zatiaľ nikde nie je**,
- titul alebo diel, ktorý streamy má, ale **nie také, aké chceš** (napríklad bez CZ titulkov alebo bez 5.1).
  Na to je **Kontrolovať ďalej**: Nokturno ho sleduje ďalej a ozve sa, keď streamov pribudne.

Sledované sú v Kodi a v Home Assistante. V Stremiu nie sú.

## Kodi

### Ako niečo pridať
| Na čo čakáš | Kde |
|---|---|
| nové diely seriálu | kontextové menu seriálu → **Sledovať nové diely** |
| film alebo seriál, ktorý zatiaľ nikde nie je | kontextové menu titulu → **Sledovať, kým bude dostupné** |
| diel, ktorý streamy má, ale nie také, aké chceš | kontextové menu dielu → **Kontrolovať ďalej 2x02** (s číslom toho dielu) |
| film, ktorý streamy má, ale nie také, aké chceš | **Sledovať, kým bude dostupné**, po prvej kontrole v Sledovaných kontextové menu → **Kontrolovať ďalej** |

Keď sa pri titule nenájde žiadny stream, Nokturno sa spýta samo: „Ozvať sa, keď bude dostupné?“ Stačí potvrdiť.
Pri diele seriálu sa tým začne sledovať celý seriál.

Zo Sledovaných titul odoberieš v kontextovom menu: **Prestať sledovať nové diely**, **Prestať sledovať**
alebo **Nekontrolovať ďalej**.

### Zoznam Sledované
Položka **Sledované** je v hlavnom menu hneď pod **Pokračovať v sledovaní**. Zobrazí sa, len čo v nej niečo je.
Keď pribudol nový diel, je to vidieť rovno v menu („Sledované · 1 nový diel“).

- **Seriály** sú hore, s novým dielom prvé: „Zrádci · nový diel 3x02“. Bez nového dielu je pri seriáli posledný diel,
  ktorý sa dá pustiť. Kliknutím seriál otvoríš a nový diel tým zhasne. V kontextovom menu je navyše
  **Označiť nový diel ako videný** a **Kontrolovať ďalej** pri poslednom diele.
- **Tituly** sú pod seriálmi a majú stav:

| Stav | Čo znamená |
|---|---|
| dá sa pustiť | titul má streamy, kliknutím otvoríš výber streamu |
| kontrolovať ďalej | streamy má, ale Nokturno ho sleduje ďalej, kým ich nepribudne |
| zatiaľ nie | titul je známy, ale žiadny zdroj ho zatiaľ nemá |
| sleduje sa | titul zatiaľ žiadny zdroj nepozná, Nokturno ho hľadá podľa názvu |

Diel s **Kontrolovať ďalej** pri seriáli, ktorý sleduješ, je priamo na riadku seriálu („Cizinka · 2x02 · kontrolovať ďalej“).

Máš prihlásený [Trakt.tv](trakt.md)? Tituly z tvojho zoznamu na pozretie na Trakte sa v Sledovaných objavia samy.

### Kedy Nokturno kontroluje
- Seriál najviac raz za 6 hodín, titul raz denne. Hneď to spustí **Skontrolovať teraz**
  (posledná položka Sledovaných, je aj v kontextovom menu).
- Kontroluje sa na pozadí, len keď má Kodi sieť, a nikdy počas prehrávania. Na telefóne s Androidom
  hlavne vtedy, keď je Kodi otvorené.
- Nový diel sa ohlási, až keď sa dá pustiť, nie hneď, ako vyšiel. Diel bez dátumu vydania sa nesleduje, kým dátum nemá.
- Upozornenie je krátka správa v rohu obrazovky: „Nový diel na pozeranie“, „Už je dostupné: …“ alebo „Pribudol zdroj: …“.
  Počas prehrávania počká na koniec.

### Synchronizácia
Keď synchronizuješ viac Kodi, zapni **Nokturno → Nastavenia → Synchronizácia → Synchronizovať Sledované** (predvolene
zapnuté). Sledované sa potom zdieľajú medzi všetkými Kodi aj s Home Assistantom. Čo jedno zariadenie skontrolovalo,
ďalšie už znova nekontroluje, a upozornenie príde na každé. Nastavenie synchronizácie:
[Synchronizácia medzi zariadeniami nefunguje](synchronizace.md).

## Home Assistant
V karte Nokturno:
- **Domov → Sledované:** tituly so stavom (dá sa pustiť, kontrolovať ďalej, sleduje sa, zatiaľ nie).
  Vlajočka pri titule so streamami zapne alebo vypne Kontrolovať ďalej. Titul, ktorý sa dá pustiť,
  presunieš tlačidlom **Presunúť do Môjho zoznamu**.
- **Knižnica → Sledované seriály:** pri každom seriáli nový diel alebo posledný diel na sledovanie.
  Vlajočka pri poslednom diele = Kontrolovať ďalej pre ten diel. Ďalej tu je **Označiť nový diel ako videný**,
  **Otvoriť** a **Prestať sledovať**.
- **V detaile titulu:** zvonček **Pridať do Sledovaných**, pri seriáli vo výpise dielov oko **Sledovať nové diely**.

Upozornenia do mobilu: v nastaveniach integrácie, sekcia **Sťahovanie a odkazy**, vyplň
**Upozornenia na stiahnutie a nové diely** (napríklad `notify.mobile_app_telefon`). Prázdne pole = upozornenie len v Home Assistante.

Hneď skontrolovať sa dá v **Nástroje pre vývojárov → Akcie**: seriály akciou **Skontrolovať nové diely**
(`nokturno.check_series`), sledované tituly akciou **Trakt – zoznam na pozretie** (`nokturno.trakt_watchlist`,
funguje aj bez Traktu).

Synchronizácia s Kodi: sekcia **Synchronizácia s Kodi → Synchronizovať Sledované**.

---
[Všetky návody](./) · [Česky](../cs/hlidane)
