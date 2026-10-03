---
slug: trakt
lang: sk
title: "Trakt.tv: prihlásenie kódom"
products: [kodi, ha, stremio]
priority: 2
templates:
  kodi: |
    Ahoj, vlastnú aplikáciu na Trakte zakladať nemusíš, Nokturno má svoju. Stačí prihlásenie kódom, ide to aj s free účtom.
    1. Nokturno → Nastavenia → Zdroje a účty, skupina Trakt.tv: zapni Používať Trakt.tv a nastavenia zavri tlačidlom OK.
    2. Otvor nastavenia znova a daj Prihlásiť sa do Traktu (kódom zariadenia).
    3. Na telefóne alebo počítači otvor trakt.tv/activate a zadaj kód z televízora.
    Polia Vlastné Trakt client id a secret nechaj prázdne. Free účet môže mať pripojené len dve aplikácie naraz, prípadne jednu odpoj na trakt.tv.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/trakt
    Tím Nokturno
---

# Trakt.tv: prihlásenie kódom

Trakt.tv vedie prehľad pozretých filmov a seriálov a zoznam titulov na pozretie. Nokturno s ním vie:
- počas prehrávania dať Traktu vedieť, čo sleduješ; dopozeraný titul sa na Trakte označí ako pozretý,
- v Kodi prepísať na Trakt aj ručné označenie pozreté a nepozreté,
- synchronizovať Watchlist na Trakte s **Mojím zoznamom** v Nokturne, a to oboma smermi,
- stiahnuť z Traktu pozreté a rozpozerané tituly z iných aplikácií (Stremio, Nuvio).

Vlastnú aplikáciu na Trakte zakladať nemusíš, Nokturno má svoju. Prihlásiš sa kódom, heslo k Traktu sa do Nokturna
nezadáva. Ide to aj s bezplatným účtom.

## Kodi
1. **Nokturno → Nastavenia → Zdroje a účty**, skupina **Trakt.tv**: zapni **Používať Trakt.tv** a nastavenia zavri
   tlačidlom **OK**, aby sa uložili.
2. Otvor nastavenia znova a klikni na **Prihlásiť sa do Traktu (kódom zariadenia)**. Na televízore sa zobrazí
   „Otvor https://trakt.tv/activate a zadaj kód: …“.
3. Na telefóne alebo počítači otvor `trakt.tv/activate`, prihlás sa do Traktu, zadaj kód a pripojenie potvrď.
   Kód platí zhruba 10 minút.
4. Kodi ohlási **Prihlásené do Traktu**.

Polia **Vlastné Trakt client id (nepovinné)** a **Vlastný Trakt client secret (nepovinné)** nechaj prázdne.
Vyplň ich, len ak máš vlastnú aplikáciu na developer.trakt.tv. Po ich zmene sa prihlás znova.

**Odhlásiť sa z Traktu** zruší prihlásenie v tomto Kodi.

Prihlásenie do Traktu sa nesynchronizuje a neprenáša ho ani prenos nastavení. Na každom zariadení sa prihlás zvlášť.

## Home Assistant
1. V **Nástroje pre vývojárov → Akcie** spusti akciu **Prepojiť Trakt.tv** (`nokturno.trakt_auth`).
2. Kód príde ako upozornenie: do mobilu, keď máš v nastaveniach integrácie (sekcia **Sťahovanie a odkazy**)
   vyplnené **Upozornenia na stiahnutie a nové diely**, inak do upozornení v Home Assistante. Kód ukáže aj odpoveď akcie.
3. Na `trakt.tv/activate` kód zadaj a pripojenie potvrď. Príde upozornenie „Účet je propojený.“ (po česky).

Polia **Trakt.tv – vlastné Client ID** a Client Secret v sekcii **Ostatné** nechaj prázdne.

## Stremio a Nuvio
Stremio aj Nuvio vedia Trakt samy, bez Nokturna. Pripoj ich k rovnakému účtu na Trakte ako Kodi a Home Assistant
a na Trakte budeš mať jednu spoločnú históriu zo všetkých zariadení.
- **Stremio:** Nastavenia → **Trakt Scrobbling** → **Authenticate**.
- **Nuvio:** Nastavenia → **Trakt**.

Od verzie 9.11 si Kodi aj Home Assistant z Traktu sťahujú pozreté a rozpozerané tituly. Čo dopozeráš alebo
rozpozeráš v Stremiu či Nuviu, sa do 15 minút objaví v **Naposledy pozreté** a v **Pokračovať v sledovaní**.
- Kodi: voľba **Synchronizovať s Traktom: pozreté, rozpozerané a Watchlist** v skupine **Trakt.tv** (predvolene zapnutá).
- Home Assistant sťahuje sám, hneď ako je prepojený s Traktom. [Synchronizáciou](synchronizace.md) to potom dostanú
  aj Kodi v skupine, ktoré k Traktu prihlásené nie sú.

Prvýkrát sa berú pozretia za posledných 90 dní. Keď na Trakte pozretie zmažeš, v Nokturne zostane.
Rozpozeraný titul bez známej stopáže (pri niektorých dieloch ju Trakt nevedie) sa neprenesie.

Každá pripojená aplikácia sa počíta do limitu bezplatného účtu (pozri nižšie).

## Watchlist = Môj zoznam
Od verzie 10.0 je Watchlist na Trakte to isté ako **Môj zoznam** v Nokturne (Kodi aj Home Assistant):
- čo si pridáš na Trakte (napríklad v Stremiu alebo v aplikácii Trakt), sa objaví v Mojom zozname,
- čo pridáš do Môjho zoznamu alebo z neho odoberieš, sa hneď prepíše na Trakt,
- prvé porovnanie obe strany len zlúči a nič nezmaže, ďalšie kolá prenášajú aj odobratie,
- kontroluje sa každých 15 minút, nie pri prehrávaní a nie bez siete,
- na Trakt idú len filmy a seriály, nie jednotlivé diely ani súbory.

Tituly z Watchlistu už nie sú v [Sledovaných](hlidane.md). Keď chceš vedieť, kedy sa niektorý dá pustiť, zapni pri ňom
stráženie ručne.

## Bezplatný účet: najviac dve aplikácie
Bezplatný účet na Trakte môže mať pripojené len **dve aplikácie tretích strán naraz**. Keď už dve iné máš,
Nokturno sa nepripojí. Niektorú odpoj na trakt.tv v nastaveniach účtu, v zozname pripojených aplikácií.
Tam sa dá odpojiť aj Nokturno.

## Hlásenia
| Hlásenie | Čo urobiť |
|---|---|
| „Kľúč aplikácie Trakt sa nepodarilo načítať zo servera Nokturna. Skús to neskôr, alebo vyplň vlastnú aplikáciu.“ | server Nokturna práve neodpovedá, skús to o chvíľu. V Kodi sa hlásenie zobrazí aj vtedy, keď **Používať Trakt.tv** nie je zapnuté a uložené (krok 1). |
| „Prihlásenie do Traktu sa nepodarilo“ | kód vypršal alebo pripojenie nebolo potvrdené. Spusti prihlásenie znova a kód zadaj hneď. Pri bezplatnom účte skontroluj počet pripojených aplikácií. |

---
[Všetky návody](./) · [Česky](../cs/trakt)
