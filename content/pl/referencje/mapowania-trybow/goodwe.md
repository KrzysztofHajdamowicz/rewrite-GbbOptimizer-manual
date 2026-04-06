---
title: "GoodWe"
weight: 20
translationKey: "mapowania-goodwe"
---

# Mapowanie trybów — GoodWe

Jak tryby GbbOptimizer przekładają się na ustawienia protokołu GoodWe.

## Battery Charge-Discharge

| Operacja | BatteryCDEnable | BatteryCDMode | BatteryCDPW |
|----------|----------------|---------------|-------------|
| **Normal** | nie | — | — |
| **Charge** | tak | 2 | ChargeLimitW |
| **Discharge** | tak | 3 | DischargeLimitW: Max GridSetpoint / Discharge (W). Jeśli rozładowanie musi być wolniejsze, aby trwało całą godzinę — program oblicza odpowiednią wartość. Po zakończeniu: powrót do poprzedniej wartości. |
| **DisableCharge** | tak | 2 | 0 |

## Brakujące opcje

> [!WARNING]
> Protokół GoodWe nie obsługuje:
> - Limitu docelowego {{< glossary "SOC" >}} (TargetSOC)
> - Opcji dla ceny < 0
