---
title: "Hinen"
weight: 50
translationKey: "hinen"
---

# Hinen

Konfiguracja falownika Hinen z GbbOptimizer.

## Mapowanie trybów GbbOptimizer na ustawienia Hinen

GbbOptimizer steruje falownikiem Hinen ustawiając odpowiedni **Work Mode** oraz parametry ładowania/rozładowania.

| Operacja GbbOptimizer | Work Mode | Charge/Discharge Enable | Start/End | SOC | Rate | AntiBackflow Enable | AntiBackflow Limit Rate |
|------------------------|-----------|------------------------|-----------|-----|------|---------------------|------------------------|
| **Normal** | Self-consumption | Nie | — | 100% | — | — | — |
| **Charge** | Time period control | Tak | Tak | Docelowy SOC% | `ChargeLimit / (MaxInverterChargeDC lub MaxBatteryChargeDC) * 100%` | Nie | — |
| **Discharge** | Time period control | Tak | Tak | Docelowy SOC% | `DischargeLimit / (MaxInverterChargeDC lub MaxBatteryChargeDC) * 100%` (ujemna wartość) | Tak | Taki sam jak Rate, ale > 0 |
| **DisableCharge** | Time period control | Tak | Tak | Bieżący SOC | 1% | Nie | — |

### Uwagi do operacji Discharge

- Wartość `DischargeLimit` odpowiada parametrowi „Max {{< glossary "GridSetpoint" >}} / Discharge (W)"
- Jeśli rozładowanie musi być wolniejsze, aby wystarczyło na całą godzinę, program automatycznie koryguje tę wartość
- **AntiBackflow** jest włączany podczas rozładowania, aby kontrolować eksport do sieci
