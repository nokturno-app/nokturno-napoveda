---
slug: stremio-mimo-domov
lang: sk
title: Nokturno pre Stremio mimo domova – Tailscale a VPN
products: [stremio]
priority: 2
templates:
  stremio: |
    Mimo domova sa k aplikácii Nokturno dostaneš cez Tailscale: nainštaluj ho na zariadenie s aplikáciou aj na mobil alebo TV.
    Nuvio vezme http://<adresa 100.x.y.z>:7140, Stremio chce HTTPS: tailscale serve --bg --https=443 http://127.0.0.1:7140
    Tailscale Funnel nepoužívaj, zverejnil by aplikáciu celému internetu.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/stremio-mimo-domov
---

# Nokturno pre Stremio mimo domova – Tailscale a VPN

!!! danger "Doplnok na cudzom serveri dostáva tvoje prihlasovacie údaje"
    Každý doplnok pre Stremio, ktorý beží na cudzom serveri, dostáva tvoje prihlasovacie údaje k zdrojom
    (vlastné úložisko, WebShare, FastShare…). Sú v adrese doplnku alebo uložené na serveri, prevádzkovateľ ich preto môže vidieť
    a uložiť a musíš mu veriť. Istotu máš len s doplnkom, ktorý beží u teba: doma, cez VPN alebo na vlastnom VPS.

Aplikácia Nokturno pre Stremio zostane doma (na televízore, počítači, Raspberry Pi, NAS alebo v Home Assistante)
a zariadenia vonku sa k nej dostanú cez súkromnú sieť medzi tvojimi zariadeniami. Do internetu sa nič neotvára.
Ako aplikáciu doma rozbehnúť, je v článku [Nokturno pre Stremio – aplikácia](stremio-aplikace.md).

## Kedy to potrebuješ
- Pozeráš na mobile alebo tablete mimo domova.
- Chceš doplnok na televízore u rodičov, na chate alebo v hoteli.
- Nechceš platiť VPS ani nič otvárať do internetu.

V domácej sieti toto nepotrebuješ, tam stačí adresa z formulára aplikácie.

