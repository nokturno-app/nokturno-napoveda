---
slug: sdilej-cz
lang: sk
title: FastShare s účtom zo Sdilej.cz
products: [kodi, ha, stremio]
priority: 2
when: {fastshare: [bad_login]}
templates:
  kodi: |
    Ahoj, Sdilej.cz má rovnaké súbory ako FastShare, ale účty sú oddelené. Účet zo Sdilej.cz s FastShare nefunguje a naopak.
    1. Nokturno → Nastavenia → Zdroje a účty, skupina FastShare.
    2. Účet z: vyber web, kde máš účet a kredit (FastShare alebo Sdilej.cz).
    3. Vyplň meno a heslo z toho webu a daj Nastavenia → Pokročilé → Overiť zdroje.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/sdilej-cz
    Tím Nokturno
  stremio: |
    Ahoj, účet zo Sdilej.cz sa dá použiť, len musí byť vybraný správny web.
    V nastavení doplnku (Doplnky → Nokturno → ozubené koliesko) v karte FastShare / Sdilej.cz prepni Účet z na Sdilej.cz a daj Overiť účet.
    Potom doplnok pridaj znova tlačidlom Pridať do Stremia a starý odinštaluj.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/sdilej-cz
    Tím Nokturno
---

# FastShare s účtom zo Sdilej.cz

Sdilej.cz má rovnaké súbory ako FastShare. **Účty sú však oddelené:** účet zo Sdilej.cz s FastShare nefunguje
a naopak. Pri FastShare preto vyberieš, na ktorom webe máš účet.

- Hľadanie je pre oba weby rovnaké a ide aj bez účtu.
- Na prehratie je potrebný účet. Kredit (alebo neobmedzené sťahovanie) sa čerpá na tom webe, kde máš účet.
- S voľbou Sdilej.cz sa streamy v zozname aj vo filtri hlásia ako **Sdilej.cz**.

## Kodi
1. **Nokturno → Nastavenia → Zdroje a účty**, skupina **FastShare**, zapni **Používať FastShare / Sdilej.cz**.
2. **Účet z:** **FastShare** alebo **Sdilej.cz**.
3. **Používateľské meno** a **Heslo** z vybraného webu.
4. **Nastavenia → Pokročilé → Overiť zdroje** ukáže, či prihlásenie prešlo.

Sprievodca prvým nastavením sa spýta sám („Máš účet FastShare alebo Sdilej.cz?“) a potom ponúkne výber webu.

## Home Assistant
**Nastavenia → Zariadenia a služby → Nokturno → Konfigurovať**, sekcia **Zdroje a účty**:
- **FastShare – účet z:** FastShare.cz alebo Sdilej.cz,
- používateľ a heslo pre **FastShare / Sdilej.cz** z vybraného webu.

## Stremio
V nastavení doplnku (v Stremiu **Doplnky → Nokturno → ozubené koliesko**, alebo `http://<IP zariadenia s aplikáciou>:7140/configure`) v karte **FastShare / Sdilej.cz**:
1. Vyplň **Používateľ** a **Heslo**.
2. **Účet z:** **FastShare.cz** alebo **Sdilej.cz**.
3. Daj **Overiť účet**.
4. Doplnok pridaj znova tlačidlom **Pridať do Stremia** a starý odinštaluj.

Súbory z FastShare aj Sdilej.cz od verzie 9.6.1 prehrávaču odovzdáva aplikácia Nokturno, hrajú teda aj v Stremiu pre Android.
Vo webovom prehrávači v prehliadači záleží na formáte súboru, pozri [„⚠️ Vo webovom prehrávači sa neprehrá“](stremio-webovy-prehravac.md).

## Hlásenia
| Hlásenie | Čo urobiť |
|---|---|
| „nesedí meno alebo heslo“ | najčastejšie je vybraný iný web, než kde máš účet. Prepni **Účet z**. Ďalej pozri [Zdroj hlási „nesedí meno alebo heslo“](prihlaseni.md) |
| „minul sa kredit“, „na soubor … nestačí kredit“ (po česky) | dobi kredit na webe, kde máš účet, pozri [„Účet bez Premium“, „účet bez VIP“, „minul sa kredit“](premium-a-kredit.md) |

---
[Všetky návody](./) · [Česky](../cs/sdilej-cz)
