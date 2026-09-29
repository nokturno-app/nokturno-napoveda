---
slug: synchronizace
lang: sk
title: Synchronizácia medzi zariadeniami nefunguje
products: [kodi, ha]
priority: 2
templates:
  kodi: |
    Ahoj, synchronizácia sa ti nedarí. Najjednoduchšie je stredisko Dashboard Nokturna, Home Assistant na to netreba.
    1. Nokturno → Nastavenia → Synchronizácia: zapni Synchronizovať medzi viacerými Kodi a ako Stredisko synchronizácie zvoľ Dashboard Nokturna.
    2. Na prvom Kodi daj Založiť skupinu / otvoriť pripojenie (v starších verziách Založiť skupinu) a opíš kód NKT-….
    3. Na ďalších Kodi rovnaké nastavenie a Pripojiť sa ku skupine s týmto kódom, do 30 minút od založenia.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/synchronizace
    Tím Nokturno
---

# Synchronizácia medzi zariadeniami nefunguje

Synchronizácia zdieľa medzi tvojimi Kodi (a prípadne Home Assistantom) pozreté a rozpozerané tituly,
Môj zoznam a ďalšie okruhy. Všetko je v **Nokturno → Nastavenia → Synchronizácia**.

## Najprv skontroluj
- Je zapnutý prepínač **Synchronizovať medzi viacerými Kodi** (nestačí vyplnený kód)?
- Majú všetky zariadenia rovnaké **Stredisko synchronizácie**?
- Kodi hlási „Synchronizácia nie je zapnutá alebo nastavená (pri Home Assistante adresa a kľúč, pri dashboarde kód skupiny)“?
  Chýba prepínač, kód skupiny, alebo adresa a kľúč.

## Dashboard Nokturna (odporúčané, funguje odkiaľkoľvek)
1. Na prvom Kodi zvoľ stredisko **Dashboard Nokturna** a daj **Založiť skupinu / otvoriť pripojenie**
   (v starších verziách **Založiť skupinu**). Zobrazí sa kód `NKT-…`, opíš si ho.
2. Na ďalších Kodi rovnaké stredisko, **Pripojiť sa ku skupine** a zadaj kód.
3. Nové zariadenie sa môže pripojiť len **30 minút** po založení. Neskôr na prvom Kodi otvor pripojenie znova
   rovnakým tlačidlom (v starších verziách **Znovu otvoriť pripojenie**). Kód zostane rovnaký.

Kód je zároveň kľúč k dátam. Bez neho ich nikto neprečíta ani neobnoví, preto si ho uschovaj.

## Home Assistant ako stredisko
- Kodi musí byť v rovnakej domácej sieti ako Home Assistant.
- **Adresa Home Assistantu:** keď nefunguje názov ako `homeassistant.local`, zadaj IP adresu,
  napríklad `http://192.168.1.10:8123`.
- **Kľúč** musí byť rovnaký ako v nastavení integrácie Nokturno v Home Assistante.

## Home Assistant v skupine Dashboardu
Chceš mať kartu v Home Assistante aktuálnu a synchronizuješ cez Dashboard Nokturna? Zadaj ten istý kód skupiny
aj v nastavení integrácie v Home Assistante (pole **Kód skupiny**). Home Assistant sa stane ďalším členom skupiny.

## Zmeny sa neprejavia hneď
Synchronizácia beží na pozadí po niekoľkých minútach. Hneď ju spustí **Synchronizovať teraz**
(v nastaveniach aj v Mojom zozname). Na telefóne s Androidom sa synchronizuje hlavne vtedy, keď je Kodi otvorené.

Prihlásenie k CZtoru a Traktu sa nesynchronizuje, páruje sa na každom zariadení zvlášť.

---
[Všetky návody](./) · [Česky](../cs/synchronizace)
