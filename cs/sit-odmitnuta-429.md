---
slug: sit-odmitnuta-429
lang: cs
title: "„Odmítá tuto síť (HTTP 429)“"
products: [kodi, ha]
priority: 2
when: {hellspy: [paused], prehrajto: [paused]}
templates:
  kodi: |
    Ahoj, {zdroj} odmítá tvoji síť (HTTP 429). Nejčastěji kvůli VPN, mobilním datům nebo adrese sdílené s dalšími lidmi.
    1. Vypni VPN, nebo zkus jinou síť.
    2. Nokturno zdroj po odmítnutí na 10 minut samo přestane zkoušet. Ostatní zdroje fungují dál.
    3. Když se to opakuje pořád, zdroj vypni v Nokturno → Nastavení → Zdroje a účty.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/sit-odmitnuta-429
    Tým Nokturno
---

# „Odmítá tuto síť (HTTP 429)“

## Co to znamená
Zdroj odmítl dotaz z tvé internetové adresy. Nokturno to hlásí:
- **HellSpy:** „odmítá tuto síť (HTTP 429) – VPN nebo mobilní data? Zkusí se za N min“, v menu zkráceně „odmítá síť“,
- **Přehraj.to:** „pozastaveno na N min (HTTP 429)“, v menu „pozastaveno N min“.

Po první takové odpovědi Nokturno zdroj **10 minut vůbec nezkouší**, aby odmítnutí neprodlužoval.
Ostatní zdroje fungují dál.

## Proč se to stává
- **HellSpy** nemá limit na rychlost dotazů. Když odmítá, odmítá celou síť hned od prvního dotazu. Typicky VPN,
  mobilní data nebo adresu, kterou sdílíš s mnoha dalšími lidmi (běžné u některých operátorů).
- **Přehraj.to** bez účtu omezuje počet dotazů z jedné adresy. S vyplněným účtem jde hledání jinou cestou a toto
  omezení se ho netýká.

## Co udělat
1. Vypni VPN, nebo zkus jinou síť (například domácí Wi-Fi místo mobilních dat).
2. Počkej. Nokturno zdroj po pauze zkusí znovu samo.
3. U Přehraj.to vyplň účet v **Nokturno → Nastavení → Zdroje a účty**, skupina **Přehraj.to**.
4. Když HellSpy tvoji síť odmítá trvale, vypni ho (**Používat HellSpy**). Nic tím nepokazíš, ostatní zdroje zůstanou.

---
[Všechny návody](../) · [Slovensky](../sk/sit-odmitnuta-429)
