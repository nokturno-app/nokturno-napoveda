---
slug: co-je-nokturno
lang: cs
title: Co je Nokturno a co umí
products: [kodi, ha, stremio]
priority: 1
---

# Co je Nokturno a co umí

Nokturno je přehrávač a vyhledávač pro Kodi a Home Assistant. Přehrává soubory z tvého vlastního úložiště
(WebDAV, NAS) i z úložišť a katalogů třetích stran, které si v nastavení zapneš (WebShare, Sosáč, HellSpy,
Sledujteto, FastShare / Sdilej.cz, Přehraj.to, CZtor, Luna), titulky hledá na OpenSubtitles. Doplní popisy
a pamatuje si, kde jsi skončil. Samo žádný obsah nehostuje ani nešíří a neověřuje, jestli je soubor na cizím
úložišti legální. Za to, co přehráváš, odpovídáš ty – používej ho jen k obsahu, ke kterému máš právo.

Plný text podmínek použití a kontakty pro nahlášení nelegálního obsahu u jednotlivých zdrojů:
[nokturno.stream/terms](https://nokturno.stream/terms).

## Kde Nokturno běží

| | Kodi | Stremio (a Nuvio, Streamlet) | Home Assistant |
|---|---|---|---|
| Co to je | doplněk do Kodi, má nejvíc funkcí | aplikace u tebe (PC, NAS, Android TV box), která přidává streamy ke Stremiu | integrace a karta na dashboard |
| Instalace | [Jak nainstalovat Nokturno do Kodi](instalace-kodi.md) | [Nokturno pro Stremio – aplikace](stremio-aplikace.md) | přes HACS, viz [Jak zjistit verzi a aktualizovat](aktualizace.md) |
| Vlastní úložiště | ano, až tři | ano | ano |
| Luna | ano | ne (Luna má pro Stremio vlastní doplněk) | ano |
| Pokračovat ve sledování, Můj seznam, Hlídané | ano | ne | ano |
| Vlastní katalogy | ano | ano | ověřuje katalogy z Kodi |
| Koncerty | ano | ano | ne |

## Co umí doplněk pro Kodi
- hledání a katalogy filmů a seriálů, žebříček „Nejsledovanější tento týden“, tipy „Pro Tebe“,
- [vlastní katalogy](vlastni-katalogy.md) ze šablon i podle žánrů, témat, země původu a let, s ověřením, že tituly jde
  přehrát v požadované kvalitě a jazyce,
- [koncerty](koncerty.md) z tvého vlastního úložiště, volitelně i z úložišť třetích stran, která máš povolená a nastavená, s interprety podle tvých oblíbených hudebních žánrů,
- [výběr streamu](vyber-streamu.md) v dialogu s odznaky kvality, filtr, řazení podle jazyka zvuku a volba Skrýt 3D streamy,
- Pokračovat ve sledování, Můj seznam a [Hlídané](hlidane.md): nový díl seriálu, film, který zatím nikde není,
  a Kontrolovat dál u titulu, který streamy má, ale ne takové, jaké chceš,
- FastShare i s [účtem ze Sdilej.cz](sdilej-cz.md), [Trakt.tv](trakt.md) s přihlášením kódem, i s bezplatným účtem (zhlédnuté oběma směry, Watchlist = Můj seznam),
- synchronizace mezi více Kodi a přenos nastavení do dalšího Kodi,
- Nastavit z mobilu přes QR kód, stahování, titulky z OpenSubtitles, TV program, SyncWatch (společné sledování).

Home Assistant umí taky Hlídané, Trakt.tv, účet ze Sdilej.cz a ověřování vlastních katalogů, doplněk pro Stremio účet ze Sdilej.cz, CZtor, vlastní katalogy a koncerty.

Co dělat, když něco nejde: [Kde hledat pomoc](kde-hledat-pomoc.md).

---
[Všechny návody](../) · [Slovensky](../sk/co-je-nokturno)
