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
    2. Nejdřív zkontroluj vlastní úložiště: Nastavení → Vlastní úložiště (adresa, jméno, heslo, úložiště zapnuté). Zdroje třetích stran v Nastavení → Zdroje a účty jsou volitelné, u nové instalace jsou vypnuté.
    3. Když zdroje fungují, titul na nich nemusí být. Zkus dole v dialogu streamů hledat volněji podle názvu souboru.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/zadny-stream
    Tým Nokturno
---

# Nejde najít žádný film („Žádný stream nenalezen“)

## Co to znamená
Katalog a hledání fungují, ale u titulu se neukáže žádný stream. Kodi hlásí „Žádný stream nenalezen“,
případně „Zdroj není zapnutý nebo nastavený – zkontroluj v nastavení Zdroje a účty a Vlastní úložiště“.

Katalog a hledání běží i bez účtů. Streamy ale přicházejí jen z tvého vlastního úložiště a ze zdrojů třetích stran,
které máš zapnuté a nastavené. Zdroje třetích stran jsou volitelné a u nové instalace jsou všechny vypnuté.

## Co udělat
1. **Ověř zdroje.** **Nokturno → Nastavení → Pokročilé → Ověřit zdroje** (ve starších verzích **Otestovat zdroje**). U každého zdroje ukáže
   „v pořádku“, „není nastaveno“ nebo důvod chyby.
2. **Nastav vlastní úložiště.** Když výsledek hlásí u všeho „není nastaveno“, začni [vlastním úložištěm](vlastni-uloziste.md)
   (**Nastavení → Vlastní úložiště**). Volitelně můžeš v **Nastavení → Zdroje a účty** zapnout i zdroj třetí strany
   a vyplnit jeho účet (WebShare potřebuje VIP).
   Nejpohodlněji to jde z mobilu: **Nastavení → Nastavit z mobilu a přenos → Nastavit z mobilu**.
3. **Zdroj hlásí chybu?** Pokračuj návodem k té hlášce:
   [přihlášení](prihlaseni.md), [Premium a kredit](premium-a-kredit.md), [Luna](luna-hlasky.md).
4. **Zdroje fungují, jen tento titul nic nemá.** Titul na zdrojích nemusí vůbec být, hlavně úplné novinky.
   Ve vlastním úložišti pomůže, když název souboru nebo složky obsahuje název titulu a rok.
   - Dole v dialogu streamů zkus **Hledat volněji podle názvu souboru** (ve starších verzích **Zkusit uvolněný fulltext**).
   - Po neúspěšném hledání se doplněk zeptá „Zkusit hledat pod jiným názvem?“. Zadej český nebo originální název.

## Proč Nokturno nenabídne soubor, který na zdroji vidím
Nokturno bere jen soubory, které k titulu opravdu patří (název, rok, u seriálu číslo série a dílu, případně název dílu nebo datum vysílání v názvu souboru).
Podobný, ale jiný film záměrně vynechá. Uvolněné hledání (bod 4) ukáže i soubory, které tím sítem neprošly.

- **Soubor je výrazně kratší než film.** U filmu se nenabízí soubory kratší než zhruba 60 % oficiální stopáže (a vždy kratší než 20 minut) – bývají to ukázky a sestřihy. Díly rozděleného filmu (CD1, part1) zůstávají.
- **Film ještě nevyšel.** U filmu s premiérou za víc než dva týdny se na zdrojích třetích stran nic nenabízí, jsou tam jen ukázky nebo jiné filmy. Soubor z [vlastního úložiště](vlastni-uloziste.md) se ukáže i tak.

---
[Všechny návody](../) · [Slovensky](../sk/zadny-stream)