## Tailscale krok za krokom
[Tailscale](https://tailscale.com) spojí tvoje zariadenia do súkromnej siete (tailnetu). Na domáce použitie je zadarmo.

1. **Účet:** na [tailscale.com](https://tailscale.com) sa zaregistruj (prihlásenie cez Google, Microsoft, GitHub
   alebo Apple).
2. **Zariadenie s aplikáciou Nokturno:** nainštaluj Tailscale a prihlás sa rovnakým účtom.
    - Linux, Raspberry Pi, NAS: `curl -fsSL https://tailscale.com/install.sh | sh`, potom `sudo tailscale up`
      a otvor odkaz, ktorý príkaz vypíše.
    - Windows a macOS: aplikácia z [tailscale.com/download](https://tailscale.com/download).
    - Android TV a Android box: aplikácia **Tailscale** z Google Play.
    - Home Assistant: doplnok **Tailscale** z obchodu s doplnkami.
3. **Zariadenie s prehrávačom** (mobil, tablet, televízor u rodičov): aplikácia Tailscale z Google Play alebo App Store,
   na Android TV z Google Play. Prihlás sa rovnakým účtom.
4. **MagicDNS a HTTPS:** v [administrácii Tailscale](https://login.tailscale.com/admin/dns) zapni **MagicDNS**
   a **HTTPS Certificates**. Stremio ich potrebuje, Nuvio nie.
5. **Adresa zariadenia s aplikáciou:** ukáže ju aplikácia Tailscale (`100.x.y.z`), na Linuxe `tailscale ip -4`.
   Adresa z karty „Z jiného zařízení v síti“ v aplikácii pre Android je z Wi-Fi alebo ethernetu a mimo domova
   nefunguje, tú nepoužívaj.

Aplikácia pozná správcu podľa mena a hesla, nie podľa siete, takže sa na zariadení vonku v nastavení (`/configure`)
prihlás ako správca. Keď správca už je založený a nie si prihlásený, uvidíš v predvolenom režime Profily len kartu **Prihlásenie**. Správca, ktorý
ešte nebol založený, chce cez Tailscale aj kód z výpisu aplikácie, pretože sa nepočíta ako domáca sieť. Založ ho
radšej doma, pozri [Správca, režimy a účty](stremio-aplikace.md#spravca-rezimy-a-ucty).

### Nuvio
Stačí adresa cez `http://<adresa 100.x.y.z zariadenia s aplikáciou>:7140`. Na zariadení vonku otvor
`http://100.x.y.z:7140/configure` a daj **Pridať do Nuvia**.

### Stremio
Stremio chce pri vzdialenom doplnku HTTPS s platným certifikátom. Spoľahlivo to zariadi `tailscale serve`
na zariadení s aplikáciou (Linux, Raspberry Pi, NAS, Windows, macOS, kde je príkaz `tailscale`):

```bash
tailscale serve --bg --https=443 http://127.0.0.1:7140
```

Nastavenie potom otvor na `https://<zariadenie>.<tailnet>.ts.net/configure` a doplnok pridaj odtiaľ. Presnú adresu
vypíše `tailscale serve status`. Platí len vnútri tvojho tailnetu a vydrží aj reštart. Vypneš to príkazom
`tailscale serve --bg --https=443 off`.

Kde príkaz `tailscale` nie je (aplikácia na Android TV, doplnok v Home Assistante), môže fungovať adresa cez
local-ip.co s adresou Tailscale: `https://100-x-y-z.my.local-ip.co:7141`. Formulár ju sám neponúkne, doplň ju
ručne a niektoré routery alebo DNS také meno zablokujú.

!!! warning "Tailscale Funnel nepoužívaj"
    Funnel zverejní aplikáciu celému internetu a s ňou aj tvoje nastavenia. Na doplnok stačí `tailscale serve`,
    ktorý platí len pre tvoje zariadenia.

### Vlastné úložisko
Súbor z vlastného úložiska (WebDAV aj SMB) prehrávaču posiela aplikácia Nokturno, prehrávač si ho z úložiska
nesťahuje sám. Stačí preto, aby na úložisko dosiahla aplikácia doma, a zariadenie vonku k nemu prístup nepotrebuje.
SMB (`smb://`) číta aplikácia priamo, takže na zdieľaný priečinok musí dosiahnuť sama: beží doma, alebo má do domácej siete VPN.

### Luna z doplnku Home Assistantu
Lunu z doplnku v Home Assistante môžeš používať aj mimo domova rovnakou cestou. Home Assistant je potom v tvojom
tailnete (doplnok **Tailscale**, pozri vyššie) a Luna na ňom počúva na všetkých jeho adresách, teda aj na tej z Tailscale.

1. V doplnku **Tailscale** v Home Assistante sa prihlás rovnakým účtom ako ostatné zariadenia a zisti adresu
   Home Assistanta (`100.x.y.z`, nájdeš ju v aplikácii Tailscale alebo v administrácii).
2. Na zariadení vonku nainštaluj aplikáciu Tailscale a prihlás sa rovnakým účtom.
3. Adresa Luny je potom namiesto domácej adresy táto:
    - Kodi, Nuvio: `http://100.x.y.z:7126`
    - Stremio (chce HTTPS): `https://100-x-y-z.my.local-ip.co:7127` – adresa Tailscale s pomlčkami namiesto bodiek.
4. V Nokturne pre Kodi ju vlož ručne: **Nastavenia → Zdroje a účty**, skupina **Luna**. **Nájsť Lunu v sieti**
   mimo domova nič nenájde, pretože hľadá len v domácej sieti. Potom klikni na **Overiť nastavenie Luny**.

Adresu s tokenom si nechaj vygenerovať doma na stránke `/setup` Luny, ako je v návode [Nastavenie Luny](../navody/kodi/nastaveni-luny.md),
a vonku v nej vymeň len začiatok (domácu adresu a port) za adresu z bodu 3. Adresu ani token nikomu neposielaj.

Niektoré routery alebo DNS mená z local-ip.co zablokujú. Potom pri Stremiu pomôže `tailscale serve`, pozri vyššie.
Funnel nepoužívaj, zverejnil by Lunu celému internetu.

## Iné VPN
- **VPN v routeri:** veľa routerov (Fritz!Box, ASUS, Turris, MikroTik…) vie VPN server, často WireGuard.
  Po pripojení je zariadenie vonku ako doma: Nuvio vezme `http://<domáca IP>:7140`, Stremio adresu
  `https://<IP s pomlčkami>.my.local-ip.co:7141` z formulára.
- **Vlastný WireGuard** na Raspberry Pi alebo NAS: potrebuje presmerovaný port v routeri a verejnú IP adresu.
  Použitie je potom rovnaké ako pri VPN v routeri.

Bez verejnej IP adresy (častý prípad pri mobilných a niektorých optických pripojeniach) VPN server doma nerozbehneš,
Tailscale áno.

## VPN, alebo VPS?
| | Tailscale alebo VPN | VPS s vlastnou doménou |
|---|---|---|
| Cena | zadarmo | VPS a doména, od pár eur mesačne |
| Čo je v internete | nič, len tvoje zariadenia | aplikácia na tvojej doméne |
| Na každom zariadení | aplikácia Tailscale alebo VPN | nič, stačí adresa doplnku |
| Doma musí bežať | zariadenie s aplikáciou | nič |
| Náročnosť | pár kliknutí, pri Stremiu jeden príkaz | VPS a doména, inštalácia jedným príkazom |

Kde VPN aplikáciu nenainštaluješ (niektoré televízory), pomôže VPS:
[Nokturno pre Stremio na VPS s vlastnou doménou](stremio-vps.md).

Doplnok je len pre teba a tvoju domácnosť. Adresu doplnku ani adresu zariadenia v tailnete nikomu nedávaj,
adresa doplnku je kľúč k tvojim účtom.

---
[Všetky návody](./) · [Česky](../cs/stremio-mimo-domov)
