---
title: "Sofar"
weight: 40
translationKey: "mapowania-sofar"
---

# Modusmapping — Sofar

Hoe de GbbOptimizer-modi zich vertalen naar de instellingen van de Sofar-omvormer in Passive Mode.

## Passive Mode

| Operatie | Gdes (Grid setpoint) | Blo (Battery high) | Bup (Battery low) | Gdzup (Grid high) | Gdzlo (Grid low) |
|----------|---------------------|--------------------|--------------------|-------------------|-----------------|
| **Normal** | Default {{< glossary "GridSetpoint" >}} (menu Discharge) | ChargeLimit of MaxBatteryChargePower of MaxInverterChargePower | -(DischargeLimit of MaxBatteryDischargePower of MaxInverterDischargeLimit) | MaxBuyPower of MaxInverterChargePower | -(MaxSellPower of MaxInverterDischargePower) |
| **Charge** | = Gdzup | ChargeLimit of MaxBatteryChargePower of MaxInverterChargePower (gecorrigeerd om de doel-SOC binnen een vol uur te bereiken) | 0 | InputLimit of MaxBuyPower of MaxInverterChargePower | 0 |
| **Discharge** | = Gdzlo | = Bup | -(DischargeLimit of MaxBatteryDischargePower of MaxInverterDischargeLimit) (gecorrigeerd om de doel-SOC binnen een vol uur te bereiken) | 0 | -(MaxSellPower of MaxInverterDischargePower) |
| **DisableCharge** | 0 | 0 | 0 | MaxBuyPower of MaxInverterChargePower | -(MaxSellPower of MaxInverterDischargePower) |

## Parameters

- **Gdes** — Grid setpoint: doelwaarde voor de energie-uitwisseling met het net
- **Blo** — Battery high: maximaal batterijlaadvermogen
- **Bup** — Battery low: maximaal batterijontlaadvermogen (negatieve waarde)
- **Gdzup** — Grid high: maximaal opnamevermogen uit het net
- **Gdzlo** — Grid low: maximaal exportvermogen naar het net (negatieve waarde)

## Opmerkingen

> [!NOTE]
> Als de optie **„SofarSolar: Support for 5 parameters (not 3) in PassiveMode"** is uitgeschakeld, worden Gdzup en Gdzlo niet gewijzigd (omdat ze niet beschikbaar zijn in de 3-parameter-modus).

Het programma stelt in:
- `StorageMode` = `3` (PassiveMode)
- `ManagementMode` = `1` (Manual) — alleen bij ondersteuning van 5 parameters
