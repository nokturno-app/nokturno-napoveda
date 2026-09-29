---
slug: vlastni-seznam
lang: sk
title: Vlastný zoznam
products: [kodi]
priority: 3
---

# Vlastný zoznam

Vlastný zoznam je súbor JSON na adrese, ktorú zadáš v nastaveniach. Nokturno z neho urobí položku v hlavnom menu
s priečinkami a videami a videá prehrá cez zdroje a účty, ktoré máš v doplnku nastavené. Za obsah zoznamu
zodpovedáš ty.

## Nastavenie v Kodi
1. **Nastavenia → Zdroje a účty → Vlastný zoznam** (ďalšie dva zoznamy sú v skupinách **Vlastný zoznam 2**
   a **Vlastný zoznam 3**).
2. **Adresa zoznamu (JSON)**: adresa súboru, musí začínať `http://` alebo `https://`.
3. **Hlavička požiadavky 1** a **2**: nepovinné, v tvare `Názov: hodnota`, napríklad `X-Key: tajny-kluc`. Pošlú sa
   pri každom načítaní zoznamu. Hodí sa, keď je súbor za prihlásením. Hodnota sa v nastaveniach nezobrazuje.

Každý zoznam s vyplnenou adresou je v hlavnom menu samostatná položka. Volá sa podľa `title` v súbore, kým sa súbor
raz nenačíta, tak **Vlastný zoznam**, **Vlastný zoznam 2** a **Vlastný zoznam 3**.

## Tvar súboru

```json
{
  "version": 1,
  "title": "Moje videá",
  "thumb": "https://example.com/obrazok.jpg",
  "groups": [
    {
      "title": "Priečinok",
      "thumb": "https://example.com/priecinok.jpg",
      "groups": [],
      "items": []
    }
  ],
  "items": [
    {
      "title": "Moje video",
      "year": 2024,
      "plot": "Krátky popis.",
      "thumb": "https://example.com/video.jpg",
      "duration": 5400,
      "refs": ["hs:123456:a1b2c3", "https://example.com/moje-video.mp4"]
    }
  ]
}
```

| Kľúč | Kde | Čo znamená |
|---|---|---|
| `version` | koreň | verzia tvaru, píš `1` |
| `title` | koreň, priečinok, video | názov; pri koreni je to názov položky v menu, priečinok aj video bez názvu sa vynechá |
| `thumb` | koreň, priečinok, video | obrázok, len adresa `http://` alebo `https://` |
| `groups` | koreň, priečinok | priečinky; pod koreňom najviac 3 úrovne, hlbšie sa ignorujú |
| `items` | koreň, priečinok | videá |
| `year` | video | rok (1800–2200), zobrazí sa v zátvorke za názvom |
| `plot` | video | popis, najviac 4000 znakov |
| `duration` | video | dĺžka v sekundách |
| `refs` | video | odkazy na súbor, povinné; vyhráva prvý, ktorý ide prehrať |

Neznáme kľúče sa ignorujú. Priečinok bez videí a bez podpriečinkov sa v menu nezobrazí, video bez platného odkazu tiež.

## Odkazy v `refs`
Odkaz je vnútorný odkaz Nokturna v tvare `zdroj:údaje`. Prehrá sa cez účet a nastavenia doplnku, takže daný zdroj
musí byť v Nokturne zapnutý a pri zdrojoch s účtom aj prihlásený. Keď prvý odkaz nejde prehrať (zmazaný súbor,
vypršaný účet), skúsi sa ďalší. Jedno video môže mať najviac 10 odkazov.

| Tvar | Zdroj |
|---|---|
| `ws:<ident>` | WebShare |
| `hs:<id>:<hash>` | HellSpy |
| `fs:<id>:<server>[:<veľkosť v bajtoch>]` | FastShare alebo Sdilej.cz, podľa voľby **Účet z**; server je `data`, `data1` a pod. |
| `pt:<id>:<slug>:<hash>` | Přehraj.to |
| `st:<id videa>` | Sledujteto (prehrávanie chce Premium) |
| `cz:m:<id>:<id streamu>`, `cz:e:<id>:<id streamu>` | CZtor, `m` film, `e` diel |
| `dav:<číslo úložiska>:<cesta>` | tvoje vlastné úložisko 1–3 z nastavení, cesta v priečinku úložiska |
| `streamuj:<adresa>` | Sosáč (chce účet Streamuj) |
| `https://…` | priama adresa súboru, prehrá sa tak, ako je |

Odkaz má najviac 500 znakov a nesmie obsahovať medzeru. Hodnoty v tabuľke sú len ukážka tvaru.

## Limity
- Súbor môže mať najviac 8 MB. Musí byť v UTF-8.
- Priečinkov a videí dokopy najviac 20 000, ďalšie sa ignorujú.
- Názvy sa skrátia na 200 znakov.
- Servera, na ktorom súbor leží, sa Nokturno pýta s hlavičkou `User-Agent: Nokturno` a čaká najviac 15 sekúnd.

## Kedy sa zoznam načíta znova
- Načítaný zoznam sa drží hodinu. Zmena v súbore sa v menu ukáže najneskôr do hodiny.
- Keď súbor nejde načítať (server neodpovedá, súbor nie je platný JSON), zobrazí sa hlásenie
  „Vlastný zoznam sa nedá načítať.“ a pod ním posledný známy stav, ak ho Nokturno má. Posledný známy stav vydrží
  14 dní.
- Zoznamy sa ukladajú podľa adresy. Dva zoznamy s rovnakou adresou sú jeden a ten istý.

## Dobré vedieť
- Vlastný zoznam je len v Kodi. Adresu aj hlavičky ide vyplniť aj cez **Nastaviť z mobilu** a prenesie ich
  aj prenos nastavení do ďalšieho Kodi.
- Súbor si môžeš dať na vlastný web, do svojho úložiska alebo na akúkoľvek adresu, na ktorú Kodi dosiahne.

---
[Všetky návody](./) · [Česky](../cs/vlastni-seznam)
