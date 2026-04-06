---
title: "Sofar"
weight: 40
translationKey: "sofar"
---

# Mode Mapping — Sofar

How GbbOptimizer modes translate to Sofar inverter settings in Passive Mode.

## Passive Mode

| Operation | Gdes (Grid setpoint) | Blo (Battery high) | Bup (Battery low) | Gdzup (Grid high) | Gdzlo (Grid low) |
|-----------|---------------------|--------------------|--------------------|-------------------|-----------------|
| **Normal** | Default {{< glossary "GridSetpoint" >}} (Discharge menu) | ChargeLimit or MaxBatteryChargePower or MaxInverterChargePower | -(DischargeLimit or MaxBatteryDischargePower or MaxInverterDischargeLimit) | MaxBuyPower or MaxInverterChargePower | -(MaxSellPower or MaxInverterDischargePower) |
| **Charge** | = Gdzup | ChargeLimit or MaxBatteryChargePower or MaxInverterChargePower (adjusted to reach target SOC in the full hour) | 0 | InputLimit or MaxBuyPower or MaxInverterChargePower | 0 |
| **Discharge** | = Gdzlo | = Bup | -(DischargeLimit or MaxBatteryDischargePower or MaxInverterDischargeLimit) (adjusted to reach target SOC in the full hour) | 0 | -(MaxSellPower or MaxInverterDischargePower) |
| **DisableCharge** | 0 | 0 | 0 | MaxBuyPower or MaxInverterChargePower | -(MaxSellPower or MaxInverterDischargePower) |

## Parameters

- **Gdes** — Grid setpoint: target grid energy exchange value
- **Blo** — Battery high: maximum battery charging power
- **Bup** — Battery low: maximum battery discharge power (negative value)
- **Gdzup** — Grid high: maximum grid import power
- **Gdzlo** — Grid low: maximum grid export power (negative value)

## Notes

> [!NOTE]
> If the option **"SofarSolar: Support for 5 parameters (not 3) in PassiveMode"** is unchecked, the Gdzup and Gdzlo parameters are not changed (because they are not available in 3-parameter mode).

The program sets:
- `StorageMode` = `3` (PassiveMode)
- `ManagementMode` = `1` (Manual) — only when 5-parameter support is enabled
