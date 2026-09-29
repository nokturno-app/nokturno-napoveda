---
slug: stremio-vps
lang: sk
title: Nokturno pre Stremio na VPS s vlastnou doménou
products: [stremio]
priority: 2
templates:
  stremio: |
    Aby doplnok fungoval aj mimo domova, spusti aplikáciu Nokturno na VPS s vlastnou doménou a pred ňu daj Caddy s HTTPS.
    Adresa doplnku potom bude https://<tvoja doména>/c/…, nikomu ju neposielaj.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/stremio-vps
---

# Nokturno pre Stremio na VPS s vlastnou doménou

V domácej sieti stačí aplikácia na televízore, počítači alebo Raspberry Pi, pozri
[Nokturno pre Stremio – aplikácia](stremio-aplikace.md). Keď chceš doplnok aj na mobile mimo domova alebo na
televízore u rodičov, spusti aplikáciu na VPS s vlastnou doménou. Stremio aj Nuvio potom len zadajú adresu
`https://<tvoja doména>/…`.

Postup počíta s tým, že vieš pracovať v príkazovom riadku Linuxu cez SSH.

## 1. VPS a doména
- **VPS** s Debianom alebo Ubuntu. Stačí 1 vCPU a 512 MB až 1 GB RAM. Súbory z VPS netečú, prehrávač si ich
  sťahuje priamo zo zdroja, takže na prenose dát nezáleží.
- **Doména alebo subdoména** (napríklad `nokturno.tvoja-domena.sk`) s **A záznamom** na verejnú IP adresu VPS.
  Overíš to príkazom `getent hosts nokturno.tvoja-domena.sk`, musí vypísať IP VPS.

## 2. Aplikácia ako služba
Zisti architektúru VPS príkazom `uname -m`: `x86_64` = súbor `linux-amd64`, `aarch64` = `linux-arm64`.
Číslo poslednej verzie nájdeš na [stránke vydaní](https://github.com/nokturno-app/nokturno-stremio-app/releases/latest).

```bash
sudo mkdir -p /opt/nokturno
sudo curl -L -o /opt/nokturno/nokturno \
  https://github.com/nokturno-app/nokturno-stremio-app/releases/download/v<verzia>/nokturno-<verzia>-linux-amd64
sudo chmod +x /opt/nokturno/nokturno
sudo useradd --system --create-home --home-dir /var/lib/nokturno --shell /usr/sbin/nologin nokturno
```

Nastavenia aplikácie `/var/lib/nokturno/nokturno.json`. HTTPS rieši Caddy, vlastné HTTPS cez local-ip.co
preto vypni (`enable_https`). Štatistiky a hlásenia o pádoch sú voliteľné:

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

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now nokturno
curl http://127.0.0.1:7140/health
```

Posledný príkaz musí odpovedať. Aplikácia počúva na všetkých rozhraniach, port **7140** preto von neotváraj,
zavrie ho firewall v ďalšom kroku.

## 3. Caddy a firewall
Caddy sa o HTTPS certifikát od Let's Encrypt postará sám.

```bash
sudo apt install caddy
```

Obsah `/etc/caddy/Caddyfile` nahraď:

```
nokturno.tvoja-domena.sk {
	reverse_proxy 127.0.0.1:7140
}
```

```bash
sudo systemctl reload caddy
```

Firewall (ufw) pustí dnu len SSH a web:

```bash
sudo apt install ufw
sudo ufw default deny incoming
sudo ufw allow OpenSSH
sudo ufw allow 80,443/tcp
sudo ufw enable
```

Keď má poskytovateľ VPS vlastný firewall v administrácii, povoľ v ňom tiež porty 80 a 443.

## 4. Pridanie do Stremia a Nuvia
1. Otvor `https://nokturno.tvoja-domena.sk/configure`.
2. Vyplň [vlastné úložisko](vlastni-uloziste.md) a prípadne účty zdrojov, pri každom daj **Overiť**.
3. **Pridať do Stremia** alebo **Pridať do Nuvia**. Adresa doplnku začína `https://nokturno.tvoja-domena.sk/c/…`.
   Na televízore sa doplnok objaví sám, keď ho pridáš na telefóne alebo počítači pod rovnakým účtom Stremio.

Vlastné úložisko doma musí byť dosiahnuteľné z VPS aj zo zariadenia, kde prehrávaš, teda cez verejnú adresu
alebo VPN. Adresa v domácej sieti (`192.168.…`) z VPS nefunguje.

## 5. Aktualizácie a logy
- Aplikácia sa aktualizuje sama, pri štarte a potom každých 6 hodín. Nové verzie sťahuje do `/var/lib/nokturno`,
  súbor `/opt/nokturno/nokturno` sa meniť nemusí. Keď nová verzia nenabehne, vráti predchádzajúcu.
- Výpis aplikácie: `journalctl -u nokturno -f`, výpis Caddy: `journalctl -u caddy -f`.
- Systém VPS aktualizuj ako obvykle (`sudo apt update && sudo apt upgrade`).

## 6. Bezpečnosť a súkromie
- **Adresa doplnku obsahuje tvoje nastavenia a účty.** Nie je zašifrovaná, len zakódovaná. Nikomu ju neposielaj.
- **Inštancia je len pre teba.** Neprevádzkuj ju ako verejnú službu pre cudzích ľudí. Kto pozná adresu tvojej domény,
  môže si vo formulári vyrobiť vlastný doplnok a hľadať cez tvoj server, preto doménu nikde nezverejňuj.
- **Heslo na celú doménu** (basic auth v Caddy) nedávaj. Stremio ani Nuvio sme s doplnkom za heslom
  neoverovali a doplnok by pravdepodobne prestal fungovať.
- **Štatistiky** vypneš v `nokturno.json`: `"stats": false`, hlásenia o pádoch `"crash_reports": false`.
  Potom aplikáciu reštartuj: `sudo systemctl restart nokturno`. Účty ani adresa doplnku sa neposielajú nikdy.
- Na VPS sa prihlasuj **SSH kľúčom**, nie heslom.

## 7. Časté problémy
| Čo sa deje | Čo urobiť |
|---|---|
| `https://…/configure` sa neotvorí, Caddy hlási chybu certifikátu | doména ešte neukazuje na VPS. Počkaj, kým `getent hosts <doména>` vypíše IP VPS (obvykle minúty, výnimočne hodiny), potom `sudo systemctl reload caddy`. |
| Certifikát sa nevydá ani po zmene DNS | Let's Encrypt potrebuje dosiahnuť na porty **80** a 443. Skontroluj `sudo ufw status` a firewall v administrácii VPS. Dôvod vypíše `journalctl -u caddy`. |
| Caddy hlási „502 Bad Gateway“ | aplikácia nebeží. `sudo systemctl status nokturno` a `journalctl -u nokturno`. |
| Pri filme nie sú streamy | pozri [Pri filme nie sú streamy Nokturna](stremio-zadne-streamy.md) |

---
[Všetky návody](./) · [Česky](../cs/stremio-vps)
