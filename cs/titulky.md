---
slug: titulky
lang: cs
title: Chybí titulky nebo nesedí k dílu
products: [kodi]
priority: 2
templates:
  kodi: |
    Ahoj, k titulkům v Nokturnu:
    1. Nokturno → Nastavení → Přehrávání: nastav Preferovaný jazyk zvuku a u Titulky zvol, kdy se mají zapínat.
    2. Když zdroj titulky nemá, Nokturno je zkusí najít na OpenSubtitles. Stav ukáže Nastavení → Zdroje a účty → OpenSubtitles → Ověřit OpenSubtitles.
    3. Bez účtu jde stáhnout 5 titulků denně, s bezplatným účtem na opensubtitles.com 20.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/titulky
    Tým Nokturno
---

# Chybí titulky nebo nesedí k dílu

## Kdy se titulky zapnou
**Nokturno → Nastavení → Přehrávání → Titulky:**
- **Nechat na Kodi** – Nokturno do titulků nezasahuje,
- **Když chybí zvuk v preferovaném jazyce** (výchozí) – titulky se zapnou, jen když film nemá zvuk
  v jazyce z **Preferovaný jazyk zvuku**. Čeština a slovenština se navzájem zastoupí,
- **Vždy v preferovaném jazyce**.

Když je zvuk v preferovaném jazyce, titulky se vypnou.

## Odkud titulky jsou
1. Z **videa samotného** (titulky uvnitř souboru).
2. Ze **zdroje**, například soubor s titulky vedle videa na WebShare. K dílu seriálu se přiřadí, jen když
   číslo dílu sedí i v názvu souboru s titulky.
3. Z **OpenSubtitles**, když stream žádné jiné titulky nemá. Hledá se podle IMDb id filmu nebo dílu,
   titulky se stáhnou až při přehrání.

## OpenSubtitles
**Nokturno → Nastavení → Zdroje a účty**, skupina **OpenSubtitles**:
- bez účtu jde stáhnout **5 titulků denně** pro tvoji internetovou adresu,
- s bezplatným účtem na opensubtitles.com **20 denně** – vyplň jméno a heslo,
- **Ověřit OpenSubtitles** (ve starších verzích **Vyzkoušet OpenSubtitles**) ukáže, jestli to funguje a kolik stažení dnes zbývá.

## Titulky nesedí časově
Titulky jsou k jiné verzi videa. Zkus jiný stream, nebo titulky posuň v nastavení titulků během přehrávání v Kodi.

---
[Všechny návody](../) · [Slovensky](../sk/titulky)
