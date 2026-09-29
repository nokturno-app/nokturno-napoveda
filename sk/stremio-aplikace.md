---
slug: stremio-aplikace
lang: sk
title: Nokturno pre Stremio – aplikácia
products: [stremio]
priority: 0
templates:
  stremio: |
    Nokturno pre Stremio je aplikácia, ktorú si spustíš u seba (PC, NAS, Android TV box).
    Stiahni ju z github.com/nokturno-app/nokturno-stremio-app/releases, spusti a otvor http://<IP zariadenia>:7140/configure.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/stremio-aplikace
---

# Nokturno pre Stremio – aplikácia

Nokturno pre Stremio a Nuvio je malá aplikácia, ktorá beží **u teba** – na počítači, NASe alebo Android TV boxe.
Stremio sa jej pýta ako každého iného doplnku.

Aplikácia musí bežať vždy, keď pozeráš. Najlepšie na zariadení, ktoré je stále zapnuté (NAS, TV box),
alebo priamo na tom, kde Stremio spúšťaš.

## 1. Stiahni aplikáciu
Z [vydaní na GitHube](https://github.com/nokturno-app/nokturno-stremio-app/releases/latest) vyber súbor podľa zariadenia:

| Zariadenie | Súbor |
|---|---|
| Windows 10 a 11 | `nokturno-<verzia>-windows-amd64.exe` |
| Mac s čipom Apple (M1 a novší) | `nokturno-<verzia>-macos-arm64` |
| Mac s procesorom Intel | `nokturno-<verzia>-macos-amd64` |
| Linux, PC a väčšina NASov | `nokturno-<verzia>-linux-amd64` |
| Raspberry Pi a ARM NAS | `nokturno-<verzia>-linux-arm64` (64bit systém), `-linux-arm` (32bit) |
| Android, Android TV, Google TV | `nokturno-<verzia>.apk` |

## 2. Spusti ju
- **Windows:** spusti `.exe`. Na hlášku „Systém Windows ochránil váš počítač“ daj **Ďalšie informácie → Napriek tomu spustiť**.
  Bránu firewall povoľ pre **súkromné siete**. Okno s výpisom nechaj otvorené, jeho zatvorením aplikáciu vypneš.
- **macOS:** v Termináli `chmod +x nokturno-*-macos-*` a `xattr -d com.apple.quarantine nokturno-*-macos-*`,
  potom `./nokturno-<verzia>-macos-arm64`. Bez druhého príkazu spustenie zablokuje Gatekeeper, pretože aplikácia
  nie je podpísaná (ide to aj cez **Nastavenia systému → Súkromie a zabezpečenie → Napriek tomu otvoriť**).
- **Linux:** `chmod +x nokturno-*-linux-*` a `./nokturno-<verzia>-linux-amd64`. Ako ju spúšťať ako službu,
  nájdeš v [README aplikácie](https://github.com/nokturno-app/nokturno-stremio-app#linux).
- **Android a Android TV:** povoľ inštaláciu z neznámych zdrojov (na TV napríklad v aplikácii **Downloader**)
  a nainštaluj APK. Aplikácia **Nokturno** ukáže adresy na nastavenie, beží na pozadí a po zapnutí zariadenia
  sa spustí sama.

## 3. Pridaj doplnok do Stremia
1. Otvor v prehliadači nastavenie:
   - na zariadení, kde aplikácia beží: `http://127.0.0.1:7140/configure`,
   - z telefónu alebo počítača v rovnakej sieti: `http://<IP adresa zariadenia s aplikáciou>:7140/configure`.
     IP adresu vypíše aplikácia pri štarte, na Androide je na hlavnej obrazovke.
2. Vyplň [vlastné úložisko](vlastni-uloziste.md) a prípadne účty zdrojov, pri každom daj **Overiť**.
   Potvrď súhlas s podmienkami.
3. Klikni na **Pridať do Stremia** alebo **Pridať do Nuvia**. Do Streamletu adresu vlož cez **Skopírovať adresu**.
4. Na televízore sa doplnok objaví sám, keď ho pridáš na telefóne alebo počítači pod rovnakým účtom Stremio.

Adresa doplnku obsahuje tvoje účty. Nikomu ju neposielaj. Podrobnosti v článku
[Ako pridať Nokturno do Stremia alebo Nuvia](stremio-instalace.md).

## Aktualizácie
Aplikácia sa aktualizuje sama: pri štarte a potom každých 6 hodín. Novú verziu overí a keď nenabehne,
vráti predchádzajúcu. Na Androide sa aktualizácia sťahuje pri spustení aplikácie alebo po zapnutí zariadenia.
Nový inštalačný súbor sťahovať nemusíš.

## Časté problémy
| Čo sa deje | Čo urobiť |
|---|---|
| Nastavenie sa z iného zariadenia neotvorí | obe zariadenia musia byť v rovnakej sieti a aplikácia musí bežať. Na Windows povoľ aplikáciu vo firewalle pre súkromné siete (porty 7140 a 7141). |
| Stremio doplnok nepridá, adresa s `my.local-ip.co` nefunguje | router blokuje mená, ktoré vedú na domácu IP (ochrana proti DNS rebinding). Povoľ v routeri výnimku pre `local-ip.co`, alebo v zariadení so Stremiom nastav DNS `1.1.1.1`. |
| Doplnok prestal fungovať po reštarte routera | zmenila sa IP adresa zariadenia s aplikáciou. V routeri mu nastav pevnú IP (rezervácia DHCP) a doplnok pridaj znova. |
| Pri štarte „Address already in use“ | port 7140 používa iný program. Spusti aplikáciu s `--port 7150 --https-port 7151`. |
| Stream s „⚠️ Vo webovom prehrávači sa neprehrá“ | hrá len v aplikácii Stremio alebo Nuvio, pozri [„⚠️ Vo webovom prehrávači sa neprehrá“](stremio-webovy-prehravac.md) |
| Pri filme nie sú streamy | pozri [Pri filme nie sú streamy Nokturna](stremio-zadne-streamy.md) |

## Prečo adresa `https://…my.local-ip.co`
Stremio prijme doplnok cez obyčajné `http` len z toho istého zariadenia. Z iného zariadenia chce HTTPS s platným
certifikátom. Aplikácia preto otvorí aj port **7141** s adresou napríklad `https://192-168-1-10.my.local-ip.co:7141`.
Služba local-ip.co také meno preloží späť na tvoju domácu IP, dáta tečú len po tvojej sieti. Rovnako to robí Luna.
Keď nastavenie otvoríš cez IP adresu, formulár dá túto adresu do doplnku sám.

## Nastavenia aplikácie a štatistiky
Na počítači vznikne pri prvom spustení súbor `nokturno.json` (Windows `%APPDATA%\Nokturno`,
macOS `~/Library/Application Support/Nokturno`, Linux `~/.local/share/nokturno`). V ňom sa dajú zmeniť porty,
vypnúť HTTPS, zadať vlastný kľúč TMDB pre katalógy TMDB (`tmdb_key`) a vypnúť anonymné štatistiky
(`"stats": false`) a hlásenia o pádoch (`"crash_reports": false`). Po úprave aplikáciu reštartuj.
Popis všetkých volieb je v [README aplikácie](https://github.com/nokturno-app/nokturno-stremio-app#nastavení-aplikace).

---
[Všetky návody](./) · [Česky](../cs/stremio-aplikace)
