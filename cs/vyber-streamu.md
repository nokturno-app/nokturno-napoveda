---
slug: vyber-streamu
lang: cs
title: "Výběr streamu: filtry, 3D a poslední filtr"
products: [kodi]
priority: 3
templates:
  kodi: |
    Ahoj, 3D verze jde schovat.
    1. Nokturno → Nastavení → Přehrávání: zapni Skrýt 3D streamy. 3D soubory se pak nezobrazí nikdy, ani když jiný stream není.
    2. Chceš mít výběr rovnou s filtrem (třeba jen CZ zvuk)? V Nastavení → Výběr streamu zapni Automaticky použít poslední filtr.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/vyber-streamu
    Tým Nokturno
---

# Výběr streamu: filtry, 3D a poslední filtr

Po kliknutí na film nebo díl (i po **Přehrát** v detailu) se otevře dialog **Vyber stream**. Kdykoli ho vyvoláš
i z kontextového menu filmu nebo dílu: **Vybrat stream**. **Vybrat stream** vždy hledá znovu a nebere výsledek uložený
z dřívějška, takže uvidíš aktuální nabídku. Když u titulu žádný zdroj nic nenašel, běžné otevření ho 20 minut znovu neprohledává;
**Vybrat stream** z kontextového menu hledá hned.

## Co je v dialogu
- Každý stream má dva řádky, vlevo obrázek kvality. Co a v jakém pořadí se ukazuje, jde nastavit (níž).
- Jazyk s vlnovkou (`~CZ`) je jen odhad z názvu souboru. Bez vlnovky ho potvrdil zdroj nebo hlavička souboru.
- `×3` za streamem znamená tři stejné verze souboru sloučené do jednoho řádku. Když jedna nejde přehrát, zkusí se další.
- Nahoře je **Filtr streamů** s počtem streamů, **Zrušit filtr** a **Použít poslední filtr**.
- Dole je **Zobrazit všechny streamy** (rozbalí sloučené verze) a u některých titulů **Hledat volněji podle názvu souboru**.

## Filtr streamů
**Filtr streamů** nabídne jen to, co se u titulu opravdu našlo: **Kvalita**, **Zvuk**, **Kanály**, **Kodek**,
**Titulky** a **Zdroj**.
- V jedné skupině stačí kterákoli vybraná hodnota: Zvuk CZ a Zvuk SK = český nebo slovenský zvuk.
- Mezi skupinami musí platit všechno: Zvuk CZ a Kvalita 1080p = jen český zvuk v 1080p.
- Zvuk, kanály a kodek se hledají na stejné zvukové stopě: Zvuk CZ a Kanály 5.1 = česká stopa v 5.1.

Nokturno si poslední filtr pamatuje (v každém Kodi zvlášť). **Použít poslední filtr** ho vrátí jedním klikem,
v závorce je počet streamů, které nechá.

| Hláška | Co znamená |
|---|---|
| „Filtr nic nenechal, zobrazeny všechny streamy“ | takový stream u titulu není, ukazuje se celý seznam |
| „Není podle čeho filtrovat“ | streamy o sobě nic nevědí (kvalitu, zvuk ani zdroj) |

## Nastavení
**Nokturno → Nastavení → Přehrávání:**

| Volba | Co dělá |
|---|---|
| **Preferovaný jazyk zvuku** | streamy s tímto jazykem jsou nahoře; nic se neskrývá |
| **Preferovat prostorový zvuk (5.1 a víc)** | při stejné kvalitě jde nahoru stream s 5.1 a víc |
| **Skrýt SD streamy** | streamy pod 720p se vyřadí. Když by nezbyl žádný, zobrazí se všechny |
| **Skrýt 3D streamy** | 3D soubory se nezobrazí nikdy, ani když jiný stream není |
| **Skrýt Dolby Vision bez záložní vrstvy (profil 5)** | streamy, které televize bez Dolby Vision ukáže zeleně a fialově. Poznáme je z hlavičky souboru, u ostatních jen podle označení P5 v názvu |
| **Skrýt Dolby Vision streamy** | soubory Dolby Vision se nezobrazí nikdy, ani když jiný stream není. Pro televize a přehrávače, které Dolby Vision neumí (fialový nebo zelený obraz) |
| **Skrýt HDR streamy** | soubory HDR včetně Dolby Vision se nezobrazí nikdy. Pro televize, kde je HDR obraz tmavý nebo vybledlý |
| **Skrýt AV1** | streamy s kodekem AV1, pro přehrávače, které ho neumí (starší Shield, Apple TV) |
| **Max. datový tok (Mb/s, 0 = bez omezení)** | streamy s vyšším tokem se vyřadí. Když se nevejde žádný, zůstane nejmenší soubor. Hodnotu nastaví i **Změřit rychlost a nastavit datový tok** |
| **Řazení streamů** | **Jak přišly**, **Nejdřív nejlepší kvalita**, **Nejdřív největší**, **Nejdřív nejmenší** |

Stejné volby (Skrýt 3D, Skrýt Dolby Vision, Skrýt HDR) má i integrace pro Home Assistant a nastavení aplikace pro Stremio.

**Nokturno → Nastavení → Výběr streamu:**

| Volba | Co dělá |
|---|---|
| **Co a v jakém pořadí ukazovat u streamu** | údaje v horním a dolním řádku. Pohodlněji přes **Nastavit z mobilu**, kde se údaje přesouvají šipkami. **Výchozí pořadí** vrátí původní stav |
| **Automaticky použít poslední filtr** | dialog se otevře rovnou s posledním filtrem. Když by u titulu nenechal žádný stream, ukážou se všechny |

## 3D streamy
3D verze jsou na běžné televizi dva obrazy vedle sebe nebo nad sebou. Nokturno je pozná podle názvu souboru
(3D, H-SBS, Half-OU, MVC a podobně) nebo podle hlavičky souboru MKV. Se zapnutým **Skrýt 3D streamy**
se nezobrazí vůbec, ani mezi sloučenými verzemi.

Hlavička souboru se při otevření seznamu čte jen u několika streamů, zbytek se dočte na pozadí. 3D soubor bez značky
v názvu se proto může ukázat napoprvé a zmizí při dalším otevření.

## Formát obrazu
Dolby Vision, HDR a kodek AV1 poznáváme z hlavičky souboru, jinak podle názvu. Ve výpisu se u streamu ukáže štítek:
**DV only** (Dolby Vision bez záložní vrstvy), **DV**, **HDR10**, **HDR10+**, **HDR**, **HLG** nebo **3D**.
U Dolby Vision se záložní vrstvou se vedle **DV** ukáže i její formát (**HDR10** nebo **HLG**), poznáme ho z hlavičky souboru.
**HDR10+** se u takového souboru pozná z označení `UHDR+DV` nebo `HDR10+DV` v názvu.

Hlavička se čte jen u prvních streamů výpisu, zbytek se dočte na pozadí. U streamu bez přečtené hlavičky platí jen název
a **Skrýt Dolby Vision bez záložní vrstvy** tam chytí jen jasné označení profilu 5 (třeba `DV.P5`), nikdy holé „DV“. U souborů z vlastního úložiště na SMB se hlavička nečte vůbec, takže tam bývá štítků méně.

---
[Všechny návody](../) · [Slovensky](../sk/vyber-streamu)
