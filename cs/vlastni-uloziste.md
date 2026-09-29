---
slug: vlastni-uloziste
lang: cs
title: Jak připojit vlastní úložiště
products: [kodi, stremio]
priority: 1
when: {storage: [unreachable, bad_login]}
templates:
  kodi: |
    Ahoj, Nokturno se nemůže spojit s tvým vlastním úložištěm.
    1. Nokturno → Nastavení → Vlastní úložiště: zkontroluj Adresu složky, uživatelské jméno a heslo.
    2. Adresa v domácí síti (například 192.168.…) funguje jen doma. Mimo domov je potřeba veřejná adresa nebo VPN.
    3. Úložiště, které nepoužíváš, vypni volbou Používat toto úložiště. Zůstane vyplněné, jen se v něm nebude hledat.
    4. Pak dej Nastavení → Pokročilé → Ověřit zdroje (ve starších verzích Otestovat zdroje).
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/vlastni-uloziste
    Tým Nokturno
---

# Jak připojit vlastní úložiště

Vlastní úložiště je hlavní funkce Nokturna: přehrává **tvoje vlastní soubory** z NAS, Nextcloudu nebo jiného serveru
s WebDAV. Soubor, který k titulu patří, se ukáže **mezi streamy jako první** a pustí se stejně jako ostatní.
Nastavit jde až **tři úložiště**.

