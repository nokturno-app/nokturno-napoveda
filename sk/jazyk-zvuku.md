---
slug: jazyk-zvuku
lang: sk
title: Pri streame chýba jazyk zvuku
products: [kodi]
priority: 3
templates:
  kodi: |
    Ahoj, jazyk zvuku sa číta z hlavičky súboru a pri časti streamov chýba:
    1. `[EAC3 5.1]` bez kódu jazyka znamená, že ho ten, kto súbor nahral, nevyplnil. Často je to originálna stopa.
    2. `~CZ` s vlnovkou je jazyk odhadnutý z názvu súboru, nie overený.
    3. Koľko streamov sa číta, nastavíš v Nastavenia → Prehrávanie → Zisťovať zvuk zo súboru (koľko streamov).
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/jazyk-zvuku
    Tím Nokturno
---

# Pri streame chýba jazyk zvuku

## Odkiaľ Nokturno jazyk pozná
Jazyk zvukovej stopy sa číta z **hlavičky súboru**. Pri každom streame to chvíľu trvá, preto:
- sa hlavičky čítajú len pri časti streamov, počet nastavíš v **Nokturno → Nastavenia → Prehrávanie →
  Zisťovať zvuk zo súboru (koľko streamov)**,
- na čítanie sa čaká najviac pár sekúnd. Čo sa nestihne, dočíta sa na pozadí a zobrazí sa pri ďalšom otvorení titulu.

## Čo znamenajú značky pri streame
- **`CZ`, `SK`, `EN`…** – jazyk overený z hlavičky súboru.
- **`~CZ`** s vlnovkou – jazyk odhadnutý z názvu súboru. Väčšinou sedí, ale overený nie je.
- **`[EAC3 5.1]`** bez kódu jazyka – stopa v súbore je, len pri nej ten, kto súbor nahral, nevyplnil jazyk.
  Typicky pri originálnej anglickej stope. Nezahadzuje sa, často je to tá najkvalitnejšia.
- **bez údajov o zvuku** – hlavičku stream ešte nemá prečítanú.

## Ako nájsť stream vo svojom jazyku
- **Nokturno → Nastavenia → Prehrávanie → Preferovaný jazyk zvuku**: streamy v tomto jazyku sú v zozname hore.
- V dialógu výberu streamu je **Filter streamov**: vyberieš napríklad len zvuk SK alebo len titulky SK.
- **Automaticky prepnúť zvuk na preferovaný jazyk**: keď má súbor viac stôp, prehrávanie začne tou tvojou.

## Znova pustený stream si pamätá zvuk a titulky
Od verzie 10.0 si Nokturno pri každom titule pamätá zvukovú stopu a titulky, ktoré si mal zapnuté naposledy.
Keď pustíš **ten istý stream** znova (pokračovanie v rozpozeranom, ďalší večer), prepne sa na ne samo.

- Ukladá sa počas prehrávania, od 90 sekúnd sledovania. Pamätá sa posledných 300 titulov.
- Obnoví sa len pri **tom istom súbore** a len keď je v ňom stopa s rovnakým číslom aj jazykom.
  Vypnuté titulky zostanú vypnuté.
- Predvoľby z nastavení (**Preferovaný jazyk zvuku**, **Automaticky prepnúť zvuk**, titulky) sa potom nepoužijú.
  Platia len pre nový alebo iný stream.

## Zoznam streamov ukazuje len názov filmu
Streamy sa vyberajú v dialógu na dva riadky. Keď ho skin kreslí orezane, uprav v **Nastavenia → Výber streamu →
Čo a v akom poradí ukazovať pri streame**, čo má byť na prvom riadku.

---
[Všetky návody](./) · [Česky](../cs/jazyk-zvuku)
