---
slug: seka-se-to
lang: cs
title: Přehrávání se seká
products: [kodi, stremio]
priority: 2
templates:
  kodi: |
    Ahoj, když se přehrávání seká, nestíhá internet nebo zdroj.
    1. Vyber menší soubor nebo nižší kvalitu. Full HD potřebuje zhruba 8–15 Mb/s, 4K 25–60 Mb/s.
    2. Nokturno → Nastavení → Přehrávání → Změřit rychlost a nastavit datový tok. Příliš velké soubory se pak nenabídnou.
    3. WebShare bez VIP stahuje jen pár kB/s, plynule nepřehraje nic.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/seka-se-to
    Tým Nokturno
  stremio: |
    Seká se ti přehrávání? Vyber menší soubor nebo nižší kvalitu.
    V nastavení doplňku (ozubené kolo) nastav v Předvolbách Nejvyšší datový tok podle svého internetu.
    WebShare bez VIP plynule nepřehraje nic.
---

# Přehrávání se seká

## Proč
Film se stahuje z internetu za běhu. Když je soubor na tvoje připojení moc velký, přehrávač čeká.
Orientačně: **Full HD 8–15 Mb/s, 4K 25–60 Mb/s**.

## Co udělat
1. **Vyber menší soubor.** V dialogu výběru je u streamu velikost a datový tok.
2. **Omez velikost souborů podle připojení:**
   - **Kodi:** **Nokturno → Nastavení → Přehrávání → Změřit rychlost a nastavit datový tok** (necelá minuta).
     Nebo nastav **Max. datový tok** ručně. Soubory, které by se nestihly načítat, se nenabídnou.
   - **Stremio:** v nastavení doplňku, sekce **Předvolby** → **Nejvyšší datový tok (Mb/s)**. Pak doplněk přidej znovu.
3. **Zkontroluj účet.** WebShare bez VIP stahuje rychlostí pár kB/s, viz [Premium, VIP a kredit](premium-a-kredit.md).
4. **Síť doma:** kabel místo Wi-Fi, nebo box blíž k routeru.

## Vlastní úložiště
Přes internet rozhoduje rychlost odesílání (upload) tam, kde úložiště stojí. Domácí linka mívá upload mnohem
menší než download.

---
[Všechny návody](../) · [Slovensky](../sk/seka-se-to)
