---
title: "Sofar"
weight: 60
translationKey: "sofar"
---

# Sofar

Configuring a Sofar inverter with GbbOptimizer. The Sofar inverter is controlled in **Passive Mode**.

## GbbOptimizer mode mapping to Sofar settings (Passive Mode)

The program sets `StorageMode = 3` (Passive Mode) and (when supporting 5 parameters) `ManagementMode = 1` (Manual).

| Operation | Gdes (Grid setpoint) | Blo (battery high) | Bup (battery low) | Gdzup (grid high) | Gdzlo (grid low) |
|-----------|---------------------|--------------------|--------------------|-------------------|------------------|
| **Normal** | Default {{< glossary "GridSetpoint" >}} (from Discharge menu) | ChargeLimit or MaxBatteryChargePower or MaxInverterChargePower | -(DischargeLimit or MaxBatteryDischargePower or MaxInverterDischargeLimit) | MaxBuyPower or MaxInverterChargePower | -(MaxSellPower or MaxInverterDischargePower) |
| **Charge** | = Gdzup | ChargeLimit (adjusted to reach TargetSOC in the full hour) | 0 | InputLimit or MaxBuyPower or MaxInverterChargePower | 0 |
| **Discharge** | = Gdzlo | = Bup | -(DischargeLimit, adjusted to reach TargetSOC in the full hour) | 0 | -(MaxSellPower or MaxInverterDischargePower) |
| **DisableCharge** | 0 | 0 | 0 | MaxBuyPower or MaxInverterChargePower | -(MaxSellPower or MaxInverterDischargePower) |

> [!NOTE]
> If the option "SofarSolar: Support for 5 parameters (not 3) in PassiveMode" is unchecked, the **Gdzup** and **Gdzlo** parameters are not changed (because they are not available in 3-parameter mode).
