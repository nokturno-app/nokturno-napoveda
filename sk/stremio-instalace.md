---
slug: stremio-instalace
lang: sk
title: Ako pridať Nokturno do Stremia alebo Nuvia
products: [stremio]
priority: 1
templates:
  stremio: |
    Nokturno pre Stremio je aplikácia, ktorú si spustíš u seba: github.com/nokturno-app/nokturno-stremio-app/releases
    Potom otvor http://<IP zariadenia s aplikáciou>:7140/configure, založ profil s názvom, vyplň vlastné úložisko, prípadne voliteľné účty zdrojov a daj Pridať do Stremia.
    Od verzie 9.6.0 sa nastavenie ukladá v aplikácii, zmeny potom stačí uložiť tlačidlom Uložiť zmeny, doplnok sa znova nepridáva.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/stremio-instalace
---

# Ako pridať Nokturno do Stremia alebo Nuvia

!!! danger "Doplnok na cudzom serveri dostáva tvoje prihlasovacie údaje"
    Každý doplnok pre Stremio, ktorý beží na cudzom serveri, dostáva tvoje prihlasovacie údaje k zdrojom
    (vlastné úložisko, WebShare, FastShare…). Sú v adrese doplnku, prevádzkovateľ servera ich preto môže vidieť
    a uložiť a musíš mu veriť. Istotu máš len s doplnkom, ktorý beží u teba: doma, cez VPN alebo na vlastnom VPS.

Doplnok pre Stremio beží v aplikácii **Nokturno pre Stremio** u teba doma. Ako ju stiahnuť a spustiť, je v článku
[Nokturno pre Stremio – aplikácia](stremio-aplikace.md). Nastavenie (účty, úložisko, predvoľby) si aplikácia od verzie
9.6.0 ukladá u seba ako **profil**. Adresa doplnku nesie len náhodný kľúč profilu, žiadne heslá.

