---
slug: stahovani
lang: sk
title: Sťahovanie zlyhalo
products: [kodi, ha]
priority: 2
templates:
  kodi: |
    Ahoj, sťahovanie sa nepodarilo.
    1. Aktualizuj Nokturno na najnovšiu verziu, staršie verzie niektoré zdroje a sieťové priečinky sťahovať nevedeli.
    2. Nokturno → Nastavenia → Prehrávanie → Sťahovanie: Priečinok na sťahovanie musí byť zapisovateľný, napríklad USB disk alebo sieťový priečinok.
    3. V menu Stiahnuté daj pri položke Skúsiť znova. Prerušené sťahovanie nadviaže, kde skončilo.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/stahovani
    Tím Nokturno
---

# Sťahovanie zlyhalo

## Kodi
Stiahnuť sa dá z kontextového menu titulu (**Stiahnuť**): otvorí sa výber streamu a vybraný stream ide do frontu.
Hotové a rozťahané videá sú v menu **Stiahnuté**.

### „Najprv nastav priečinok na sťahovanie v nastaveniach.“
**Nokturno → Nastavenia → Prehrávanie → Sťahovanie → Priečinok na sťahovanie.** Bez neho sa sťahovať nedá a položka
**Stiahnuté** v menu nie je.

### Vo výbere na stiahnutie chýbajú streamy z CZtoru
CZtor povoľuje sťahovanie len pri časti obsahu. Streamy, ktoré stiahnuť nedovolí, sa vo výbere na stiahnutie
neukážu – prehrať ich ide ďalej normálne.

### „Sťahovanie zlyhalo: …“
1. **Aktualizuj Nokturno.** Staršie verzie nesťahovali z CZtoru (do 6.0.3), z Přehraj.to (do 7.0.3)
   a do sieťového priečinka (do 7.9.6).
2. **Skontroluj priečinok.** Musí byť zapisovateľný a musí na ňom byť miesto. Na televízoroch bez vlastného úložiska
   použi USB disk alebo sieťový priečinok (`smb://…`).
   Rovnaký zdieľaný priečinok môžeš mať aj ako [vlastné úložisko](vlastni-uloziste.md) a prehrávať z neho.
3. **Skontroluj zdroj.** Sťahovanie potrebuje rovnaký účet ako prehrávanie (Premium, VIP, kredit).
   Pozri [Premium, VIP a kredit](premium-a-kredit.md).
4. V menu **Stiahnuté** daj pri položke **Skúsiť znova**.

### Sťahovanie sa prerušilo
Po výpadku siete, reštarte Kodi alebo vypnutí boxu sťahovanie **nadviaže tam, kde skončilo** (pri nedokončenej položke
**Skúsiť znova**). Do sieťového priečinka sa nenadväzuje, začne znova.

Hotové sťahovanie sa dá v kontextovom menu **Vymazať** (zmaže súbor z disku).

## Home Assistant
Integrácia sťahuje do **Priečinka na sťahovanie** zo sekcie **Sťahovanie a odkazy**. Priečinok musí na disku Home Assistantu
existovať a byť zapisovateľný. Upozornenia na dokončenie chodia do služby `notify.`
z poľa **Upozornenia na stiahnutie a nové diely**. Prázdne pole pošle upozornenie len do Home Assistantu.

Sťahovanie spustíš ikonou sťahovania (bublina **Stiahnuť**) pri streame v karte Nokturno. Bežiace sťahovanie je v karte
pod nadpisom **Sťahovanie** a hotové súbory v sekcii **Stiahnuté**, oboje úplne dole na úvodnej obrazovke. V editore karty sa sekcia
**Stiahnuté** dá vynechať v **Sekcie a ich poradie (rady plagátov)**, potom sa nezobrazí ani bežiace sťahovanie. CZtor povoľuje sťahovanie len pri časti obsahu: pri streame, ktorý nedovolí, skončí **Stiahnuť**
hláškou „CZtor stažení tohohle streamu nepovoluje.“ (prehrať ide ďalej normálne).

---
[Všetky návody](./) · [Česky](../cs/stahovani)
