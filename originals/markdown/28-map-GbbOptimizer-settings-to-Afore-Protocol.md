|  |  |  |
| --- | --- | --- |
| Register | value | on end |
| AC charging maximum SOC | Charging: target MaxSOC |  |
| ACCharging start/end timeX | Charging: table of next charge 4 periods |  |
| Forced charging start/end timeX | Charging: table of next charge 4 periods |  |
| ACCharging power percentage | Charging: Input Limit (% based on MaxBuyPower(kW) or MaxBatteryChargeDC (kW)) | return to oryginal value |
| Forced charging power percentage | Charging: Charge Limit (% based on MaxBatteryChargeDC (kW)) | return to oryginal value |
| Minimum SOC for forced discharge | Discharge: targen MinSOC |  |
| Forced discharge start timeX | Discharge: table of next discharge 4 periods |  |
| Power grid power limit percentage | Discharge: GridSetpoint (% based on MaxSellPower (kW) or MaxBatteryDischargeDC (kW) |  |
| Maximum charging current | Disable charge: set 0 | return to oryginal value |

## Checklist:

- Timming DChg ON/OFF  = Enable
- PDisChgMax (Forced discharge power percentage) = 100%
