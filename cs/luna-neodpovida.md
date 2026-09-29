---
slug: luna-neodpovida
lang: cs
title: "Luna: „server neodpovídá“"
products: [kodi]
priority: 0
when: {luna: [unreachable, not_luna, bad_url, no_url]}
templates:
  kodi: |
    Ahoj, Nokturno se nemůže spojit se serverem Luna, proto se z ní nic nenačte.
    1. Lunu nepoužíváš? Nokturno → Nastavení → Zdroje a účty, ve skupině Luna vypni Používat Lunu. Ostatní zdroje fungují dál.
    2. Používáš ji? Zařízení, kde Luna běží, musí být zapnuté a ve stejné síti jako Kodi. Home Assistant není potřeba: Luna běží i přímo na Android TV boxu (adresa http://127.0.0.1:7126), na počítači nebo na NAS. Potřebuje WebShare VIP.
    3. Ve skupině Luna klikni na Najít Lunu v síti a pak na Ověřit nastavení Luny. Ověření napíše, co přesně nesedí.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/luna-neodpovida
    Tým Nokturno
---

# Luna: „server neodpovídá“

## Co to znamená
Nokturno se nedostalo na adresu, kterou má u Luny vyplněnou. Hláška se ukazuje na několika místech:

- nahoře v hlavním menu: „Luna: server neodpovídá“,
- po kliknutí na **Ověřit nastavení Luny**: „Na adrese … se nikdo neozval.“ nebo „Na adrese … něco odpovídá, ale není to Luna.“,
- po kliknutí na **Najít Lunu v síti**: „V této síti se Luna nenašla.“,
- při hledání: „Luna neodpovídá“.

Ostatní zdroje na Luně nezávisí a fungují dál.

## Proč se to stává
Od nejčastějšího:

1. **Lunu nemáš a nikdy nebyla nastavená.** Ve verzích do 8.2 je přepínač Luny zapnutý a adresa předvyplněná
   i u lidí, kteří Lunu nikdy neměli. Je to nejčastější důvod hlášky.
2. **Zařízení s Lunou je vypnuté** nebo je v jiné síti (síť pro hosty, VPN, jiná Wi-Fi).
3. **Adresa ukazuje jinam**: na jiné zařízení, nebo je v ní jiný port než 7126.
4. **Luna na tvé televizi běžet nemůže.** Například na televizi LG (webOS) nebo Samsung (Tizen) musí Luna běžet
   na jiném zařízení v síti.

## Co udělat
Cesta v Kodi: **Nokturno → Nastavení → Zdroje a účty**, skupina **Luna**.

1. **Lunu nepoužíváš?** Vypni **Používat Lunu** a dej OK. Hláška zmizí, všechno ostatní jede dál.
2. **Používáš ji?** Zkontroluj, že zařízení s Lunou je zapnuté a že je ve stejné síti jako Kodi.
   Home Assistant potřeba není. Luna běží:
   - přímo na Android TV boxu s Kodi, adresa je pak `http://127.0.0.1:7126`,
   - na počítači s Windows, Linuxem nebo macOS, na NAS nebo Raspberry Pi,
   - nebo jako doplněk Home Assistantu.

   Vždy potřebuje účet **WebShare VIP**.
3. Klikni na **Najít Lunu v síti**. Nokturno projde domácí síť a adresu vyplní samo.
4. Klikni na **Ověřit nastavení Luny** a řiď se hláškou, co každá znamená, najdeš v článku
   [Co znamenají hlášky z Ověřit nastavení Luny](luna-hlasky.md).

Celý návod na zprovoznění Luny krok za krokem je v návodu:
[Nastavení Luny](../navody/kodi/nastaveni-luny.md).

## Pořád to nejde?
V okně ověření klikni na **Poslat log** a napiš nám, viz [Kde hledat pomoc](kde-hledat-pomoc.md).

---
[Všechny návody](../) · [Slovensky](../sk/luna-neodpovida)
