---
slug: cztor
lang: cs
title: "CZtor: „zařízení není spárované“"
products: [kodi, ha, stremio]
priority: 2
when: {cztor: [not_paired, expired]}
templates:
  kodi: |
    Ahoj, CZtor u tebe není spárovaný, proto z něj nic nepřijde.
    1. Nokturno → Nastavení → Zdroje a účty, skupina CZtor → Spárovat PINem.
    2. Na telefonu nebo počítači otevři cztor.com/activate, přihlas se a zadej PIN z televize.
    3. Stav účtu ve stejné skupině ukáže předplatné. CZtor bez předplatného nepřehraje nic.
    Nepoužíváš CZtor? Ve skupině CZtor vypni Používat CZtor.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/cztor
    Tým Nokturno
---

# CZtor: „zařízení není spárované“

CZtor je katalog na předplatné (cztor.com). Heslo se do Nokturna nezadává, zařízení se spáruje PINem.

## Kodi
1. **Nokturno → Nastavení → Zdroje a účty**, skupina **CZtor**, zapni **Používat CZtor**.
2. Klikni na **Spárovat PINem**. Na televizi se ukáže adresa a PIN.
3. Na telefonu nebo počítači otevři `cztor.com/activate`, přihlas se a zadej PIN.
4. **Stav účtu** ukáže, jaké máš předplatné a do kdy.

Hlášky:
| Hláška | Co udělat |
|---|---|
| nahoře v menu „CZtor: není spárováno“, ve výpisu „zařízení není spárované“ | spáruj PINem (klik na řádek vede rovnou tam) |
| „CZtor není spárovaný – použij Spárovat PINem.“ | spáruj PINem |
| „Spárování s CZtorem se nepodařilo.“, „PIN vypršel…“ | spusť Spárovat PINem znovu a PIN zadej hned |
| „Předplatné CZtor není aktivní.“, „předplatné vypršelo“ | prodluž předplatné na cztor.com |

**Odhlásit toto zařízení** zruší spárování jen v tomto Kodi.

Po **přenosu nastavení** nebo **synchronizaci účtů** do jiného Kodi se spárování nepřenáší. Každé zařízení
se páruje samo.

## Home Assistant
**Nastavení → Zařízení a služby → Nokturno → Konfigurovat**, sekce **Zdroje a účty**: zapni **Používat CZtor**.
Formulář pak ukáže PIN a adresu `cztor.com/activate`. Vypršelý PIN si vyžádej znovu.

## Stremio
V nastavení doplňku (ve Stremiu **Doplňky → Nokturno → ozubené kolo**, nebo `http://<IP zařízení s aplikací>:7140/configure`) je karta **CZtor**:
1. Klikni na **Spárovat CZtor**. Ukáže se PIN a odkaz na `cztor.com/activate`.
2. Tam se přihlas a PIN zadej. Formulář to za pár vteřin sám pozná a ukáže „✓ Spárováno“ s datem konce předplatného.
3. Adresa doplňku se tím změní. Doplněk přidej znovu tlačítkem **Přidat do Stremia** a starý odinstaluj.

Heslo se ani tady nezadává. Do adresy doplňku jde jen náhodný klíč. Přihlášení k CZtoru drží aplikace Nokturno zapečetěné
tímto klíčem, takže bez tvé adresy doplňku ho nikdo nepřečte. Streamy z CZtoru hrají i ve webovém Stremiu.

Po spárování má karta tlačítka **Ověřit účet** (stav předplatného) a **Zrušit párování**. Po zrušení párování
odeber zařízení „Nokturno Stremio“ i na cztor.com v seznamu zařízení.

| Hláška ve formuláři | Co udělat |
|---|---|
| „Spárováno, ale bez aktivního předplatného – streamy se neukážou.“ | prodluž předplatné na cztor.com |
| „PIN vypršel, zkus to znovu.“ | klikni na **Spárovat CZtor** znovu a PIN zadej hned |

---
[Všechny návody](../) · [Slovensky](../sk/cztor)
