---
slug: stremio-kde-spustit
lang: sk
title: Kde doma spustiť Nokturno pre Stremio – nápady a príklady
products: [stremio]
priority: 1
templates:
  stremio: |
    Nokturno pre Stremio nie je náročné, stačí mu čokoľvek, čo doma stále beží: starý Android telefón, Raspberry Pi, NAS, starý notebook alebo box.
    Video totiž netečie cez aplikáciu, tá len vracia odkazy, takže zvládne aj slabý hardvér.
    Nápady a postupy: https://nokturno-app.github.io/nokturno-napoveda/sk/stremio-kde-spustit
---

# Kde doma spustiť Nokturno pre Stremio – nápady a príklady

Nokturno pre Stremio je malá aplikácia, ktorá musí bežať, kedykoľvek sa pozeráš. Nie je náročná: **video cez ňu
netečie**. Aplikácia Stremiu len vracia zoznam streamov s odkazmi a prehrávač si súbor sťahuje priamo zo zdroja.
Stačí jej preto takmer akýkoľvek starý hardvér, hlavne nech je **stále zapnutý**, pripojený k domácej sieti
a má **pevnú IP adresu** (rezervácia v routeri).

Podrobný postup inštalácie je v článku [Nokturno pre Stremio – aplikácia](stremio-aplikace.md). Tu sú nápady,
na čom ju spustiť.

