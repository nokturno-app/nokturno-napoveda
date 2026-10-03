---
slug: popisy-anglicky
lang: cs
title: Popisy filmů jsou anglicky
products: [kodi]
priority: 2
templates:
  kodi: |
    Ahoj, s vlastním klíčem TMDB budou popisy, žánry i herci česky. Klíč je zdarma.
    1. Na themoviedb.org se zaregistruj, v nastavení profilu otevři API, požádej o klíč (Developer) a zkopíruj API Key (v3 auth).
    2. Nokturno → Nastavení → Zdroje a účty, skupina TMDB API → API klíč TMDB, vlož klíč.
    3. Pak dej Nastavení → Pokročilé → Vymazat cache (katalogy, hledání, streamy).
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/popisy-anglicky
    Tým Nokturno
---

# Popisy filmů jsou anglicky

## Proč
Nokturno bere popisy z několika zdrojů. Bez vlastního klíče TMDB a bez Luny zbude Cinemeta, a ta má popisy
jen anglicky (katalog Sosáče popis nemá vůbec).

## Co udělat: vlastní klíč TMDB (zdarma)
1. Zaregistruj se na [themoviedb.org](https://www.themoviedb.org/).
2. Ikona profilu → **Nastavení** → **API** (v levém menu) → **Request an API Key** → **Developer**.
   Ve formuláři stačí jako název aplikace „Nokturno“.
3. Zkopíruj **API Key (v3 auth)**, ne delší „API Read Access Token“.
4. V Kodi: **Nokturno → Nastavení → Zdroje a účty**, skupina **TMDB API** → **API klíč TMDB**, vlož klíč.
   Z mobilu to jde pohodlněji: **Nastavit z mobilu a přenos → Nastavit z mobilu**.
5. **Nastavení → Pokročilé → Vymazat cache (katalogy, hledání, streamy)**, ať se popisy načtou znovu.

**Nastavení → Pokročilé → Ověřit zdroje** (ve starších verzích **Otestovat zdroje**) ověří i klíč.
Tlačítko **Ověřit klíč** hned pod polem zkontroluje, že ho TMDB přijímá. „Klíč TMDB neplatí.“ znamená překlep, nebo zkopírovaný dlouhý token místo klíče.

## Detail filmu z TMDb Helperu je anglicky
TMDb Helper má vlastní nastavení jazyka a jazyk Kodi nepřebírá. V jeho nastavení přepni jazyk na češtinu.
Novější průvodce nastavením Nokturna to nabídne sám.

## Žánry vypadají divně
U titulů z katalogu Sosáče můžou žánry přijít anglicky. S klíčem TMDB se přepíšou. Když zůstanou,
vymaž cache (krok 5).

---
[Všechny návody](../) · [Slovensky](../sk/popisy-anglicky)
