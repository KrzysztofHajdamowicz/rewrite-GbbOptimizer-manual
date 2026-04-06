# Map Protocol Modes to Inverter settings

---

## Passive Mode:

| Protocol Operation | Gdes: Grid setpoint | Blo: battery high | Bup: battery low | Gdzup: grid hight | Gdzlo: Grid low |
| --- | --- | --- | --- | --- | --- |
| Normal | Default Gridsetpoint (menu Discharge) | ChargeLimit or MaxBatteryChargePower or MaxInverterChargePower | -(DischargeLimit or MaxBatteryDischargePower or MaxInverterDischargeLimit) | MaxBuyPower or MaxInverterChargePower | -(MaxSellPower or MaxInverterDischargePowe) |
| Charge | =Gdzup | ChargeLimit or MaxBatteryChargePower or MaxInverterChargePower  -> corrected to ritch TargetSOC in full hour | 0 | InputLimit or MaxBuyPower or MaxInverterChargePower | 0 |
| Discharge | =Gdzlo | =Bup | -(DischargeLimit or MaxBatteryDischargePower or MaxInverterDischargeLimit)  -> corrected to ritch TargetSOC in full hour | 0 | -(MaxSellPower or MaxInverterDischargePowe) |
| DisableCharge | 0 | 0 | 0 | MaxBuyPower or MaxInverterChargePower | -(MaxSellPower or MaxInverterDischargePowe) |

### Remark

- if 'SofarSolar: Support for 5 parameters (not 3) in PassiveMode'
is unchecked than Gdzup and Gdzlo are not
changing (because are missing)
- Program setup 'StorageMode' to '3=PassiveMode' and (for 5 param support) 'ManagementMode' to '1=Manual'
