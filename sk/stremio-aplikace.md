---
slug: stremio-aplikace
lang: sk
title: Nokturno pre Stremio – aplikácia
products: [stremio]
priority: 0
templates:
  stremio: |
    Nokturno pre Stremio je aplikácia, ktorú si spustíš u seba (Android TV box, počítač, Home Assistant, Raspberry Pi, NAS).
    Stiahni ju z github.com/nokturno-app/nokturno-stremio-app/releases, spusti a otvor http://<IP zariadenia>:7140/configure.
    Doplnok na cudzom serveri dostáva tvoje prihlasovacie údaje k zdrojom. Keď beží u teba, nedostane ich nikto iný.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/stremio-aplikace
---

# Nokturno pre Stremio – aplikácia

!!! danger "Doplnok na cudzom serveri dostáva tvoje prihlasovacie údaje"
    Každý doplnok pre Stremio, ktorý beží na cudzom serveri, dostáva tvoje prihlasovacie údaje k zdrojom
    (vlastné úložisko, WebShare, FastShare…). Sú totiž v adrese doplnku a s každou požiadavkou prechádzajú cez ten
    server. Jeho prevádzkovateľ ich tak môže vidieť a uložiť a musíš mu veriť. Istotu, že ich nemá nikto iný,
    máš len vtedy, keď doplnok beží u teba: na televízore, počítači, Home Assistante, Raspberry Pi alebo na vlastnom VPS.

