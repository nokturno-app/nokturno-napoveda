---
slug: luna-hlasky
lang: cs
title: Co znamenají hlášky z Ověřit nastavení Luny
products: [kodi]
priority: 0
---

# Co znamenají hlášky z Ověřit nastavení Luny

Tlačítko **Ověřit nastavení Luny** najdeš v **Nokturno → Nastavení → Zdroje a účty**, ve skupině **Luna**.
Nejdřív se zeptá na adresu (předvyplněná je uložená, stačí OK), pak projde celou cestu od serveru po streamy
a napíše, kde to vázne. Při chybě nabídne **Zadat adresu** (zkusit jinou) a **Poslat log**.

Nahoře v hlavním menu a ve výpisu **Stav zdrojů** se ukazuje zkrácená podoba téže hlášky (sloupec „V menu“).

| Hláška v ověření | V menu | Co to znamená | Co udělat |
|---|---|---|---|
| Luna … odpovídá a vrací streamy. Nastavení je v pořádku. | – | vše funguje | nic |
| Není vyplněná adresa Luny ani token. | chybí adresa i token | pole jsou prázdná | [Luna: „běží, ale chybí token“](luna-token.md), nebo Lunu vypni |
| Adresa … nemá očekávaný tvar. | adresa nedává smysl | překlep v adrese | tvar `http://192.168.1.10:7126` |
| Na adrese … se nikdo neozval. | server neodpovídá | na adrese nic neběží | [Luna: „server neodpovídá“](luna-neodpovida.md) |
| Na adrese … něco odpovídá, ale není to Luna. | na té adrese neběží Luna | jiné zařízení nebo port | Luna má port 7126 |
| Luna … běží, ale chybí token. | běží, ale chybí token | chybí adresa doplňku ze `/setup` | [Luna: „běží, ale chybí token“](luna-token.md) |
| V poli Token není token. | v poli Token není token | vložený jen kus adresy | zkopíruj celou adresu tlačítkem Kopírovat |
| Luna … běží, ale tento token nepřijala. | token Luna nepřijala | token z jiné nebo přeinstalované Luny | vygeneruj adresu znovu na `/setup` této Luny |
| … hledání na WebShare funguje, ale její hlavní zdroj nic nevrací. | hlavní zdroj nic nevrací – účet WebShare v Luně? | token z jiné Luny nebo chybí WebShare | na `/setup` zkontroluj WebShare a token |
| … běží, ale nenašla streamy ani u známých filmů. | nenašla žádné streamy – účet WebShare v Luně? | v Luně není přihlášený WebShare nebo nemá VIP | na `/setup` se znovu přihlas do WebShare |
| V této síti se Luna nenašla. (po Najít Lunu v síti) | – | hledání v síti nic nenašlo | Luna neběží, je v jiné síti nebo má jiný port; adresu vyplň ručně |

Home Assistant pro Lunu potřeba není. Luna běží i přímo na Android TV boxu (adresa `http://127.0.0.1:7126`),
na počítači nebo na NAS. Vždy potřebuje účet WebShare VIP.

Celý návod: [Nastavení Luny](../navody/kodi/nastaveni-luny.md).

---
[Všechny návody](../) · [Slovensky](../sk/luna-hlasky)
