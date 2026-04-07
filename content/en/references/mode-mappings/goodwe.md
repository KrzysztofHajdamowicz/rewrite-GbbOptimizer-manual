---
title: "GoodWe"
weight: 20
translationKey: "mapowania-goodwe"
---

# Mode Mapping — GoodWe

How GbbOptimizer modes translate to GoodWe protocol settings.

## Battery Charge-Discharge

| Operation | BatteryCDEnable | BatteryCDMode | BatteryCDPW |
|-----------|----------------|---------------|-------------|
| **Normal** | no | — | — |
| **Charge** | yes | 2 | ChargeLimitW |
| **Discharge** | yes | 3 | DischargeLimitW: Max GridSetpoint / Discharge (W). If discharge must be slower to last the full hour — the program calculates the appropriate value. On completion: restore previous value. |
| **DisableCharge** | yes | 2 | 0 |

## Missing Options

> [!WARNING]
> The GoodWe protocol does not support:
> - Target {{< glossary "SOC" >}} limit (TargetSOC)
> - Options for price < 0
