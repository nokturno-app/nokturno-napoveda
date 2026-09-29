---
slug: stremio-vps
lang: cs
title: Nokturno pro Stremio na VPS s vlastní doménou
products: [stremio]
priority: 2
templates:
  stremio: |
    Aby doplněk fungoval i mimo domov, pusť aplikaci Nokturno na VPS s vlastní doménou a před ni dej Caddy s HTTPS.
    Adresa doplňku pak bude https://<tvoje doména>/c/…, nikomu ji neposílej.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/stremio-vps
---

# Nokturno pro Stremio na VPS s vlastní doménou

V domácí síti stačí aplikace na televizi, počítači nebo Raspberry Pi, viz
[Nokturno pro Stremio – aplikace](stremio-aplikace.md). Když chceš doplněk i na mobilu mimo domov nebo na
televizi u rodičů, pusť aplikaci na VPS s vlastní doménou. Stremio i Nuvio pak jen zadají adresu
`https://<tvoje doména>/…`.

Postup počítá s tím, že umíš pracovat v příkazové řádce Linuxu přes SSH.

## 1. VPS a doména
- **VPS** s Debianem nebo Ubuntu. Stačí 1 vCPU a 512 MB až 1 GB RAM. Soubory z VPS netečou, přehrávač si je
  stahuje přímo ze zdroje, takže na přenosu dat nezáleží.
- **Doména nebo subdoména** (třeba `nokturno.tvoje-domena.cz`) s **A záznamem** na veřejnou IP adresu VPS.
  Ověříš to příkazem `getent hosts nokturno.tvoje-domena.cz`, musí vypsat IP VPS.

## 2. Aplikace jako služba
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

## 3. Caddy a firewall
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

## 4. Přidání do Stremia a Nuvia
1. Otevři `https://nokturno.tvoje-domena.cz/configure`.
2. Vyplň [vlastní úložiště](vlastni-uloziste.md) a případně účty zdrojů, u každého dej **Ověřit**.
3. **Přidat do Stremia** nebo **Přidat do Nuvia**. Adresa doplňku začíná `https://nokturno.tvoje-domena.cz/c/…`.
   Na televizi se doplněk objeví sám, když ho přidáš na telefonu nebo počítači pod stejným účtem Stremio.

Vlastní úložiště doma musí být dosažitelné z VPS i ze zařízení, kde přehráváš, tedy přes veřejnou adresu
nebo VPN. Adresa v domácí síti (`192.168.…`) z VPS nefunguje.

## 5. Aktualizace a logy
- Aplikace se aktualizuje sama, při startu a pak každých 6 hodin. Nové verze stahuje do `/var/lib/nokturno`,
  soubor `/opt/nokturno/nokturno` se měnit nemusí. Když nová verze nenaběhne, vrátí předchozí.
- Výpis aplikace: `journalctl -u nokturno -f`, výpis Caddy: `journalctl -u caddy -f`.
- Systém VPS aktualizuj jako obvykle (`sudo apt update && sudo apt upgrade`).

## 6. Bezpečnost a soukromí
- **Adresa doplňku obsahuje tvoje nastavení a účty.** Není zašifrovaná, jen zakódovaná. Nikomu ji neposílej.
- **Instance je jen pro tebe.** Neprovozuj ji jako veřejnou službu pro cizí lidi. Kdo zná adresu tvé domény,
  může si ve formuláři vyrobit vlastní doplněk a hledat přes tvůj server, proto doménu nikde nezveřejňuj.
- **Heslo na celou doménu** (basic auth v Caddy) nedávej. Stremio ani Nuvio jsme s doplňkem za heslem
  neověřovali a doplněk by nejspíš přestal fungovat.
- **Statistiky** vypneš v `nokturno.json`: `"stats": false`, hlášení o pádech `"crash_reports": false`.
  Pak aplikaci restartuj: `sudo systemctl restart nokturno`. Účty ani adresa doplňku se neposílají nikdy.
- Na VPS se přihlašuj **SSH klíčem**, ne heslem.

## 7. Časté problémy
| Co se děje | Co udělat |
|---|---|
| `https://…/configure` se neotevře, Caddy hlásí chybu certifikátu | doména ještě neukazuje na VPS. Počkej, až `getent hosts <doména>` vypíše IP VPS (obvykle minuty, výjimečně hodiny), pak `sudo systemctl reload caddy`. |
| Certifikát se nevydá ani po změně DNS | Let's Encrypt potřebuje dosáhnout na porty **80** a 443. Zkontroluj `sudo ufw status` a firewall v administraci VPS. Důvod vypíše `journalctl -u caddy`. |
| Caddy hlásí „502 Bad Gateway“ | aplikace neběží. `sudo systemctl status nokturno` a `journalctl -u nokturno`. |
| U filmu nejsou streamy | viz [U filmu nejsou streamy Nokturna](stremio-zadne-streamy.md) |

---
[Všechny návody](../) · [Slovensky](../sk/stremio-vps)
