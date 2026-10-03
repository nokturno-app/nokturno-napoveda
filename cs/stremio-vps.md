---
slug: stremio-vps
lang: cs
title: Nokturno pro Stremio na VPS s vlastní doménou
products: [stremio]
priority: 2
templates:
  stremio: |
    Aby doplněk fungoval i mimo domov, pusť aplikaci Nokturno na VPS s vlastní doménou. Instalace jedním příkazem:
    curl -fsSL https://raw.githubusercontent.com/nokturno-app/nokturno-stremio-app/main/install.sh | sudo bash -s -- --domain <tvoje doména>
    Instance je jen pro tebe, adresu doplňku ani doménu nikomu nedávej.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/stremio-vps
---

# Nokturno pro Stremio na VPS s vlastní doménou

V domácí síti stačí aplikace na televizi, počítači nebo Raspberry Pi, viz
[Nokturno pro Stremio – aplikace](stremio-aplikace.md). Mimo domov se k ní dostaneš i bez VPS, přes Tailscale
nebo jinou VPN, viz [Nokturno pro Stremio mimo domov – Tailscale a VPN](stremio-mimo-domov.md).
Když chceš doplněk na mobilu nebo televizi bez VPN, pusť aplikaci na vlastním VPS s vlastní doménou.
Stremio i Nuvio pak jen zadají adresu `https://<tvoje doména>/…`.

Instance na VPS je ve výchozím stavu **osobní**: je pro tebe a tvou domácnost. Adresu doplňku ani doménu nikomu nedávej
a provoz pro cizí lidi nedělej. Výjimku tvoří sekce „Nastavení pro kamarády“ níž, kterou zapneš jen vědomě.

Postup počítá s tím, že umíš pracovat v příkazové řádce Linuxu přes SSH.

## Kde vzít VPS a doménu
### VPS
Stačí nejmenší VPS s **1 vCPU, 1 GB RAM** a systémem **Debian 12** nebo **Ubuntu 24.04**. Pár příkladů
poskytovatelů, ceny jsou orientační, ověř je na webu poskytovatele. S žádným z nich nejsme nijak spojeni.

| Poskytovatel | Orientační cena | Poznámka |
|---|---|---|
| Hetzner Cloud (nejmenší stroj řady CX nebo CAX, třeba CX22 nebo CAX11) | kolem 4 € měsíčně | datacentra v EU, CAX je procesor ARM |
| Contabo | kolem 5 € měsíčně | víc RAM a disku za podobnou cenu |
| Oracle Cloud Always Free | zdarma | stroj s procesorem ARM, registrace je složitější, chce platební kartu a volná kapacita někdy chybí |
| WEDOS (VPS ON), Forpsi | podle konfigurace | české, s administrací a podporou v češtině |

### Stačí nejlevnější VPS?
Ano, s velkou rezervou. Data filmu přes VPS u většiny zdrojů neteče, přehrávač si soubor stahuje přímo ze zdroje. Server hledá
a vrací seznam streamů. Soubory z vlastního úložiště a FastShare ale tečou přes VPS, počítej proto s jeho přenosem dat. Z měření: aplikace si bere zhruba 250 MB RAM a na jednom jádře zvládla i tisíce hledání
denně při zhruba 5 % vytížení procesoru. Pro tebe a tvou domácnost je to víc než dost.

Omezení je jinde než ve výkonu: všechno hledání jde z jedné IP adresy VPS a zdroje můžou IP, ze které přichází
hodně dotazů, omezit nebo zablokovat. I proto je instance osobní, adresu doplňku ani doménu nikomu nedávej.

### Doména
- **Vlastní doména nebo subdoména** od libovolného registrátora (třeba `nokturno.tvoje-domena.cz`)
  s **A záznamem** na veřejnou IP adresu VPS.
