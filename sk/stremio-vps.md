---
slug: stremio-vps
lang: sk
title: Nokturno pre Stremio na VPS s vlastnou doménou
products: [stremio]
priority: 2
templates:
  stremio: |
    Aby doplnok fungoval aj mimo domova, spusti aplikáciu Nokturno na VPS s vlastnou doménou. Inštalácia jedným príkazom:
    curl -fsSL https://raw.githubusercontent.com/nokturno-app/nokturno-stremio-app/main/install.sh | sudo bash -s -- --domain <tvoja doména>
    Inštancia je len pre teba, adresu doplnku ani doménu nikomu nedávaj.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/stremio-vps
---

# Nokturno pre Stremio na VPS s vlastnou doménou

V domácej sieti stačí aplikácia na televízore, počítači alebo Raspberry Pi, pozri
[Nokturno pre Stremio – aplikácia](stremio-aplikace.md). Mimo domova sa k nej dostaneš aj bez VPS, cez Tailscale
alebo inú VPN, pozri [Nokturno pre Stremio mimo domova – Tailscale a VPN](stremio-mimo-domov.md).
Keď chceš doplnok na mobile alebo televízore bez VPN, spusti aplikáciu na vlastnom VPS s vlastnou doménou.
Stremio aj Nuvio potom len zadajú adresu `https://<tvoja doména>/…`.

Inštancia na VPS je v predvolenom stave **osobná**: je pre teba a tvoju domácnosť. Adresu doplnku ani doménu nikomu nedávaj
a prevádzku pre cudzích ľudí nerob. Výnimku tvorí sekcia „Nastavenie pre kamarátov“ nižšie, ktorú zapneš len vedome.

Postup počíta s tým, že vieš pracovať v príkazovom riadku Linuxu cez SSH.

## Kde vziať VPS a doménu
### VPS
Stačí najmenší VPS s **1 vCPU, 1 GB RAM** a systémom **Debian 12** alebo **Ubuntu 24.04**. Pár príkladov
poskytovateľov, ceny sú orientačné, over ich na webe poskytovateľa. S nikým z nich nie sme nijako spojení.

| Poskytovateľ | Orientačná cena | Poznámka |
|---|---|---|
| Hetzner Cloud (najmenší stroj radu CX alebo CAX, napríklad CX22 alebo CAX11) | okolo 4 € mesačne | dátové centrá v EÚ, CAX je procesor ARM |
| Contabo | okolo 5 € mesačne | viac RAM a disku za podobnú cenu |
| Oracle Cloud Always Free | zadarmo | stroj s procesorom ARM, registrácia je zložitejšia, chce platobnú kartu a voľná kapacita niekedy chýba |
| WEDOS (VPS ON), Forpsi | podľa konfigurácie | české, s administráciou a podporou v češtine |

### Stačí najlacnejší VPS?
Áno, s veľkou rezervou. Dáta filmu cez VPS pri väčšine zdrojov netečú, prehrávač si súbor sťahuje priamo zo zdroja. Server hľadá
a vracia zoznam streamov. Súbory z vlastného úložiska a FastShare však tečú cez VPS, počítaj preto s jeho prenosom dát. Z merania: aplikácia si berie zhruba 250 MB RAM a na jednom jadre zvládla aj tisíce hľadaní
denne pri zhruba 5 % vyťažení procesora. Pre teba a tvoju domácnosť je to viac než dosť.

Obmedzenie je inde než vo výkone: všetko hľadanie ide z jednej IP adresy VPS a zdroje môžu IP, z ktorej prichádza
veľa dopytov, obmedziť alebo zablokovať. Aj preto je inštancia osobná, adresu doplnku ani doménu nikomu nedávaj.

### Doména
- **Vlastná doména alebo subdoména** od ľubovoľného registrátora (napríklad `nokturno.tvoja-domena.sk`)
  s **A záznamom** na verejnú IP adresu VPS.
