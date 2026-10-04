---
slug: stremio-kde-spustit
lang: cs
title: Kde doma pustit Nokturno pro Stremio – nápady a příklady
products: [stremio]
priority: 1
templates:
  stremio: |
    Nokturno pro Stremio není náročné, stačí mu cokoli, co doma pořád běží: starý Android telefon, Raspberry Pi, NAS, starý notebook nebo box.
    Video totiž netěče přes aplikaci, ta jen vrací odkazy, takže zvládne i slabý hardware.
    Nápady a postupy: https://nokturno-app.github.io/nokturno-napoveda/cs/stremio-kde-spustit
---

# Kde doma pustit Nokturno pro Stremio – nápady a příklady

Nokturno pro Stremio je malá aplikace, která musí běžet, kdykoli se díváš. Není náročná: **video přes ni
u většiny zdrojů neteče**. Aplikace Stremiu vrací seznam streamů s odkazy a přehrávač si soubor stahuje přímo ze zdroje.
Výjimkou jsou soubory z tvého vlastního úložiště (a z FastShare), které přehrávači předává aplikace (stačí domácí síť; slabý hardware
nebo Wi-Fi může u 4K brzdit).
Stačí jí proto skoro jakýkoli starý hardware, hlavně ať je **pořád zapnutý**, připojený k domácí síti
a má **pevnou IP adresu** (rezervace v routeru).

Podrobný postup instalace je v článku [Nokturno pro Stremio – aplikace](stremio-aplikace.md). Tady jsou nápady,
na čem ji pustit.

