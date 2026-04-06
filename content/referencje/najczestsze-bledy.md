---
title: "Najczestsze bledy"
weight: 60
---

# Najczestsze bledy

Lista najczesciej spotykanych komunikatow o bledach w GbbOptimizer, ich zrodel i mozliwych rozwiazani.

## Solarman

| Komunikat | Opis |
|-----------|------|
| `SolarmanError: Solarman timeout!` | Solarman nie moze wyslac danych do falownika. Sprawdz siec lokalna. |
| `Solarman error: 2101040-device not found` | Falownik nie wysyla danych do Solarmana. Sprawdz polaczenie sieciowe falownika. |
| `Response status code: 503 / 500 / 504` | API Solarman nie dziala poprawnie. Problem po stronie Solarmana — poczekaj i sprobuj ponownie. |

## DeyeCloud

| Komunikat | Opis |
|-----------|------|
| `DeyeCloud error: timeout` | DeyeCloud nie moze wyslac danych do falownika. Sprawdz siec lokalna. |
| `DeyeCloud error: 2104006-device offline` | Falownik nie wysyla danych do DeyeCloud. Sprawdz polaczenie sieciowe falownika. |
| `DeyeCloud error: 2101042-auth no operation permission` | Za malo uprawnien dla konta DeyeCloud (np. konto nadane przez instalatora). Skontaktuj sie z instalatorem w celu nadania pelnych uprawnien. |

## GbbConnect2

| Komunikat | Opis |
|-----------|------|
| `Mqtt to GbbConnect2: timeout!` | GbbOptimizer nie moze sie polaczyc z lokalnym {{< glossary "GbbConnect2" >}}. Sprawdz, czy GbbConnect2 jest uruchomiony. |
| `GbbConnect2Error: Connection timed out 192.168.x.xx:8899` | {{< glossary "GbbConnect2" >}} nie moze sie polaczyc z donglem Deye. Sprawdz, czy dongle jest w sieci. |

## Victron

| Komunikat | Opis |
|-----------|------|
| `Victron Mqtt: timeout! (15 sec)` | GbbOptimizer nie moze sie polaczyc z Cerbo przez serwery MQTT Victrona. Sprawdz siec lokalna i dostep zdalny w {{< glossary "VRM" >}}. |
| `Error during checking whether Schedules reached Cerbo successfully` | Harmonogramy ESS nie dotarly do Cerbo. Sprawdz polaczenie Cerbo z internetem. |

## Ceny energii

| Komunikat | Zrodlo | Opis |
|-----------|--------|------|
| `Get Prices: The SSL connection could not be established` | ENTSO-E | API ENTSO-E z cenami nie dziala. Problem po stronie dostawcy. |
| `Get Prices: Proba polaczenia nie powiodla sie` | ENTSO-E | API ENTSO-E niedostepne. |
| `Get Prices: HTTP POST ... Gateway timeout / 502 Bad Gateway` | Tibber | API Tibber z cenami nie dziala. |
| `Get Prices: Response status code: 502 (Bad Gateway)` | AU Amber | API Amber z cenami nie dziala. |

## Inne

| Komunikat | Zrodlo | Opis |
|-----------|--------|------|
| `Solcast.com: Too many requests` | Solcast | Osiagniety limit 10 zapytan dziennie do Solcast.com. Poczekaj do polnocy. |
| `ERROR from Cache: Response status code: 500` | Pstryk | Blad po stronie API Pstryka. |
| `B0220-System function downgrade` | Hinen | API Hinen jest aktualizowane. Poczekaj az aktualizacja sie zakonczy. |

> [!NOTE]
> Komunikaty o bledach sa wysylane emailem z programu. Wiekszsc bledow typu "timeout" i "device offline" jest zwiazana z problemami sieci lokalnej — sprawdz polaczenie falownika i routera.
