---
slug: prehrat-v-detailu
lang: cs
title: Přehrát v detailu filmu nic nepustí
products: [kodi]
priority: 2
templates:
  kodi: |
    Ahoj, aby tlačítko Přehrát v detailu filmu (TMDb Helper, Arctic Fuse a další skiny) hledalo streamy v Nokturnu:
    1. Nokturno → Nastavení → Pokročilé → Přidat Nokturno do TMDb Helperu (Přehrát v detailu filmu).
    2. Potvrď Nokturno jako výchozí přehrávač.
    3. Pak dej v detailu filmu Přehrát. Otevře se výběr streamu.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/prehrat-v-detailu
    Tým Nokturno
---

# Přehrát v detailu filmu nic nepustí

## Detail z TMDb Helperu (Arctic Fuse a další skiny)
Detail filmu v mnoha skinech kreslí doplněk **TMDb Helper**. Ten přehrává přes takzvané přehrávače a o Nokturnu
musí vědět.

1. **Nokturno → Nastavení → Pokročilé → Přidat Nokturno do TMDb Helperu (Přehrát v detailu filmu).**
2. Na otázku „Nastavit Nokturno jako výchozí přehrávač v TMDb Helperu?“ odpověz ano.
   Objeví se „Nokturno je v TMDb Helperu“.
3. Tlačítko **Přehrát** v detailu pak otevře výběr streamu v Nokturnu.

Hláška „TMDb Helper není nainstalovaný“ znamená, že detail kreslí skin sám. Pak Přehrát funguje bez nastavování.

## Z widgetu přišlo jen oznámení, ne dialog
Dialogy „zdroj neodpověděl“ a „Zkusit hledat pod jiným názvem?“ se ukážou jen po kliku ve výpisu Nokturna.
Z widgetu, karty Home Assistantu a TMDb Helperu by dialog blokoval i vypínání Kodi, proto tam přijde jen oznámení.
Když chceš hledat pod jiným názvem, otevři titul přímo v Nokturnu.

## „Jednu nebo více položek se nepodařilo přehrát“ po zavření výběru
Když výběr streamu zavřeš tlačítkem Zpět, Kodi to hlásí jako neúspěšné přehrání. Je to hláška Kodi, ne chyba.

---
[Všechny návody](../) · [Slovensky](../sk/prehrat-v-detailu)
