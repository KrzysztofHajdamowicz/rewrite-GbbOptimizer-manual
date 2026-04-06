---
title: "Deye"
weight: 20
---

# Deye

{{< badge "deye-only" >}}

Falowniki hybrydowe Deye mogą być podłączone do GbbOptimizer na kilka sposobów. Na tej stronie znajdziesz listę kontrolną ustawień falownika oraz porównanie metod połączenia.

## Lista kontrolna

Przed uruchomieniem GbbOptimizer sprawdź na falowniku Deye:

1. **Tryb pracy** — `Zero export to CT` lub `Zero export to Loads` (nie „Selling First”!)

   > [!WARNING]
   > Nie sprawdzaj trybu pracy podczas aktywnego rozładowania — GbbOptimizer tymczasowo zmienia tryb.

2. **TimeOfUse** — musi być **włączony**
3. **TimeOfUse** — ustawiony na **%** (a nie V), chyba że zdefiniowano mapowanie SOC do V
4. **System Work Mode** (Harmonogram) — włączony dla **wszystkich 7 dni** tygodnia
5. **Energy pattern** — `Load First`
6. **SolarSell / Sprzedaj energię** — **zaznaczone**
7. **Grid Charge (Opłata sieciowa)** — `Enable`
8. **Grid Start, Battery Restart** — wartości **niższe niż** {{< glossary "MinSOC" >}}
9. **Interwał wysyłania danych** — co **1 min** (domyślnie co 5 min — trzeba zmienić)
10. **Copilot** — musi być **wyłączony**

## Metody połączenia — porównanie

Falownik Deye można podłączyć do GbbOptimizer na cztery sposoby:

|  | [Solarman]({{< relref "/instalacja/metody-polaczenia/solarman" >}}) / [DeyeCloud]({{< relref "/instalacja/metody-polaczenia/deye-cloud" >}}) | [GbbConnect2]({{< relref "/instalacja/metody-polaczenia/gbbconnect2" >}}) | [DongleDirect]({{< relref "/instalacja/metody-polaczenia/dongle-direct" >}}) | HomeAssistant / {{< glossary "SolarAssistant" >}} |
|--|--|--|--|--|
| **Dane z GbbOptimizer do falownika** | GbbOptimizer → DeyeCloud → Solarman → Dongle → Falownik | GbbOptimizer → GbbConnect2 → Dongle → Falownik | GbbOptimizer → Dongle → Falownik | GbbOptimizer → HA Automation → Falownik |
| **Dane z falownika do GbbOptimizer** | Falownik → Dongle → Solarman → DeyeCloud → GbbOptimizer | Falownik → Dongle → GbbConnect2 → GbbOptimizer | Falownik → Dongle → GbbOptimizer | Falownik → HA Automation → GbbOptimizer |
| **Dane z DeyeCloud/Solarman do falownika** | DeyeCloud → Solarman → Dongle → Falownik | DeyeCloud → Solarman → Dongle → Falownik | DeyeCloud → Solarman → GbbOptimizer → Dongle → Falownik | N/A |
| **Dane z falownika do DeyeCloud/Solarman** | Falownik → Dongle → Solarman → DeyeCloud | Falownik → Dongle → Solarman → DeyeCloud | Falownik → Dongle → GbbOptimizer → Solarman → DeyeCloud | N/A |
| **Problem z rozłączaniem Dongle** | Tak | Nie | Tak | Nie |
| **Wymagane oprogramowanie** | Brak | GbbConnect2 w sieci lokalnej | Brak | HomeAssistant w sieci lokalnej |
| **Dane przechodzą przez serwery chińskie** | Tak | Tak (nie, jeśli zablokujesz Dongle na firewallu) | Twój wybór | Nie |
| **Zmiana parametrów poza domem** | Tak | Nie (ale możesz używać Solarman/DeyeCloud równolegle) | Twój wybór | Tak |

> [!NOTE]
> Szczegółowe instrukcje konfiguracji każdej metody znajdziesz w sekcji [Metody połączenia]({{< relref "/instalacja/metody-polaczenia" >}}).
