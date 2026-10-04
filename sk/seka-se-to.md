---
slug: seka-se-to
lang: sk
title: Prehrávanie sa seká
products: [kodi, stremio]
priority: 2
templates:
  kodi: |
    Ahoj, keď sa prehrávanie seká, nestíha internet alebo zdroj.
    1. Vyber menší súbor alebo nižšiu kvalitu. Full HD potrebuje zhruba 8–15 Mb/s, 4K 25–60 Mb/s.
    2. Nokturno → Nastavenia → Prehrávanie → Zmerať rýchlosť a nastaviť dátový tok. Príliš veľké súbory sa potom neponúknu.
    3. Pri vlastnom úložisku cez internet rozhoduje rýchlosť odosielania (upload) tam, kde úložisko stojí.
    4. Z voliteľných zdrojov: WebShare bez VIP sťahuje len pár kB/s, plynulo neprehrá nič.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/seka-se-to
    Tím Nokturno
  stremio: |
    Seká sa ti prehrávanie? Vyber menší súbor alebo nižšiu kvalitu.
    V nastaveniach doplnku (ozubené koliesko) nastav v Predvoľbách Najvyšší dátový tok podľa svojho internetu.
    WebShare bez VIP plynulo neprehrá nič.
---

# Prehrávanie sa seká

## Prečo
Film sa sťahuje z internetu za behu. Keď je súbor na tvoje pripojenie príliš veľký, prehrávač čaká.
Orientačne: **Full HD 8–15 Mb/s, 4K 25–60 Mb/s**.

## Čo urobiť
1. **Vyber menší súbor.** V dialógu výberu je pri streame veľkosť a dátový tok.
2. **Obmedz veľkosť súborov podľa pripojenia:**
   - **Kodi:** **Nokturno → Nastavenia → Prehrávanie → Zmerať rýchlosť a nastaviť dátový tok** (necelá minúta).
     Alebo nastav **Max. dátový tok** ručne. Súbory, ktoré by sa nestihli načítavať, sa neponúknu.
   - **Stremio:** v nastaveniach doplnku, sekcia **Predvoľby** → **Najvyšší dátový tok (Mb/s)**. Potom ulož zmeny.
3. **Skontroluj zdroj.** Pri [vlastnom úložisku](#vlastne-ulozisko) rozhoduje rýchlosť linky, kde stojí.
   Z voliteľných zdrojov tretích strán: WebShare bez VIP sťahuje rýchlosťou pár kB/s, pozri [Premium, VIP a kredit](premium-a-kredit.md).
4. **Sieť doma:** kábel namiesto Wi-Fi, alebo box bližšie k routeru.

## Vlastné úložisko
Cez internet rozhoduje rýchlosť odosielania (upload) tam, kde úložisko stojí. Domáca linka máva upload oveľa
menší ako download.

---
[Všetky návody](./) · [Česky](../cs/seka-se-to)
