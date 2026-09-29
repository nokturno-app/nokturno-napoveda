---
slug: zadny-stream
lang: cs
title: "Nejde najít žádný film („Žádný stream nenalezen“)"
products: [kodi]
priority: 1
templates:
  kodi: |
    Ahoj, Nokturno k titulu nenašlo žádný stream.
    1. Nokturno → Nastavení → Pokročilé → Ověřit zdroje (ve starších verzích Otestovat zdroje). Ukáže, které zdroje fungují. Když žádný, začni u něj.
    2. V Nastavení → Zdroje a účty musí být zapnutý a přihlášený aspoň jeden zdroj, nebo nastavené vlastní úložiště.
    3. Když zdroje fungují, titul na nich nemusí být. Zkus dole v dialogu streamů hledat volněji podle názvu souboru.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/zadny-stream
    Tým Nokturno
---

# Nejde najít žádný film („Žádný stream nenalezen“)

## Co to znamená
Katalog a hledání fungují, ale u titulu se neukáže žádný stream. Kodi hlásí „Žádný stream nenalezen“,
případně „Zdroj není zapnutý nebo nastavený – zkontroluj v nastavení Zdroje a účty a Vlastní úložiště“.

Katalog a hledání běží i bez účtů. Streamy ale přicházejí jen ze zdrojů, které máš zapnuté a nastavené.

## Co udělat
1. **Ověř zdroje.** **Nokturno → Nastavení → Pokročilé → Ověřit zdroje** (ve starších verzích **Otestovat zdroje**). U každého zdroje ukáže
   „v pořádku“, „není nastaveno“ nebo důvod chyby.
2. **Zapni aspoň jeden zdroj.** Když výsledek hlásí u všeho „není nastaveno“, otevři **Nastavení → Zdroje a účty**
   a vyplň účet (WebShare potřebuje VIP), nebo nastav [vlastní úložiště](vlastni-uloziste.md).
   Nejpohodlněji to jde z mobilu: **Nastavení → Nastavit z mobilu a přenos → Nastavit z mobilu**.
3. **Zdroj hlásí chybu?** Pokračuj návodem k té hlášce:
   [přihlášení](prihlaseni.md), [Premium a kredit](premium-a-kredit.md), [Luna](luna-hlasky.md).
4. **Zdroje fungují, jen tento titul nic nemá.** Titul na zdrojích nemusí vůbec být, hlavně úplné novinky.
   - Dole v dialogu streamů zkus **Hledat volněji podle názvu souboru** (ve starších verzích **Zkusit uvolněný fulltext**).
   - Po neúspěšném hledání se doplněk zeptá „Zkusit hledat pod jiným názvem?“. Zadej český nebo originální název.

## Proč Nokturno nenabídne soubor, který na zdroji vidím
Nokturno bere jen soubory, které k titulu opravdu patří (název, rok, u seriálu číslo série a dílu).
Podobný, ale jiný film záměrně vynechá. Uvolněné hledání (bod 4) ukáže i soubory, které tím sítem neprošly.

---
[Všechny návody](../) · [Slovensky](../sk/zadny-stream)
