---
slug: luna-token
lang: sk
title: "Luna: „beží, ale chýba token“"
products: [kodi]
priority: 0
when: {luna: [no_token, bad_token_format, bad_token, main_empty, no_streams]}
templates:
  kodi: |
    Ahoj, Luna ti beží, ale Nokturno od nej nemá token. Bez neho z nej nič nepríde.
    1. Na mobile alebo počítači otvor v prehliadači adresu Luny s /setup na konci, napríklad http://192.168.1.10:7126/setup.
    2. Prihlás sa do WebShare (účet s VIP), zvoľ ručnú inštaláciu a pri Luna: Absolute Cinema daj Kopírovať.
    3. V Kodi: Nokturno → Nastavenia → Nastaviť z mobilu a prenos → Nastaviť z mobilu. Naskenuj QR kód a skopírovanú adresu vlož do sekcie Luna.
    4. Potom v Nastavenia → Zdroje a účty, v skupine Luna, klikni na Overiť nastavenie Luny.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/luna-token
    Tím Nokturno
---

# Luna: „beží, ale chýba token“

## Čo to znamená
Server Luny Nokturno našlo a ozval sa, ale chýba mu **adresa doplnku s tokenom**. Token je dlhý kód,
ktorý začína `e1.`, a Luna podľa neho spozná tvoj účet WebShare. Bez neho z Luny nič nepríde.

Rovnaký problém ohlasujú aj tieto hlásenia z **Overiť nastavenie Luny**:

- „Luna … beží, ale chýba token.“
- „V poli Token nie je token.“
- „Luna … beží, ale tento token neprijala.“
- „… odpovedá a hľadanie na WebShare funguje, ale jej hlavný zdroj nič nevracia.“
- „… beží, ale nenašla streamy ani pri známych filmoch.“

## Prečo sa to stáva
- V poli je len adresa servera (`http://…:7126`), nie adresa doplnku zo stránky `/setup`.
- V poli je len kus adresy.
- Token je zo starej alebo inej Luny (Luna bola preinštalovaná alebo ich máš viac).
- V Lune nie je prihlásený WebShare, alebo účet nemá VIP.

## Čo urobiť
1. Na **mobile alebo počítači** otvor v prehliadači adresu Luny s `/setup` na konci, napríklad
   `http://192.168.1.10:7126/setup`. Keď Luna beží priamo na TV boxe, zadaj IP adresu boxu.
2. Na stránke `/setup` zvoľ ručnú inštaláciu, prihlás sa do **WebShare** (účet s VIP) a v kroku s adresami
   klikni pri **Luna: Absolute Cinema** na kopírovanie. Adresa končí zhruba `…:7126/e1.AbCd…/manifest.json`.
3. Adresu dostaň do Kodi. Najpohodlnejšie z mobilu:
   **Nokturno → Nastavenia → Nastaviť z mobilu a prenos → Nastaviť z mobilu**, naskenuj QR kód,
   rozbaľ sekciu **Luna** a adresu vlož do poľa pre adresu doplnku. Mobil musí byť v rovnakej sieti ako Kodi.
4. V **Nastavenia → Zdroje a účty**, skupina **Luna**, klikni na **Overiť nastavenie Luny**.
   Keď napíše „Luna … odpovedá a vracia streamy. Nastavenie je v poriadku.“, je hotovo.

Adresu doplnku nikomu neposielaj, obsahuje tvoj token.

Návod so snímkami obrazovky je v návode (po česky):
[Nastavení Luny](../navody/kodi/nastaveni-luny.md).
Význam všetkých hlásení: [Čo znamenajú hlásenia z Overiť nastavenie Luny](luna-hlasky.md).

## Stále to nejde?
V okne overenia klikni na **Poslať log** a napíš nám, pozri [Kde hľadať pomoc](kde-hledat-pomoc.md).

---
[Všetky návody](./) · [Česky](../cs/luna-token)
