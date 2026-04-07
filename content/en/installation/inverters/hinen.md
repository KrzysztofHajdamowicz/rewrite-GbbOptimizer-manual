---
title: "Hinen"
weight: 50
translationKey: "hinen"
---

# Hinen

Configuring a Hinen inverter with GbbOptimizer.

## GbbOptimizer mode mapping to Hinen settings

GbbOptimizer controls the Hinen inverter by setting the appropriate **Work Mode** and charge/discharge parameters.

| GbbOptimizer operation | Work Mode | Charge/Discharge Enable | Start/End | SOC | Rate | AntiBackflow Enable | AntiBackflow Limit Rate |
|------------------------|-----------|------------------------|-----------|-----|------|---------------------|------------------------|
| **Normal** | Self-consumption | No | — | 100% | — | — | — |
| **Charge** | Time period control | Yes | Yes | Target SOC% | `ChargeLimit / (MaxInverterChargeDC or MaxBatteryChargeDC) * 100%` | No | — |
| **Discharge** | Time period control | Yes | Yes | Target SOC% | `DischargeLimit / (MaxInverterChargeDC or MaxBatteryChargeDC) * 100%` (negative value) | Yes | Same as Rate, but > 0 |
| **DisableCharge** | Time period control | Yes | Yes | Current SOC | 1% | No | — |

### Notes on the Discharge operation

- The `DischargeLimit` value corresponds to the "Max {{< glossary "GridSetpoint" >}} / Discharge (W)" parameter
- If the discharge must be slower to last the full hour, the program automatically corrects this value
- **AntiBackflow** is enabled during discharge to control grid export
