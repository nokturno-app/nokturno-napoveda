---
slug: stremio-instalace
lang: sk
title: Ako pridať Nokturno do Stremia alebo Nuvia
products: [stremio]
priority: 1
templates:
  stremio: |
    Nokturno pre Stremio je aplikácia, ktorú si spustíš u seba: github.com/nokturno-app/nokturno-stremio-app/releases
    Potom otvor http://<IP zariadenia s aplikáciou>:7140/configure, vyplň úložisko alebo účty, daj Overiť a Pridať do Stremia.
    Na TV sa doplnok objaví sám, keď ho pridáš na telefóne pod rovnakým účtom Stremio.
---

# Ako pridať Nokturno do Stremia alebo Nuvia

Doplnok pre Stremio beží v aplikácii **Nokturno pre Stremio** u teba doma. Ako ju stiahnuť a spustiť, je v článku
[Nokturno pre Stremio – aplikácia](stremio-aplikace.md). Tvoje nastavenie je zakódované v adrese doplnku,
ktorú si vyrobíš na stránke nastavenia v aplikácii.

## 1. Vyplň nastavenie
Otvor v prehliadači `http://<IP adresa zariadenia s aplikáciou>:7140/configure` (na tom istom zariadení
`http://127.0.0.1:7140/configure`, po slovensky sa zobrazí podľa jazyka prehliadača):
1. **Vlastné úložisko a zdroje** – vlastné úložisko a voliteľne účty zdrojov. Pri každom daj **Overiť účet**
   (pri úložisku **Overiť úložisko**).
2. **Predvoľby** – jazyk zvuku, radenie, katalógy. Tento krok sa dá preskočiť.
3. Potvrď súhlas s podmienkami použitia.

## 2. Pridaj doplnok
| Kde | Ako |
|---|---|
| **Počítač** | **Pridať do Stremia**, prehliadač sa spýta, či otvoriť Stremio, potvrď. V Stremiu **Inštalovať**. |
| **Telefón** | Otvor stránku v telefóne so Stremiom, **Pridať do Stremia** a **Inštalovať**. Keď sa Stremio neotvorí, použi **Skopírovať adresu**. |
| **Televízor** | Pridaj doplnok na telefóne alebo počítači **pod rovnakým účtom Stremio**. Na TV sa objaví do minúty. Ručne: Stremio → Doplnky → pole hore → vložiť adresu → Inštalovať. |
| **Nuvio** | **Pridať do Nuvia**. Na TV: **Skopírovať adresu**, potom v Nuviu Nastavenia → Doplnky → vložiť adresu → Inštalovať. |
| **Streamlet** | **Skopírovať adresu**, v Streamlete pridaj doplnok Stremia a adresu vlož. |

Keď stránku otvoríš cez IP adresu, dostane doplnok adresu `https://…my.local-ip.co:7141`. Tú Stremio prijme
aj z iného zariadenia v sieti, pozri [Nokturno pre Stremio – aplikácia](stremio-aplikace.md).
Doplnok funguje len vtedy, keď aplikácia beží.

Adresa doplnku obsahuje tvoje účty. Nikomu ju neposielaj.

## Zmena nastavenia
V Stremiu **Doplnky → Nokturno → ozubené koliesko**. Otvorí sa stránka s tvojím nastavením. Uprav ho a znova daj
**Pridať do Stremia**. Zmenené nastavenie je nová adresa: starý doplnok v Stremiu odinštaluj, inak tam
Nokturno bude dvakrát.

## Nokturno mám v Stremiu dvakrát
Je to starý a nový doplnok s iným nastavením. V Stremiu **Doplnky** odinštaluj ten, ktorý nechceš. Doplnok
s adresou `nokturno.stream` odinštaluj vždy, ten od 30. 9. 2026 nefunguje.

---
[Všetky návody](./) · [Česky](../cs/stremio-instalace)
