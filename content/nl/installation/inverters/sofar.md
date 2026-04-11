---
title: "Sofar"
weight: 60
translationKey: "sofar"
---

# Sofar

Configuratie van de Sofar-omvormer met GbbOptimizer. De Sofar-omvormer wordt aangestuurd in **Passive Mode**.

## Mapping van GbbOptimizer-modi op Sofar-instellingen (Passive Mode)

Het programma stelt `StorageMode = 3` (Passive Mode) in en (bij ondersteuning van 5 parameters) `ManagementMode = 1` (Manual).

| Bewerking | Gdes (Grid setpoint) | Blo (battery high) | Bup (battery low) | Gdzup (grid high) | Gdzlo (grid low) |
|----------|---------------------|--------------------|--------------------|-------------------|------------------|
| **Normal** | Standaard-{{< glossary "GridSetpoint" >}} (uit het menu Discharge) | ChargeLimit of MaxBatteryChargePower of MaxInverterChargePower | -(DischargeLimit of MaxBatteryDischargePower of MaxInverterDischargeLimit) | MaxBuyPower of MaxInverterChargePower | -(MaxSellPower of MaxInverterDischargePower) |
| **Charge** | = Gdzup | ChargeLimit (gecorrigeerd om TargetSOC in een heel uur te bereiken) | 0 | InputLimit of MaxBuyPower of MaxInverterChargePower | 0 |
| **Discharge** | = Gdzlo | = Bup | -(DischargeLimit, gecorrigeerd om TargetSOC in een heel uur te bereiken) | 0 | -(MaxSellPower of MaxInverterDischargePower) |
| **DisableCharge** | 0 | 0 | 0 | MaxBuyPower of MaxInverterChargePower | -(MaxSellPower of MaxInverterDischargePower) |

> [!NOTE]
> Als de optie „SofarSolar: Support for 5 parameters (not 3) in PassiveMode" niet is aangevinkt, worden de parameters **Gdzup** en **Gdzlo** niet gewijzigd (omdat ze niet beschikbaar zijn in de 3-parameter-modus).