## 1. Založ profil
Otvor v prehliadači `http://<IP adresa zariadenia s aplikáciou>:7140/configure` (na tom istom zariadení
`http://127.0.0.1:7140/configure`). Pri úplne prvom otvorení stránka chce najprv
[heslo správcu](stremio-aplikace.md#heslo-spravcu-a-profily-kamaratov) (od verzie 9.12.0). Potom ukáže kartu **Profily**:
- **Uložené profily** – zoznam profilov, ktoré už máš. Klik na názov otvorí jeho nastavenie, **Zmazať** ho odstráni.
- **Názov nového profilu** a **Založiť nový profil** – napíš názov (napríklad *Obývačka* alebo *Mobil*) a založ profil.
  Bez názvu profil nevznikne.

Po založení sa otvorí formulár s nastavením nového profilu. Hore je jeho názov (dá sa prepísať) a odkaz
**← Všetky profily** späť na zoznam.

## 2. Vyplň nastavenie
1. **Vlastné úložisko a zdroje** – každý zdroj má vlastnú záložku (Vlastné úložisko, WebShare, Sosáč, Sledujteto,
   FastShare, Přehraj.to, CZtor, HellSpy). Začni prvou záložkou **Vlastné úložisko**. Zdroje tretích strán sú voliteľné
   a v novom profile sú všetky vypnuté, HellSpy tiež. Vyplnený zdroj má na záložke zelenú bodku. Účet overíš tlačidlom
   **Overiť účet** v jeho záložke, alebo všetky naraz tlačidlom **✓ Overiť všetky účty** vedľa záložiek –
   výsledok sa ukáže v modrom rámčeku, klik na riadok otvorí záložku zdroja. Rámček zavrieš krížikom, sám zmizne po 10 s.
2. **Predvoľby** – jazyk zvuku, radenie, katalógy. Tento krok sa dá preskočiť.
3. Potvrď súhlas s podmienkami použitia.

## 3. Pridaj doplnok
| Kde | Ako |
|---|---|
| **Počítač** | **Pridať do Stremia**, prehliadač sa opýta, či otvoriť Stremio, potvrď. V Stremiu **Inštalovať**. |
| **Telefón** | **QR pre mobil** na počítači a naskenuj kód telefónom. Otvorí sa stránka s tlačidlami **Pridať do Stremia**, **Pridať do Nuvia** a **Skopírovať adresu**. Telefón musí byť v rovnakej sieti ako aplikácia. Ide to aj bez QR: otvor `/configure` priamo v telefóne. |
| **Televízor** | Pridaj doplnok na telefóne alebo počítači **pod rovnakým účtom Stremio**. Na TV sa objaví do minúty. Ručne: Stremio → Doplnky → pole hore → vložiť adresu → Inštalovať. Keď aplikácia beží na telefóne, adresa z neho (`127-0-0-1…`) na TV nefunguje – otvor na TV alebo počítači `http://<IP telefónu>:7140/configure` a pridaj doplnok odtiaľ. |
| **Nuvio** | **Pridať do Nuvia**. Na TV: **Skopírovať adresu**, potom v Nuviu Nastavenia → Doplnky → vložiť adresu → Inštalovať. |
| **Streamlet** | **Skopírovať adresu**, v Streamlete pridaj doplnok Stremia a adresu vlož. |

Tlačidlá nastavenie pred pridaním samy uložia. Keď stránku otvoríš cez IP adresu, dostane doplnok adresu
`https://…my.local-ip.co:7141`. Tú Stremio prijme aj z iného zariadenia v sieti, pozri
[Nokturno pre Stremio – aplikácia](stremio-aplikace.md). Doplnok funguje len vtedy, keď aplikácia beží.

Adresu doplnku nikomu neposielaj. Heslá v nej nie sú, ale kto ju má a dostane sa k aplikácii, používa tvoje účty.

## Zmena nastavenia
V Stremiu **Doplnky → Nokturno → ozubené koliesko**, alebo otvor `/configure` a klikni na názov profilu. Uprav nastavenie
a daj **Uložiť zmeny** (tlačidlo sa objaví, len čo niečo zmeníš). Účty, úložisko a predvoľby platia hneď,
**doplnok do Stremia znova nepridávaš**.

Výnimkou sú **katalógy**: Stremio si zoznam katalógov pamätá, takže po zapnutí alebo vypnutí katalógu doplnok
v Stremiu odinštaluj a pridaj znova.

## Viac profilov
Každý profil má vlastnú adresu doplnku a vlastné nastavenie. Hodí sa, keď má každý člen domácnosti iné účty, alebo keď
chceš na televízore iné predvoľby ako na mobile. Nový profil založíš cez **← Všetky profily** → **Založiť nový profil**.
Zmazaný profil prestane fungovať vo všetkých aplikáciách, kam si ho pridal.

## Stará dlhá adresa (do verzie 9.5.x)
Skoršia adresa doplnku niesla celé nastavenie aj s účtami (začínala `/c/eyJ…`). Keď v Stremiu pri takom doplnku
otvoríš ozubené koliesko, stránka nastavenia ho sama prevedie na profil a ukáže hlášku. Potom:
1. Pridaj doplnok znova tlačidlom **Pridať do Stremia** (už s krátkou adresou).
2. Starý doplnok v Stremiu odinštaluj.
3. Doplň profilu názov, nech ho v zozname spoznáš.

Odvtedy pri zmenách nastavenia doplnok pridávať nemusíš. Stará adresa funguje ďalej, kým ju neodinštaluješ.

## Nokturno mám v Stremiu dvakrát
Je to starý a nový doplnok, alebo dva rôzne profily. V Stremiu **Doplnky** odinštaluj ten, ktorý nechceš.

## Časté problémy
| Čo sa deje | Čo urobiť |
|---|---|
| „Tohle nastavení už v aplikaci není“ (hláška je po česky) | profil bol zmazaný. Otvor `/configure`, založ nový profil a doplnok pridaj znova. |
| QR kód sa v telefóne neotvorí | telefón nie je v rovnakej sieti ako aplikácia. Pripoj ho na domácu Wi-Fi, alebo použi [Tailscale alebo VPN](stremio-mimo-domov.md). |
| Zmena sa v Stremiu neprejavila | pri účtoch a predvoľbách otvor titul znova. Pri katalógoch doplnok odinštaluj a pridaj znova. |
| „Unable to resolve host …my.local-ip.co“ alebo *Failed to fetch* | DNS zahodilo adresu doplnku (ochrana proti DNS rebinding). Android: Nastavenia → Pripojenia → Ďalšie nastavenia pripojenia → Súkromné DNS → `one.one.one.one`. Router alebo Pi-hole: výnimka pre `my.local-ip.co` (`rebind-domain-ok=/my.local-ip.co/`). |

---
[Všetky návody](./) · [Česky](../cs/stremio-instalace)
