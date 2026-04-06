GbbOptimizer changes only following topics/properties in Victron System:

|  |  |  |
| --- | --- | --- |
| Topic | Property | Remarks |
| settings/0/Settings/CGwacs/BatteryLife/Schedule/Charge/{i}/Day | Schedule/Day |  |
| settings/0/Settings/CGwacs/BatteryLife/Schedule/Charge/{i}/Soc | Schedule/SOC limit |  |
| settings/0/Settings/CGwacs/BatteryLife/Schedule/Charge/{i}/Start | Schedule/Start time |  |
| settings/0/Settings/CGwacs/BatteryLife/Schedule/Charge/{i}/Duration | Schedule/Duration |  |
| settings/0/Settings/CGwacs/BatteryLife/MinimumSocLimit | ESS/Minimum SOC |  |
| settings/0/Settings/CGwacs/AcPowerSetPoint | ESS/Grid setpoint |  |
| system/0/Relay/0/State | Relay 1 | Price<0 |
| system/0/Relay/1/State | Relay 2 | Price<0 |
| vebus/{257 or other}/Mode | Inverter mode | Price<0 |
| settings/0/Settings/CGwacs/OvervoltageFeedIn | DC-coupled PV - feed in excess | Price<0 |
| vebus/{257 or other}/Ac/ActiveIn/CurrentLimit | MultiPlus/Input current limit |  |
| settings/0/Settings/SystemSetup/MaxChargeCurrent | DVCC/Maximum charge current |  |
