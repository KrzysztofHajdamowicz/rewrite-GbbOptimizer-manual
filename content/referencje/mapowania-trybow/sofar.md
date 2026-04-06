---
title: "Sofar"
weight: 40
---

# Mapowanie trybow — Sofar

Jak tryby GbbOptimizer przekladaja sie na ustawienia falownika Sofar w trybie pasywnym (Passive Mode).

## Tryb pasywny (Passive Mode)

| Operacja | Gdes (Grid setpoint) | Blo (Battery high) | Bup (Battery low) | Gdzup (Grid high) | Gdzlo (Grid low) |
|----------|---------------------|--------------------|--------------------|-------------------|-----------------|
| **Normal** | Default {{< glossary "GridSetpoint" >}} (menu Discharge) | ChargeLimit lub MaxBatteryChargePower lub MaxInverterChargePower | -(DischargeLimit lub MaxBatteryDischargePower lub MaxInverterDischargeLimit) | MaxBuyPower lub MaxInverterChargePower | -(MaxSellPower lub MaxInverterDischargePower) |
| **Charge** | = Gdzup | ChargeLimit lub MaxBatteryChargePower lub MaxInverterChargePower (korygowane, aby osiagnac docelowy SOC w pelnej godzinie) | 0 | InputLimit lub MaxBuyPower lub MaxInverterChargePower | 0 |
| **Discharge** | = Gdzlo | = Bup | -(DischargeLimit lub MaxBatteryDischargePower lub MaxInverterDischargeLimit) (korygowane, aby osiagnac docelowy SOC w pelnej godzinie) | 0 | -(MaxSellPower lub MaxInverterDischargePower) |
| **DisableCharge** | 0 | 0 | 0 | MaxBuyPower lub MaxInverterChargePower | -(MaxSellPower lub MaxInverterDischargePower) |

## Parametry

- **Gdes** — Grid setpoint: docelowa wartosc wymiany energii z siecia
- **Blo** — Battery high: maksymalna moc ladowania baterii
- **Bup** — Battery low: maksymalna moc rozladowania baterii (wartosc ujemna)
- **Gdzup** — Grid high: maksymalna moc poboru z sieci
- **Gdzlo** — Grid low: maksymalna moc eksportu do sieci (wartosc ujemna)

## Uwagi

> [!NOTE]
> Jesli opcja **"SofarSolar: Support for 5 parameters (not 3) in PassiveMode"** jest odznaczona, parametry Gdzup i Gdzlo nie sa zmieniane (poniewaz nie sa dostepne w trybie 3-parametrowym).

Program ustawia:
- `StorageMode` = `3` (PassiveMode)
- `ManagementMode` = `1` (Manual) — tylko przy obsludze 5 parametrow
