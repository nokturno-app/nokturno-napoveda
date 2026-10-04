---
slug: instalace-kodi
lang: sk
title: Ako nainštalovať Nokturno do Kodi
products: [kodi]
priority: 1
---

# Ako nainštalovať Nokturno do Kodi

Nokturno beží na Kodi 20 a novšom (Android TV, Google TV, CoreELEC, Windows, Linux, macOS).
Inštaluj ho cez **repozitár** – len tak budú chodiť aktualizácie samy.

## 1. Povoliť neznáme zdroje
V Kodi otvor **Nastavenia → Systém → Doplnky** a zapni **Neznáme zdroje**.

## 2. Pridať zdroj
**Nastavenia → Správca súborov → Pridať zdroj**. Ako adresu zadaj

```
https://nokturno.stream/repo/
```

a pomenuj ho `Nokturno`.

## 3. Nainštalovať repozitár
**Doplnky → Inštalovať zo ZIP súboru → Nokturno → repository.nokturno → repository.nokturno.zip**.

## 4. Nainštalovať doplnok
**Doplnky → Inštalovať z repozitára → Nokturno repozitár → Video doplnky → Nokturno → Inštalovať**.

## 5. Prvé spustenie
Doplnok sa spýta na súhlas s podmienkami použitia (**Súhlasím**) a ponúkne sprievodcu nastavením:
vlastné úložisko a prípadné účty môžeš vyplniť **z mobilu cez QR kód**, prejsť krátkym sprievodcom ovládačom,
alebo to preskočiť. Sprievodca sa ako prvé pýta na vlastné úložisko.
Sprievodcu kedykoľvek spustíš znova v **Nastavenia → Pokročilé → Sprievodca nastavením**.

Na prehrávanie potrebuješ hlavne [vlastné úložisko](vlastni-uloziste.md). Zdroje tretích strán (napríklad WebShare
s VIP) sú voliteľné a pri novej inštalácii sú všetky vypnuté.

## Keď niečo nejde
- **Kodi hlási, že nemôže nainštalovať doplnok z neznámeho zdroja:** vráť sa ku kroku 1.
- **V Správcovi súborov máš adresu `nokturno.tailf0014.ts.net`:** tá od septembra 2026 nefunguje. Zdroj zmaž
  a pridaj `https://nokturno.stream/repo/`.
- **Doplnok máš zo zipu bez repozitára:** aktualizácie chodiť nebudú. Nainštaluj repozitár podľa krokov 2 a 3,
  nastavenie zostane.

Podrobný návod vrátane beta verzií je v návode (po česky): [Instalace](../navody/kodi/instalace.md).

---
[Všetky návody](./) · [Česky](../cs/instalace-kodi)
