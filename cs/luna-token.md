---
slug: luna-token
lang: cs
title: "Luna: „běží, ale chybí token“"
products: [kodi]
priority: 0
when: {luna: [no_token, bad_token_format, bad_token, main_empty, no_streams]}
templates:
  kodi: |
    Ahoj, Luna ti běží, ale Nokturno od ní nemá token. Bez něj z ní nic nepřijde.
    1. Na mobilu nebo počítači otevři v prohlížeči adresu Luny s /setup na konci, například http://192.168.1.10:7126/setup.
    2. Přihlas se do WebShare (účet s VIP), zvol Ruční instalace a u Luna: Absolute Cinema dej Kopírovat.
    3. V Kodi: Nokturno → Nastavení → Nastavit z mobilu a přenos → Nastavit z mobilu. Naskenuj QR kód a zkopírovanou adresu vlož do sekce Luna.
    4. Pak v Nastavení → Zdroje a účty, ve skupině Luna, klikni na Ověřit nastavení Luny.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/luna-token
    Tým Nokturno
---

# Luna: „běží, ale chybí token“

## Co to znamená
Server Luny Nokturno našlo a ozval se, ale chybí mu **adresa doplňku s tokenem**. Token je dlouhý kód,
který začíná `e1.`, a Luna podle něj pozná tvůj účet WebShare. Bez něj z Luny nic nepřijde.

Stejný problém ohlašují i tyhle hlášky z **Ověřit nastavení Luny**:

- „Luna … běží, ale chybí token.“
- „V poli Token není token.“
- „Luna … běží, ale tento token nepřijala.“
- „… odpovídá a hledání na WebShare funguje, ale její hlavní zdroj nic nevrací.“
- „… běží, ale nenašla streamy ani u známých filmů.“

## Proč se to stává
- V poli je jen adresa serveru (`http://…:7126`), ne adresa doplňku ze stránky `/setup`.
- V poli je jen kus adresy.
- Token je ze staré nebo jiné Luny (Luna byla přeinstalovaná nebo jich máš víc).
- V Luně není přihlášený WebShare, nebo účet nemá VIP.

## Co udělat
1. Na **mobilu nebo počítači** otevři v prohlížeči adresu Luny s `/setup` na konci, například
   `http://192.168.1.10:7126/setup`. Když Luna běží přímo na TV boxu, zadej IP adresu boxu.
2. Na stránce `/setup` zvol **Ruční instalace**, přihlas se do **WebShare** (účet s VIP) a v kroku s adresami
   klikni u **Luna: Absolute Cinema** na **Kopírovat**. Adresa končí zhruba `…:7126/e1.AbCd…/manifest.json`.
3. Adresu dostaň do Kodi. Nejpohodlněji z mobilu:
   **Nokturno → Nastavení → Nastavit z mobilu a přenos → Nastavit z mobilu**, naskenuj QR kód,
   rozbal sekci **Luna** a adresu vlož do pole pro adresu doplňku. Mobil musí být ve stejné síti jako Kodi.
4. V **Nastavení → Zdroje a účty**, skupina **Luna**, klikni na **Ověřit nastavení Luny**.
   Když napíše „Luna … odpovídá a vrací streamy. Nastavení je v pořádku.“, je hotovo.

Adresu doplňku nikomu neposílej, obsahuje tvůj token.

Návod se screenshoty je v návodu:
[Nastavení Luny](../navody/kodi/nastaveni-luny.md).
Význam všech hlášek: [Co znamenají hlášky z Ověřit nastavení Luny](luna-hlasky.md).

## Pořád to nejde?
V okně ověření klikni na **Poslat log** a napiš nám, viz [Kde hledat pomoc](kde-hledat-pomoc.md).

---
[Všechny návody](../) · [Slovensky](../sk/luna-token)
