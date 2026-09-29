---
slug: stremio-aplikace
lang: cs
title: Nokturno pro Stremio – aplikace
products: [stremio]
priority: 0
templates:
  stremio: |
    Nokturno pro Stremio je aplikace, kterou si pustíš u sebe (Android TV box, počítač, Raspberry Pi, NAS).
    Stáhni ji z github.com/nokturno-app/nokturno-stremio-app/releases, spusť a otevři http://<IP zařízení>:7140/configure.
    Doplněk na cizím serveru dostává tvoje přihlašovací údaje ke zdrojům. Když běží u tebe, nedostane je nikdo jiný.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/stremio-aplikace
---

# Nokturno pro Stremio – aplikace

!!! warning "Přihlašovací údaje jsou v adrese doplňku"
    Každý doplněk pro Stremio, který běží na cizím serveru, dostává tvoje přihlašovací údaje ke zdrojům
    (WebShare, FastShare, Přehraj.to…). Jsou totiž v adrese doplňku a s každým požadavkem procházejí přes ten
    server. Jeho provozovatel je tak může vidět a uložit a musíš mu věřit. Jistotu, že je nemá nikdo jiný,
    máš jen tehdy, když doplněk běží u tebe: na televizi, počítači, Raspberry Pi nebo na vlastním VPS.

Nokturno pro Stremio a Nuvio je malá aplikace, která běží **u tebe**. Stremio i Nuvio pak jen zadají adresu
doplňku a ptají se aplikace jako každého jiného doplňku. Aplikace musí běžet, kdykoli se díváš.

