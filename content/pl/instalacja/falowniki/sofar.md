---
title: "Sofar"
weight: 60
translationKey: "sofar"
---

# Sofar

Konfiguracja falownika Sofar z GbbOptimizer. Falownik Sofar jest sterowany w trybie **Passive Mode**.

## Mapowanie trybów GbbOptimizer na ustawienia Sofar (Passive Mode)

Program ustawia `StorageMode = 3` (Passive Mode) oraz (przy obsłudze 5 parametrów) `ManagementMode = 1` (Manual).

| Operacja | Gdes (Grid setpoint) | Blo (battery high) | Bup (battery low) | Gdzup (grid high) | Gdzlo (grid low) |
|----------|---------------------|--------------------|--------------------|-------------------|------------------|
| **Normal** | Domyślny {{< glossary "GridSetpoint" >}} (z menu Discharge) | ChargeLimit lub MaxBatteryChargePower lub MaxInverterChargePower | -(DischargeLimit lub MaxBatteryDischargePower lub MaxInverterDischargeLimit) | MaxBuyPower lub MaxInverterChargePower | -(MaxSellPower lub MaxInverterDischargePower) |
| **Charge** | = Gdzup | ChargeLimit (korygowane, aby osiągnąć TargetSOC w pełnej godzinie) | 0 | InputLimit lub MaxBuyPower lub MaxInverterChargePower | 0 |
| **Discharge** | = Gdzlo | = Bup | -(DischargeLimit, korygowane, aby osiągnąć TargetSOC w pełnej godzinie) | 0 | -(MaxSellPower lub MaxInverterDischargePower) |
| **DisableCharge** | 0 | 0 | 0 | MaxBuyPower lub MaxInverterChargePower | -(MaxSellPower lub MaxInverterDischargePower) |

> [!NOTE]
> Jeśli opcja „SofarSolar: Support for 5 parameters (not 3) in PassiveMode" jest odznaczona, parametry **Gdzup** i **Gdzlo** nie są zmieniane (ponieważ nie są dostępne w trybie 3-parametrowym).
