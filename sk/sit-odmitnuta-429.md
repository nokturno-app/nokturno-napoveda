---
slug: sit-odmitnuta-429
lang: sk
title: "„Odmieta túto sieť (HTTP 429)“"
products: [kodi, ha]
priority: 2
when: {hellspy: [paused], prehrajto: [paused]}
templates:
  kodi: |
    Ahoj, {zdroj} odmieta tvoju sieť (HTTP 429). Najčastejšie kvôli VPN, mobilným dátam alebo adrese zdieľanej s ďalšími ľuďmi.
    1. Vypni VPN, alebo skús inú sieť.
    2. Nokturno zdroj po odmietnutí na 10 minút samo prestane skúšať. Ostatné zdroje fungujú ďalej.
    3. Keď sa to opakuje stále, zdroj vypni v Nokturno → Nastavenia → Zdroje a účty.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/sit-odmitnuta-429
    Tím Nokturno
---

# „Odmieta túto sieť (HTTP 429)“

## Čo to znamená
Zdroj odmietol dotaz z tvojej internetovej adresy. Nokturno to hlási:
- **HellSpy:** „odmieta túto sieť (HTTP 429) – VPN alebo mobilné dáta? Skúsi sa o N min“, v menu skrátene „odmieta sieť“,
- **Přehraj.to:** „pozastavené na N min (HTTP 429)“, v menu „pozastavené N min“.

Po prvej takej odpovedi Nokturno zdroj **10 minút vôbec neskúša**, aby odmietnutie nepredlžovalo.
Ostatné zdroje fungujú ďalej.

## Prečo sa to stáva
- **HellSpy** nemá limit na rýchlosť dotazov. Keď odmieta, odmieta celú sieť hneď od prvého dotazu. Typicky VPN,
  mobilné dáta alebo adresu, ktorú zdieľaš s mnohými ďalšími ľuďmi (bežné pri niektorých operátoroch).
- **Přehraj.to** bez účtu obmedzuje počet dotazov z jednej adresy. S vyplneným účtom ide hľadanie inou cestou a toto
  obmedzenie sa ho netýka.

## Čo urobiť
1. Vypni VPN, alebo skús inú sieť (napríklad domácu Wi-Fi namiesto mobilných dát).
2. Počkaj. Nokturno zdroj po pauze skúsi znova samo.
3. Pri Přehraj.to vyplň účet v **Nokturno → Nastavenia → Zdroje a účty**, skupina **Přehraj.to**.
4. Keď HellSpy tvoju sieť odmieta trvalo, vypni ho (**Používať HellSpy**). Nič tým nepokazíš, ostatné zdroje zostanú.

---
[Všetky návody](./) · [Česky](../cs/sit-odmitnuta-429)
