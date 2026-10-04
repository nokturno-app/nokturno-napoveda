---
slug: stremio-instalace
lang: cs
title: Jak přidat Nokturno do Stremia nebo Nuvia
products: [stremio]
priority: 1
templates:
  stremio: |
    Nokturno pro Stremio je aplikace, kterou si pustíš u sebe: github.com/nokturno-app/nokturno-stremio-app/releases
    Pak otevři http://<IP zařízení s aplikací>:7140/configure, založ profil s názvem, vyplň úložiště nebo účty a dej Přidat do Stremia.
    Od verze 9.6.0 se nastavení ukládá v aplikaci, změny pak stačí uložit tlačítkem Uložit změny, doplněk se znovu nepřidává.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/stremio-instalace
---

# Jak přidat Nokturno do Stremia nebo Nuvia

!!! danger "Doplněk na cizím serveru dostává tvoje přihlašovací údaje"
    Každý doplněk pro Stremio, který běží na cizím serveru, dostává tvoje přihlašovací údaje ke zdrojům
    (WebShare, FastShare, Přehraj.to…). Jsou v adrese doplňku, provozovatel serveru je proto může vidět
    a uložit a musíš mu věřit. Jistotu máš jen s doplňkem, který běží u tebe: doma, přes VPN nebo na vlastním VPS.

Doplněk pro Stremio běží v aplikaci **Nokturno pro Stremio** u tebe doma. Jak ji stáhnout a spustit, je v článku
[Nokturno pro Stremio – aplikace](stremio-aplikace.md). Nastavení (účty, úložiště, předvolby) si aplikace od verze
9.6.0 ukládá u sebe jako **profil**. Adresa doplňku nese jen náhodný klíč profilu, žádná hesla.

