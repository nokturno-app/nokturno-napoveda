---
slug: trakt
lang: cs
title: "Trakt.tv: přihlášení kódem"
products: [kodi, ha, stremio]
priority: 2
templates:
  kodi: |
    Ahoj, vlastní aplikaci na Traktu zakládat nemusíš, Nokturno má svou. Stačí přihlášení kódem, jde to i s free účtem.
    1. Nokturno → Nastavení → Zdroje a účty, skupina Trakt.tv: zapni Používat Trakt.tv a nastavení zavři tlačítkem OK.
    2. Otevři nastavení znovu a dej Přihlásit se k Traktu (kódem zařízení).
    3. Na telefonu nebo počítači otevři trakt.tv/activate a zadej kód z televize.
    Pole Vlastní Trakt client id a secret nech prázdná. Free účet může mít připojené jen dvě aplikace naráz, případně jednu odpoj na trakt.tv.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/trakt
    Tým Nokturno
---

# Trakt.tv: přihlášení kódem

Trakt.tv vede přehled zhlédnutých filmů a seriálů a seznam titulů ke zhlédnutí. Nokturno s ním umí:
- během přehrávání dát Traktu vědět, co sleduješ; dokoukaný titul se na Traktu označí jako zhlédnutý,
- v Kodi propsat na Trakt i ruční označení zhlédnuto a nezhlédnuto,
- tituly ze seznamu ke zhlédnutí na Traktu zařadit do [Hlídaných](hlidane.md) a ohlásit, až půjdou pustit.

Vlastní aplikaci na Traktu zakládat nemusíš, Nokturno má svou. Přihlásíš se kódem, heslo k Traktu se do Nokturna
nezadává. Jde to i s bezplatným účtem.

## Kodi
1. **Nokturno → Nastavení → Zdroje a účty**, skupina **Trakt.tv**: zapni **Používat Trakt.tv** a nastavení zavři
   tlačítkem **OK**, ať se uloží.
2. Otevři nastavení znovu a klikni na **Přihlásit se k Traktu (kódem zařízení)**. Na televizi se ukáže
   „Otevři https://trakt.tv/activate a zadej kód: …“.
3. Na telefonu nebo počítači otevři `trakt.tv/activate`, přihlas se k Traktu, zadej kód a připojení potvrď.
   Kód platí zhruba 10 minut.
4. Kodi ohlásí **Přihlášeno k Traktu**.

Pole **Vlastní Trakt client id (nepovinné)** a **Vlastní Trakt client secret (nepovinné)** nech prázdná.
Vyplň je jen tehdy, když máš vlastní aplikaci na developer.trakt.tv. Po jejich změně se přihlas znovu.

**Odhlásit se z Traktu** zruší přihlášení v tomto Kodi.

Přihlášení k Traktu se nesynchronizuje a nepřenáší ho ani přenos nastavení. Na každém zařízení se přihlas zvlášť.

## Home Assistant
1. V **Nástroje pro vývojáře → Akce** spusť akci **Propojit Trakt.tv** (`nokturno.trakt_auth`).
2. Kód přijde jako oznámení: do mobilu, když máš v nastavení integrace (sekce **Stahování a odkazy**)
   vyplněné **Oznámení o stažení a nových dílech**, jinak do oznámení v Home Assistantu. Kód ukáže i odpověď akce.
3. Na `trakt.tv/activate` kód zadej a připojení potvrď. Přijde oznámení „Účet je propojený.“

Pole **Trakt.tv – vlastní Client ID** a **Trakt.tv – vlastní Client Secret** v sekci **Ostatní** nech prázdná.

## Stremio a Nuvio
Stremio i Nuvio umí Trakt samy, bez Nokturna. Připoj je ke stejnému účtu na Traktu jako Kodi a Home Assistant
a na Traktu budeš mít jednu společnou historii ze všech zařízení.
- **Stremio:** Nastavení → **Trakt Scrobbling** → **Authenticate**.
- **Nuvio:** Nastavení → **Trakt**.

Kodi a Home Assistant historii na Trakt jen posílají. Zpátky si z Traktu berou jen seznam ke zhlédnutí
(do Hlídaných), ne zhlédnuté a rozkoukané tituly. Co dokoukáš ve Stremiu, se v Kodi jako zhlédnuté neoznačí.
Mezi Kodi a Home Assistantem drží zhlédnuté a rozkoukané [synchronizace](synchronizace.md).

Každá připojená aplikace se počítá do limitu bezplatného účtu (viz níž).

## Bezplatný účet: nejvýš dvě aplikace
Bezplatný účet na Traktu může mít připojené jen **dvě aplikace třetích stran naráz**. Když už dvě jiné máš,
Nokturno se nepřipojí. Některou odpoj na trakt.tv v nastavení účtu, v seznamu připojených aplikací.
Tam jde odpojit i Nokturno.

## Hlášky
| Hláška | Co udělat |
|---|---|
| „Klíč aplikace Trakt se nepodařilo načíst ze serveru Nokturna. Zkus to později, nebo vyplň vlastní aplikaci.“ | server Nokturna zrovna neodpovídá, zkus to za chvíli. V Kodi se hláška ukáže i tehdy, když **Používat Trakt.tv** není zapnuté a uložené (krok 1). |
| „Přihlášení k Traktu se nepodařilo“ | kód vypršel nebo připojení nebylo potvrzené. Spusť přihlášení znovu a kód zadej hned. U bezplatného účtu zkontroluj počet připojených aplikací. |

---
[Všechny návody](../) · [Slovensky](../sk/trakt)
