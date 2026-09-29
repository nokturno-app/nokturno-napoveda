---
slug: stremio-zadne-streamy
lang: cs
title: U filmu nejsou streamy Nokturna
products: [stremio]
priority: 1
templates:
  stremio: |
    U filmu nevidíš streamy Nokturna? Ve Stremiu otevři Doplňky → Nokturno → ozubené kolo a u každého zdroje dej Ověřit účet.
    Nejčastěji jde o překlep v hesle nebo vypršelé VIP na WebShare.
    Po opravě dej Přidat do Stremia a starý doplněk odinstaluj.
---

# U filmu nejsou streamy Nokturna

## Nejdřív zkontroluj
1. **Počkej pár sekund.** Stremio ukazuje streamy postupně, jak doplňky odpovídají.
2. **Běží aplikace Nokturno?** Doplněk funguje jen ve chvíli, kdy aplikace běží, viz
   [Nokturno pro Stremio – aplikace](stremio-aplikace.md).
3. **Máš doplněk z `nokturno.stream`, nebo je u filmu položka ⚠️ Nokturno?** Ten od 30. 9. 2026 nefunguje, viz
   [Stremio: doplněk z nokturno.stream nefunguje](stremio-stara-adresa.md).
4. **Je tam položka ⛔ Nokturno?** Přišlo příliš mnoho požadavků za sebou, viz
   [Položky „📢 Nokturno“, „⚠️ Nokturno“ a „⛔ Nokturno“](stremio-polozky-nokturno.md).

## Ověř účty
Ve Stremiu otevři **Doplňky → Nokturno → ozubené kolo** a u každého zdroje dej **Ověřit účet**.
- „Přihlášení neprošlo – zkontroluj jméno a heslo.“ (u některých zdrojů „e-mail a heslo“): viz [Zdroj hlásí „nesedí jméno nebo heslo“](prihlaseni.md).
- WebShare bez VIP, Sledujteto bez Premium, FastShare bez kreditu: viz [Premium, VIP a kredit](premium-a-kredit.md).

Po opravě dej **Přidat do Stremia** a starý doplněk odinstaluj.

## Jeden zdroj nefunguje, ostatní ano
Zdroj, který neodpověděl, se přeskočí a streamy přijdou z ostatních. Zkus to za chvíli znovu.

## Účty jsou v pořádku, a stejně nic
- **Titul na zdrojích nemusí vůbec být**, hlavně úplné novinky a málo známé seriály.
- Nokturno bere jen soubory, které k titulu opravdu patří (název, rok, díl). Podobné, ale jiné filmy záměrně vynechá.
- **Vlastní úložiště:** musí na něj dosáhnout zařízení s aplikací Nokturno i zařízení, kde přehráváš, viz
  [Jak připojit vlastní úložiště](vlastni-uloziste.md).

## Stream je vidět, ale nepřehraje se
- U streamu je „⚠️ Ve webovém přehrávači se nepřehraje – jen v aplikaci“: takový stream (vlastní úložiště,
  FastShare) jde pustit jen v aplikaci Stremio pro počítač, Android a Android TV, nebo v Nuviu. Ve Stremiu
  v prohlížeči ne.
- WebShare občas hlásí, že je soubor dočasně nedostupný. Vyber jiný stream.

---
[Všechny návody](../) · [Slovensky](../sk/stremio-zadne-streamy)
