---
slug: stremio-aplikace
lang: cs
title: Nokturno pro Stremio – aplikace
products: [stremio]
priority: 0
templates:
  stremio: |
    Nokturno pro Stremio je aplikace, kterou si pustíš u sebe (PC, NAS, Android TV box).
    Stáhni ji z github.com/nokturno-app/nokturno-stremio-app/releases, spusť a otevři http://<IP zařízení>:7140/configure.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/stremio-aplikace
---

# Nokturno pro Stremio – aplikace

Nokturno pro Stremio a Nuvio je malá aplikace, která běží **u tebe** – na počítači, NASu nebo Android TV boxu.
Stremio se na ni ptá jako na každý jiný doplněk.

Aplikace musí běžet, kdykoli se díváš. Nejlíp na zařízení, které je pořád zapnuté (NAS, TV box),
nebo přímo na tom, kde Stremio pouštíš.

## 1. Stáhni aplikaci
Z [vydání na GitHubu](https://github.com/nokturno-app/nokturno-stremio-app/releases/latest) vyber soubor podle zařízení:

| Zařízení | Soubor |
|---|---|
| Windows 10 a 11 | `nokturno-<verze>-windows-amd64.exe` |
| Mac s čipem Apple (M1 a novější) | `nokturno-<verze>-macos-arm64` |
| Mac s procesorem Intel | `nokturno-<verze>-macos-amd64` |
| Linux, PC a většina NASů | `nokturno-<verze>-linux-amd64` |
| Raspberry Pi a ARM NAS | `nokturno-<verze>-linux-arm64` (64bit systém), `-linux-arm` (32bit) |
| Android, Android TV, Google TV | `nokturno-<verze>.apk` |

## 2. Spusť ji
- **Windows:** spusť `.exe`. Na hlášku „Systém Windows ochránil váš počítač“ dej **Další informace → Přesto spustit**.
  Bránu firewall povol pro **soukromé sítě**. Okno s výpisem nech otevřené, jeho zavřením aplikaci vypneš.
- **macOS:** v Terminálu `chmod +x nokturno-*-macos-*` a `xattr -d com.apple.quarantine nokturno-*-macos-*`,
  pak `./nokturno-<verze>-macos-arm64`. Bez druhého příkazu spuštění zablokuje Gatekeeper, protože aplikace
  není podepsaná (jde to i přes **Nastavení systému → Soukromí a zabezpečení → Přesto otevřít**).
- **Linux:** `chmod +x nokturno-*-linux-*` a `./nokturno-<verze>-linux-amd64`. Jak ji pouštět jako službu,
  najdeš v [README aplikace](https://github.com/nokturno-app/nokturno-stremio-app#linux).
- **Android a Android TV:** povol instalaci z neznámých zdrojů (na TV třeba v aplikaci **Downloader**)
  a nainstaluj APK. Aplikace **Nokturno** ukáže adresy pro nastavení, běží na pozadí a po zapnutí zařízení
  se spustí sama.

## 3. Přidej doplněk do Stremia
1. Otevři v prohlížeči nastavení:
   - na zařízení, kde aplikace běží: `http://127.0.0.1:7140/configure`,
   - z telefonu nebo počítače ve stejné síti: `http://<IP adresa zařízení s aplikací>:7140/configure`.
     IP adresu vypíše aplikace při startu, na Androidu je na hlavní obrazovce.
2. Vyplň [vlastní úložiště](vlastni-uloziste.md) a případně účty zdrojů, u každého dej **Ověřit**.
   Potvrď souhlas s podmínkami.
3. Klikni na **Přidat do Stremia** nebo **Přidat do Nuvia**. Do Streamletu adresu vlož přes **Zkopírovat adresu**.
4. Na televizi se doplněk objeví sám, když ho přidáš na telefonu nebo počítači pod stejným účtem Stremio.

Adresa doplňku obsahuje tvoje účty. Nikomu ji neposílej. Podrobnosti v článku
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
Na počítači vznikne při prvním spuštění soubor `nokturno.json` (Windows `%APPDATA%\Nokturno`,
macOS `~/Library/Application Support/Nokturno`, Linux `~/.local/share/nokturno`). V něm jde změnit porty,
vypnout HTTPS, zadat vlastní klíč TMDB pro katalogy TMDB (`tmdb_key`) a vypnout anonymní statistiky
(`"stats": false`) a hlášení o pádech (`"crash_reports": false`). Po úpravě aplikaci restartuj.
Popis všech voleb je v [README aplikace](https://github.com/nokturno-app/nokturno-stremio-app#nastavení-aplikace).

---
[Všechny návody](../) · [Slovensky](../sk/stremio-aplikace)
