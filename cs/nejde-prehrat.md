---
slug: nejde-prehrat
lang: cs
title: Film se najde, ale nejde přehrát
products: [kodi]
priority: 1
templates:
  kodi: |
    Ahoj, stream se ti ukáže, ale nepřehraje se.
    1. U souboru z vlastního úložiště zkontroluj, že na úložiště zařízení dosáhne (Nastavení → Vlastní úložiště, Ověřit zdroje).
    2. Zkus jiný stream ze seznamu. Když jeden nejde, Nokturno samo zkusí ještě několik dalších.
    3. Když nejdou streamy jen z jednoho volitelného zdroje třetí strany, zkontroluj u něj účet: Sledujteto a Přehraj.to potřebují Premium, FastShare / Sdilej.cz kredit, WebShare VIP.
    4. Nokturno → Nastavení → Pokročilé → Ověřit zdroje (ve starších verzích Otestovat zdroje) ukáže stav úložiště i účtů.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/nejde-prehrat
    Tým Nokturno
---

# Film se najde, ale nejde přehrát

## Co to znamená
V dialogu výběru se streamy ukážou, ale po výběru se nic nepustí. Kodi hlásí třeba
„Jednu nebo více položek se nepodařilo přehrát“, nebo Nokturno ukáže důvod od zdroje.

Když jeden stream nejde, Nokturno samo zkusí jeho kopie a pak několik dalších streamů. Chyba se ukáže,
až když neprojde žádný z nich.

## Co udělat podle hlášky
| Hláška | Co to znamená | Co udělat |
|---|---|---|
| Úložiště: neodpovídá, Úložiště: nesedí jméno nebo heslo | zařízení nedosáhne na tvoje vlastní úložiště, nebo nesedí přihlášení | [Jak připojit vlastní úložiště](vlastni-uloziste.md) |
| Sledujteto: přehrávání vyžaduje Premium účet | Sledujteto bez Premium odkaz na soubor nevydá | [Premium, VIP a kredit](premium-a-kredit.md) |
| FastShare: na soubor … nestačí kredit (…) | na účtu FastShare / Sdilej.cz chybí kredit | dobij kredit, nebo vyber menší soubor |
| FastShare: přihlášení se nepovedlo…, Přehraj.to: přihlášení se nepovedlo… | zdroj odmítl přihlášení | [Zdroj hlásí „nesedí jméno nebo heslo“](prihlaseni.md) |
| CZtor: stream už v CZtor není… | soubor mezitím zmizel | vyber jiný stream |
| file_link: File temporarily unavailable | WebShare soubor zrovna nevydal | vyber jiný stream |
| Jednu nebo více položek se nepodařilo přehrát (hláška Kodi) | přehrání skončilo bez streamu, třeba po zrušení výběru | zkus to znovu a vyber stream |

## Přehrává se, ale seká se
- **Vlastní úložiště přes internet:** rozhoduje rychlost uploadu tam, kde úložiště stojí.
- **WebShare bez VIP** stahuje rychlostí pár kB/s, plynule se přehrát nedá. Nahoře v menu to hlásí
  „WebShare: účet bez VIP“.
- **Pomalý internet:** vyber menší soubor, nebo nastav strop v **Nastavení → Přehrávání → Změřit rychlost
  a nastavit datový tok**. Soubory, které by se nestihly načítat, se pak nenabídnou.

Víc v článku [Přehrávání se seká](seka-se-to.md).

## Přehrát v detailu filmu nic nepustí
Když používáš TMDb Helper, dej **Nastavení → Pokročilé → Přidat Nokturno do TMDb Helperu**.
Viz [Přehrát v detailu filmu nic nepustí](prehrat-v-detailu.md).

---
[Všechny návody](../) · [Slovensky](../sk/nejde-prehrat)
