---
slug: poslat-log
lang: cs
title: Jak poslat log a zjistit ID instalace
products: [kodi]
priority: 1
templates:
  kodi: |
    Ahoj, díky za log. Podíváme se na něj a odpověď ti pošleme sem do Kodi.
    Tým Nokturno
---

# Jak poslat log a zjistit ID instalace

Log je záznam toho, co Kodi a Nokturno dělaly. Podle něj většinou hned poznáme, kde je problém.
Týká se doplňku pro Kodi.

## Poslat log
1. Zopakuj to, co nefunguje (ať je chyba v logu čerstvá).
2. Otevři **Nokturno → Nastavení → Pokročilé** a klikni na **Odeslat log Kodi**.
3. Potvrď „Opravdu odeslat log?“. Objeví se „Log odeslán“.

Když ověření Luny skončí chybou, nabídne tlačítko **Poslat log** rovnou v okně.

Co se posílá: posledních zhruba 500 kB souboru `kodi.log`. Hesla, tokeny, e-maily a IP adresy doplněk
před odesláním vymaže. Log jde poslat i s vypnutými statistikami.

## Zjistit ID instalace
**Nokturno → Nastavení → Pokročilé**, ve skupině **Když něco nefunguje** klikni na **Verze a ID této instalace**.
ID je náhodný kód, který nic neprozradí o tobě ani o zařízení. Podle něj ale najdeme tvůj log a můžeme
ti poslat odpověď přímo do Kodi.

## Co dál
Napiš nám na [Discord](https://discord.gg/ChmMPmDDEj) do fóra #pomoc nebo na fórum,
co nefunguje, kdy byl log odeslaný a ID instalace. Viz [Kde hledat pomoc](kde-hledat-pomoc.md).

Odpověď přijde do Kodi jako okno se zprávou. Ukáže se, až se doplněk příště spojí se serverem Nokturna
(nejpozději do několika hodin) a když zrovna nic nepřehráváš.

Zprávy dostanou jen verze 7.9.3 a novější. Starší verze neznají novou adresu serveru, nejdřív
[aktualizuj](aktualizace.md).

---
[Všechny návody](../) · [Slovensky](../sk/poslat-log)