## 1. Založ profil
Otevři v prohlížeči `http://<IP adresa zařízení s aplikací>:7140/configure` (na tomtéž zařízení
`http://127.0.0.1:7140/configure`). Při úplně prvním otevření stránka chce nejdřív
[heslo správce](stremio-aplikace.md#heslo-spravce-a-profily-kamaradu) (od verze 9.12.0). Pak ukáže kartu **Profily**:
- **Uložené profily** – seznam profilů, které už máš. Klik na název otevře jeho nastavení, **Smazat** ho odstraní.
- **Název nového profilu** a **Založit nový profil** – napiš název (třeba *Obývák* nebo *Mobil*) a založ profil.
  Bez názvu profil nevznikne.

Po založení se otevře formulář s nastavením nového profilu. Nahoře je jeho název (jde přepsat) a odkaz
**← Všechny profily** zpátky na seznam.

## 2. Vyplň nastavení
1. **Vlastní úložiště a zdroje** – každý zdroj má vlastní záložku (Vlastní úložiště, WebShare, Sosáč, Sledujteto,
   FastShare, Přehraj.to, CZtor, HellSpy). Vyplněný zdroj má na záložce zelenou tečku. Účet ověříš tlačítkem
   **Ověřit účet** v jeho záložce, nebo všechny naráz tlačítkem **✓ Ověřit všechny účty** vedle záložek –
   výsledek se ukáže v modrém rámečku, klik na řádek otevře záložku zdroje. Rámeček zavřeš křížkem, sám zmizí po 10 s.
2. **Předvolby** – jazyk zvuku, řazení, katalogy. Tento krok se dá přeskočit.
3. Potvrď souhlas s podmínkami použití.

## 3. Přidej doplněk
| Kde | Jak |
|---|---|
| **Počítač** | **Přidat do Stremia**, prohlížeč se zeptá, jestli otevřít Stremio, potvrď. Ve Stremiu **Instalovat**. |
| **Telefon** | **QR pro mobil** na počítači a naskenuj kód telefonem. Otevře se stránka s tlačítky **Přidat do Stremia**, **Přidat do Nuvia** a **Zkopírovat adresu**. Telefon musí být ve stejné síti jako aplikace. Jde to i bez QR: otevři `/configure` přímo v telefonu. |
| **Televize** | Přidej doplněk na telefonu nebo počítači **pod stejným účtem Stremio**. Na TV se objeví do minuty. Ručně: Stremio → Doplňky → pole nahoře → vložit adresu → Instalovat. Když aplikace běží na telefonu, adresa z něj (`127-0-0-1…`) na TV nefunguje – otevři na TV nebo počítači `http://<IP telefonu>:7140/configure` a přidej doplněk odtud. |
| **Nuvio** | **Přidat do Nuvia**. Na TV: **Zkopírovat adresu**, pak v Nuviu Nastavení → Doplňky → vložit adresu → Instalovat. |
| **Streamlet** | **Zkopírovat adresu**, ve Streamletu přidej doplněk Stremia a adresu vlož. |

Tlačítka nastavení před přidáním samy uloží. Když stránku otevřeš přes IP adresu, dostane doplněk adresu
`https://…my.local-ip.co:7141`. Tu Stremio přijme i z jiného zařízení v síti, viz
[Nokturno pro Stremio – aplikace](stremio-aplikace.md). Doplněk funguje jen ve chvíli, kdy aplikace běží.

Adresu doplňku nikomu neposílej. Hesla v ní nejsou, ale kdo ji má a dostane se k aplikaci, používá tvoje účty.

## Změna nastavení
Ve Stremiu **Doplňky → Nokturno → ozubené kolo**, nebo otevři `/configure` a klikni na název profilu. Uprav nastavení
a dej **Uložit změny** (tlačítko se objeví, jakmile něco změníš). Účty, úložiště a předvolby platí hned,
**doplněk do Stremia znovu nepřidáváš**.

Výjimka jsou **katalogy**: Stremio si seznam katalogů pamatuje, takže po zapnutí nebo vypnutí katalogu doplněk
ve Stremiu odinstaluj a přidej znovu.

## Víc profilů
Každý profil má vlastní adresu doplňku a vlastní nastavení. Hodí se, když má každý člen domácnosti jiné účty, nebo když
chceš na televizi jiné předvolby než na mobilu. Nový profil založíš přes **← Všechny profily** → **Založit nový profil**.
Smazaný profil přestane fungovat ve všech aplikacích, kam jsi ho přidal.

## Stará dlouhá adresa (do verze 9.5.x)
Dřívější adresa doplňku nesla celé nastavení i s účty (začínala `/c/eyJ…`). Když ve Stremiu u takového doplňku
otevřeš ozubené kolo, stránka nastavení ho sama převede na profil a ukáže hlášku. Pak:
1. Přidej doplněk znovu tlačítkem **Přidat do Stremia** (už s krátkou adresou).
2. Starý doplněk ve Stremiu odinstaluj.
3. Doplň profilu název, ať ho v seznamu poznáš.

Od té chvíle při změnách nastavení doplněk přidávat nemusíš. Stará adresa funguje dál, dokud ji neodinstaluješ.

## Nokturno mám ve Stremiu dvakrát
Je to starý a nový doplněk, nebo dva různé profily. Ve Stremiu **Doplňky** odinstaluj ten, který nechceš.

## Časté problémy
| Co se děje | Co udělat |
|---|---|
| „Tohle nastavení už v aplikaci není“ | profil byl smazaný. Otevři `/configure`, založ nový profil a doplněk přidej znovu. |
| QR kód se v telefonu neotevře | telefon není ve stejné síti jako aplikace. Připoj ho na domácí Wi-Fi, nebo použij [Tailscale nebo VPN](stremio-mimo-domov.md). |
| Změna se ve Stremiu neprojevila | u účtů a předvoleb otevři titul znovu. U katalogů doplněk odinstaluj a přidej znovu. |
| „Unable to resolve host …my.local-ip.co“ nebo *Failed to fetch* | DNS zahodilo adresu doplňku (ochrana proti DNS rebinding). Android: Nastavení → Připojení → Další nastavení připojení → Soukromé DNS → `one.one.one.one`. Router nebo Pi-hole: výjimka pro `my.local-ip.co` (`rebind-domain-ok=/my.local-ip.co/`). |

---
[Všechny návody](../) · [Slovensky](../sk/stremio-instalace)
