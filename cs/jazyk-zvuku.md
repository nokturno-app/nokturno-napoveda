---
slug: jazyk-zvuku
lang: cs
title: U streamu chybí jazyk zvuku
products: [kodi]
priority: 3
templates:
  kodi: |
    Ahoj, jazyk zvuku se čte z hlavičky souboru a u části streamů chybí:
    1. `[EAC3 5.1]` bez kódu jazyka znamená, že ho ten, kdo soubor nahrál, nevyplnil. Často je to originální stopa.
    2. `~CZ` s vlnovkou je jazyk odhadnutý z názvu souboru, ne ověřený.
    3. Kolik streamů se čte, nastavíš v Nastavení → Přehrávání → Zjišťovat zvuk ze souboru (kolik streamů).
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/jazyk-zvuku
    Tým Nokturno
---

# U streamu chybí jazyk zvuku

## Odkud Nokturno jazyk zná
Jazyk zvukové stopy se čte z **hlavičky souboru**. U každého streamu to chvíli trvá, proto:
- se hlavičky čtou jen u části streamů, počet nastavíš v **Nokturno → Nastavení → Přehrávání →
  Zjišťovat zvuk ze souboru (kolik streamů)**,
- na čtení se čeká nejvýš pár sekund. Co se nestihne, dočte se na pozadí a ukáže se při dalším otevření titulu.

## Co znamenají značky u streamu
- **`CZ`, `SK`, `EN`…** – jazyk ověřený z hlavičky souboru.
- **`~CZ`** s vlnovkou – jazyk odhadnutý z názvu souboru. Většinou sedí, ale ověřený není.
- **`[EAC3 5.1]`** bez kódu jazyka – stopa v souboru je, jen u ní ten, kdo soubor nahrál, nevyplnil jazyk.
  Typicky u originální anglické stopy. Nezahazuje se, často je to ta nejkvalitnější.
- **bez údajů o zvuku** – hlavičku stream ještě nemá přečtenou.

## Jak najít stream ve svém jazyce
- **Nokturno → Nastavení → Přehrávání → Preferovaný jazyk zvuku**: streamy v tomto jazyce jsou v seznamu nahoře.
- V dialogu výběru streamu je **Filtr streamů**: vybereš třeba jen zvuk CZ nebo jen titulky CZ.
- **Automaticky přepnout zvuk na preferovaný jazyk**: když má soubor víc stop, přehrávání začne tou tvojí.

## Znovu puštěný stream si pamatuje zvuk a titulky
Od verze 10.0 si Nokturno u každého titulu pamatuje zvukovou stopu a titulky, které jsi měl zapnuté naposledy.
Když pustíš **stejný stream** znovu (pokračování v rozkoukaném, další večer), přepne se na ně samo.

- Ukládá se během přehrávání, od 90 sekund sledování. Pamatuje se posledních 300 titulů.
- Obnoví se jen u **téhož souboru** a jen když v něm je stopa se stejným číslem i jazykem.
  Vypnuté titulky zůstanou vypnuté.
- Předvolby z nastavení (**Preferovaný jazyk zvuku**, **Automaticky přepnout zvuk**, titulky) se pak nepoužijí.
  Platí jen pro nový nebo jiný stream.

## Seznam streamů ukazuje jen název filmu
Streamy se vybírají v dialogu na dva řádky. Když ho skin kreslí oříznutě, uprav v **Nastavení → Výběr streamu →
Co a v jakém pořadí ukazovat u streamu**, co má být na prvním řádku.

---
[Všechny návody](../) · [Slovensky](../sk/jazyk-zvuku)
