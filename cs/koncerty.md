---
slug: koncerty
lang: cs
title: Koncerty
products: [kodi, stremio]
priority: 3
templates:
  kodi: |
    Ahoj, Koncerty jsou od verze 10.0 v hlavním menu Nokturna. Potřebují vlastní API klíč Last.fm, je zdarma.
    1. Klíč si založ na https://www.last.fm/api/account/create (stačí účet na Last.fm, název aplikace libovolný) a zkopíruj API key.
    2. V Kodi otevři Koncerty → Nastavit koncerty, vlož klíč a vyber hudební žánry.
    3. Hledání běží na pozadí a seznam se plní postupně, první dávka prohledá 40 interpretů hned.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/koncerty
    Tým Nokturno
  stremio: |
    Ahoj, Koncerty zapneš v nastavení doplňku, karta Koncerty: zaškrtni hudební žánry a vlož Last.fm API klíč (zdarma na https://www.last.fm/api/account/create).
    Pak dej Uložit změny a doplněk ve Stremiu přidej znovu. Seznam se plní postupně, dokud aplikace běží.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/koncerty
    Tým Nokturno
---

# Koncerty

Koncerty jsou záznamy koncertů interpretů z hudebních žánrů, které si vybereš. Nokturno si od verze 10.0 skládá
seznam samo: z [Last.fm](https://www.last.fm) vezme nejposlouchanější interprety tvých žánrů a u každého hledá
záznamy koncertů na tvých zdrojích (WebShare, HellSpy, FastShare). Seznam se plní na pozadí a pořád roste.

Funguje v Kodi a ve Stremiu. Home Assistant koncerty sám nezobrazuje, ale s vyplněným klíčem Last.fm (Nastavení integrace → Ostatní) je hledá na pozadí a sdílí se skupinou.

## Klíč Last.fm
Koncerty potřebují vlastní **API klíč Last.fm**. Je zdarma a patří jen tobě.

1. Přihlas se na [last.fm](https://www.last.fm) (nebo si založ účet).
2. Otevři [last.fm/api/account/create](https://www.last.fm/api/account/create).
3. Vyplň **Application name** (třeba „Nokturno“) a krátký popis. Ostatní pole nech prázdná.
4. Zkopíruj **API key** (ne „Shared secret“).

## Kodi
### Nastavení
1. V hlavním menu otevři **Koncerty → Nastavit koncerty**.
2. Když klíč ještě nemáš, Nokturno se na něj zeptá. Vlož **Last.fm API klíč** a Nokturno ho hned ověří.
3. V dialogu **Hudební žánry katalogu** vyber jeden nebo víc žánrů: Česká scéna, Slovenská scéna, Český rock,
   Classic rock, Hard rock, Metal, Rock, Pop, Punk, Hip-hop, Jazz, Elektronika, Folk, Klasika, Reggae, World.
4. Na otázku **„Spustit hledání koncertů nyní?“** dej **Ano**. První dávka hned prohledá 40 interpretů.

Klíč najdeš i v **Nastavení → Zdroje a účty**, skupina **Last.fm**. Tlačítko **Ověřit klíč** zkontroluje, že ho
Last.fm přijímá. Klíč jde vyplnit i přes Nastavit z mobilu a se zapnutou synchronizací účtů se dostane i do
ostatních Kodi ve skupině.

### Co je v menu Koncerty
| Položka | Co ukáže |
|---|---|
| **Nově přidané** | 50 naposledy nalezených koncertů |
| **Podle žánru** | žánry, ve kterých už je nějaký nález → interpreti s počtem koncertů |
| **Podle abecedy** | písmena (čísla a ostatní znaky pod „#“) → interpreti |
| **Prohledáno X interpretů, další přibývají – načíst teď** | průběh. Klik prohledá hned dalších 20 interpretů. |
| **Hledat interpreta** | napíšeš jméno a vybereš interpreta z výsledků (s klíčem Last.fm i podobná jména: Lucie → Lucie, Lucie Bílá). Výběr ho hned prohledá ve tvých zdrojích a přidá do seznamu – i bez žánrů. |
| **Nastavit koncerty** | změna žánrů nebo klíče |

U interpreta jsou koncerty od nejnovějšího roku. Koncert má náhled ze zdroje, stopáž a velikost souboru. Na konci je **Znovu prohledat** s datem posledního hledání.
Klik ho přehraje. Když první soubor nejde, Nokturno zkusí další kopii.

### Jak seznam roste
- Interpreti přicházejí z žebříčku Last.fm. Další stránka žebříčku přibude, jakmile jsou skoro všichni dosavadní
  prohledaní (nejvýš jednou za hodinu). Seznam tedy není omezený na 200 interpretů, roste až do 3000.
- Na pozadí se prohledá 8 interpretů za 10 minut, při přehrávání jen 1. Střídají se s
  [vlastními katalogy](vlastni-katalogy.md), které se ověřují.
- Interpret s nálezem se kontroluje každý týden, bez nálezu za 3 dny. Kdo nemá nic ani na třetí pokus, zkusí se
  znovu až za 30 dní.
- Staré odkazy se ověřují. Smazaný soubor ze seznamu zmizí.

### Synchronizace
Se zapnutým okruhem **Synchronizovat koncerty** (Nastavení → Synchronizace) se nalezené koncerty sdílí se skupinou, tedy s dalšími Kodi
i s Home Assistantem. Každé zařízení ukáže jen soubory ze zdrojů, které má samo zapnuté. Zařízení se stejnými zdroji
stejného interpreta znovu neprohledává.

### Změna žánrů
Žánry změníš přes **Nastavit koncerty**. Když žánr **přidáš**, interpreti, které už máš, zůstanou a přibudou noví.
Když žánr **odebereš**, zmizí interpreti, kteří do žádného z vybraných žánrů nepatří.

## Stremio
1. Otevři nastavení doplňku (**Doplňky → Nokturno → Konfigurovat**, nebo `http://<IP zařízení s aplikací>:7140/configure`).
2. V kartě **Koncerty** zaškrtni hudební žánry a vyplň **Last.fm API klíč**.
3. Dej **Uložit změny** a doplněk ve Stremiu **přidej znovu**, ať Stremio načte nové katalogy.

Ve Stremiu přibude druh **Koncerty** se seznamy **Nově přidané** a **Podle abecedy** (s výběrem žánru). Interpret
je plakát, jeho koncerty jsou jako díly. V seznamu **Podle abecedy** jde hledat jménem interpreta, neznámého doplněk prohledá ve zdrojích a přidá. Hledá aplikace na pozadí, dokud běží, takže se seznam zaplňuje postupně.

## Když něco nejde
| Co vidíš | Co udělat |
|---|---|
| „Klíč Last.fm neplatí.“ | překlep, nebo zkopírovaný „Shared secret“ místo API key. Zkopíruj klíč znovu. |
| „Last.fm se nepodařilo zeptat. Zkus to později.“ | Last.fm zrovna neodpovídá, zkus to za chvíli. |
| „Katalog se připravuje – interpreti se prohledávají na pozadí.“ | hledání teprve běží. Dej **načíst teď** nebo počkej. |
| interpret v seznamu chybí | ještě na něj nedošla řada, nebo na tvých zdrojích žádný koncert není. |
| málo nálezů | zapni víc zdrojů (WebShare, HellSpy, FastShare). FastShare bez kreditu se na pozadí přeskakuje. |

---
[Všechny návody](../) · [Slovensky](../sk/koncerty)
