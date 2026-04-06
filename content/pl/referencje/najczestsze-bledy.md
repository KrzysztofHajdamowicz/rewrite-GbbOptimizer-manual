---
title: "Najczęstsze błędy"
weight: 60
translationKey: "najczestsze-bledy"
---

# Najczęstsze błędy

Lista najczęściej spotykanych komunikatów o błędach w GbbOptimizer, ich źródeł i możliwych rozwiązań.

## Solarman

| Komunikat | Opis |
|-----------|------|
| `SolarmanError: Solarman timeout!` | Solarman nie może wysłać danych do falownika. Sprawdź sieć lokalną. |
| `Solarman error: 2101040-device not found` | Falownik nie wysyła danych do Solarmana. Sprawdź połączenie sieciowe falownika. |
| `Response status code: 503 / 500 / 504` | API Solarman nie działa poprawnie. Problem po stronie Solarmana — poczekaj i spróbuj ponownie. |

## DeyeCloud

| Komunikat | Opis |
|-----------|------|
| `DeyeCloud error: timeout` | DeyeCloud nie może wysłać danych do falownika. Sprawdź sieć lokalną. |
| `DeyeCloud error: 2104006-device offline` | Falownik nie wysyła danych do DeyeCloud. Sprawdź połączenie sieciowe falownika. |
| `DeyeCloud error: 2101042-auth no operation permission` | Za mało uprawnień dla konta DeyeCloud (np. konto nadane przez instalatora). Skontaktuj się z instalatorem w celu nadania pełnych uprawnień. |

## GbbConnect2

| Komunikat | Opis |
|-----------|------|
| `Mqtt to GbbConnect2: timeout!` | GbbOptimizer nie może się połączyć z lokalnym {{< glossary "GbbConnect2" >}}. Sprawdź, czy GbbConnect2 jest uruchomiony. |
| `GbbConnect2Error: Connection timed out 192.168.x.xx:8899` | {{< glossary "GbbConnect2" >}} nie może się połączyć z donglem Deye. Sprawdź, czy dongle jest w sieci. |

## Victron

| Komunikat | Opis |
|-----------|------|
| `Victron Mqtt: timeout! (15 sec)` | GbbOptimizer nie może się połączyć z Cerbo przez serwery MQTT Victrona. Sprawdź sieć lokalną i dostęp zdalny w {{< glossary "VRM" >}}. |
| `Error during checking whether Schedules reached Cerbo successfully` | Harmonogramy ESS nie dotarły do Cerbo. Sprawdź połączenie Cerbo z internetem. |

## Ceny energii

| Komunikat | Źródło | Opis |
|-----------|--------|------|
| `Get Prices: The SSL connection could not be established` | ENTSO-E | API ENTSO-E z cenami nie działa. Problem po stronie dostawcy. |
| `Get Prices: Proba polaczenia nie powiodla sie` | ENTSO-E | API ENTSO-E niedostępne. |
| `Get Prices: HTTP POST ... Gateway timeout / 502 Bad Gateway` | Tibber | API Tibber z cenami nie działa. |
| `Get Prices: Response status code: 502 (Bad Gateway)` | AU Amber | API Amber z cenami nie działa. |

## Inne

| Komunikat | Źródło | Opis |
|-----------|--------|------|
| `Solcast.com: Too many requests` | Solcast | Osiągnięty limit 10 zapytań dziennie do Solcast.com. Poczekaj do północy. |
| `ERROR from Cache: Response status code: 500` | Pstryk | Błąd po stronie API Pstryka. |
| `B0220-System function downgrade` | Hinen | API Hinen jest aktualizowane. Poczekaj aż aktualizacja się zakończy. |

> [!NOTE]
> Komunikaty o błędach są wysyłane e-mailem z programu. Większość błędów typu "timeout" i "device offline" jest związana z problemami sieci lokalnej — sprawdź połączenie falownika i routera.