Stejná úložiště umí i [integrace pro Home Assistant](../navody/ha/nastaveni.md#vlastni-uloziste)
a [Nokturno pro Stremio](../navody/stremio/zdroje-a-nastaveni.md#vlastni-uloziste).

## Co je potřeba
- Složka dostupná přes **WebDAV** (`http://` nebo `https://`, tvar `davs://` z Kodi jde taky). Umí to Synology a QNAP
  (balíček WebDAV Server), Nextcloud, ownCloud i obyčejný Apache nebo nginx. Stačí i server, který umí jen **výpis
  složky** v HTML.
- Jméno a heslo, pokud je úložiště chráněné (HTTP Basic). Bez hesla nech pole prázdná.
- Úložiště musí být **dosažitelné ze zařízení, na kterém přehráváš**. Adresa v domácí síti funguje jen doma,
  mimo domov je potřeba veřejná adresa nebo VPN.

Do úložiště se nic nezapisuje a nic se v něm nevytváří – žádné `.nfo`, `.strm` ani XML. Nokturno soubory jen čte.

## Kodi
![Kategorie Vlastní úložiště v nastavení](../navody/kodi/images/kodi-nastaveni.jpg)

**Nokturno → Nastavení → Vlastní úložiště**, pro každé ze tří úložišť:

| Pole | K čemu | Příklad |
|---|---|---|
| **Používat toto úložiště** (dřív **Použít toto úložiště**) | vypnuté úložiště zůstane vyplněné, jen se v něm nehledá a v menu se neukáže | |
| **Adresa složky** | WebDAV složka s filmy a seriály, prázdné = úložiště vypnuté | `https://nas.example.cz:5006/video/` · `https://cloud.example.cz/remote.php/dav/files/jmeno/Video/` |
| **Uživatelské jméno**, **Heslo** | přihlášení k úložišti | |
| **Název** | ukáže se u streamů, ať je jasné, odkud soubor je; prázdné = jméno serveru | `NAS` |

Pak dej **Nastavení → Pokročilé → Ověřit zdroje** (ve starších verzích **Otestovat zdroje**). U každého úložiště
ukáže, jestli se přihlášení povedlo, nebo `NAS neodpovídá` / `NAS: špatné jméno nebo heslo`.

## Stremio
V nastavení doplňku (ve Stremiu **Doplňky → Nokturno → ozubené kolo**, nebo `http://<IP zařízení s aplikací>:7140/configure`) vyplň kartu
**Vlastní úložiště** a dej **Ověřit úložiště**. Pak doplněk přidej znovu tlačítkem **Přidat do Stremia**.

Ve Stremiu platí dvě věci navíc:
- Úložiště musí být dosažitelné **ze zařízení, kde běží aplikace Nokturno** (ta v něm hledá soubory), **i ze zařízení**,
  kde přehráváš. Když je obojí doma, stačí adresa z domácí sítě.
- Soubor z úložiště se **nepřehraje ve webovém Stremiu** v prohlížeči, jen v aplikaci (Stremio pro počítač,
  Android a Android TV, nebo Nuvio). U takového streamu je upozornění „⚠️ Ve webovém přehrávači se nepřehraje – jen v aplikaci“.

## Jak pojmenovat soubory
Nokturno soubor k titulu přiřazuje **podle názvu souboru a podle složek nad ním** – stejně přísně jako fulltext
WebShare, aby se k titulu nepřimíchal jiný. Na struktuře složek jinak nezáleží, prochází se celé úložiště.

### Filmy
```
Filmy/Pelíšky (1999).mkv
Filmy/National Lampoon's Vacation (1983)/Bláznivá dovolená (1983) 2160p CZ SK.mkv
```

- **Název na začátku**, za ním **rok** v závorce. Rok odliší stejnojmenné filmy a pokračování („Bláznivá dovolená“ 1983 × „Bláznivá dovolená v Evropě“ 1985).
- **Složka s originálním názvem** se vyplatí u filmů, které mají český název úplně jiný než originál. Kodi s TMDB zná film česky, Stremio a Cinemeta jen anglicky – se složkou `National Lampoon's Vacation (1983)` a souborem `Bláznivá dovolená (1983)…` se najde oběma cestami.
- **Kvalita a jazyky v názvu** (`2160p`, `1080p`, `CZ`, `SK`, `titulky`) pomůžou řazení a filtru streamů. Zvukové stopy si Nokturno stejně dočte z hlavičky souboru (MKV, MP4, AVI).

### Seriály
```
Seriály/Okresní přebor/Okresní přebor S01E02 - Nábor.mkv
Seriály/Hospoda/Hospoda S02E04 - Úraz.avi
```

- **Značka dílu `S01E02` je nutná** (jde i `1x02`). Bez ní Nokturno nepozná, o který díl jde – soubory pojmenované jen `1. Závěť.avi` se nenabídnou.
- Název seriálu může být v názvu souboru, nebo jen ve složce nad ním (`Seriály/Sherlock/Season 1/S01E02.mkv` taky projde).
- Číslo série a dílu musí sedět na katalog (TMDB). Když má seriál v katalogu dvě série po 26 dílech, je 27. díl `S02E01`.

Podporované přípony: `mkv mp4 avi m4v mov ts m2ts wmv webm mpg mpeg flv iso`. Soubory a složky začínající tečkou
a systémové složky NAS (`@eaDir`, `#recycle`) se přeskakují.

## Kde se soubory objeví
- **U titulu mezi streamy** – vždy **první**, na začátku řádku zelený název úložiště, za ním kvalita, zvuk, velikost a délka. Pouští se rovnou z úložiště.
- **Moje úložiště** v hlavním menu Kodi – procházení úložiště po složkách; u složky je počet videí uvnitř. Při víc úložištích se napřed vybírá úložiště.
- Ve **výsledcích hledání** se soubory neukazují – hledání je o titulech, soubor přijde na řadu až u titulu.

![Moje úložiště: filmy ve složkách Název (rok)](../navody/kodi/images/kodi-uloziste.jpg)

## Kdy doplněk uvidí nový soubor
Seznam souborů si Nokturno pamatuje **hodinu**, takže nově nahraný soubor se ukáže nejpozději do hodiny. Chceš-li to
rychleji, ulož do kořene složky soubor `.nokturno-rev` a po každé změně v úložišti změň jeho obsah (třeba na aktuální
čas). Jakmile se obsah změní, Nokturno seznam načte znovu hned.

## Hlášky a řešení problémů
| Kde nebo co | Hláška | Co udělat |
|---|---|---|
| nahoře v menu, Ověřit zdroje | „Úložiště: neodpovídá“, „<název> neodpovídá“ | adresa není ze zařízení dosažitelná: jiná síť, vypnutý server, nevystavený port. Zkus adresu otevřít v prohlížeči ve stejné síti. |
| nahoře v menu | „Úložiště: nesedí jméno nebo heslo“ | přihlašovací údaje k úložišti, ne k Nokturnu |
| při hledání | „<název>: špatné jméno nebo heslo“, „<název>: složka neexistuje“ | oprav jméno, heslo nebo cestu ke složce |
| soubor se u titulu nenabídne | – | zkontroluj [pojmenování](#jak-pojmenovat-soubory); nový soubor se ukáže nejpozději do hodiny |
| díly seriálu se nenabídnou, film ano | – | soubory nemají značku dílu, nebo nesedí číslování sérií s katalogem |
| stream se nabídne, ale nepřehraje | – | úložiště vrací soubor pomalu nebo přeruší přenos; zkus soubor stáhnout prohlížečem. U 4K přes internet rozhoduje hlavně rychlost linky. |

---
[Všechny návody](../) · [Slovensky](../sk/vlastni-uloziste)
