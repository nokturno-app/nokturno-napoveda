---
slug: synchronizace
lang: cs
title: Synchronizace mezi zařízeními nefunguje
products: [kodi, ha]
priority: 2
templates:
  kodi: |
    Ahoj, synchronizace se ti nedaří. Nejjednodušší je středisko Dashboard Nokturna, Home Assistant k tomu potřeba není.
    1. Nokturno → Nastavení → Synchronizace: zapni Synchronizovat mezi více Kodi a jako Středisko synchronizace zvol Dashboard Nokturna.
    2. Na prvním Kodi dej Založit skupinu / otevřít připojení (ve starších verzích Založit skupinu) a opiš kód NKT-….
    3. Na dalších Kodi stejné nastavení a Připojit se ke skupině s tímto kódem, do 30 minut od založení.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/cs/synchronizace
    Tým Nokturno
---

# Synchronizace mezi zařízeními nefunguje

Synchronizace sdílí mezi tvými Kodi (a případně Home Assistantem) zhlédnuté a rozkoukané tituly,
Můj seznam a další okruhy. Všechno je v **Nokturno → Nastavení → Synchronizace**.

## Nejdřív zkontroluj
- Je zapnutý přepínač **Synchronizovat mezi více Kodi** (nestačí vyplněný kód)?
- Mají všechna zařízení stejné **Středisko synchronizace**?
- Kodi hlásí „Synchronizace není zapnutá nebo nastavená (u Home Assistantu adresa a klíč, u dashboardu kód skupiny)“?
  Chybí přepínač, kód skupiny, nebo adresa a klíč.

## Dashboard Nokturna (doporučeno, funguje odkudkoli)
1. Na prvním Kodi zvol středisko **Dashboard Nokturna** a dej **Založit skupinu / otevřít připojení**
   (ve starších verzích **Založit skupinu**). Ukáže se kód `NKT-…`, opiš si ho.
2. Na dalších Kodi stejné středisko, **Připojit se ke skupině** a zadej kód.
3. Nové zařízení se může připojit jen **30 minut** po založení. Později na prvním Kodi otevři připojení znovu
   stejným tlačítkem (ve starších verzích **Znovu otevřít připojení**). Kód zůstane stejný.

Kód je zároveň klíč k datům. Bez něj je nikdo nepřečte ani neobnoví, proto si ho uschovej.

## Home Assistant jako středisko
- Kodi musí být ve stejné domácí síti jako Home Assistant.
- **Adresa Home Assistantu:** když nefunguje název jako `homeassistant.local`, zadej IP adresu,
  například `http://192.168.1.10:8123`.
- **Klíč** musí být stejný jako v nastavení integrace Nokturno v Home Assistantu.

## Home Assistant ve skupině Dashboardu
Chceš mít kartu v Home Assistantu aktuální a synchronizuješ přes Dashboard Nokturna? Zadej týž kód skupiny
i v nastavení integrace v Home Assistantu (pole **Kód skupiny**). Home Assistant se stane dalším členem skupiny.

## Změny se neprojeví hned
Synchronizace běží na pozadí po několika minutách. Hned ji spustí **Synchronizovat teď**
(v nastavení i v Mém seznamu). Na telefonu s Androidem se synchronizuje hlavně ve chvíli, kdy je Kodi otevřené.

Přihlášení k CZtoru a Traktu se nesynchronizuje, páruje se na každém zařízení zvlášť.

---
[Všechny návody](../) · [Slovensky](../sk/synchronizace)
