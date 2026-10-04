---
slug: instalace-kodi
lang: cs
title: Jak nainstalovat Nokturno do Kodi
products: [kodi]
priority: 1
---

# Jak nainstalovat Nokturno do Kodi

Nokturno běží na Kodi 20 a novějším (Android TV, Google TV, CoreELEC, Windows, Linux, macOS).
Instaluj ho přes **repozitář** – jen tak budou chodit aktualizace samy.

## 1. Povolit neznámé zdroje
V Kodi otevři **Nastavení → Systém → Doplňky** a zapni **Neznámé zdroje**.

## 2. Přidat zdroj
**Nastavení → Správce souborů → Přidat zdroj**. Jako adresu zadej

```
https://nokturno.stream/repo/
```

a pojmenuj ho `Nokturno`.

## 3. Nainstalovat repozitář
**Doplňky → Instalovat ze souboru ZIP → Nokturno → repository.nokturno → repository.nokturno.zip**.

## 4. Nainstalovat doplněk
**Doplňky → Instalovat z repozitáře → Nokturno repozitář → Video doplňky → Nokturno → Instalovat**.

## 5. První spuštění
Doplněk se zeptá na souhlas s podmínkami použití (**Souhlasím**) a nabídne průvodce nastavením:
vlastní úložiště a případné účty můžeš vyplnit **z mobilu přes QR kód**, projít krátkého průvodce ovladačem,
nebo to přeskočit. Průvodce se jako první ptá na vlastní úložiště.
Průvodce kdykoli spustíš znovu v **Nastavení → Pokročilé → Průvodce nastavením**.

K přehrávání potřebuješ hlavně [vlastní úložiště](vlastni-uloziste.md). Zdroje třetích stran (například WebShare
s VIP) jsou volitelné a u nové instalace jsou všechny vypnuté.

## Když něco nejde
- **Kodi hlásí, že nemůže nainstalovat doplněk z neznámého zdroje:** vrať se ke kroku 1.
- **Ve Správci souborů máš adresu `nokturno.tailf0014.ts.net`:** ta od září 2026 nefunguje. Zdroj smaž
  a přidej `https://nokturno.stream/repo/`.
- **Doplněk máš ze zipu bez repozitáře:** aktualizace chodit nebudou. Nainstaluj repozitář podle kroků 2 a 3,
  nastavení zůstane.

Podrobný návod včetně beta verzí je v návodu: [Instalace](../navody/kodi/instalace.md).

---
[Všechny návody](../) · [Slovensky](../sk/instalace-kodi)
