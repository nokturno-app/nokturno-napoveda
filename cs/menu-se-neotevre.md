---
slug: menu-se-neotevre
lang: cs
title: Nokturno se neotevře nebo je menu prázdné
products: [kodi]
priority: 2
templates:
  kodi: |
    Ahoj, když se ti menu Nokturna neotevře, chybí nejspíš souhlas s podmínkami použití.
    1. Otevři Nokturno z Doplňky → Video doplňky a v dialogu „Souhlasíš s podmínkami použití výše?“ zvol Souhlasím.
    2. Když se dialog neukáže: Nokturno → Nastavení → Podmínky použití (poslední kategorie) a zapni souhlas.
    3. Pak projdi Nastavení → Pokročilé → Průvodce nastavením.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/menu-se-neotevre
    Tým Nokturno
---

# Nokturno se neotevře nebo je menu prázdné

## Menu se neotevře vůbec
Při prvním spuštění se Nokturno zeptá „Souhlasíš s podmínkami použití výše?“. Bez souhlasu se menu neotevře.

1. Otevři Nokturno z **Doplňky → Video doplňky** (ne z widgetu na hlavní obrazovce) a zvol **Souhlasím**.
2. Po volbě **Nesouhlasím**, nebo když se dialog neukázal, otevři **Nokturno → Nastavení → Podmínky použití**.
   Je to **poslední** kategorie nastavení. Zapni tam souhlas a dej OK.

Z widgetu nebo z Home Assistantu se dialog neukáže, přijde jen oznámení. Nokturno proto jednou otevři přímo.

## Menu je skoro prázdné
Katalogy a hledání fungují i bez účtů. Když chybí nebo nic nepřehrají, nemáš zapnutý žádný zdroj:
- dokud nemáš nastavený žádný zdroj, je v menu jako první položka **Průvodce nastavením**,
- průvodce spustíš i v **Nastavení → Pokročilé → Průvodce nastavením**,
- viz [První nastavení: průvodce a Nastavit z mobilu](prvni-nastaveni.md).

## Nokturno spadne hned po otevření
1. Aktualizuj na nejnovější verzi, viz [Jak zjistit verzi a aktualizovat](aktualizace.md).
2. Vymaž uložená data: **Nastavení → Pokročilé → Vymazat cache (katalogy, hledání, streamy)**.
3. Když to nepomůže, pošli log: [Jak poslat log a zjistit ID instalace](poslat-log.md).

---
[Všechny návody](../) · [Slovensky](../sk/menu-se-neotevre)
