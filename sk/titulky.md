---
slug: titulky
lang: sk
title: Chýbajú titulky alebo nesedia k dielu
products: [kodi]
priority: 2
templates:
  kodi: |
    Ahoj, k titulkom v Nokturne:
    1. Nokturno → Nastavenia → Prehrávanie: nastav Preferovaný jazyk zvuku a pri Titulky zvoľ, kedy sa majú zapínať.
    2. Keď zdroj titulky nemá, Nokturno ich skúsi nájsť na OpenSubtitles. Stav ukáže Nastavenia → Zdroje a účty → OpenSubtitles → Overiť OpenSubtitles.
    3. Bez účtu sa dá stiahnuť 5 titulkov denne, s bezplatným účtom na opensubtitles.com 20.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/titulky
    Tím Nokturno
---

# Chýbajú titulky alebo nesedia k dielu

## Kedy sa titulky zapnú
**Nokturno → Nastavenia → Prehrávanie → Titulky:**
- **Nechať na Kodi** – Nokturno do titulkov nezasahuje,
- **Keď chýba zvuk v preferovanom jazyku** (predvolené) – titulky sa zapnú, len keď film nemá zvuk
  v jazyku z **Preferovaný jazyk zvuku**. Slovenčina a čeština sa navzájom zastúpia,
- **Vždy v preferovanom jazyku**.

Keď je zvuk v preferovanom jazyku, titulky sa vypnú.

## Odkiaľ sú titulky
1. Z **videa samotného** (titulky vo vnútri súboru, aj pri súboroch z vlastného úložiska).
2. Z voliteľného **zdroja tretej strany**, napríklad súbor s titulkami vedľa videa na WebShare. K dielu seriálu sa priradí, len keď
   číslo dielu sedí aj v názve súboru s titulkami.
3. Z **OpenSubtitles**, keď stream žiadne iné titulky nemá. Hľadá sa podľa IMDb id filmu alebo dielu,
   titulky sa stiahnu až pri prehrávaní.

## OpenSubtitles
**Nokturno → Nastavenia → Zdroje a účty**, skupina **OpenSubtitles**:
- bez účtu sa dá stiahnuť **5 titulkov denne** pre tvoju internetovú adresu,
- s bezplatným účtom na opensubtitles.com **20 denne** – vyplň meno a heslo,
- **Overiť OpenSubtitles** (v starších verziách **Vyskúšať OpenSubtitles**) ukáže, či to funguje a koľko stiahnutí dnes zostáva.

## Titulky nesedia časovo
Titulky sú k inej verzii videa. Skús iný stream, alebo titulky posuň v nastaveniach titulkov počas prehrávania v Kodi.

---
[Všetky návody](./) · [Česky](../cs/titulky)
