---
slug: stremio-webovy-prehravac
lang: sk
title: „⚠️ Vo webovom prehrávači sa neprehrá“
products: [stremio]
priority: 2
templates:
  stremio: |
    Od verzie 9.6.1 riadok „⚠️ Vo webovom prehrávači sa neprehrá“ pri streamoch nie je. Ak ho vidíš, máš staršiu aplikáciu Nokturno, aktualizuj ju.
    Súbory z vlastného úložiska a FastShare teraz prehrávaču odovzdáva aplikácia Nokturno.
    Stremio v prehliadači (web.stremio.com) neprehrá súbory .mkv, .avi a podobné, v aplikácii Stremio alebo Nuvio hrajú.
    Návod: https://nokturno-app.github.io/nokturno-napoveda/sk/stremio-webovy-prehravac
---

# „⚠️ Vo webovom prehrávači sa neprehrá“

## Čo to znamená
Od verzie 9.6.1 tento riadok pri streamoch **nie je**. Súbory z **vlastného úložiska** a z **FastShare** (aj Sdilej.cz)
teraz prehrávaču odovzdáva aplikácia Nokturno, prihlásenie do Stremia neodchádza.

Ak riadok pri streame stále vidíš, máš **staršiu aplikáciu** (do verzie 9.6.0). Aplikácia sa aktualizuje sama,
alebo ju stiahni znova, pozri [Aplikácia Nokturno](stremio-aplikace.md).

## Webový prehrávač a formát súboru
Stremio v prehliadači (web.stremio.com) neprehrá súbory `.mkv`, `.avi`, `.ts`, `.m2ts`, `.wmv` a `.flv`
(označí ich, že nie sú pre web). V aplikácii Stremio alebo Nuvio hrajú. O prehraní vo webovom prehrávači
teda rozhoduje formát súboru, nie zdroj.

## Čo urobiť
- Spusti stream v aplikácii Stremio alebo Nuvio.
- V prehliadači vyber iný stream, napríklad súbor `.mp4` z vlastného úložiska, alebo z voliteľného zdroja (WebShare, HellSpy).

## Vlastné úložisko nehrá ani v aplikácii
Úložisko musí byť dosiahnuteľné zo zariadenia, kde beží aplikácia Nokturno (tá v ňom hľadá súbory a odovzdáva ich prehrávaču).
Prehrávač potrebuje dosiahnuť len na aplikáciu. Keď je aplikácia doma, stačí adresa z domácej siete (`192.168.…`).
Pozri [Ako pripojiť vlastné úložisko](vlastni-uloziste.md).

---
[Všetky návody](./) · [Česky](../cs/stremio-webovy-prehravac)
