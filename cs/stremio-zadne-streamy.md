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
2. **Je u filmu položka ⚠️ Nokturno?** Pak máš starou adresu doplňku, viz
   [Stremio: „Adresa doplňku je zastaralá“](stremio-stara-adresa.md).
3. **Je tam položka ⛔ Nokturno?** Přes tvůj doplněk přišlo příliš mnoho požadavků za sebou a server ho na chvíli
   zastavil („Příliš mnoho požadavků…“ na pár minut, „…přístup na hodinu zablokovaný“ na hodinu). Zkus to později.

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
- **Vlastní úložiště:** adresa v domácí síti s doplňkem na `nokturno.stream` nefunguje, viz
  [Jak připojit vlastní úložiště](vlastni-uloziste.md).

## Stream je vidět, ale nepřehraje se
- U streamu je „⚠️ Ve webovém přehrávači se nepřehraje – jen v aplikaci“: takový stream (vlastní úložiště,
  FastShare) jde pustit jen v aplikaci Stremio pro počítač, Android a Android TV, nebo v Nuviu. Ve Stremiu
  v prohlížeči ne.
- WebShare občas hlásí, že je soubor dočasně nedostupný. Vyber jiný stream.

---
[Všechny návody](../) · [Slovensky](../sk/stremio-zadne-streamy)