- **Zadarmo:** subdoména od [DuckDNS](https://www.duckdns.org) (napríklad `tvoje-meno.duckdns.org`). VPS má
  verejnú IP, stačí ju v DuckDNS nastaviť raz.

Overíš to príkazom `getent hosts nokturno.tvoja-domena.sk`, musí vypísať IP VPS.

## Inštalácia jedným príkazom
Na VPS sa prihlás cez SSH a spusti:

```bash
sudo apt install -y curl ufw
curl -fsSL https://raw.githubusercontent.com/nokturno-app/nokturno-stremio-app/main/install.sh | sudo bash -s -- --domain nokturno.tvoja-domena.sk
```

Skript:
- rozpozná architektúru, stiahne aplikáciu z posledného vydania a overí jej odtlačok SHA-256;
- založí systémového používateľa `nokturno` a službu `nokturno` (aplikácia v `/opt/nokturno/nokturno`,
  nastavenia a dáta v `/opt/nokturno/data`);
- nainštaluje [Caddy](https://caddyserver.com), ktorý pred aplikáciou zabezpečí HTTPS s certifikátom Let's Encrypt;
- keď je nainštalovaný firewall `ufw`, povolí porty 22, 80 a 443 a zapne ho (preto ho prvý riadok inštaluje);
- skontroluje, že doména mieri na tento server, a na konci vypíše adresu nastavenia.

Aplikácia potom počúva len na `127.0.0.1` a zvonku je dostupná len cez Caddy. Túto izoláciu vie aplikácia
od verzie 9.0.4. So staršou verziou počúva na všetkých rozhraniach, skript jej port vo firewalle nepovolí a na konci
na to upozorní. Keď má poskytovateľ VPS vlastný firewall v administrácii, povoľ v ňom len porty 22, 80 a 443.

| Prepínač | Čo robí |
|---|---|
| `--domain DOMÉNA` | inštalácia s doménou a Caddy |
| `--port 7140` | iný port aplikácie |
| `--no-firewall` | na `ufw` nesiaha |
| `--uninstall` | odstráni službu, aplikáciu a konfiguráciu Caddy pre Nokturno, dáta nechá v `/opt/nokturno/data` |

**Aktualizácie:** aplikácia sa aktualizuje sama. Nový súbor aplikácie stiahne aj opätovné spustenie toho istého príkazu,
doménu a port si skript pamätá a nastavenia zachová. **Odinštalovanie:** rovnaký príkaz s `--uninstall`
namiesto `--domain …`.

Stav služby: `systemctl status nokturno`, výpis: `journalctl -u nokturno -f`.

## Ručná inštalácia
Keď chceš mať každý krok pod kontrolou, ide to aj bez skriptu.

### Aplikácia ako služba
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

### Caddy a firewall
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

## Pridanie do Stremia a Nuvia
1. Otvor `https://nokturno.tvoja-domena.sk/configure` hneď po inštalácii a založ
   [správcu aplikácie](stremio-aplikace.md#spravca-rezimy-a-ucty): meno, heslo, e-mail a kód z výpisu aplikácie
   (`journalctl -u nokturno | grep "nemá správce"`). Ulož si obnovovací kód, ktorý sa potom raz ukáže.
2. Založ profil s názvom, pozri [Nastavenie a pridanie do Stremia](stremio-instalace.md).
3. Vyplň [vlastné úložisko](vlastni-uloziste.md) a prípadne účty zdrojov, pri každom daj **Overiť**.
4. **Pridať do Stremia** alebo **Pridať do Nuvia**. Adresa doplnku začína `https://nokturno.tvoja-domena.sk/c/p…`.
   Na televízore sa doplnok objaví sám, keď ho pridáš na telefóne alebo počítači pod rovnakým účtom Stremio.

Vlastné úložisko doma musí byť dosiahnuteľné z VPS (prehrávač ide cez VPS), teda cez verejnú adresu
alebo VPN. Adresa v domácej sieti (`192.168.…`) z VPS nefunguje. To isté platí pre zdieľaný priečinok SMB (`smb://…`): VPS naň musí dosiahnuť, napríklad cez VPN.

## Aktualizácie a logy
- Aplikácia sa aktualizuje sama, pri štarte a potom každých 6 hodín. Nové verzie sťahuje do priečinka s dátami,
  súbor `/opt/nokturno/nokturno` sa meniť nemusí. Keď nová verzia nenabehne, vráti predchádzajúcu.
- Pri inštalácii skriptom stiahne nový súbor aplikácie aj opätovné spustenie toho istého príkazu.
- Výpis aplikácie: `journalctl -u nokturno -f`, výpis Caddy: `journalctl -u caddy -f`.
- Systém VPS aktualizuj ako obvykle (`sudo apt update && sudo apt upgrade`).

## Nastavenie pre kamarátov
Na inštancii s verejnou adresou sa dá sprístupniť stránka nastavení aj z internetu (od verzie 9.7.0). Kamarátom potom
v sekcii **⚙ Aplikácia** prepni režim na **Používateľské účty** a každému pridaj účet s menom a heslom. Kamarát sa
na `https://<tvoja doména>/configure` prihlási, založí si **vlastný profil so svojimi účtami** a doplnok pridá do
svojho Stremia. Vidí a mení len svoje profily, uložené heslá sa mu do stránky nevracajú. Správca vidí, koľko kto má
profilov a ako často prehráva (nie čo), a môže účet zablokovať alebo zmazať. Viac v článku
[Správca, režimy a účty](stremio-aplikace.md#spravca-rezimy-a-ucty).

Stránku nastavení z internetu zapneš voľbou `"sdilena": true` v `nokturno.json` (vedľa `"port"`, `"stats"` a ďalších;
`/opt/nokturno/data` pri inštalácii skriptom, `/var/lib/nokturno` pri ručnej inštalácii). Potom aplikáciu reštartuj:
`sudo systemctl restart nokturno`. Predvolená hodnota je `false`.

Skôr ako to zapneš, počítaj s týmto:
- **Účty len pre ľudí, ktorým veríš.** Profily zakladá len správca alebo prihlásený používateľ. Kto pozná len adresu
  doplnku, prehráva, ale nastavenie ani heslá nevidí.
- **Staré adresy s nastavením vypni.** V režime s účtami je voľba **Vypnúť staré adresy s nastavením** zapnutá hneď
  po prepnutí. Inak si ktokoľvek, kto pozná doménu, zostaví adresu s vlastnými účtami a hľadá cez tvoj server.
- **Jedna IP.** Všetko hľadanie ide z IP tvojho VPS, zdroje môžu IP s množstvom dotazov obmedziť.
- **Prenos dát.** Súbory z vlastného úložiska a FastShare tečú cez VPS.

## Bezpečnosť a súkromie
- **Adresa doplnku neobsahuje heslá ani nastavenia**, len náhodný kľúč profilu (`/c/p<kľúč>/manifest.json`).
  Kto adresu má a dostane sa k aplikácii, aj tak používa tvoje účty, preto ju ďalej nikomu neposielaj. Nastavenie
  profilu ani uložené heslá s ňou však nezíska a profil nezmení (od verzie 11.0.0).
- **Inštancia je v predvolenom stave len pre teba.** Neprevádzkuj ju ako verejnú službu pre cudzích ľudí (výnimka pozri vyššie). Kto pozná adresu tvojej domény,
  môže si zostaviť adresu s vlastným nastavením a hľadať cez tvoj server, kým v sekcii **⚙ Aplikácia** nevypneš
  staré adresy s nastavením. Doménu preto nikde nezverejňuj.
- **Heslo na celú doménu** (basic auth v Caddy) nedávaj. Stremio ani Nuvio sme s doplnkom za heslom
  neoverovali a doplnok by pravdepodobne prestal fungovať.
- **Štatistiky** vypneš v `nokturno.json` (`/opt/nokturno/data` pri inštalácii skriptom, `/var/lib/nokturno`
  pri ručnej inštalácii): `"stats": false`, hlásenia o pádoch `"crash_reports": false`.
  Potom aplikáciu reštartuj: `sudo systemctl restart nokturno`. Účty ani adresa doplnku sa neposielajú nikdy.
- Na VPS sa prihlasuj **SSH kľúčom**, nie heslom.

## Časté problémy
| Čo sa deje | Čo urobiť |
|---|---|
| `https://…/configure` sa neotvorí, Caddy hlási chybu certifikátu | doména ešte neukazuje na VPS. Počkaj, kým `getent hosts <doména>` vypíše IP VPS (obvykle minúty, výnimočne hodiny), potom `sudo systemctl reload caddy`. |
| Certifikát sa nevydá ani po zmene DNS | Let's Encrypt potrebuje dosiahnuť na porty **80** a 443. Skontroluj `sudo ufw status` a firewall v administrácii VPS. Dôvod vypíše `journalctl -u caddy`. |
| Caddy hlási „502 Bad Gateway“ | aplikácia nebeží. `sudo systemctl status nokturno` a `journalctl -u nokturno`. |
| Vo výpise streamov je namiesto streamov hlásenie „Adresy s nastavením sú v tejto aplikácii vypnuté“ alebo „Účet je zablokovaný správcom aplikácie.“ | prvé znamená, že ide o starú adresu s nastavením, ktorá je vypnutá (správca ju vypol v sekcii **⚙ Aplikácia**, alebo je v predvolenom stave vypnutá v režime **Používateľské účty**, správca ju môže zapnúť): ulož nastavenie ako profil na `/configure` a doplnok pridaj znova. Profil ukladá správca aplikácie, v režime **Používateľské účty** aj prihlásený používateľ. Druhé znamená, že účet majiteľa profilu zablokoval správca aplikácie. |
| Pri filme nie sú streamy | pozri [Pri filme nie sú streamy Nokturna](stremio-zadne-streamy.md) |

---
[Všetky návody](./) · [Česky](../cs/stremio-vps)
