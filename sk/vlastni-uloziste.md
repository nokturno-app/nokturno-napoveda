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
    1. Nokturno → Nastavenia → Vlastné úložisko: skontroluj Adresu priečinka, používateľské meno a heslo. Adresa môže byť WebDAV (https://…) alebo zdieľaný priečinok SMB (smb://server/priečinok), SMB len v domácej sieti.
    2. Adresa v domácej sieti (napríklad 192.168.…) funguje len doma. Mimo domova je potrebná verejná adresa alebo VPN.
    3. Úložisko, ktoré nepoužívaš, vypni voľbou Používať toto úložisko. Zostane vyplnené, len sa v ňom nebude hľadať.
    4. Potom daj Nastavenia → Pokročilé → Overiť zdroje (v starších verziách Otestovať zdroje).
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/vlastni-uloziste
    Tím Nokturno
---

# Ako pripojiť vlastné úložisko

Vlastné úložisko je hlavná funkcia Nokturna: prehráva **tvoje vlastné súbory** z NAS, Nextcloudu, domáceho počítača alebo iného servera –
cez **WebDAV** (adresa `http://` alebo `https://`) alebo zo **zdieľaného priečinka SMB** (adresa `smb://`, teda Windows alebo Samba na NAS).
Súbor, ktorý k titulu patrí, sa zobrazí **medzi streamami ako prvý**. Nastaviť ide až **tri úložiská**, každé môže byť iného druhu. Zdroje tretích strán (WebShare, HellSpy a ďalšie)
sú len voliteľné doplnenie, pri novej inštalácii sú všetky vypnuté.

## Čo je potrebné
- priečinok dostupný cez **WebDAV** (`http://` alebo `https://`, tvar `davs://` z Kodi funguje tiež),
- **alebo** zdieľaný priečinok **SMB** (Samba) – Windows, Synology, QNAP, router s diskom, Raspberry Pi so Sambou. Adresa má tvar `smb://server/zdieľaný-priečinok/podpriečinok`, napríklad `smb://nas/video/` alebo `smb://192.168.1.10/filmy/`. SMB funguje len v domácej sieti, pozri [SMB (zdieľaný priečinok)](#smb-zdielany-priecinok),
- meno a heslo, ak je úložisko chránené,
- úložisko musí byť **dosiahnuteľné zo zariadenia, na ktorom prehrávaš**. Adresa v domácej sieti funguje len doma.

## Kodi
**Nokturno → Nastavenia → Vlastné úložisko**, pre každé z troch úložísk:

| Pole | Na čo |
|---|---|
| **Používať toto úložisko** (predtým **Použiť toto úložisko**) | vypnuté úložisko zostane vyplnené, len sa v ňom nehľadá |
| **Adresa priečinka** | WebDAV alebo SMB priečinok s filmami a seriálmi, napríklad `https://nas.example.cz:5006/video/` alebo `smb://nas/video/` |
| **Používateľské meno**, **Heslo** | prihlásenie k úložisku |
| **Názov** | zobrazí sa pri streamoch (napríklad `NAS`) |

Potom daj **Nastavenia → Pokročilé → Overiť zdroje** (v starších verziách **Otestovať zdroje**).

## SMB (zdieľaný priečinok)
Do **Adresy priečinka** napíš `smb://server/zdieľaný-priečinok`, prípadne aj s podpriečinkom (`smb://nas/video/filmy/`). Meno a heslo vyplň, keď je zdieľaný priečinok chránený; pri verejnom priečinku bez hesla ich nechaj prázdne. Potom daj **Nastavenia → Pokročilé → Overiť zdroje**.
- SMB funguje v **domácej sieti**. Na zdieľaný priečinok musí dosiahnuť zariadenie, kde Nokturno beží: Kodi, Home Assistant, alebo počítač či telefón s aplikáciou Nokturno pre Stremio. Cez internet sa SMB nepoužíva – mimo domova potrebuješ WebDAV s verejnou adresou alebo VPN.
- Cestu píš normálne, s medzerami a diakritikou, nie `%20`.
- Filmy, seriály, vlastné katalógy aj koncerty fungujú rovnako ako pri WebDAV a súbor sa prehráva priamo, nič sa vopred nesťahuje.
- Jazyk zvuku sa pri súboroch zo SMB berie len z **názvu súboru** (hlavička súboru sa nečíta). Daj preto do názvu `CZ`, `SK` a podobne, pozri [Ako pomenovať súbory](#ako-pomenovat-subory).

## Stremio
V nastavení doplnku (v Stremiu **Doplnky → Nokturno → ozubené koliesko**, alebo `http://<IP zariadenia s aplikáciou>:7140/configure`) vyplň v sekcii
**Vlastné úložisko a zdroje** prvú kartu **Vlastné úložisko** a daj **Overiť úložisko**. Potom ulož zmeny. Keď už doplnok
v Stremiu máš, zmeny platia hneď a znova ho pridávať nemusíš.

V Stremiu platia tri veci navyše:
- Úložisko môže byť WebDAV aj SMB (`smb://server/priečinok`). SMB číta aplikácia Nokturno, takže počítač alebo telefón s aplikáciou musí byť v rovnakej sieti ako zdieľaný priečinok. Na VPS ani cez internet SMB nefunguje (hlásenie „SMB jen z domácí sítě“).
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
| Stremio, Overiť úložisko | „SMB jen z domácí sítě“ (po česky) | aplikácia pre Stremio dostala požiadavku z internetu (VPS, prístup mimo domova). SMB ide len v domácej sieti, mimo nej použi WebDAV. |
| Overiť zdroje | „v adrese chybí sdílená složka (smb://server/složka)“ (po česky) | adresa končí menom servera. Doplň názov zdieľaného priečinka, napríklad `smb://nas/video/`. |
| Overiť zdroje, WebDAV | chyba presmerovania alebo „HTTP 301“ | server adresu presmerováva (napríklad z http na https). Aktuálne Nokturno presmerovanie sleduje samo; keď to napriek tomu nejde, zadaj rovno konečnú adresu tak, ako ju ukáže prehliadač (zvyčajne `https://…/` s lomkou na konci). |
| pri titule | súbor sa neponúkne | skontroluj pomenovanie (nižšie); nový súbor sa zobrazí najneskôr do hodiny |

## Ako pomenovať súbory
- **Film:** názov na začiatku, rok v zátvorke – `Filmy/Pelíšky (1999).mkv`.
- **Seriál:** najistejšia je značka dielu – `Seriály/Hospoda/Hospoda S02E04 - Úraz.avi` (funguje aj `2x04`). Súbor bez nej sa nájde aj vtedy, keď je v jeho názve **názov dielu** (`1. Závěť.avi`) alebo **dátum vysielania** (`07.03.2025`, `2025-03-07`) a sedí s katalógom. Samotné číslo dielu bez názvu nestačí. Pre istotu daj značku dielu do názvu.
- Keď má film slovenský či český názov úplne iný ako originál, daj ho do priečinka s originálnym názvom.

Podrobnosti (po česky): [Jak připojit vlastní úložiště](https://nokturno-app.github.io/nokturno-napoveda/cs/vlastni-uloziste).

---
[Všetky návody](./) · [Česky](../cs/vlastni-uloziste)
