---
slug: stremio-zadne-streamy
lang: cs
title: U filmu nejsou streamy Nokturna
products: [stremio]
priority: 1
templates:
  stremio: |
    U filmu nevidíš streamy Nokturna? Ve Stremiu otevři Doplňky → Nokturno → ozubené kolo.
    Nejdřív na kartě Vlastní úložiště dej Ověřit úložiště: aplikace Nokturno na něj musí dosáhnout. Pak dej ✓ Ověřit všechny účty u volitelných zdrojů třetích stran, které máš zapnuté.
    Nejčastěji jde o nedosažitelné úložiště, překlep v hesle nebo vypršelé VIP na WebShare. Po opravě ulož změny.
---

# U filmu nejsou streamy Nokturna

## Nejdřív zkontroluj
1. **Počkej pár sekund.** Stremio ukazuje streamy postupně, jak doplňky odpovídají.
2. **Běží aplikace Nokturno?** Doplněk funguje jen ve chvíli, kdy aplikace běží, viz
   [Nokturno pro Stremio – aplikace](stremio-aplikace.md).
3. **Je tam položka ⛔ Nokturno?** Přišlo příliš mnoho požadavků za sebou, viz
   [Položka „⛔ Nokturno“](stremio-polozky-nokturno.md).

## Ověř vlastní úložiště
Ve Stremiu otevři **Doplňky → Nokturno → ozubené kolo**, na kartě **Vlastní úložiště** dej **Ověřit úložiště**.
Musí na něj dosáhnout zařízení s aplikací Nokturno, viz [Jak připojit vlastní úložiště](vlastni-uloziste.md).
Soubor se k titulu přiřadí podle názvu, viz [Jak pojmenovat soubory](vlastni-uloziste.md#jak-pojmenovat-soubory).

## Ověř účty
Zdroje třetích stran jsou volitelné a v novém profilu vypnuté. U těch, které máš zapnuté, dej **Ověřit účet**
(nebo **✓ Ověřit všechny účty**).
- „Přihlášení neprošlo – zkontroluj jméno a heslo.“ (u některých zdrojů „e-mail a heslo“): viz [Zdroj hlásí „nesedí jméno nebo heslo“](prihlaseni.md).
- WebShare bez VIP, Sledujteto bez Premium, FastShare bez kreditu: viz [Premium, VIP a kredit](premium-a-kredit.md).

Po opravě dej **Uložit změny**. Když už doplněk ve Stremiu máš, platí hned.

## Jeden zdroj nefunguje, ostatní ano
Zdroj, který neodpověděl, se přeskočí a streamy přijdou z ostatních. Zkus to za chvíli znovu.

## Účty jsou v pořádku, a stejně nic
- **Titul na zdrojích nemusí vůbec být**, hlavně úplné novinky a málo známé seriály.
- Nokturno bere jen soubory, které k titulu opravdu patří (název, rok, díl). Podobné, ale jiné filmy záměrně vynechá.

## Stream je vidět, ale nepřehraje se
- U streamu je „⚠️ Ve webovém přehrávači se nepřehraje – jen v aplikaci“: takový řádek ukazuje jen starší
  aplikace Nokturno (do verze 9.6.0). Aktualizuj ji, viz [„⚠️ Ve webovém přehrávači se nepřehraje“](stremio-webovy-prehravac.md).
- WebShare občas hlásí, že je soubor dočasně nedostupný. Vyber jiný stream.

---
[Všechny návody](../) · [Slovensky](../sk/stremio-zadne-streamy)
