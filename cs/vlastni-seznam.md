---
slug: vlastni-seznam
lang: cs
title: Vlastní seznam
products: [kodi]
priority: 3
---

# Vlastní seznam

Vlastní seznam je soubor JSON na adrese, kterou zadáš v nastavení. Nokturno z něj udělá položku v hlavním menu
se složkami a videi a videa přehraje přes zdroje a účty, které máš v doplňku nastavené. Za obsah seznamu
odpovídáš ty.

## Nastavení v Kodi
1. **Nastavení → Zdroje a účty → Vlastní seznam** (další dva seznamy jsou ve skupinách **Vlastní seznam 2**
   a **Vlastní seznam 3**).
2. **Adresa seznamu (JSON)**: adresa souboru, musí začínat `http://` nebo `https://`.
3. **Hlavička požadavku 1** a **2**: nepovinné, ve tvaru `Název: hodnota`, třeba `X-Key: tajny-klic`. Pošlou se
   při každém načtení seznamu. Hodí se, když je soubor za přihlášením. Hodnota se v nastavení nezobrazuje.

Každý seznam s vyplněnou adresou je v hlavním menu vlastní položka. Jmenuje se podle `title` v souboru, dokud se
soubor jednou nenačte, tak **Vlastní seznam**, **Vlastní seznam 2** a **Vlastní seznam 3**.

## Tvar souboru

```json
{
  "version": 1,
  "title": "Moje videa",
  "thumb": "https://example.com/obrazek.jpg",
  "groups": [
    {
      "title": "Složka",
      "thumb": "https://example.com/slozka.jpg",
      "groups": [],
      "items": []
    }
  ],
  "items": [
    {
      "title": "Moje video",
      "year": 2024,
      "plot": "Krátký popis.",
      "thumb": "https://example.com/video.jpg",
      "duration": 5400,
      "refs": ["hs:123456:a1b2c3", "https://example.com/moje-video.mp4"]
    }
  ]
}
```

| Klíč | Kde | Co znamená |
|---|---|---|
| `version` | kořen | verze tvaru, piš `1` |
| `title` | kořen, složka, video | název; u kořene je to název položky v menu, složka i video bez názvu se vynechá |
| `thumb` | kořen, složka, video | obrázek, jen adresa `http://` nebo `https://` |
| `groups` | kořen, složka | složky; pod kořenem nejvýš 3 úrovně, hlubší se ignorují |
| `items` | kořen, složka | videa |
| `year` | video | rok (1800–2200), ukáže se v závorce za názvem |
| `plot` | video | popis, nejvýš 4000 znaků |
| `duration` | video | délka v sekundách |
| `refs` | video | odkazy na soubor, povinné; první, který jde přehrát, vyhrává |

Neznámé klíče se ignorují. Složka bez videí a bez podsložek se v menu nezobrazí, video bez platného odkazu taky.

## Odkazy v `refs`
Odkaz je vnitřní odkaz Nokturna ve tvaru `zdroj:údaje`. Přehraje se přes účet a nastavení doplňku, takže daný zdroj
musí být v Nokturnu zapnutý a u zdrojů s účtem i přihlášený. Když první odkaz nejde přehrát (smazaný soubor,
vypršelý účet), zkusí se další. Jedno video může mít nejvýš 10 odkazů.

| Tvar | Zdroj |
|---|---|
| `ws:<ident>` | WebShare |
| `hs:<id>:<hash>` | HellSpy |
| `fs:<id>:<server>[:<velikost v bajtech>]` | FastShare nebo Sdilej.cz, podle volby **Účet z**; server je `data`, `data1` apod. |
| `pt:<id>:<slug>:<hash>` | Přehraj.to |
| `st:<id videa>` | Sledujteto (přehrávání chce Premium) |
| `cz:m:<id>:<id streamu>`, `cz:e:<id>:<id streamu>` | CZtor, `m` film, `e` díl |
| `dav:<číslo úložiště>:<cesta>` | tvoje vlastní úložiště 1–3 z nastavení, cesta ve složce úložiště |
| `streamuj:<adresa>` | Sosáč (chce účet Streamuj) |
| `https://…` | přímá adresa souboru, přehraje se tak, jak je |

Odkaz má nejvýš 500 znaků a nesmí obsahovat mezeru. Hodnoty v tabulce jsou jen ukázka tvaru.

## Limity
- Soubor může mít nejvýš 8 MB. Musí být v UTF-8.
- Složek a videí dohromady nejvýš 20 000, další se ignorují.
- Názvy se zkrátí na 200 znaků.
- Serveru, na kterém soubor leží, se Nokturno ptá s hlavičkou `User-Agent: Nokturno` a čeká nejvýš 15 sekund.

## Kdy se seznam načte znovu
- Načtený seznam se drží hodinu. Změna v souboru se v menu ukáže nejpozději do hodiny.
- Když soubor nejde načíst (server neodpovídá, soubor není platný JSON), ukáže se hláška
  „Vlastní seznam nejde načíst.“ a pod ní poslední známý stav, pokud ho Nokturno má. Poslední známý stav vydrží
  14 dní.
- Seznamy se ukládají podle adresy. Dva seznamy se stejnou adresou jsou jeden a tentýž.

## Dobré vědět
- Vlastní seznam je jen v Kodi. Adresu i hlavičky jde vyplnit i přes **Nastavit z mobilu** a přenese je
  i přenos nastavení do dalšího Kodi.
- Soubor si můžeš dát na vlastní web, do svého úložiště nebo na jakoukoli adresu, na kterou Kodi dosáhne.

---
[Všechny návody](../) · [Slovensky](../sk/vlastni-seznam)
