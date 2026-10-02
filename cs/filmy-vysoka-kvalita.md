---
slug: filmy-vysoka-kvalita
lang: cs
title: "Filmy ve vysoké kvalitě"
products: [kodi]
priority: 2
templates:
  kodi: |
    Ahoj, na to je v Nokturnu pro Kodi položka Filmy ve vysoké kvalitě (od verze 9.8.0).
    1. V menu Filmy otevři Filmy ve vysoké kvalitě.
    2. Dej Nastavit a vyber minimální kvalitu, kanály zvuku, jazyk zvuku a titulky.
    3. Seznam se plní na pozadí, první naplnění trvá hodiny. Spustit dávku nyní to urychlí.
    4. Když tam film chybí, zkus u parametrů Libovolné.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/filmy-vysoka-kvalita
    Tým Nokturno
---

# Filmy ve vysoké kvalitě

Funkce je v Nokturnu pro Kodi od verze 9.8.0. Máš starší verzi? Postup je v [aktualizaci](aktualizace.md).

## Co to je
Seznam filmů, ke kterým Nokturno našlo stream přesně podle tvých parametrů: kvalita, kanály zvuku, jazyk zvuku a titulky.
Vychází z populárních, nejsledovanějších a nejlépe hodnocených filmů (až 200 kandidátů).
Ve Stremiu ani v Home Assistantu tato funkce není.

## Kde to najdu
V menu **Filmy** je položka **Filmy ve vysoké kvalitě**, hned pod **Nejlépe hodnocené**. Jen u filmů, ne u seriálů.
Uvnitř je:
- **Nastavit: …** – souhrn nastavení, třeba „4K · 5.1+ · zvuk CZ · titulky –“,
- **Spustit dávku nyní – ověřeno X z Y**,
- **Jak to funguje**,
- **Vše** a žánry (jen žánry, ve kterých je aspoň jeden film).

## Nastavit
**Nastavit** nabídne postupně 5 výběrů. Zpět v kterémkoli kroku = nic se neuloží.

| Krok | Volby | Výchozí |
|---|---|---|
| **Minimální kvalita** | Libovolná / Full HD / 2K / 4K | 4K |
| **Kanály zvuku** | Libovolné / 5.1 a víc | 5.1 a víc |
| **Jazyk zvuku** | Libovolný / Čeština / Slovenština / Angličtina | Čeština |
| **Titulky** | Libovolné / Čeština / Slovenština / Angličtina | Libovolné |
| **Zobrazit položku v menu Filmy** | Ano / Ne | – |

Po uložení se ukáže „Uloženo – seznam se přepočítá na pozadí.“ Změna parametrů znamená, že se seznam počítá znovu od nuly.

„Libovolné“ znamená, že na parametru nezáleží. Jazyk zvuku a titulky se berou z informací o streamu.
3D verze se nezobrazují nikdy. Za 4K se nepovažuje soubor menší než 4 GB, za 2K menší než 2,5 GB
(příliš malý soubor je podezřelý, ne skutečné 4K).

## Jak se seznam plní
- Ověřuje se na pozadí po jednom titulu. Čtou se k tomu hlavičky souborů, takže **první naplnění trvá hodiny**.
- Nové filmy přibývají, nevyhovující mizí a kontrola se opakuje po 3 dnech.
- Služba spouští dávku zhruba po 10 minutách. Neověřuje se během přehrávání a bez sítě, takže to nebrzdí zbytek doplňku.
- Seznam se udržuje sám, i když ho neotevřeš – stačí, když byl otevřený v posledních 14 dnech.

### Spustit dávku nyní
Ruční dávka 20 titulů. Průběh je v rohu obrazovky („Ověřuji X z Y – název“), na konci se ukáže
„Dávka hotová – ověřeno X, vyhovuje Y (v seznamu celkem Z)“.

## Proč tam film není
| Co se děje | Co udělat |
|---|---|
| Seznam je prázdný, ukáže „Seznam se připravuje – filmy se ověřují na pozadí.“ | Počkej, ověřování běží na pozadí. Urychlí to **Spustit dávku nyní**. |
| Film chybí | Žádný stream nesplňuje všechny parametry naráz. Zkus u některého parametru **Libovolné**. |
| Film je jen ve zmenšeném 4K | Soubor pod 4 GB se za 4K nepočítá. Sniž minimální kvalitu. |
| Film je jen ve 3D | 3D verze se nezobrazují nikdy. |

## Skrytí a vrácení položky
Když položku v **Nastavit** vypneš (**Zobrazit položku v menu Filmy** → **Ne**), z menu Filmy zmizí.
Znovu ji zapneš v **Nastavení → Přehrávání → Filmy ve vysoké kvalitě → Zobrazit položku v menu Filmy**.
Tam jdou nastavit i ostatní parametry.

---
[Všechny návody](../) · [Slovensky](../sk/filmy-vysoka-kvalita)
