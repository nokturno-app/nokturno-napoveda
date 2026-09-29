---
slug: vlastni-katalogy
lang: cs
title: Vlastní katalogy
products: [kodi, stremio]
priority: 3
---

# Vlastní katalogy

Vlastní katalog si poskládáš podle žánrů, původního jazyka, let a řazení. Tituly do něj skládá server Nokturna,
vlastní klíč TMDB k tomu nepotřebuješ.

## Jak založit katalog v Kodi
1. **Filmy** nebo **Seriály → Vlastní katalogy → Nový katalog**.
2. Postupně se ukážou tyto volby:

| Dialog | Co vybrat |
|---|---|
| **Žánry (nic = všechny)** | jeden nebo víc žánrů, na konci seznamu i **Pohádky**; bez výběru jsou všechny |
| **Tituly musí mít** | jen při dvou a víc žánrech: **všechny vybrané žánry**, nebo **aspoň jeden vybraný žánr** |
| **Původní jazyk** | Jakýkoli, Čeština, Slovenština, Čeština nebo slovenština, Angličtina, Němčina, Francouzština, Španělština, Italština, Polština, Maďarština, Korejština, Japonština |
| **Od roku**, **Do roku** | prázdné = bez omezení |
| **Řadit podle** | Oblíbenosti, Hodnocení, Data vydání |
| **Název katalogu** | předvyplněný z voleb (třeba „Rodinný · Fantasy · Čeština“), můžeš ho přepsat |

3. Katalog se objeví ve **Vlastních katalozích**. Kliknutím ho otevřeš.

## Úprava a smazání
Kontextové menu katalogu:
- **Upravit katalog** projde stejné dialogy, předvybrané jsou uložené volby.
- **Smazat katalog** se ještě zeptá, jestli opravdu.

## Výpis katalogu
- Na stránce je 20 titulů, na konci **Další strana »**. Stran je nejvýš 10.
- Řazení podle **Hodnocení** bere jen tituly, které mají dost hodnocení. Jinak by nahoře byly filmy s jediným hlasem.
- Výpis se obnovuje zhruba dvakrát denně.
- Katalog vybírá tituly, ne streamy. Streamy se k titulu hledají až po kliknutí, stejně jako jinde v Nokturnu.

## Tipy
| Chceš | Nastav |
|---|---|
| české a slovenské pohádky | Filmy: žánr **Pohádky**, původní jazyk **Čeština nebo slovenština** |
| české filmy | Filmy: žádný žánr, původní jazyk **Čeština** |
| české a slovenské seriály | Seriály: žádný žánr, původní jazyk **Čeština nebo slovenština** |
| nejlepší horory 80. let | Filmy: žánr **Horor**, od roku 1980 do roku 1989, řadit podle **Hodnocení** |

Seriály mají jiný seznam žánrů než filmy (třeba **Sci-fi a fantasy** nebo **Dětský**).

## Když se katalog nenačte
- „Katalog se nepodařilo načíst. Zkus to později.“ – server Nokturna zrovna neodpovídá. Zkus to za chvíli.
- Katalog je prázdný – podmínky nic nenechaly. Uber žánr, zvol **aspoň jeden vybraný žánr** nebo rozšiř roky.

## Ve Stremiu
Ve Stremiu se vlastní katalogy skládají ve formuláři nastavení doplňku (od verze 8.5.0).

1. Otevři nastavení doplňku: ve Stremiu **Doplňky → Nokturno → Konfigurovat**, nebo stránku `http://<IP zařízení s aplikací>:7140/configure`.
2. V kroku 2 najdi kartu **Vlastní katalogy** a dej **Přidat katalog**.
3. Vyplň **Název**, **Druh** (Filmy nebo Seriály), žánry (i **Pohádky**), případně **Stačí jeden z vybraných žánrů**,
   **Původní jazyk**, **Od roku**, **Do roku** a **Řadit podle**. Prázdný název se doplní z voleb.
4. Dole dej **Přidat do Stremia** (nebo **Přidat do Nuvia**).

- Katalogů může být nejvýš 5. Ukážou se na domovské stránce Stremia hned za katalogy Nokturna.
- **Po každé změně katalogu přidej doplněk znovu.** Nastavení je uložené v adrese doplňku, takže změna znamená novou adresu.
- Při rolování se načítá po 100 titulech, jeden katalog má nejvýš kolem 200 titulů.
- Tip na české pohádky: Filmy, žánr **Pohádky**, původní jazyk **Čeština nebo slovenština**.

## Dobré vědět
- V Kodi jsou vlastní katalogy uložené jen v tom jednom zařízení. Mezi zařízeními se nesynchronizují a nepřenáší je ani přenos
  nastavení.
- Ve Stremiu jsou katalogy uložené v adrese doplňku, takže platí všude, kde je doplněk přidaný touto adresou.
- V Home Assistantu vlastní katalogy nejsou.

---
[Všechny návody](../) · [Slovensky](../sk/vlastni-katalogy)
