---
slug: zdroj-neodpovida
lang: cs
title: "„<Zdroj> neodpovídá“"
products: [kodi, ha, stremio]
priority: 2
when: {webshare: [unreachable], sledujteto: [unreachable], fastshare: [unreachable], prehrajto: [unreachable], cztor: [unreachable]}
templates:
  kodi: |
    Ahoj, Nokturno se nemůže spojit se zdrojem {zdroj}. Ostatní zdroje fungují dál.
    1. Zkus to za chvíli, zdroj mohl mít výpadek.
    2. Máš zapnutou VPN, rodičovskou kontrolu nebo blokování reklam v DNS (Pi-hole, AdGuard)? Zkus je vypnout, nebo v routeru nastav DNS 1.1.1.1.
    3. Pak dej Nokturno → Nastavení → Pokročilé → Ověřit zdroje (ve starších verzích Otestovat zdroje).
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/zdroj-neodpovida
    Tým Nokturno
---

# „<Zdroj> neodpovídá“

## Co to znamená
Nokturno se ke zdroji nedostalo: server neodpověděl včas nebo spojení skončilo chybou sítě. Hláška se ukazuje:
- nahoře v menu a ve výpisu **Stav zdrojů**: „<zdroj>: neodpovídá“,
- při hledání jako oznámení „<zdroj> neodpovídá“, ve výpisu hledání jako položka „Zdroj neodpověděl“,
- v **Ověřit zdroje**: „<zdroj> neodpovídá“.

Zdroj, který se neozve do 20 sekund, Nokturno při hledání přeskočí a ukáže streamy z ostatních.

## Proč se to stává
- **Výpadek na straně zdroje.** Za chvíli to obvykle přejde.
- **DNS blokuje adresu zdroje.** Pi-hole, AdGuard, rodičovská kontrola nebo filtr operátora.
- **VPN nebo firemní síť** spojení se zdrojem nepustí.
- **Telefon nebo tablet s Androidem:** na pozadí nemá Kodi přístup k síti. Stav pak chvíli ukazuje „neodpovídá“,
  po otevření menu se sám obnoví.
- **Luna a vlastní úložiště** mají vlastní návody: [Luna: „server neodpovídá“](luna-neodpovida.md),
  [Jak připojit vlastní úložiště](vlastni-uloziste.md).

## Co udělat
1. Zkus to za pár minut.
2. Otevři web zdroje v prohlížeči **na stejné síti**. Když nejde ani tam, je problém v síti nebo u zdroje.
3. Vypni VPN nebo blokování v DNS, případně v routeru nastav jiné DNS (například `1.1.1.1`).
4. Pak dej **Nokturno → Nastavení → Pokročilé → Ověřit zdroje** (ve starších verzích **Otestovat zdroje**).

Zdroj, který teď nechceš zkoušet, můžeš uspat: ve výpisu **Stav zdrojů** podrž OK na jeho řádku a zvol
**Uspat zdroj** (10 minut, 1 hodina, 12 hodin).

## HellSpy nebo Přehraj.to a HTTP 429
To není výpadek, ale odmítnutá síť. Viz [„Odmítá tuto síť (HTTP 429)“](sit-odmitnuta-429.md).

---
[Všechny návody](../) · [Slovensky](../sk/zdroj-neodpovida)