Nokturno pre Stremio a Nuvio je malá aplikácia, ktorá beží **u teba**. Stremio aj Nuvio potom len zadajú adresu
doplnku a pýtajú sa aplikácie ako každého iného doplnku. Aplikácia musí bežať vždy, keď pozeráš.
Doma ju spustíš na televízore s Androidom, na počítači, na Raspberry Pi alebo NAS, alebo ako
[doplnok Home Assistantu](#home-assistant), ak Home Assistant doma máš.

## Kde ju spustiť
| Čo máš | Kde aplikácia beží | Postup |
|---|---|---|
| Android TV, Google TV alebo Android box | priamo na televízore alebo boxe | [Android TV a Android box](#android-tv-a-android-box) |
| Počítač s Windows, macOS alebo Linuxom | na počítači, doplnok funguje len vtedy, keď počítač beží | [Počítač](#pocitac) |
| Home Assistant (HA OS) | ako doplnok Home Assistantu | [Home Assistant](#home-assistant) |
| Raspberry Pi, NAS alebo iný malý linuxový počítač | na ňom, beží stále | [Raspberry Pi a NAS](#raspberry-pi-a-nas) |
| Starý Android telefón, Docker na NAS, MikroTik, starý notebook | nápady a príklady, na čom to doma rozbehnúť | [Kde doma spustiť Nokturno pre Stremio](stremio-kde-spustit.md) |
| Mobil alebo TV mimo domova, aplikácia zostane doma | doma, prístup cez Tailscale alebo VPN | [Nokturno pre Stremio mimo domova – Tailscale a VPN](stremio-mimo-domov.md) |
| VPS s vlastnou doménou, prístup odkiaľkoľvek bez VPN | na VPS | [Nokturno pre Stremio na VPS s vlastnou doménou](stremio-vps.md) |

Najlepšie je spustiť aplikáciu na zariadení, ktoré je stále zapnuté (box, Raspberry Pi, NAS), alebo priamo na tom,
kde Stremio spúšťaš.

## Android TV a Android box
1. Povoľ inštaláciu z neznámych zdrojov pre aplikáciu, cez ktorú APK dostaneš do televízora, napríklad
   **Downloader** alebo **Send files to TV**.
2. Stiahni `nokturno-<verzia>.apk` z [vydaní na GitHube](https://github.com/nokturno-app/nokturno-stremio-app/releases/latest)
   (v Downloaderi zadaj adresu `github.com/nokturno-app/nokturno-stremio-app/releases/latest`) a nainštaluj ho.
3. Otvor aplikáciu **Nokturno**. Ukáže adresy na nastavenie. Beží na pozadí s trvalým oznámením „Nokturno beží“,
   počúva na porte **7140** (a **7141** pre HTTPS) a po zapnutí zariadenia sa spustí sama. Po inštalácii ju
   raz otvor, inak ju Android po zapnutí nespustí.
4. Otvor nastavenie: na televízore priamo v aplikácii Nokturno (bez prehliadača sa formulár otvorí v nej), alebo
   pohodlnejšie z telefónu v rovnakej sieti na `http://<IP adresa televízora>:7140/configure`. IP adresu ukazuje
   hlavná obrazovka aplikácie.
5. Založ profil (napíš jeho názov a daj **Založiť nový profil**), potom vyplň [vlastné úložisko](vlastni-uloziste.md)
   a prípadne účty zdrojov a daj **✓ Overiť všetky účty**. Postup je v článku [Ako pridať Nokturno do Stremia alebo Nuvia](stremio-instalace.md).
6. **Pridať do Stremia** alebo **Pridať do Nuvia**. Na tom istom televízore to ide rovno z formulára v aplikácii,
   na ostatných zariadeniach v sieti z formulára otvoreného cez IP adresu.

## Počítač
Z [vydaní na GitHube](https://github.com/nokturno-app/nokturno-stremio-app/releases/latest) vyber súbor podľa systému:

| Zariadenie | Súbor |
|---|---|
| Windows 10 a 11 | `nokturno-<verzia>-windows-amd64.exe` |
| Mac s čipom Apple (M1 a novší) | `nokturno-<verzia>-macos-arm64` |
| Mac s procesorom Intel | `nokturno-<verzia>-macos-amd64` |
| Linux | `nokturno-<verzia>-linux-amd64` |

Spusti ho:
- **Windows:** spusti `.exe`. Na hlášku „Systém Windows ochránil váš počítač“ daj **Ďalšie informácie → Napriek tomu spustiť**.
  Bránu firewall povoľ pre **súkromné siete**. Od verzie 9.3.0 beží bez okna. Nájdeš ju ako ikonu mesiaca v oblasti oznámení vpravo dole (prípadne pod šípkou ^): dvojklik otvorí nastavenia, **Ukončiť** ju vypne.
  Aby bežala stále, aj po reštarte a bez prihlásenia (od verzie 9.5.0): ukonči aplikáciu v oblasti oznámení, v Príkazovom riadku v priečinku so stiahnutým súborom spusti `nokturno-<verzia>-windows-amd64.exe --install` a potvrď oprávnenie správcu. Aplikácia sa nainštaluje ako služba **Nokturno pro Stremio** (je v `services.msc`), sama si povolí bránu firewall, po páde sa reštartuje a nastavenia prenesie do `C:\ProgramData\Nokturno`. Odinštalovanie: `C:\ProgramData\Nokturno\nokturno.exe --uninstall` (nastavenia zostanú). Bez služby ide dať odkaz na `.exe` do priečinka `shell:startup` (`Win + R`).
- **macOS:** v Termináli `chmod +x nokturno-*-macos-*` a `xattr -d com.apple.quarantine nokturno-*-macos-*`,
  potom `./nokturno-<verzia>-macos-arm64`. Bez druhého príkazu spustenie zablokuje Gatekeeper, pretože aplikácia
  nie je podpísaná (ide to aj cez **Nastavenia systému → Súkromie a zabezpečenie → Napriek tomu otvoriť**).
  Aby bežala stále, aj po reštarte a bez prihlásenia (od verzie 9.5.0): `sudo ./nokturno-<verzia>-macos-arm64 --install`. Aplikácia sa nainštaluje ako služba do `/Library/Application Support/Nokturno` a okno Terminálu potom môžeš zavrieť. Odinštalovanie: `sudo "/Library/Application Support/Nokturno/nokturno" --uninstall`.
- **Linux:** `chmod +x nokturno-*-linux-*` a `./nokturno-<verzia>-linux-amd64`. Ako ju spúšťať ako službu,
  je v časti [Raspberry Pi a NAS](#raspberry-pi-a-nas).

Potom otvor `http://127.0.0.1:7140/configure`, vyplň vlastné úložisko, prípadne voliteľné účty zdrojov a daj **Pridať do Stremia** alebo
**Pridať do Nuvia**. Ostatné zariadenia v sieti otvoria `http://<IP adresa počítača>:7140/configure`, IP adresu
vypíše aplikácia pri štarte.

Doplnok funguje len vtedy, keď počítač beží a aplikácia je spustená. Na televízore a telefóne tiež.

## Home Assistant
Nokturno pre Stremio sa dá nainštalovať ako doplnok Home Assistantu (HA OS alebo Supervised, len 64bit systémy
amd64 a aarch64; Raspberry Pi s 32bit systémom nie). Beží potom doma stále, kým beží Home Assistant.

1. Pridaj úložisko doplnkov: [tlačidlom](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fnokturno-app%2Fnokturno-stremio-ha), alebo ručne **Nastavenia → Doplnky → Obchod s doplnkami → ⋮ →
   Úložiská** a vlož `https://github.com/nokturno-app/nokturno-stremio-ha`.
2. Nainštaluj **Nokturno pro Stremio** a daj **Spustiť**.
3. **Otvoriť webové rozhranie**, alebo z telefónu či počítača v rovnakej sieti `http://<IP Home Assistantu>:7140/configure`.
4. Založ profil s názvom, vyplň vlastné úložisko, prípadne voliteľné účty zdrojov, daj **✓ Overiť všetky účty** a potom **Pridať do Stremia** alebo **Pridať do Nuvia**.

Doplnok používa sieť hostiteľa: port **7140** (nastavenie a doplnok pre Nuvio) a **7141** (HTTPS cez local-ip.co
pre Stremio). V záložke **Konfigurácia** sa dajú vypnúť štatistiky (`stats`), hlásenia o pádoch (`crash_reports`)
a HTTPS (`enable_https`), zadať vlastný kľúč TMDB (`tmdb_key`). Nové verzie si doplnok sťahuje sám.
Home Assistantu nastav v routeri pevnú IP.

Popis doplnku a jeho zdrojový kód sú v repozitári
[nokturno-app/nokturno-stremio-ha](https://github.com/nokturno-app/nokturno-stremio-ha).

## Raspberry Pi a NAS
Platí pre Raspberry Pi, NAS s Linuxom a iný malý počítač so systemd. Aplikácia na ňom beží stále,
aj keď ostatné zariadenia vypneš.

1. Zisti architektúru príkazom `uname -m` a vyber súbor:

   | `uname -m` | Súbor |
   |---|---|
   | `aarch64` | `nokturno-<verzia>-linux-arm64` |
   | `armv7l`, `armv6l` | `nokturno-<verzia>-linux-arm` |
   | `x86_64` | `nokturno-<verzia>-linux-amd64` |

2. Stiahni ho a priprav používateľa a priečinok (číslo verzie nájdeš na stránke vydaní):

   ```bash
   sudo mkdir -p /opt/nokturno
   sudo curl -L -o /opt/nokturno/nokturno \
     https://github.com/nokturno-app/nokturno-stremio-app/releases/download/v<verzia>/nokturno-<verzia>-linux-arm64
   sudo chmod +x /opt/nokturno/nokturno
   sudo useradd --system --create-home --home-dir /var/lib/nokturno --shell /usr/sbin/nologin nokturno
   ```

3. Vytvor službu `/etc/systemd/system/nokturno.service`:

   ```ini
   [Unit]
   Description=Nokturno pre Stremio
   After=network-online.target
   Wants=network-online.target

   [Service]
   User=nokturno
   ExecStart=/opt/nokturno/nokturno --data /var/lib/nokturno
   Restart=always
   RestartSec=10

   [Install]
   WantedBy=multi-user.target
   ```

4. Zapni ju: `sudo systemctl daemon-reload` a `sudo systemctl enable --now nokturno`. Výpis uvidíš cez
   `journalctl -u nokturno -f`.
5. Z telefónu alebo počítača v rovnakej sieti otvor `http://<IP adresa zariadenia>:7140/configure`, vyplň úložisko
   alebo účty a daj **Pridať do Stremia** alebo **Pridať do Nuvia**.

Nastavenia aplikácie sú potom v `/var/lib/nokturno/nokturno.json`. Aktualizácie sa sťahujú do toho istého priečinka,
súbor `/opt/nokturno/nokturno` sa preto pri novej verzii meniť nemusí.

## Ako to rozbehnúť
### V domácej sieti
- **Stremio** prijme doplnok cez obyčajné `http` len z toho istého zariadenia. Na ostatných zariadeniach chce HTTPS.
  Keď formulár otvoríš cez IP adresu, dá do doplnku adresu `https://<IP s pomlčkami>.my.local-ip.co:7141` sám.
  Prečo, je vysvetlené nižšie v časti o adrese local-ip.co.
- **Nuvio** vezme aj adresu cez `http://<IP adresa>:7140`.
- Zariadeniu s aplikáciou nastav v routeri **pevnú IP** (rezervácia DHCP). Inak sa po reštarte routera adresa
  zmení a doplnok prestane fungovať.

### Mimo domova cez VPN
Aplikácia zostane doma, do internetu sa nič neotvára a zariadenia vonku (mobil, televízor u rodičov) sa k nej dostanú
cez Tailscale alebo inú VPN. Postup krok za krokom je v článku
[Nokturno pre Stremio mimo domova – Tailscale a VPN](stremio-mimo-domov.md).

### Mimo domova na vlastnej doméne
Adresa cez local-ip.co funguje len v domácej sieti. Kto chce doplnok aj na mobile mimo domova alebo na televízore
u rodičov, spustí aplikáciu na VPS s vlastnou doménou: [Nokturno pre Stremio na VPS s vlastnou doménou](stremio-vps.md).

Adresu doplnku nikomu neposielaj: heslá v nej od verzie 9.6.0 nie sú, ale kto ju má a dostane sa k aplikácii, používa tvoje účty. Podrobnosti o pridaní v článku
[Ako pridať Nokturno do Stremia alebo Nuvia](stremio-instalace.md).

## Heslo správcu a profily kamarátov
Od verzie 9.12.0 aplikácia spozná svojho majiteľa podľa **hesla správcu**, nie podľa siete. Funguje tak rovnako
doma, na VPS aj za vlastnou doménou.

**Prvé spustenie.** Keď heslo ešte nie je nastavené, stránka nastavení (`/configure`) ukáže len kartu
**Heslo správcu**. Zadaj heslo (aspoň 6 znakov) dvakrát a daj **Nastaviť heslo správcu**. Kto stránku otvorí
prvý, stane sa správcom. Na verejnej adrese (VPS, vlastná doména) ju preto otvor hneď po inštalácii.

**Čo vidí správca:**
- všetky profily v aplikácii, aj tie, ktoré si založili kamaráti,
- sekciu **⚙ Aplikácia**: prepínač profilov, zmena hesla správcu, odhlásenie a kontrola aktualizácií,
- povoľovanie zariadení.

**Čo vidia ostatní** (kamarát na zdieľanej inštancii, druhý člen domácnosti v inom prehliadači):
- heslo nepotrebujú, profil si založia a doplnok pridajú ako predtým,
- v zozname vidia len profily, ktoré si sami uložili v tomto prehliadači,
- sekciu Aplikácia ani cudzie profily neuvidia.

Doplnok v Stremiu ani v Nuviu heslo nechce, adresa doplnku sa nemení.

**Prihlásenie v inom prehliadači.** Dole na stránke nastavení rozbaľ **Si správca aplikácie? Prihlás sa**
a zadaj heslo. Prihlásenie vydrží rok.

**Zmena hesla.** V sekcii **⚙ Aplikácia** vyplň **Nové heslo správcu** a daj **Uložiť voľby aplikácie**.
Ostatné prihlásenia správcu tým skončia.

**Zabudnuté heslo.** V dátovom priečinku aplikácie otvor súbor `aplikace.json`, zmaž z neho položku
`spravce` a aplikáciu reštartuj. Potom ide heslo nastaviť znova. Dátový priečinok nájdeš v sekcii
[Nastavenia aplikácie a štatistiky](#nastavenia-aplikacie-a-statistiky), pri aplikácii pre Android sa k súboru
dostaneš len cez zmazanie dát aplikácie (zmiznú tým aj profily).

Po 20 zlých heslách za 10 minút aplikácia ďalšie pokusy na chvíľu odmieta.

## Aktualizácie
Aplikácia sa aktualizuje sama: pri štarte a potom každých 6 hodín. Novú verziu overí a keď nenabehne,
vráti predchádzajúcu. Na Androide sa aktualizácia sťahuje pri spustení aplikácie alebo po zapnutí zariadenia.
Nový inštalačný súbor sťahovať nemusíš.

Nechceš čakať? Na stránke nastavení (`/configure`) je dole v sekcii **⚙ Aplikácia** (od verzie 9.12.0 ju vidí len
[správca](#heslo-spravcu-a-profily-kamaratov)) tlačidlo **Skontrolovať aktualizácie** (od verzie 9.0.7). Ukáže nainštalovanú a najnovšiu verziu
a novšiu hneď stiahne. Rovnako poslúži reštart aplikácie: na počítači ju zavri a spusť znova,
na VPS `sudo systemctl restart nokturno`, v Home Assistante reštart doplnku, na Androide
zatvorenie a nové spustenie aplikácie.

## Časté problémy
| Čo sa deje | Čo urobiť |
|---|---|
| Nastavenie sa z iného zariadenia neotvorí | obe zariadenia musia byť v rovnakej sieti a aplikácia musí bežať. Na Windows povoľ aplikáciu vo firewalle pre súkromné siete (porty 7140 a 7141). |
| Stremio doplnok nepridá, adresa s `my.local-ip.co` nefunguje | router blokuje mená, ktoré vedú na domácu IP (ochrana proti DNS rebinding). Povoľ v routeri výnimku pre `local-ip.co`, alebo v zariadení so Stremiom nastav DNS `1.1.1.1`. |
| Doplnok prestal fungovať po reštarte routera | zmenila sa IP adresa zariadenia s aplikáciou. V routeri mu nastav pevnú IP (rezervácia DHCP) a doplnok pridaj znova. |
| Na Windows sa po dvojkliku na `.exe` len otvorí nastavenie | Nokturno už beží ako služba (`--install`), ďalšia kópia sa nespúšťa. |
| Pri štarte „Address already in use“ | port 7140 používa iný program. Spusti aplikáciu s `--port 7150 --https-port 7151`. |
| Stream s „⚠️ Vo webovom prehrávači sa neprehrá“ | riadok ukazuje len staršia aplikácia (do 9.6.0), aktualizuj ju; vo webovom prehrávači záleží na formáte súboru, pozri [„⚠️ Vo webovom prehrávači sa neprehrá“](stremio-webovy-prehravac.md) |
| Pri filme nie sú streamy | pozri [Pri filme nie sú streamy Nokturna](stremio-zadne-streamy.md) |

## Prečo adresa `https://…my.local-ip.co`
Stremio prijme doplnok cez obyčajné `http` len z toho istého zariadenia. Z iného zariadenia chce HTTPS s platným
certifikátom. Aplikácia preto otvorí aj port **7141** s adresou napríklad `https://192-168-1-10.my.local-ip.co:7141`.
Služba local-ip.co také meno preloží späť na tvoju domácu IP, dáta tečú len po tvojej sieti. Rovnako to robí Luna.
Keď nastavenie otvoríš cez IP adresu, formulár dá túto adresu do doplnku sám.

## Nastavenia aplikácie a štatistiky
Pri prvom spustení vznikne súbor `nokturno.json` (Windows `%APPDATA%\Nokturno`, ako služba Windows `C:\ProgramData\Nokturno`, ako služba macOS `/Library/Application Support/Nokturno`,
macOS `~/Library/Application Support/Nokturno`, Linux `~/.local/share/nokturno`, ako služba v priečinku
z parametra `--data`). V ňom sa dajú zmeniť porty, vypnúť HTTPS, zadať vlastný kľúč TMDB pre katalógy TMDB
(`tmdb_key`) a vypnúť anonymné štatistiky (`"stats": false`) a hlásenia o pádoch (`"crash_reports": false`).
Po úprave aplikáciu reštartuj.
Popis všetkých volieb je v [README aplikácie](https://github.com/nokturno-app/nokturno-stremio-app#nastavení-aplikace).

---
[Všetky návody](./) · [Česky](../cs/stremio-aplikace)
