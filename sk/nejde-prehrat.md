---
slug: nejde-prehrat
lang: sk
title: Film sa nájde, ale nedá sa prehrať
products: [kodi]
priority: 1
templates:
  kodi: |
    Ahoj, stream sa ti zobrazí, ale neprehrá sa.
    1. Skús iný stream zo zoznamu. Keď jeden nejde, Nokturno samo skúsi ešte niekoľko ďalších.
    2. Keď nejdú streamy len z jedného zdroja, skontroluj pri ňom účet: Sledujteto a Přehraj.to potrebujú Premium, FastShare / Sdilej.cz kredit, WebShare VIP.
    3. Nokturno → Nastavenia → Pokročilé → Overiť zdroje (v starších verziách Otestovať zdroje) ukáže stav účtov.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/nejde-prehrat
    Tím Nokturno
---

# Film sa nájde, ale nedá sa prehrať

## Čo to znamená
V dialógu výberu sa streamy zobrazia, ale po výbere sa nič nespustí. Kodi hlási napríklad
„Jednu alebo viac položiek sa nepodarilo prehrať“, alebo Nokturno ukáže dôvod od zdroja.

Keď jeden stream nejde, Nokturno samo skúsi jeho kópie a potom niekoľko ďalších streamov. Chyba sa zobrazí,
až keď neprejde žiadny z nich.

## Čo urobiť podľa hlásenia
Hlásenia zdrojov sú zatiaľ po česky.

| Hlásenie | Čo to znamená | Čo urobiť |
|---|---|---|
| Sledujteto: přehrávání vyžaduje Premium účet | Sledujteto bez Premium odkaz na súbor nevydá | [Premium, VIP a kredit](premium-a-kredit.md) |
| FastShare: na soubor … nestačí kredit (…) | na účte FastShare / Sdilej.cz chýba kredit | dobi kredit, alebo vyber menší súbor |
| FastShare: přihlášení se nepovedlo…, Přehraj.to: přihlášení se nepovedlo… | zdroj odmietol prihlásenie | [Zdroj hlási „nesedí meno alebo heslo“](prihlaseni.md) |
| CZtor: stream už v CZtor není… | súbor medzitým zmizol | vyber iný stream |
| file_link: File temporarily unavailable | WebShare súbor práve nevydal | vyber iný stream |
| Jednu alebo viac položiek sa nepodarilo prehrať (hlásenie Kodi) | prehrávanie skončilo bez streamu, napríklad po zrušení výberu | skús to znova a vyber stream |

## Prehráva sa, ale seká sa
- **WebShare bez VIP** sťahuje rýchlosťou pár kB/s, plynulo sa prehrať nedá. Hore v menu to hlási
  „WebShare: účet bez VIP“.
- **Pomalý internet:** vyber menší súbor, alebo nastav strop v **Nastavenia → Prehrávanie → Zmerať rýchlosť
  a nastaviť dátový tok**. Súbory, ktoré by sa nestihli načítať, sa potom neponúknu.
- **Vlastné úložisko cez internet:** rozhoduje rýchlosť uploadu tam, kde úložisko stojí.

Viac v článku [Prehrávanie sa seká](seka-se-to.md).

## Prehrať v detaile filmu nič nespustí
Keď používaš TMDb Helper, daj **Nastavenia → Pokročilé → Pridať Nokturno do TMDb Helpera**.
Pozri [Prehrať v detaile filmu nič nespustí](prehrat-v-detailu.md).

---
[Všetky návody](./) · [Česky](../cs/nejde-prehrat)