## Rýchly výber
| Čo doma máš | Prečo to dáva zmysel | Kam ďalej |
|---|---|---|
| Starý Android telefón alebo tablet | zadarmo, má batériu ako záložný zdroj a Wi-Fi | [Starý Android telefón](#stary-android-telefon-alebo-tablet) |
| Raspberry Pi (aj staršie) | tiché, pár wattov, beží roky | [Raspberry Pi](#raspberry-pi) |
| NAS (Synology, QNAP, TrueNAS…) | zapnutý stále | [NAS a Docker](#nas-a-docker) |
| Android TV alebo Android box | aplikácia ide priamo do televízora | [Android TV box](#android-tv-alebo-android-box) |
| Starý notebook alebo mini PC | výkonu je dosť, stačí ho nechať zapnutý | [Starý notebook alebo mini PC](#stary-notebook-alebo-mini-pc) |
| Router MikroTik s kontajnermi | pobeží na zariadení, ktoré aj tak stále beží | [MikroTik](#mikrotik) |
| Home Assistant | doplnok, nič ďalšie nepotrebuješ | [Home Assistant](stremio-aplikace.md#home-assistant) |

## Starý Android telefón alebo tablet
Telefón, ktorý leží v zásuvke, je na toto takmer ideálny. Potrebuješ Android **7.0 alebo novší**.

1. Nainštaluj `nokturno-<verzia>.apk` z [vydania na GitHube](https://github.com/nokturno-app/nokturno-stremio-app/releases/latest).
   Postup je v časti [Android TV a Android box](stremio-aplikace.md#android-tv-a-android-box), rovnaký je aj pre telefón.
2. Otvor aplikáciu Nokturno. Android sa opýta na výnimku z úspory batérie: **povoľ ju**. Bez nej službu po
   nejakom čase uspí a doplnok prestane odpovedať.
3. Nechaj telefón pripojený k nabíjačke a k domácej Wi-Fi. V nastaveniach Wi-Fi vypni úsporu energie, ak ju telefón ponúka.
4. V routeri mu nastav pevnú IP (rezervácia DHCP).
5. Nastavenie doplnku otvor z iného zariadenia na `http://<IP telefónu>:7140/configure` a daj **Pridať do Stremia**
   alebo **Pridať do Nuvia**.

Rady: telefón s batériou, ktorá bobtná, nenechávaj zapojený v nabíjačke. Nastav mu radšej zhasnutie displeja
a nechaj ho na chladnom mieste, nie na kúrení alebo pod televízorom.

## Raspberry Pi
Hodí sa akékoľvek Raspberry Pi od verzie Zero 2 W vyššie, teda aj to, ktoré je na iné veci už malé. Pre Stremio
nepotrebuje obrazovku ani myš.

1. Nainštaluj Raspberry Pi OS Lite (64bit, ak to tvoje Pi vie).
2. Podľa architektúry (`uname -m`) stiahni `linux-arm64` alebo `linux-arm` a vytvor službu systemd. Postup je v časti
   [Raspberry Pi a NAS](stremio-aplikace.md#raspberry-pi-a-nas).
3. Nastavenie otvor na `http://<IP Raspberry Pi>:7140/configure`.

Rady: napájaj ho kvalitným zdrojom (slabý zdroj robí záhadné pády). Aplikácia zapisuje cache a nastavenia,
preto je vhodná kvalitná SD karta alebo malý USB disk.

## NAS a Docker
Ak máš NAS s Dockerom (Synology s balíčkom Container Manager, QNAP, TrueNAS, Unraid), je najjednoduchší obraz
Dockeru. Ku každému vydaniu je priložený ako súbor `nokturno-<verzia>-docker-<architektúra>.tar`
v [poslednom vydaní](https://github.com/nokturno-app/nokturno-stremio-app/releases/latest):

| Zariadenie | Súbor |
|---|---|
| bežný NAS a PC (64bit Intel/AMD) | `…-docker-amd64.tar` |
| Raspberry Pi 4 a 5, ARM NAS (64bit) | `…-docker-arm64.tar` |
| staršie Raspberry Pi, 32bit ARM | `…-docker-arm.tar` |

Na počítači s Dockerom:

```bash
docker load -i nokturno-<verzia>-docker-amd64.tar
docker run -d --name nokturno --restart unless-stopped \
  -p 7140:7140 -v nokturno-data:/data nokturno:<verzia>
```

Alebo ako `docker-compose.yml`:

```yaml
services:
  nokturno:
    image: nokturno:<verzia>
    restart: unless-stopped
    ports:
      - "7140:7140"
    volumes:
      - nokturno-data:/data
volumes:
  nokturno-data:
```

Väčšina NAS vie `.tar` importovať aj v grafickom rozhraní Dockeru (zvyčajne Image → Import, prípadne Add from file).
Nastavenie potom otvor na `http://<IP NAS>:7140/configure`.

V kontajneri sa aplikácia **sama neaktualizuje**. Pre novú verziu stiahni nový `.tar`, načítaj ho a kontajner
vytvor znova. Dáta (`/data`) ostanú vo zväzku.

## Android TV alebo Android box
Ak máš televízor alebo box s Androidom, beží aplikácia priamo v ňom a nepotrebuješ ďalšie zariadenie. Postup je
v časti [Android TV a Android box](stremio-aplikace.md#android-tv-a-android-box). Pri najlacnejších boxoch vypni
v nastaveniach úsporný režim, ktorý ich po čase uspí.

## Starý notebook alebo mini PC
Notebook zo zásuvky zvládne Windows, Linux aj macOS verziu. Len ho musíš prinútiť, aby **nespal**:

- **Windows:** Nastavenia → Systém → Napájanie → Režim spánku: nikdy. A **Pri zatvorení veka: nič nerobiť**,
  nech môže ležať zatvorený v kúte. Aplikácia beží ako ikona mesiaca pri hodinách. Nech sa spúšťa s počítačom, je v časti
  [Počítač](stremio-aplikace.md#pocitac).
- **Linux:** spusti ju ako službu systemd (pozri [Raspberry Pi a NAS](stremio-aplikace.md#raspberry-pi-a-nas)).

## MikroTik
Router MikroTik s architektúrou **arm, arm64 alebo x86** vie balíček `container` a Docker obraz spustí. Architektúru
zistíš príkazom `/system resource print` (riadok `architecture-name`). Staršie modely s architektúrou
MIPSBE alebo MMIPS (napríklad hAP lite, hEX) kontajnery nevedia.

Nahraj `.tar` z vydania do routera a v **Container → Add** zvoľ **File**, port 7140 a mount na `/data`.
Hodí sa len na modely, ktoré majú dosť pamäte a úložiska (najlepšie USB disk).

## Čo platí všade
- **Zariadenie musí bežať stále** a byť v rovnakej sieti ako Stremio, alebo dostupné cez VPN.
- **Pevná IP** v routeri, inak sa po reštarte routera adresa zmení a doplnok prestane fungovať.
- **Adresa doplnku obsahuje tvoje účty.** Nikomu ju neposielaj.
- Doma to funguje hneď. Pre televízor u rodičov alebo mobil vonku použi
  [Tailscale alebo VPN](stremio-mimo-domov.md), prípadne [VPS s vlastnou doménou](stremio-vps.md).
- Ak sa ti nastavenie z iného zariadenia neotvorí alebo sa doplnok nedá pridať, prejdi tabuľku *Časté problémy*
  v článku [Nokturno pre Stremio – aplikácia](stremio-aplikace.md#caste-problemy).

---
[Všetky návody](./) · [Česky](../cs/stremio-kde-spustit)
