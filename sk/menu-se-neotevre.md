---
slug: menu-se-neotevre
lang: sk
title: Nokturno sa neotvorí alebo je menu prázdne
products: [kodi]
priority: 2
templates:
  kodi: |
    Ahoj, keď sa ti menu Nokturna neotvorí, chýba najskôr súhlas s podmienkami použitia.
    1. Otvor Nokturno z Doplnky → Video doplnky a v dialógu „Súhlasíš s podmienkami použitia vyššie?“ zvoľ Súhlasím.
    2. Keď sa dialóg nezobrazí: Nokturno → Nastavenia → Podmienky použitia (posledná kategória) a zapni súhlas.
    3. Potom prejdi Nastavenia → Pokročilé → Sprievodca nastavením.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/menu-se-neotevre
    Tím Nokturno
---

# Nokturno sa neotvorí alebo je menu prázdne

## Menu sa neotvorí vôbec
Pri prvom spustení sa Nokturno opýta „Súhlasíš s podmienkami použitia vyššie?“. Bez súhlasu sa menu neotvorí.

1. Otvor Nokturno z **Doplnky → Video doplnky** (nie z widgetu na hlavnej obrazovke) a zvoľ **Súhlasím**.
2. Po voľbe **Nesúhlasím**, alebo keď sa dialóg nezobrazil, otvor **Nokturno → Nastavenia → Podmienky použitia**.
   Je to **posledná** kategória nastavení. Zapni tam súhlas a daj OK.

Z widgetu alebo z Home Assistantu sa dialóg nezobrazí, príde len upozornenie. Nokturno preto raz otvor priamo.

## Menu je skoro prázdne
Katalógy a hľadanie fungujú aj bez účtov. Keď chýbajú alebo nič neprehrajú, nemáš nastavené vlastné úložisko
ani zapnutý žiadny voliteľný zdroj tretej strany (pri novej inštalácii sú všetky vypnuté):
- kým nemáš nastavené vlastné úložisko ani žiadny zdroj, je v menu ako prvá položka **Sprievodca nastavením**,
  ktorý sa ako prvé pýta na vlastné úložisko,
- sprievodcu spustíš aj v **Nastavenia → Pokročilé → Sprievodca nastavením**,
- pozri [Prvé nastavenie: sprievodca a Nastaviť z mobilu](prvni-nastaveni.md).

## Nokturno spadne hneď po otvorení
1. Aktualizuj na najnovšiu verziu, pozri [Ako zistiť verziu a aktualizovať](aktualizace.md).
2. Vymaž uložené dáta: **Nastavenia → Pokročilé → Vymazať cache (katalógy, hľadanie, streamy)**.
3. Keď to nepomôže, pošli log: [Ako poslať log a zistiť ID inštalácie](poslat-log.md).

---
[Všetky návody](./) · [Česky](../cs/menu-se-neotevre)
