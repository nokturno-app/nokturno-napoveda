---
slug: vlastni-uloziste
lang: cs
title: Jak připojit vlastní úložiště
products: [kodi, stremio]
priority: 1
when: {storage: [unreachable, bad_login]}
templates:
  kodi: |
    Ahoj, Nokturno se nemůže spojit s tvým vlastním úložištěm.
    1. Nokturno → Nastavení → Vlastní úložiště: zkontroluj Adresu složky, uživatelské jméno a heslo.
    2. Adresa v domácí síti (například 192.168.…) funguje jen doma. Mimo domov je potřeba veřejná adresa nebo VPN.
    3. Úložiště, které nepoužíváš, vypni volbou Používat toto úložiště. Zůstane vyplněné, jen se v něm nebude hledat.
    4. Pak dej Nastavení → Pokročilé → Ověřit zdroje (ve starších verzích Otestovat zdroje).
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/vlastni-uloziste
    Tým Nokturno
---

# Jak připojit vlastní úložiště

Vlastní úložiště je hlavní funkce Nokturna: přehrává tvoje soubory z NAS, Nextcloudu nebo jiného serveru s WebDAV.
Soubor, který k titulu patří, se ukáže **mezi streamy jako první**.

## Co je potřeba
- složka dostupná přes **WebDAV** (`http://` nebo `https://`, tvar `davs://` z Kodi jde taky),
- jméno a heslo, pokud je úložiště chráněné,
- úložiště musí být **dosažitelné ze zařízení, na kterém přehráváš**. Adresa v domácí síti funguje jen doma.

## Kodi
**Nokturno → Nastavení → Vlastní úložiště**, pro každé ze tří úložišť:

| Pole | K čemu |
|---|---|
| **Používat toto úložiště** (dřív **Použít toto úložiště**) | vypnuté úložiště zůstane vyplněné, jen se v něm nehledá |
| **Adresa složky** | WebDAV složka s filmy a seriály, například `https://nas.example.cz:5006/video/` |
| **Uživatelské jméno**, **Heslo** | přihlášení k úložišti |
| **Název** | ukáže se u streamů (například `NAS`) |

Pak dej **Nastavení → Pokročilé → Ověřit zdroje** (ve starších verzích **Otestovat zdroje**).

## Stremio
Na stránce nastavení doplňku ([nokturno.stream/configure](https://nokturno.stream/configure)) vyplň kartu
**Vlastní úložiště** a dej **Ověřit úložiště**. Pak doplněk přidej znovu tlačítkem **Přidat do Stremia**.

Ve Stremiu platí dvě věci navíc:
- Úložiště musí být dosažitelné **ze serveru doplňku** (ten v něm hledá soubory) **i ze zařízení**, kde přehráváš.
  Adresa v domácí síti proto s doplňkem na `nokturno.stream` nefunguje.
- Soubor z úložiště se **nepřehraje ve webovém Stremiu** v prohlížeči, jen v aplikaci (Stremio pro počítač,
  Android a Android TV, nebo Nuvio). U takového streamu je upozornění „⚠️ Ve webovém přehrávači se nepřehraje – jen v aplikaci“.

## Hlášky
| Kde | Hláška | Co udělat |
|---|---|---|
| nahoře v menu, Ověřit zdroje | „Úložiště: neodpovídá“, „<název> neodpovídá“ | adresa není z Kodi dosažitelná: jiná síť, vypnutý server, nevystavený port. Zkus adresu otevřít v prohlížeči ve stejné síti. |
| nahoře v menu | „Úložiště: nesedí jméno nebo heslo“ | přihlašovací údaje k úložišti, ne k Nokturnu |
| při hledání | „<název>: špatné jméno nebo heslo“, „<název>: složka neexistuje“ | oprav jméno, heslo nebo cestu ke složce |
| u titulu | soubor se nenabídne | zkontroluj pojmenování (níže); nový soubor se ukáže nejpozději do hodiny |

## Jak pojmenovat soubory
- **Film:** název na začátku, rok v závorce – `Filmy/Pelíšky (1999).mkv`.
- **Seriál:** značka dílu je nutná – `Seriály/Hospoda/Hospoda S02E04 - Úraz.avi` (jde i `2x04`).
- Když má film český název úplně jiný než originál, dej ho do složky s originálním názvem.

Podrobnosti: [Vlastní úložiště](../navody/kodi/vlastni-uloziste.md).

---
[Všechny návody](../) · [Slovensky](../sk/vlastni-uloziste)
