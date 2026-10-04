---
slug: vlastni-uloziste
lang: sk
title: Ako pripojiť vlastné úložisko
products: [kodi, stremio]
priority: 1
when: {storage: [unreachable, bad_login]}
templates:
  kodi: |
    Ahoj, Nokturno sa nemôže spojiť s tvojím vlastným úložiskom.
    1. Nokturno → Nastavenia → Vlastné úložisko: skontroluj Adresu priečinka, používateľské meno a heslo.
    2. Adresa v domácej sieti (napríklad 192.168.…) funguje len doma. Mimo domova je potrebná verejná adresa alebo VPN.
    3. Úložisko, ktoré nepoužívaš, vypni voľbou Používať toto úložisko. Zostane vyplnené, len sa v ňom nebude hľadať.
    4. Potom daj Nastavenia → Pokročilé → Overiť zdroje (v starších verziách Otestovať zdroje).
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/vlastni-uloziste
    Tím Nokturno
---

# Ako pripojiť vlastné úložisko

Vlastné úložisko je hlavná funkcia Nokturna: prehráva tvoje súbory z NAS, Nextcloudu alebo iného servera s WebDAV.
Súbor, ktorý k titulu patrí, sa zobrazí **medzi streamami ako prvý**. Zdroje tretích strán (WebShare, HellSpy a ďalšie)
sú len voliteľné doplnenie, pri novej inštalácii sú všetky vypnuté.

## Čo je potrebné
- priečinok dostupný cez **WebDAV** (`http://` alebo `https://`, tvar `davs://` z Kodi funguje tiež),
- meno a heslo, ak je úložisko chránené,
- úložisko musí byť **dosiahnuteľné zo zariadenia, na ktorom prehrávaš**. Adresa v domácej sieti funguje len doma.

## Kodi
**Nokturno → Nastavenia → Vlastné úložisko**, pre každé z troch úložísk:

| Pole | Na čo |
|---|---|
| **Používať toto úložisko** (predtým **Použiť toto úložisko**) | vypnuté úložisko zostane vyplnené, len sa v ňom nehľadá |
| **Adresa priečinka** | WebDAV priečinok s filmami a seriálmi, napríklad `https://nas.example.cz:5006/video/` |
| **Používateľské meno**, **Heslo** | prihlásenie k úložisku |
| **Názov** | zobrazí sa pri streamoch (napríklad `NAS`) |

Potom daj **Nastavenia → Pokročilé → Overiť zdroje** (v starších verziách **Otestovať zdroje**).

## Stremio
V nastavení doplnku (v Stremiu **Doplnky → Nokturno → ozubené koliesko**, alebo `http://<IP zariadenia s aplikáciou>:7140/configure`) vyplň v sekcii
**Vlastné úložisko a zdroje** prvú kartu **Vlastné úložisko** a daj **Overiť úložisko**. Potom ulož zmeny. Keď už doplnok
v Stremiu máš, zmeny platia hneď a znova ho pridávať nemusíš.

V Stremiu platia dve veci navyše:
- Úložisko musí byť dosiahnuteľné **zo zariadenia, kde beží aplikácia Nokturno**. Tá v ňom hľadá súbory a od verzie 9.6.1
  ich odovzdáva aj prehrávaču, prehrávač potrebuje dosiahnuť len na aplikáciu. Keď je aplikácia doma, stačí adresa z domácej siete.
- V Stremiu v prehliadači sa súbory `.mkv`, `.avi` a podobné neprehrajú, o prehraní rozhoduje formát súboru.
  V aplikácii Stremio alebo Nuvio hrajú. Pozri [„⚠️ Vo webovom prehrávači sa neprehrá“](stremio-webovy-prehravac.md).

## Hlásenia
| Kde | Hlásenie | Čo urobiť |
|---|---|---|
| hore v menu, Overiť zdroje | „Úložisko: neodpovedá“, „<názov> neodpovídá“ | adresa nie je z Kodi dosiahnuteľná: iná sieť, vypnutý server, nevystavený port. Skús adresu otvoriť v prehliadači v rovnakej sieti. |
| hore v menu | „Úložisko: nesedí meno alebo heslo“ | prihlasovacie údaje k úložisku, nie k Nokturnu |
| pri hľadaní | „<názov>: špatné jméno nebo heslo“, „<názov>: složka neexistuje“ (po česky) | oprav meno, heslo alebo cestu k priečinku |
| pri titule | súbor sa neponúkne | skontroluj pomenovanie (nižšie); nový súbor sa zobrazí najneskôr do hodiny |

## Ako pomenovať súbory
- **Film:** názov na začiatku, rok v zátvorke – `Filmy/Pelíšky (1999).mkv`.
- **Seriál:** značka dielu je nutná – `Seriály/Hospoda/Hospoda S02E04 - Úraz.avi` (funguje aj `2x04`).
- Keď má film slovenský či český názov úplne iný ako originál, daj ho do priečinka s originálnym názvom.

Podrobnosti (po česky): [Jak připojit vlastní úložiště](https://nokturno-app.github.io/nokturno-napoveda/cs/vlastni-uloziste).

---
[Všetky návody](./) · [Česky](../cs/vlastni-uloziste)
