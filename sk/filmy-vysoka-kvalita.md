---
slug: filmy-vysoka-kvalita
lang: sk
title: "Filmy vo vysokej kvalite"
products: [kodi]
priority: 2
templates:
  kodi: |
    Ahoj, na toto je v Nokturne pre Kodi položka Filmy vo vysokej kvalite (od verzie 9.8.0).
    1. V menu Filmy otvor Filmy vo vysokej kvalite.
    2. Daj Nastaviť a vyber minimálnu kvalitu, kanály zvuku, jazyk zvuku a titulky.
    3. Zoznam sa plní na pozadí, prvé naplnenie trvá hodiny. Spustiť dávku teraz to urýchli.
    4. Ak tam film chýba, skús pri parametroch Ľubovoľné.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/filmy-vysoka-kvalita
    Tím Nokturno
---

# Filmy vo vysokej kvalite

Funkcia je v Nokturne pre Kodi od verzie 9.8.0. Máš staršiu verziu? Postup je v [aktualizácii](aktualizace.md).

## Čo to je
Zoznam filmov, ku ktorým Nokturno našlo stream presne podľa tvojich parametrov: kvalita, kanály zvuku, jazyk zvuku a titulky.
Vychádza z populárnych, najsledovanejších a najlepšie hodnotených filmov (až 200 kandidátov).
V Stremiu ani v Home Assistante táto funkcia nie je.

## Kde to nájdem
V menu **Filmy** je položka **Filmy vo vysokej kvalite**, hneď pod **Najlepšie hodnotené**. Len pri filmoch, nie pri seriáloch.
Vnútri je:
- **Nastaviť: …** – súhrn nastavenia, napríklad „4K · 5.1+ · zvuk CZ · titulky –“,
- **Spustiť dávku teraz – overených X z Y**,
- **Ako to funguje**,
- **Všetko** a žánre (len žánre, v ktorých je aspoň jeden film).

## Nastaviť
**Nastaviť** ponúkne postupne 5 výberov. Späť v ktoromkoľvek kroku = nič sa neuloží.

| Krok | Voľby | Predvolené |
|---|---|---|
| **Minimálna kvalita** | Ľubovoľná / Full HD / 2K / 4K | 4K |
| **Kanály zvuku** | Ľubovoľné / 5.1 a viac | 5.1 a viac |
| **Jazyk zvuku** | Ľubovoľný / Čeština / Slovenčina / Angličtina | Čeština |
| **Titulky** | Ľubovoľné / Čeština / Slovenčina / Angličtina | Ľubovoľné |
| **Zobraziť položku v menu Filmy** | Áno / Nie | – |

Po uložení sa ukáže „Uložené – zoznam sa prepočíta na pozadí.“ Zmena parametrov znamená, že sa zoznam počíta znova od nuly.

„Ľubovoľné“ znamená, že na parametri nezáleží. Jazyk zvuku a titulky sa berú z informácií o streame.
3D verzie sa nezobrazujú nikdy. Za 4K sa nepovažuje súbor menší ako 4 GB, za 2K menší ako 2,5 GB
(príliš malý súbor je podozrivý, nie skutočné 4K).

## Ako sa zoznam plní
- Overuje sa na pozadí po jednom titule. Číta sa na to hlavičky súborov, takže **prvé naplnenie trvá hodiny**.
- Nové filmy pribúdajú, nevyhovujúce miznú a kontrola sa opakuje po 3 dňoch.
- Služba spúšťa dávku zhruba po 10 minútach. Neoveruje sa počas prehrávania a bez siete, takže to nebrzdí zvyšok doplnku.
- Zoznam sa udržiava sám, aj keď ho neotvoríš – stačí, keď bol otvorený v posledných 14 dňoch.

### Spustiť dávku teraz
Ručná dávka 20 titulov. Priebeh je v rohu obrazovky („Overujem X z Y – názov“), na konci sa ukáže
„Dávka hotová – overených X, vyhovuje Y (v zozname celkom Z)“.

## Prečo tam film nie je
| Čo sa deje | Čo urobiť |
|---|---|
| Zoznam je prázdny, ukáže „Zoznam sa pripravuje – filmy sa overujú na pozadí.“ | Počkaj, overovanie beží na pozadí. Urýchli to **Spustiť dávku teraz**. |
| Film chýba | Žiadny stream nespĺňa všetky parametre naraz. Skús pri niektorom parametri **Ľubovoľné**. |
| Film je len v zmenšenom 4K | Súbor pod 4 GB sa za 4K nepočíta. Zníž minimálnu kvalitu. |
| Film je len v 3D | 3D verzie sa nezobrazujú nikdy. |

## Skrytie a vrátenie položky
Keď položku v **Nastaviť** vypneš (**Zobraziť položku v menu Filmy** → **Nie**), z menu Filmy zmizne.
Znova ju zapneš v **Nastaveniach → Prehrávanie → Filmy vo vysokej kvalite → Zobraziť položku v menu Filmy**.
Tam sa dajú nastaviť aj ostatné parametre.

---
[Všetky návody](./) · [Česky](../cs/filmy-vysoka-kvalita)
