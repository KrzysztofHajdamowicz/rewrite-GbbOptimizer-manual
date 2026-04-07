---
title: "Victron"
weight: 10
translationKey: "victron"
---

# Victron

{{< badge "victron-only" >}}

Konfiguracja falownika Victron z GbbOptimizer wymaga poprawnego ustawienia systemu {{< glossary "ESS" >}} oraz portalu {{< glossary "VRM" >}}.

## Lista kontrolna

Przed uruchomieniem GbbOptimizer sprawdź następujące ustawienia:

1. **Nie instaluj wersji Beta** oprogramowania sprzętowego (firmware)
2. **DESS musi być wyłączony**
3. **Schedules** — opcja „Self-consumption above limit" powinna być ustawiona na **PV** (a nie „PV & Battery"). Dzięki temu harmonogramy nie powodują rozładowania baterii w nocy
4. **Battery Life** w {{< glossary "ESS" >}} musi być **wyłączone** — wybierz tryb: `Optimized (without BatteryLife)`
5. **Log interval** (w VRM Online Portal) ustaw na **1 min**
6. **Uprawnienia VRM** — użytkownik musi mieć włączone prawo **Full Control**
7. **Zrestartuj Cerbo** po wprowadzeniu zmian

> [!WARNING]
> Nieprawidłowe ustawienia Battery Life lub Schedules mogą powodować nieoczekiwane rozładowanie baterii w nocy.

## Parametry Victron w GbbOptimizer

Szczegółowy opis parametrów Victron (VRM Portal Id, Installation Id, VRM Token itp.) znajdziesz w sekcji [Parametry instalacji]({{< relref "/instalacja/parametry-instalacji" >}}).

## Topiki MQTT zmieniane przez GbbOptimizer

GbbOptimizer modyfikuje **wyłącznie** poniższe topiki/właściwości w systemie Victron. Zmienna `{i}` oznacza numer harmonogramu (0-4).

### Harmonogramy ładowania (Schedules)

| Topik MQTT | Właściwość | Uwagi |
|------------|------------|-------|
| `settings/0/Settings/CGwacs/BatteryLife/Schedule/Charge/{i}/Day` | Dzień harmonogramu | |
| `settings/0/Settings/CGwacs/BatteryLife/Schedule/Charge/{i}/Soc` | Limit SOC | |
| `settings/0/Settings/CGwacs/BatteryLife/Schedule/Charge/{i}/Start` | Godzina rozpoczęcia | |
| `settings/0/Settings/CGwacs/BatteryLife/Schedule/Charge/{i}/Duration` | Czas trwania | |

### ESS i sterowanie mocą

| Topik MQTT | Właściwość | Uwagi |
|------------|------------|-------|
| `settings/0/Settings/CGwacs/BatteryLife/MinimumSocLimit` | {{< glossary "ESS" >}} / Minimum SOC | |
| `settings/0/Settings/CGwacs/AcPowerSetPoint` | {{< glossary "ESS" >}} / {{< glossary "GridSetpoint" >}} | |
| `settings/0/Settings/SystemSetup/MaxChargeCurrent` | DVCC / Maksymalny prąd ładowania | |
| `vebus/{257 or other}/Ac/ActiveIn/CurrentLimit` | MultiPlus / Limit prądu wejściowego | |

### Sterowanie przy ujemnych cenach (Price < 0)

| Topik MQTT | Właściwość | Uwagi |
|------------|------------|-------|
| `system/0/Relay/0/State` | Relay 1 | Aktywowany gdy cena < 0 |
| `system/0/Relay/1/State` | Relay 2 | Aktywowany gdy cena < 0 |
| `vebus/{257 or other}/Mode` | Tryb falownika | Aktywowany gdy cena < 0 |
| `settings/0/Settings/CGwacs/OvervoltageFeedIn` | DC-coupled PV — feed in excess | Aktywowany gdy cena < 0 |

> [!NOTE]
> Numer instancji VE.Bus (domyślnie `257`) może się różnić w Twoim systemie. Sprawdź go w parametrach instalacji jako „Numer VRM Instance urządzenia VE.Bus System".
