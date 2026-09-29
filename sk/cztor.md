---
slug: cztor
lang: sk
title: "CZtor: „zariadenie nie je spárované“"
products: [kodi, ha, stremio]
priority: 2
when: {cztor: [not_paired, expired]}
templates:
  kodi: |
    Ahoj, CZtor u teba nie je spárovaný, preto z neho nič nepríde.
    1. Nokturno → Nastavenia → Zdroje a účty, skupina CZtor → Spárovať PIN kódom.
    2. Na telefóne alebo počítači otvor cztor.com/activate, prihlás sa a zadaj PIN z televízora.
    3. Stav účtu v rovnakej skupine ukáže predplatné. CZtor bez predplatného neprehrá nič.
    Nepoužívaš CZtor? V skupine CZtor vypni Používať CZtor.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/cztor
    Tím Nokturno
---

# CZtor: „zariadenie nie je spárované“

CZtor je katalóg na predplatné (cztor.com). Heslo sa do Nokturna nezadáva, zariadenie sa spáruje PIN kódom.

## Kodi
1. **Nokturno → Nastavenia → Zdroje a účty**, skupina **CZtor**, zapni **Používať CZtor**.
2. Klikni na **Spárovať PIN kódom**. Na televízore sa zobrazí adresa a PIN.
3. Na telefóne alebo počítači otvor `cztor.com/activate`, prihlás sa a zadaj PIN.
4. **Stav účtu** ukáže, aké máš predplatné a do kedy.

Hlásenia:
| Hlásenie | Čo urobiť |
|---|---|
| hore v menu „CZtor: nie je spárované“, vo výpise „zariadenie nie je spárované“ | spáruj PIN kódom (klik na riadok vedie rovno tam) |
| „CZtor nie je spárovaný – použi Spárovať PIN kódom.“ | spáruj PIN kódom |
| „Spárovanie s CZtorom sa nepodarilo.“, „PIN vypršel…“ (po česky) | spusti Spárovať PIN kódom znova a PIN zadaj hneď |
| „Predplatné CZtor nie je aktívne.“, „predplatné vypršalo“ | predĺž predplatné na cztor.com |

**Odhlásiť toto zariadenie** zruší spárovanie len v tomto Kodi.

Po **prenose nastavení** alebo **synchronizácii účtov** do iného Kodi sa spárovanie neprenáša. Každé zariadenie
sa páruje samo.

## Home Assistant
**Nastavenia → Zariadenia a služby → Nokturno → Konfigurovať**, sekcia **Zdroje a účty**: zapni **Používať CZtor**.
Formulár potom ukáže PIN a adresu `cztor.com/activate`. Vypršaný PIN si vyžiadaj znova.

## Stremio
Na stránke [nokturno.stream/configure](https://nokturno.stream/configure) je karta **CZtor**:
1. Klikni na **Spárovať CZtor**. Zobrazí sa PIN a odkaz na `cztor.com/activate`.
2. Tam sa prihlás a PIN zadaj. Formulár to o pár sekúnd sám spozná a ukáže „✓ Spárované“ s dátumom konca predplatného.
3. Adresa doplnku sa tým zmení. Doplnok pridaj znova tlačidlom **Pridať do Stremia** a starý odinštaluj.

Heslo sa ani tu nezadáva. Do adresy doplnku ide len náhodný kľúč. Prihlásenie do CZtoru drží server zapečatené
týmto kľúčom, takže bez tvojej adresy doplnku ho nikto neprečíta. Streamy z CZtoru hrajú aj vo webovom Stremiu.

Po spárovaní má karta tlačidlá **Overiť účet** (stav predplatného) a **Zrušiť párovanie**. Po zrušení párovania
odober zariadenie „Nokturno Stremio“ aj na cztor.com v zozname zariadení.

| Hlásenie vo formulári | Čo urobiť |
|---|---|
| „Spárované, ale bez aktívneho predplatného – streamy sa neukážu.“ | predĺž predplatné na cztor.com |
| „PIN vypršal, skús to znova.“ | klikni na **Spárovať CZtor** znova a PIN zadaj hneď |

---
[Všetky návody](./) · [Česky](../cs/cztor)
