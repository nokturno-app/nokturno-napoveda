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
Súbor, ktorý k titulu patrí, sa zobrazí **medzi streamami ako prvý**.

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
Na stránke nastavenia doplnku ([nokturno.stream/configure](https://nokturno.stream/configure)) vyplň kartu
**Vlastné úložisko** a daj **Overiť úložisko**. Potom doplnok pridaj znova tlačidlom **Pridať do Stremia**.

V Stremiu platia dve veci navyše:
- Úložisko musí byť dosiahnuteľné **zo servera doplnku** (ten v ňom hľadá súbory) **aj zo zariadenia**, kde prehrávaš.
  Adresa v domácej sieti preto s doplnkom na `nokturno.stream` nefunguje.
- Súbor z úložiska sa **neprehrá vo webovom Stremiu** v prehliadači, len v aplikácii (Stremio pre počítač,
  Android a Android TV, alebo Nuvio). Pri takom streame je upozornenie „⚠️ Vo webovom prehrávači sa neprehrá – len v aplikácii“
  (pri niektorých adresách doplnku po česky „⚠️ Ve webovém přehrávači se nepřehraje – jen v aplikaci“).

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

Podrobnosti (po česky): [Vlastní úložiště](../navody/kodi/vlastni-uloziste.md).

---
[Všetky návody](./) · [Česky](../cs/vlastni-uloziste)