- **Zdarma:** subdoména od [DuckDNS](https://www.duckdns.org) (třeba `tvoje-jmeno.duckdns.org`). VPS má
  veřejnou IP, stačí ji v DuckDNS nastavit jednou.

Ověříš to příkazem `getent hosts nokturno.tvoje-domena.cz`, musí vypsat IP VPS.

## Instalace jedním příkazem
Na VPS se přihlas přes SSH a spusť:

```bash
sudo apt install -y curl ufw
curl -fsSL https://raw.githubusercontent.com/nokturno-app/nokturno-stremio-app/main/install.sh | sudo bash -s -- --domain nokturno.tvoje-domena.cz
```

Skript:
- pozná architekturu, stáhne aplikaci z posledního vydání a ověří její otisk SHA-256;
- založí systémového uživatele `nokturno` a službu `nokturno` (aplikace v `/opt/nokturno/nokturno`,
  nastavení a data v `/opt/nokturno/data`);
- nainstaluje [Caddy](https://caddyserver.com), který před aplikací zajistí HTTPS s certifikátem Let's Encrypt;
- když je nainstalovaný firewall `ufw`, povolí porty 22, 80 a 443 a zapne ho (proto ho první řádek instaluje);
- zkontroluje, že doména míří na tento server, a na konci vypíše adresu nastavení.

Aplikace pak poslouchá jen na `127.0.0.1` a zvenku je dostupná jen přes Caddy. Tuhle izolaci umí aplikace
od verze 9.0.4. Se starší verzí poslouchá na všech rozhraních, skript její port ve firewallu nepovolí a na konci
na to upozorní. Když má poskytovatel VPS vlastní firewall v administraci, povol v něm jen porty 22, 80 a 443.

| Přepínač | Co dělá |
|---|---|
| `--domain DOMÉNA` | instalace s doménou a Caddy |
| `--port 7140` | jiný port aplikace |
| `--no-firewall` | na `ufw` nesahá |
| `--uninstall` | odstraní službu, aplikaci a konfiguraci Caddy pro Nokturno, data nechá v `/opt/nokturno/data` |

**Aktualizace:** aplikace se aktualizuje sama. Nový soubor aplikace stáhne i opětovné spuštění téhož příkazu,
doménu a port si skript pamatuje a nastavení zachová. **Odinstalace:** stejný příkaz s `--uninstall`
místo `--domain …`.

Stav služby: `systemctl status nokturno`, výpis: `journalctl -u nokturno -f`.

## Ruční instalace
Když chceš mít každý krok pod kontrolou, jde to i bez skriptu.

### Aplikace jako služba
Zjisti architekturu VPS příkazem `uname -m`: `x86_64` = soubor `linux-amd64`, `aarch64` = `linux-arm64`.
Číslo poslední verze najdeš na [stránce vydání](https://github.com/nokturno-app/nokturno-stremio-app/releases/latest).

```bash
sudo mkdir -p /opt/nokturno
sudo curl -L -o /opt/nokturno/nokturno \
  https://github.com/nokturno-app/nokturno-stremio-app/releases/download/v<verze>/nokturno-<verze>-linux-amd64
sudo chmod +x /opt/nokturno/nokturno
sudo useradd --system --create-home --home-dir /var/lib/nokturno --shell /usr/sbin/nologin nokturno
```

Nastavení aplikace `/var/lib/nokturno/nokturno.json`. HTTPS řeší Caddy, vlastní HTTPS přes local-ip.co
proto vypni (`enable_https`). Statistiky a hlášení o pádech jsou volitelné:

```json
{
  "port": 7140,
  "enable_https": false,
  "stats": true,
  "crash_reports": true
}
```

Nastav vlastníka: `sudo chown nokturno: /var/lib/nokturno/nokturno.json`.

Služba `/etc/systemd/system/nokturno.service`:

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

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now nokturno
curl http://127.0.0.1:7140/health
```

Poslední příkaz musí odpovědět. Aplikace poslouchá na všech rozhraních, port **7140** proto ven neotevírej,
zavře ho firewall v dalším kroku.

### Caddy a firewall
Caddy se postará o HTTPS certifikát od Let's Encrypt sám.

```bash
sudo apt install caddy
```

Obsah `/etc/caddy/Caddyfile` nahraď:

```
nokturno.tvoje-domena.cz {
	reverse_proxy 127.0.0.1:7140
}
```

```bash
sudo systemctl reload caddy
```

Firewall (ufw) pustí dovnitř jen SSH a web:

```bash
sudo apt install ufw
sudo ufw default deny incoming
sudo ufw allow OpenSSH
sudo ufw allow 80,443/tcp
sudo ufw enable
```

Když má poskytovatel VPS vlastní firewall v administraci, povol v něm taky porty 80 a 443.

## Přidání do Stremia a Nuvia
1. Otevři `https://nokturno.tvoje-domena.cz/configure` hned po instalaci a nastav
   [heslo správce](stremio-aplikace.md#heslo-spravce-a-profily-kamaradu). Kdo stránku otevře první, stane se správcem.
2. Založ profil s názvem, viz [Nastavení a přidání do Stremia](stremio-instalace.md).
3. Vyplň [vlastní úložiště](vlastni-uloziste.md) a případně účty zdrojů, u každého dej **Ověřit**.
4. **Přidat do Stremia** nebo **Přidat do Nuvia**. Adresa doplňku začíná `https://nokturno.tvoje-domena.cz/c/p…`.
   Na televizi se doplněk objeví sám, když ho přidáš na telefonu nebo počítači pod stejným účtem Stremio.

Vlastní úložiště doma musí být dosažitelné z VPS (přehrávač jde přes VPS), tedy přes veřejnou adresu
nebo VPN. Adresa v domácí síti (`192.168.…`) z VPS nefunguje.

## Aktualizace a logy
- Aplikace se aktualizuje sama, při startu a pak každých 6 hodin. Nové verze stahuje do složky s daty,
  soubor `/opt/nokturno/nokturno` se měnit nemusí. Když nová verze nenaběhne, vrátí předchozí.
- Při instalaci skriptem stáhne nový soubor aplikace i opětovné spuštění téhož příkazu.
- Výpis aplikace: `journalctl -u nokturno -f`, výpis Caddy: `journalctl -u caddy -f`.
- Systém VPS aktualizuj jako obvykle (`sudo apt update && sudo apt upgrade`).

## Nastavení pro kamarády
Od verze 9.7.0 jde na instanci s veřejnou adresou zpřístupnit stránku nastavení i z internetu. Kamarád si pak
na `https://<tvoje doména>/configure` založí **vlastní profil se svými účty** a doplněk přidá do svého Stremia.
Od verze 9.12.0 vidí jen profily, které si uložil ve svém prohlížeči. Všechny profily, povolování zařízení
a aktualizace vidí jen [správce](stremio-aplikace.md#heslo-spravce-a-profily-kamaradu) přihlášený heslem.

Zapneš to volbou `"sdilena": true` v `nokturno.json` (vedle `"port"`, `"stats"` a dalších; `/opt/nokturno/data`
při instalaci skriptem, `/var/lib/nokturno` při ruční instalaci). Pak aplikaci restartuj:
`sudo systemctl restart nokturno`. Výchozí hodnota je `false`.

Než to zapneš, počítej s tímhle:
- **Bez přihlášení kamarádů.** Kamarád heslo nepotřebuje. Kdo zná doménu, může si založit profil a hledat přes tvůj
  server. Cizí profily od verze 9.12.0 neuvidí. Doménu dávej jen lidem, kterým věříš.
- **Jedna IP.** Všechno hledání jde z IP tvého VPS, zdroje mohou IP s mnoha dotazy omezit.
- **Přenos dat.** Soubory z vlastního úložiště a FastShare tečou přes VPS.

## Bezpečnost a soukromí
- **Adresa doplňku neobsahuje hesla ani nastavení**, jen náhodný klíč profilu (`/c/p<klíč>/manifest.json`).
  Kdo adresu má a dostane se k aplikaci, přesto používá tvoje účty, proto ji dál nikomu neposílej.
- **Instance je ve výchozím stavu jen pro tebe.** Neprovozuj ji jako veřejnou službu pro cizí lidi (výjimka viz výš). Kdo zná adresu tvé domény,
  může si ve formuláři vyrobit vlastní doplněk a hledat přes tvůj server, proto doménu nikde nezveřejňuj.
- **Heslo na celou doménu** (basic auth v Caddy) nedávej. Stremio ani Nuvio jsme s doplňkem za heslem
  neověřovali a doplněk by nejspíš přestal fungovat.
- **Statistiky** vypneš v `nokturno.json` (`/opt/nokturno/data` při instalaci skriptem, `/var/lib/nokturno`
  při ruční instalaci): `"stats": false`, hlášení o pádech `"crash_reports": false`.
  Pak aplikaci restartuj: `sudo systemctl restart nokturno`. Účty ani adresa doplňku se neposílají nikdy.
- Na VPS se přihlašuj **SSH klíčem**, ne heslem.

## Časté problémy
| Co se děje | Co udělat |
|---|---|
| `https://…/configure` se neotevře, Caddy hlásí chybu certifikátu | doména ještě neukazuje na VPS. Počkej, až `getent hosts <doména>` vypíše IP VPS (obvykle minuty, výjimečně hodiny), pak `sudo systemctl reload caddy`. |
| Certifikát se nevydá ani po změně DNS | Let's Encrypt potřebuje dosáhnout na porty **80** a 443. Zkontroluj `sudo ufw status` a firewall v administraci VPS. Důvod vypíše `journalctl -u caddy`. |
| Caddy hlásí „502 Bad Gateway“ | aplikace neběží. `sudo systemctl status nokturno` a `journalctl -u nokturno`. |
| U filmu nejsou streamy | viz [U filmu nejsou streamy Nokturna](stremio-zadne-streamy.md) |

---
[Všechny návody](../) · [Slovensky](../sk/stremio-vps)
