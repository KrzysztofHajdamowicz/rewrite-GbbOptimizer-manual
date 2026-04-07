---
title: "Hinen"
weight: 30
translationKey: "mapowania-hinen"
---

# Mode Mapping — Hinen

How GbbOptimizer modes translate to Hinen protocol settings.

## Mapping Table

| Operation | Work Mode | Charge/Discharge Enable | Charge/Discharge Start/End | Charge/Discharge SOC | Charge/Discharge Rate | AntiBackflow Enable | AntiBackflow Limit Rate |
|-----------|-----------|------------------------|---------------------------|---------------------|----------------------|--------------------|-----------------------|
| **Normal** | Self-consumption | no | — | 100% | — | — | — |
| **Charge** | Time period control | yes | yes | SOC% | = ChargeLimit / (MaxInverterChargeDC_kW or MaxBatteryChargeDC_kW) * 100% | no | — |
| **Discharge** | Time period control | yes | yes | SOC% | = -abs(DischargeLimit) / (MaxInverterChargeDC_kW or MaxBatteryChargeDC_kW) * 100%. DischargeLimit = Max GridSetpoint / Discharge (W). If discharge must be slower — the program calculates the value. | yes | same as Charge/Discharge Rate but > 0 |
| **DisableCharge** | Time period control | yes | yes | current SOC | 1% | no | — |

## Notes

- **Rate** is expressed as a percentage of the maximum inverter (or battery) power, not in watts
- In **Normal** mode the system returns to Self-consumption mode with SOC = 100% and Charge/Discharge disabled
- In **DisableCharge** mode SOC is set to the current level and Rate to a minimum of 1%
