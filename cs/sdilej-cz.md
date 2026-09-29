---
slug: sdilej-cz
lang: cs
title: FastShare s účtem ze Sdilej.cz
products: [kodi, ha, stremio]
priority: 2
when: {fastshare: [bad_login]}
templates:
  kodi: |
    Ahoj, Sdilej.cz má stejné soubory jako FastShare, ale účty jsou oddělené. Účet ze Sdilej.cz s FastShare nefunguje a naopak.
    1. Nokturno → Nastavení → Zdroje a účty, skupina FastShare.
    2. Účet z: vyber web, kde máš účet a kredit (FastShare, nebo Sdilej.cz).
    3. Vyplň jméno a heslo z toho webu a dej Nastavení → Pokročilé → Ověřit zdroje.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/sdilej-cz
    Tým Nokturno
  stremio: |
    Ahoj, účet ze Sdilej.cz jde použít, jen musí být vybraný správný web.
    V nastavení doplňku (Doplňky → Nokturno → ozubené kolo) v kartě FastShare / Sdilej.cz přepni Účet z na Sdilej.cz a dej Ověřit účet.
    Pak doplněk přidej znovu tlačítkem Přidat do Stremia a starý odinstaluj.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/sdilej-cz
    Tým Nokturno
---

# FastShare s účtem ze Sdilej.cz

Sdilej.cz má stejné soubory jako FastShare. **Účty jsou ale oddělené:** účet ze Sdilej.cz s FastShare nefunguje
a naopak. U FastShare proto vybereš, na kterém webu máš účet.

- Hledání je pro oba weby stejné a jde i bez účtu.
- K přehrání je potřeba účet. Kredit (nebo neomezené stahování) se čerpá u toho webu, kde máš účet.
- S volbou Sdilej.cz se streamy v seznamu i ve filtru hlásí jako **Sdilej.cz**.

## Kodi
1. **Nokturno → Nastavení → Zdroje a účty**, skupina **FastShare**, zapni **Používat FastShare / Sdilej.cz**.
2. **Účet z:** **FastShare**, nebo **Sdilej.cz**.
3. **Uživatelské jméno** a **Heslo** z vybraného webu.
4. **Nastavení → Pokročilé → Ověřit zdroje** ukáže, jestli přihlášení prošlo.

Průvodce prvním nastavením se zeptá sám („Máš účet FastShare nebo Sdilej.cz?“) a pak nabídne výběr webu.

## Home Assistant
**Nastavení → Zařízení a služby → Nokturno → Konfigurovat**, sekce **Zdroje a účty**:
- **FastShare – účet z:** FastShare.cz, nebo Sdilej.cz,
- **FastShare / Sdilej.cz – uživatel** a **FastShare / Sdilej.cz – heslo** z vybraného webu.

## Stremio
V nastavení doplňku (ve Stremiu **Doplňky → Nokturno → ozubené kolo**, nebo `http://<IP zařízení s aplikací>:7140/configure`) v kartě **FastShare / Sdilej.cz**:
1. Vyplň **Uživatel** a **Heslo**.
2. **Účet z:** **FastShare.cz**, nebo **Sdilej.cz**.
3. Dej **Ověřit účet**.
4. Doplněk přidej znovu tlačítkem **Přidat do Stremia** a starý odinstaluj.

Soubory z FastShare i Sdilej.cz se nepřehrají ve webovém Stremiu v prohlížeči, jen v aplikaci,
viz [„⚠️ Ve webovém přehrávači se nepřehraje“](stremio-webovy-prehravac.md).

## Hlášky
| Hláška | Co udělat |
|---|---|
| „nesedí jméno nebo heslo“ | nejčastěji je vybraný jiný web, než kde máš účet. Přepni **Účet z**. Dál viz [Zdroj hlásí „nesedí jméno nebo heslo“](prihlaseni.md) |
| „došel kredit“, „na soubor … nestačí kredit“ | dobij kredit na webu, kde máš účet, viz [„Účet bez Premium“, „účet bez VIP“, „došel kredit“](premium-a-kredit.md) |

---
[Všechny návody](../) · [Slovensky](../sk/sdilej-cz)