## Kde ji pustit
| Co máš | Kde aplikace běží | Postup |
|---|---|---|
| Android TV, Google TV nebo Android box | přímo na televizi nebo boxu | [Android TV a Android box](#android-tv-a-android-box) |
| Počítač s Windows, macOS nebo Linuxem | na počítači, doplněk funguje jen, když počítač běží | [Počítač](#pocitac) |
| Home Assistant | – | [připravujeme](#home-assistant) |
| Raspberry Pi, NAS nebo jiný malý linuxový počítač | na něm, běží pořád | [Raspberry Pi a NAS](#raspberry-pi-a-nas) |
| VPS s vlastní doménou, přístup odkudkoli | na VPS | [Nokturno pro Stremio na VPS s vlastní doménou](stremio-vps.md) |

Nejlíp je pustit aplikaci na zařízení, které je pořád zapnuté (box, Raspberry Pi, NAS), nebo přímo na tom,
kde Stremio pouštíš.

## Android TV a Android box
1. Povol instalaci z neznámých zdrojů pro aplikaci, přes kterou APK dostaneš do televize, například
   **Downloader** nebo **Send files to TV**.
2. Stáhni `nokturno-<verze>.apk` z [vydání na GitHubu](https://github.com/nokturno-app/nokturno-stremio-app/releases/latest)
   (v Downloaderu zadej adresu `github.com/nokturno-app/nokturno-stremio-app/releases/latest`) a nainstaluj ho.
3. Otevři aplikaci **Nokturno**. Ukáže adresy pro nastavení. Běží na pozadí s trvalým oznámením „Nokturno běží“,
   poslouchá na portu **7140** (a **7141** pro HTTPS) a po zapnutí zařízení se spustí sama. Po instalaci ji
   jednou otevři, jinak ji Android po zapnutí nespustí.
4. Otevři nastavení: na televizi přímo v aplikaci Nokturno (bez prohlížeče se formulář otevře v ní), nebo
   pohodlněji z telefonu ve stejné síti na `http://<IP adresa televize>:7140/configure`. IP adresu ukazuje
   hlavní obrazovka aplikace.
5. Vyplň [vlastní úložiště](vlastni-uloziste.md) a případně účty zdrojů, u každého dej **Ověřit**.
6. **Přidat do Stremia** nebo **Přidat do Nuvia**. Na téže televizi to jde rovnou z formuláře v aplikaci,
   na ostatních zařízeních v síti z formuláře otevřeného přes IP adresu.

## Počítač
Z [vydání na GitHubu](https://github.com/nokturno-app/nokturno-stremio-app/releases/latest) vyber soubor podle systému:

| Zařízení | Soubor |
|---|---|
| Windows 10 a 11 | `nokturno-<verze>-windows-amd64.exe` |
| Mac s čipem Apple (M1 a novější) | `nokturno-<verze>-macos-arm64` |
| Mac s procesorem Intel | `nokturno-<verze>-macos-amd64` |
| Linux | `nokturno-<verze>-linux-amd64` |

Spusť ho:
- **Windows:** spusť `.exe`. Na hlášku „Systém Windows ochránil váš počítač“ dej **Další informace → Přesto spustit**.
  Bránu firewall povol pro **soukromé sítě**. Okno s výpisem nech otevřené, jeho zavřením aplikaci vypneš.
- **macOS:** v Terminálu `chmod +x nokturno-*-macos-*` a `xattr -d com.apple.quarantine nokturno-*-macos-*`,
  pak `./nokturno-<verze>-macos-arm64`. Bez druhého příkazu spuštění zablokuje Gatekeeper, protože aplikace
  není podepsaná (jde to i přes **Nastavení systému → Soukromí a zabezpečení → Přesto otevřít**).
- **Linux:** `chmod +x nokturno-*-linux-*` a `./nokturno-<verze>-linux-amd64`. Jak ji pouštět jako službu,
  je v části [Raspberry Pi a NAS](#raspberry-pi-a-nas).

Pak otevři `http://127.0.0.1:7140/configure`, vyplň úložiště nebo účty a dej **Přidat do Stremia** nebo
**Přidat do Nuvia**. Ostatní zařízení v síti otevřou `http://<IP adresa počítače>:7140/configure`, IP adresu
vypíše aplikace při startu.

Doplněk funguje jen, když počítač běží a aplikace je spuštěná. Na televizi a telefonu taky.

## Home Assistant
Doplněk pro Home Assistant připravujeme. Zatím aplikaci pusť na jiném zařízení v síti, například na Android TV
boxu nebo Raspberry Pi.

## Raspberry Pi a NAS
Platí pro Raspberry Pi, NAS s Linuxem a jiný malý počítač se systemd. Aplikace na něm běží pořád,
i když ostatní zařízení vypneš.

1. Zjisti architekturu příkazem `uname -m` a vyber soubor:

   | `uname -m` | Soubor |
   |---|---|
   | `aarch64` | `nokturno-<verze>-linux-arm64` |
   | `armv7l`, `armv6l` | `nokturno-<verze>-linux-arm` |
   | `x86_64` | `nokturno-<verze>-linux-amd64` |

2. Stáhni ho a připrav uživatele a složku (číslo verze najdeš na stránce vydání):

   ```bash
   sudo mkdir -p /opt/nokturno
   sudo curl -L -o /opt/nokturno/nokturno \
     https://github.com/nokturno-app/nokturno-stremio-app/releases/download/v<verze>/nokturno-<verze>-linux-arm64
   sudo chmod +x /opt/nokturno/nokturno
   sudo useradd --system --create-home --home-dir /var/lib/nokturno --shell /usr/sbin/nologin nokturno
   ```

3. Vytvoř službu `/etc/systemd/system/nokturno.service`:

   ```ini
   [Unit]
   Description=Nokturno pro Stremio
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

4. Zapni ji: `sudo systemctl daemon-reload` a `sudo systemctl enable --now nokturno`. Výpis uvidíš přes
   `journalctl -u nokturno -f`.
5. Z telefonu nebo počítače ve stejné síti otevři `http://<IP adresa zařízení>:7140/configure`, vyplň úložiště
   nebo účty a dej **Přidat do Stremia** nebo **Přidat do Nuvia**.

Nastavení aplikace je pak v `/var/lib/nokturno/nokturno.json`. Aktualizace se stahují do téže složky,
soubor `/opt/nokturno/nokturno` se proto při nové verzi měnit nemusí.

## Jak to rozjet
### V domácí síti
- **Stremio** přijme doplněk přes obyčejné `http` jen z téhož zařízení. Na ostatních zařízeních chce HTTPS.
  Když formulář otevřeš přes IP adresu, dá do doplňku adresu `https://<IP s pomlčkami>.my.local-ip.co:7141` sám,
  Proč, je vysvětleno níž v části o adrese local-ip.co.
- **Nuvio** vezme i adresu přes `http://<IP adresa>:7140`.
- Zařízení s aplikací nastav v routeru **pevnou IP** (rezervace DHCP). Jinak se po restartu routeru adresa
  změní a doplněk přestane fungovat.

### Mimo domov přes VPN
Aplikace zůstane doma, do internetu se nic neotevírá a zařízení venku (mobil, televize u rodičů) se k ní dostane
přes soukromou síť mezi tvými zařízeními. Nejjednodušší je [Tailscale](https://tailscale.com), jde to i přes
WireGuard nebo VPN v routeru. Tailscale musí běžet na zařízení s aplikací i na zařízení, kde přehráváš
(pro Android TV je aplikace Tailscale v obchodě Google Play).

- **Nuvio** stačí adresa přes `http://<adresa 100.x.y.z zařízení s aplikací>:7140`.
- **Stremio** chce u vzdáleného doplňku HTTPS. Spolehlivě to zařídí `tailscale serve` na zařízení s aplikací
  (v administraci Tailscale musí být zapnuté MagicDNS a HTTPS certifikáty):

  ```bash
  tailscale serve --bg --https=443 http://127.0.0.1:7140
  ```

  Nastavení pak otevři na `https://<zařízení>.<tailnet>.ts.net/configure` a doplněk přidej odtud. Adresa platí
  jen uvnitř tvého tailnetu. Vypneš to příkazem `tailscale serve --bg --https=443 off`.
- Adresa přes local-ip.co s adresou Tailscale (`https://100-x-y-z.my.local-ip.co:7141`) může fungovat taky,
  formulář ji ale sám nenabídne a některé routery nebo DNS takové jméno zablokují.
- **Tailscale Funnel nepoužívej.** Zveřejnil by aplikaci celému internetu.

### Mimo domov na vlastní doméně
Adresa přes local-ip.co funguje jen v domácí síti. Kdo chce doplněk i na mobilu mimo domov nebo na televizi
u rodičů, pustí aplikaci na VPS s vlastní doménou: [Nokturno pro Stremio na VPS s vlastní doménou](stremio-vps.md).

Adresa doplňku obsahuje tvoje účty. Nikomu ji neposílej. Podrobnosti o přidání v článku
[Jak přidat Nokturno do Stremia nebo Nuvia](stremio-instalace.md).

## Aktualizace
Aplikace se aktualizuje sama: při startu a pak každých 6 hodin. Novou verzi ověří a když nenaběhne,
vrátí předchozí. Na Androidu se aktualizace stahuje při spuštění aplikace nebo po zapnutí zařízení.
Nový instalační soubor stahovat nemusíš.

## Časté problémy
| Co se děje | Co udělat |
|---|---|
| Nastavení se z jiného zařízení neotevře | obě zařízení musí být ve stejné síti a aplikace musí běžet. Na Windows povol aplikaci ve firewallu pro soukromé sítě (porty 7140 a 7141). |
| Stremio doplněk nepřidá, adresa s `my.local-ip.co` nefunguje | router blokuje jména, která vedou na domácí IP (ochrana proti DNS rebinding). Povol v routeru výjimku pro `local-ip.co`, nebo v zařízení se Stremiem nastav DNS `1.1.1.1`. |
| Doplněk přestal fungovat po restartu routeru | změnila se IP adresa zařízení s aplikací. V routeru mu nastav pevnou IP (rezervace DHCP) a doplněk přidej znovu. |
| Při startu „Address already in use“ | port 7140 používá jiný program. Spusť aplikaci s `--port 7150 --https-port 7151`. |
| Stream s „⚠️ Ve webovém přehrávači se nepřehraje“ | hraje jen v aplikaci Stremio nebo Nuvio, viz [„⚠️ Ve webovém přehrávači se nepřehraje“](stremio-webovy-prehravac.md) |
| U filmu nejsou streamy | viz [U filmu nejsou streamy Nokturna](stremio-zadne-streamy.md) |

## Proč adresa `https://…my.local-ip.co`
Stremio přijme doplněk přes obyčejné `http` jen z téhož zařízení. Z jiného zařízení chce HTTPS s platným
certifikátem. Aplikace proto otevře i port **7141** s adresou třeba `https://192-168-1-10.my.local-ip.co:7141`.
Služba local-ip.co takové jméno přeloží zpátky na tvoji domácí IP, data tečou jen po tvé síti. Stejně to dělá Luna.
Když nastavení otevřeš přes IP adresu, formulář dá tuhle adresu do doplňku sám.

## Nastavení aplikace a statistiky
Při prvním spuštění vznikne soubor `nokturno.json` (Windows `%APPDATA%\Nokturno`,
macOS `~/Library/Application Support/Nokturno`, Linux `~/.local/share/nokturno`, jako služba ve složce
z parametru `--data`). V něm jde změnit porty, vypnout HTTPS, zadat vlastní klíč TMDB pro katalogy TMDB
(`tmdb_key`) a vypnout anonymní statistiky (`"stats": false`) a hlášení o pádech (`"crash_reports": false`).
Po úpravě aplikaci restartuj.
Popis všech voleb je v [README aplikace](https://github.com/nokturno-app/nokturno-stremio-app#nastavení-aplikace).

---
[Všechny návody](../) · [Slovensky](../sk/stremio-aplikace)
