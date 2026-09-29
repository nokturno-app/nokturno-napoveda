---
slug: stav-zdroju
lang: cs
title: "Nahoře v menu je řádek se zdrojem („Stav zdrojů“)"
products: [kodi, ha]
priority: 1
---

# Nahoře v menu je řádek se zdrojem („Stav zdrojů“)

## Co to znamená
Když některý zapnutý zdroj potřebuje zásah, ukáže se **úplně nahoře v hlavním menu** Nokturna řádek se jménem
zdroje a krátkým popisem, například „Luna: server neodpovídá“ nebo „WebShare: zbývá dní: 3“. Když je potíží víc,
za textem je „+1“, „+2“…

Když je všechno v pořádku, řádek v menu vůbec není.

## Co udělat
1. Klikni na řádek. Otevře se výpis **Stav zdrojů**, každý zdroj má vlastní řádek s plným popisem.
2. Klikni na řádek zdroje. Vede rovnou tam, kde se to opravuje: u Luny na **Ověřit nastavení Luny**,
   u CZtoru na **Spárovat PINem**, u předplatného WebShare na **Stav předplatného WebShare**, jinak do nastavení.
3. Pod zdroji je **Ověřit zdroje** (ve starších verzích **Otestovat zdroje**). Zkusí všechny zdroje znovu a stav přepíše.

Zdroj, se kterým teď nic udělat nejde (třeba výpadek na jeho straně), můžeš **uspat**: podrž OK nebo klikni
pravým tlačítkem na jeho řádek a zvol **Uspat zdroj** (10 minut, 1 hodina, 12 hodin). Po tu dobu se v něm nehledá.

## Co jednotlivé stavy znamenají
| Ve výpisu | Co to znamená | Návod |
|---|---|---|
| neodpovídá | zdroj nebo server není dosažitelný | [„<Zdroj> neodpovídá“](zdroj-neodpovida.md) |
| nesedí jméno nebo heslo | zdroj odmítl přihlášení | [Zdroj hlásí „nesedí jméno nebo heslo“](prihlaseni.md) |
| předplatné vypršelo, do konce předplatného zbývá dní: N | WebShare, CZtor nebo Přehraj.to | [Premium, VIP a kredit](premium-a-kredit.md) |
| účet bez VIP – stahování pár kB/s | WebShare bez VIP | [Premium, VIP a kredit](premium-a-kredit.md) |
| účet bez Premium – přehrávání nepůjde | Sledujteto bez Premium | [Premium, VIP a kredit](premium-a-kredit.md) |
| došel kredit | FastShare / Sdilej.cz | [Premium, VIP a kredit](premium-a-kredit.md) |
| zařízení není spárované | CZtor | klikni na řádek a spáruj PINem, viz [CZtor](cztor.md) |
| odmítá tuto síť (HTTP 429) – VPN nebo mobilní data? | HellSpy odmítá tvoji síť, typicky VPN nebo mobilní data | [„Odmítá tuto síť (HTTP 429)“](sit-odmitnuta-429.md) |
| server neodpovídá, běží, ale chybí token… | Luna | [Co znamenají hlášky Luny](luna-hlasky.md) |
| Úložiště: neodpovídá | vlastní úložiště | [Jak připojit vlastní úložiště](vlastni-uloziste.md) |

## Stav se po opravě nezměnil
Stav se obnovuje na pozadí po několika hodinách. Hned ho přepíše **Ověřit zdroje** ve výpisu
nebo v **Nastavení → Pokročilé**.

Na telefonu nebo tabletu s Androidem nemá Kodi na pozadí přístup k síti. Stav pak může chvíli ukazovat
„neodpovídá“, i když zdroj funguje. Po otevření menu se sám obnoví.

## Home Assistant
Stejný přehled ukazuje senzor **Stav zdrojů**: hodnota je počet zdrojů, které potřebují zásah
(0 = vše v pořádku), podrobnosti jsou v jeho atributech.

---
[Všechny návody](../) · [Slovensky](../sk/stav-zdroju)
