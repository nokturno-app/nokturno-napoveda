---
slug: popisy-anglicky
lang: sk
title: Popisy filmov sú po anglicky
products: [kodi]
priority: 2
templates:
  kodi: |
    Ahoj, s vlastným kľúčom TMDB budú popisy, žánre aj herci po česky. Kľúč je zadarmo.
    1. Na themoviedb.org sa zaregistruj, v nastaveniach profilu otvor API, požiadaj o kľúč (Developer) a skopíruj API Key (v3 auth).
    2. Nokturno → Nastavenia → Zdroje a účty, skupina TMDB API → API kľúč TMDB, vlož kľúč.
    3. Potom daj Nastavenia → Pokročilé → Vymazať cache (katalógy, hľadanie, streamy).
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/popisy-anglicky
    Tím Nokturno
---

# Popisy filmov sú po anglicky

## Prečo
Nokturno berie popisy z niekoľkých zdrojov. Bez vlastného kľúča TMDB a bez Luny zostane Cinemeta a tá má popisy
len po anglicky (katalóg Sosáča popis nemá vôbec).

## Čo urobiť: vlastný kľúč TMDB (zadarmo)
S kľúčom TMDB sú popisy, žánre aj herci po česky.

1. Zaregistruj sa na [themoviedb.org](https://www.themoviedb.org/).
2. Ikona profilu → **Nastavenia** → **API** (v ľavom menu) → **Request an API Key** → **Developer**.
   Vo formulári stačí ako názov aplikácie „Nokturno“.
3. Skopíruj **API Key (v3 auth)**, nie dlhší „API Read Access Token“.
4. V Kodi: **Nokturno → Nastavenia → Zdroje a účty**, skupina **TMDB API** → **API kľúč TMDB**, vlož kľúč.
   Z mobilu to ide pohodlnejšie: **Nastaviť z mobilu a prenos → Nastaviť z mobilu**.
5. **Nastavenia → Pokročilé → Vymazať cache (katalógy, hľadanie, streamy)**, nech sa popisy načítajú znova.

**Nastavenia → Pokročilé → Overiť zdroje** (v starších verziách **Otestovať zdroje**) overí aj kľúč.
Hlásenie „neplatný TMDB API klíč“ (po česky) znamená preklep, alebo skopírovaný dlhý token namiesto kľúča.

## Detail filmu z TMDb Helpera je po anglicky
TMDb Helper má vlastné nastavenie jazyka a jazyk Kodi nepreberá. V jeho nastaveniach prepni jazyk na slovenčinu.
Novší sprievodca nastavením Nokturna to ponúkne sám.

## Žánre vyzerajú divne
Pri tituloch z katalógu Sosáča môžu žánre prísť po anglicky. S kľúčom TMDB sa prepíšu. Keď zostanú,
vymaž cache (krok 5).

---
[Všetky návody](./) · [Česky](../cs/popisy-anglicky)
