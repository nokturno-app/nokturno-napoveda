---
slug: stremio-instalace
lang: cs
title: Jak přidat Nokturno do Stremia nebo Nuvia
products: [stremio]
priority: 1
templates:
  stremio: |
    Nokturno pro Stremio je aplikace, kterou si pustíš u sebe: github.com/nokturno-app/nokturno-stremio-app/releases
    Pak otevři http://<IP zařízení s aplikací>:7140/configure, vyplň úložiště nebo účty, dej Ověřit a Přidat do Stremia.
    Na TV se doplněk objeví sám, když ho přidáš na telefonu pod stejným účtem Stremio.
---

# Jak přidat Nokturno do Stremia nebo Nuvia

!!! danger "Doplněk na cizím serveru dostává tvoje přihlašovací údaje"
    Každý doplněk pro Stremio, který běží na cizím serveru, dostává tvoje přihlašovací údaje ke zdrojům
    (WebShare, FastShare, Přehraj.to…). Jsou v adrese doplňku, provozovatel serveru je proto může vidět
    a uložit a musíš mu věřit. Jistotu máš jen s doplňkem, který běží u tebe: doma, přes VPN nebo na vlastním VPS.

Doplněk pro Stremio běží v aplikaci **Nokturno pro Stremio** u tebe doma. Jak ji stáhnout a spustit, je v článku
[Nokturno pro Stremio – aplikace](stremio-aplikace.md). Tvoje nastavení je zakódované v adrese doplňku,
kterou si vyrobíš na stránce nastavení v aplikaci.

## 1. Vyplň nastavení
Otevři v prohlížeči `http://<IP adresa zařízení s aplikací>:7140/configure` (na tomtéž zařízení
`http://127.0.0.1:7140/configure`):
1. **Vlastní úložiště a zdroje** – vlastní úložiště a volitelně účty zdrojů. U každého dej **Ověřit účet**
   (u úložiště **Ověřit úložiště**).
2. **Předvolby** – jazyk zvuku, řazení, katalogy. Tento krok se dá přeskočit.
3. Potvrď souhlas s podmínkami použití.

## 2. Přidej doplněk
| Kde | Jak |
|---|---|
| **Počítač** | **Přidat do Stremia**, prohlížeč se zeptá, jestli otevřít Stremio, potvrď. Ve Stremiu **Instalovat**. |
| **Telefon** | Otevři stránku v telefonu se Stremiem, **Přidat do Stremia** a **Instalovat**. Když se Stremio neotevře, použij **Zkopírovat adresu**. |
| **Televize** | Přidej doplněk na telefonu nebo počítači **pod stejným účtem Stremio**. Na TV se objeví do minuty. Ručně: Stremio → Doplňky → pole nahoře → vložit adresu → Instalovat. |
| **Nuvio** | **Přidat do Nuvia**. Na TV: **Zkopírovat adresu**, pak v Nuviu Nastavení → Doplňky → vložit adresu → Instalovat. |
| **Streamlet** | **Zkopírovat adresu**, ve Streamletu přidej doplněk Stremia a adresu vlož. |

Když stránku otevřeš přes IP adresu, dostane doplněk adresu `https://…my.local-ip.co:7141`. Tu Stremio přijme
i z jiného zařízení v síti, viz [Nokturno pro Stremio – aplikace](stremio-aplikace.md).
Doplněk funguje jen ve chvíli, kdy aplikace běží.

Adresa doplňku obsahuje tvoje účty. Nikomu ji neposílej.

## Změna nastavení
Ve Stremiu **Doplňky → Nokturno → ozubené kolo**. Otevře se stránka s tvým nastavením. Uprav ho a znovu dej
**Přidat do Stremia**. Změněné nastavení je nová adresa: starý doplněk ve Stremiu odinstaluj, jinak tam
Nokturno bude dvakrát.

## Nokturno mám ve Stremiu dvakrát
Je to starý a nový doplněk s jiným nastavením. Ve Stremiu **Doplňky** odinstaluj ten, který nechceš.

---
[Všechny návody](../) · [Slovensky](../sk/stremio-instalace)