## Rychlý výběr
| Co doma máš | Proč to dává smysl | Kam dál |
|---|---|---|
| Starý Android telefon nebo tablet | zadarmo, má baterii jako záložní zdroj a Wi-Fi | [Starý Android telefon](#stary-android-telefon-nebo-tablet) |
| Raspberry Pi (i starší) | tichý, pár wattů, běží roky | [Raspberry Pi](#raspberry-pi) |
| NAS (Synology, QNAP, TrueNAS…) | zapnutý stejně pořád | [NAS a Docker](#nas-a-docker) |
| Android TV nebo Android box | aplikace jde přímo do televize | [Android TV box](#android-tv-nebo-android-box) |
| Starý notebook nebo mini PC | výkonu je dost, stačí ho nechat zapnutý | [Starý notebook nebo mini PC](#stary-notebook-nebo-mini-pc) |
| Router MikroTik s kontejnery | poběží na zařízení, které stejně neustále běží | [MikroTik](#mikrotik) |
| Home Assistant | doplněk, nic dalšího nepotřebuješ | [Home Assistant](stremio-aplikace.md#home-assistant) |

## Starý Android telefon nebo tablet
Telefon, který leží v šuplíku, je na tohle skoro ideální. Potřebuješ Android **7.0 nebo novější**.

1. Nainstaluj `nokturno-<verze>.apk` z [vydání na GitHubu](https://github.com/nokturno-app/nokturno-stremio-app/releases/latest).
   Postup je v části [Android TV a Android box](stremio-aplikace.md#android-tv-a-android-box), stejný je i pro telefon.
2. Otevři aplikaci Nokturno. Android se zeptá na výjimku z úspor baterie: **povol ji**. Bez ní službu po
   nějaké době uspí a doplněk přestane odpovídat.
3. Nech telefon připojený k nabíječce a k domácí Wi-Fi. V nastavení Wi-Fi vypni úsporu energie, pokud ji telefon nabízí.
4. V routeru mu nastav pevnou IP (rezervace DHCP).
5. Nastavení doplňku otevři z jiného zařízení na `http://<IP telefonu>:7140/configure` a dej **Přidat do Stremia**
   nebo **Přidat do Nuvia**.

Rady: telefon s baterií, která bobtná, nenech zapojený v nabíječce. Nastav mu raději zhasnutí displeje
a nech ho na chladném místě, ne na topení nebo pod televizí.

## Raspberry Pi
Hodí se jakékoli Raspberry Pi od verze Zero 2 W výš, tedy i to, které je na jiné věci už malé. Pro Stremio
nepotřebuje obrazovku ani myš.

1. Nainstaluj Raspberry Pi OS Lite (64bit, pokud to tvoje Pi umí).
2. Podle architektury (`uname -m`) stáhni `linux-arm64` nebo `linux-arm` a vytvoř službu systemd. Postup je v části
   [Raspberry Pi a NAS](stremio-aplikace.md#raspberry-pi-a-nas).
3. Nastavení otevři na `http://<IP Raspberry Pi>:7140/configure`.

Rady: napájej ho kvalitním zdrojem (slabý zdroj dělá záhadné pády). Aplikace zapisuje cache a nastavení,
proto je vhodná kvalitní SD karta nebo malý USB disk.

## NAS a Docker
Pokud máš NAS s Dockerem (Synology s balíčkem Container Manager, QNAP, TrueNAS, Unraid), je nejjednodušší obraz
Dockeru. Ke každému vydání je přiložený jako soubor `nokturno-<verze>-docker-<architektura>.tar`
v [posledním vydání](https://github.com/nokturno-app/nokturno-stremio-app/releases/latest):

| Zařízení | Soubor |
|---|---|
| běžný NAS a PC (64bit Intel/AMD) | `…-docker-amd64.tar` |
| Raspberry Pi 4 a 5, ARM NAS (64bit) | `…-docker-arm64.tar` |
| starší Raspberry Pi, 32bit ARM | `…-docker-arm.tar` |

Na počítači s Dockerem:

```bash
docker load -i nokturno-<verze>-docker-amd64.tar
docker run -d --name nokturno --restart unless-stopped \
  -p 7140:7140 -v nokturno-data:/data nokturno:<verze>
```

Nebo jako `docker-compose.yml`:

```yaml
services:
  nokturno:
    image: nokturno:<verze>
    restart: unless-stopped
    ports:
      - "7140:7140"
    volumes:
      - nokturno-data:/data
volumes:
  nokturno-data:
```

Většina NASů umí `.tar` importovat i v grafickém rozhraní Dockeru (obvykle Image → Import, případně Add from file).
Nastavení pak otevři na `http://<IP NASu>:7140/configure`.

V kontejneru se aplikace **sama neaktualizuje**. Pro novou verzi stáhni nový `.tar`, načti ho a kontejner
vytvoř znovu. Data (`/data`) zůstanou ve svazku.

## Android TV nebo Android box
Když máš televizi nebo box s Androidem, běží aplikace přímo v něm a nepotřebuješ další zařízení. Postup je
v části [Android TV a Android box](stremio-aplikace.md#android-tv-a-android-box). U nejlevnějších boxů vypni
v nastavení úsporný režim, který je po čase uspí.

## Starý notebook nebo mini PC
Notebook ze šuplíku zvládne Windows, Linux i macOS verzi. Jen ho musíš přimět, aby **nespal**:

- **Windows:** Nastavení → Systém → Napájení → Režim spánku: nikdy. A **Při zavření víka: neprovádět nic**,
  ať může ležet zavřený v koutě. Aplikace běží jako ikona měsíce u hodin. Ať se spouští s počítačem, je v části
  [Počítač](stremio-aplikace.md#pocitac).
- **Linux:** pusť ji jako službu systemd (viz [Raspberry Pi a NAS](stremio-aplikace.md#raspberry-pi-a-nas)).

## MikroTik
Router MikroTik s architekturou **arm, arm64 nebo x86** umí balíček `container` a Docker obraz pustí. Architekturu
zjistíš příkazem `/system resource print` (řádek `architecture-name`). Starší modely s architekturou
MIPSBE nebo MMIPS (třeba hAP lite, hEX) kontejnery neumí.

Nahraj `.tar` z vydání do routeru a v **Container → Add** zvol **File**, port 7140 a mount na `/data`.
Hodí se jen na ty modely, které mají dost paměti a úložiště (nejlépe USB disk).

## Co platí všude
- **Zařízení musí běžet pořád** a být ve stejné síti jako Stremio, nebo přístupné přes VPN.
- **Pevná IP** v routeru, jinak se po restartu routeru adresa změní a doplněk přestane fungovat.
- **Adresa doplňku obsahuje tvoje účty.** Nikomu ji neposílej.
- Doma to funguje hned. Pro televizi u rodičů nebo mobil venku použij
  [Tailscale nebo VPN](stremio-mimo-domov.md), případně [VPS s vlastní doménou](stremio-vps.md).
- Když ti nastavení neotevře z jiného zařízení nebo doplněk nejde přidat, projdi tabulku *Časté problémy*
  v článku [Nokturno pro Stremio – aplikace](stremio-aplikace.md#caste-problemy).

---
[Všechny návody](../) · [Slovensky](../sk/stremio-kde-spustit)
