---
slug: stremio-mimo-domov
lang: cs
title: Nokturno pro Stremio mimo domov – Tailscale a VPN
products: [stremio]
priority: 2
templates:
  stremio: |
    Mimo domov se k aplikaci Nokturno dostaneš přes Tailscale: nainstaluj ho na zařízení s aplikací i na mobil nebo TV.
    Nuvio vezme http://<adresa 100.x.y.z>:7140, Stremio chce HTTPS: tailscale serve --bg --https=443 http://127.0.0.1:7140
    Tailscale Funnel nepoužívej, zveřejnil by aplikaci celému internetu.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/stremio-mimo-domov
---

# Nokturno pro Stremio mimo domov – Tailscale a VPN

!!! danger "Doplněk na cizím serveru dostává tvoje přihlašovací údaje"
    Každý doplněk pro Stremio, který běží na cizím serveru, dostává tvoje přihlašovací údaje ke zdrojům
    (WebShare, FastShare, Přehraj.to…). Jsou v adrese doplňku, provozovatel serveru je proto může vidět
    a uložit a musíš mu věřit. Jistotu máš jen s doplňkem, který běží u tebe: doma, přes VPN nebo na vlastním VPS.

Aplikace Nokturno pro Stremio zůstane doma (na televizi, počítači, Raspberry Pi, NAS nebo v Home Assistantu)
a zařízení venku se k ní dostanou přes soukromou síť mezi tvými zařízeními. Do internetu se nic neotevírá.
Jak aplikaci doma rozjet, je v článku [Nokturno pro Stremio – aplikace](stremio-aplikace.md).

## Kdy to potřebuješ
- Díváš se na mobilu nebo tabletu mimo domov.
- Chceš doplněk na televizi u rodičů, na chatě nebo na hotelu.
- Nechceš platit VPS ani nic otevírat do internetu.

V domácí síti tohle nepotřebuješ, tam stačí adresa z formuláře aplikace.

## Tailscale krok za krokem
[Tailscale](https://tailscale.com) spojí tvoje zařízení do soukromé sítě (tailnetu). Pro domácí použití je zdarma.

1. **Účet:** na [tailscale.com](https://tailscale.com) se zaregistruj (přihlášení přes Google, Microsoft, GitHub
   nebo Apple).
2. **Zařízení s aplikací Nokturno:** nainstaluj Tailscale a přihlas se stejným účtem.
    - Linux, Raspberry Pi, NAS: `curl -fsSL https://tailscale.com/install.sh | sh`, pak `sudo tailscale up`
      a otevři odkaz, který příkaz vypíše.
    - Windows a macOS: aplikace z [tailscale.com/download](https://tailscale.com/download).
    - Android TV a Android box: aplikace **Tailscale** z Google Play.
    - Home Assistant: doplněk **Tailscale** z obchodu s doplňky.
3. **Zařízení s přehrávačem** (mobil, tablet, televize u rodičů): aplikace Tailscale z Google Play nebo App Store,
   na Android TV z Google Play. Přihlas se stejným účtem.
4. **MagicDNS a HTTPS:** v [administraci Tailscale](https://login.tailscale.com/admin/dns) zapni **MagicDNS**
   a **HTTPS Certificates**. Stremio je potřebuje, Nuvio ne.
5. **Adresa zařízení s aplikací:** ukáže ji aplikace Tailscale (`100.x.y.z`), na Linuxu `tailscale ip -4`.

### Nuvio
Stačí adresa přes `http://<adresa 100.x.y.z zařízení s aplikací>:7140`. Na zařízení venku otevři
`http://100.x.y.z:7140/configure` a dej **Přidat do Nuvia**.

### Stremio
Stremio chce u vzdáleného doplňku HTTPS s platným certifikátem. Spolehlivě to zařídí `tailscale serve`
na zařízení s aplikací (Linux, Raspberry Pi, NAS, Windows, macOS, kde je příkaz `tailscale`):

```bash
tailscale serve --bg --https=443 http://127.0.0.1:7140
```

Nastavení pak otevři na `https://<zařízení>.<tailnet>.ts.net/configure` a doplněk přidej odtud. Přesnou adresu
vypíše `tailscale serve status`. Platí jen uvnitř tvého tailnetu a vydrží i restart. Vypneš to příkazem
`tailscale serve --bg --https=443 off`.

Kde příkaz `tailscale` není (aplikace na Android TV, doplněk v Home Assistantu), může fungovat adresa přes
local-ip.co s adresou Tailscale: `https://100-x-y-z.my.local-ip.co:7141`. Formulář ji sám nenabídne, doplň ji
ručně a některé routery nebo DNS takové jméno zablokují.

!!! warning "Tailscale Funnel nepoužívej"
    Funnel zveřejní aplikaci celému internetu a s ní i tvoje nastavení. Na doplněk stačí `tailscale serve`,
    který platí jen pro tvoje zařízení.

### Vlastní úložiště
Přehrávač si soubor stahuje sám. Když je úložiště doma, musí na něj dosáhnout i zařízení venku: v adrese
úložiště použij jeho adresu v Tailscale (`100.x.y.z` nebo jméno z MagicDNS), nebo na domácím zařízení zapni
v Tailscale sdílení domácí sítě (subnet router).

## Jiné VPN
- **VPN v routeru:** řada routerů (Fritz!Box, ASUS, Turris, MikroTik…) umí VPN server, často WireGuard.
  Po připojení je zařízení venku jako doma: Nuvio vezme `http://<domácí IP>:7140`, Stremio adresu
  `https://<IP s pomlčkami>.my.local-ip.co:7141` z formuláře.
- **Vlastní WireGuard** na Raspberry Pi nebo NAS: potřebuje přesměrovaný port v routeru a veřejnou IP adresu.
  Použití je pak stejné jako u VPN v routeru.

Bez veřejné IP adresy (častý případ u mobilních a některých optických připojení) VPN server doma nerozjedeš,
Tailscale ano.

## VPN, nebo VPS?
| | Tailscale nebo VPN | VPS s vlastní doménou |
|---|---|---|
| Cena | zdarma | VPS a doména, od pár eur měsíčně |
| Co je v internetu | nic, jen tvoje zařízení | aplikace na tvé doméně |
| Na každém zařízení | aplikace Tailscale nebo VPN | nic, stačí adresa doplňku |
| Doma musí běžet | zařízení s aplikací | nic |
| Náročnost | pár kliknutí, u Stremia jeden příkaz | VPS a doména, instalace jedním příkazem |

Kde VPN aplikaci nenainstaluješ (některé televize), pomůže VPS:
[Nokturno pro Stremio na VPS s vlastní doménou](stremio-vps.md).

Doplněk je jen pro tebe a tvou domácnost. Adresu doplňku ani adresu zařízení v tailnetu nikomu nedávej,
adresa doplňku obsahuje tvoje účty.

---
[Všechny návody](../) · [Slovensky](../sk/stremio-mimo-domov)
