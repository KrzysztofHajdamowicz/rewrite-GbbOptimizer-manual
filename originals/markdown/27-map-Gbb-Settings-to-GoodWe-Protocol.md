# Map Protocol Modes to Goodwe settings

---

##

Battery Charge-Discharge

| Protocol Operation | BatteryCDEnable | BatteryCDMode | BatteryCDPW |
| --- | --- | --- | --- |
| Normal | no |  |  |
| Charge | yes | 2 | ChargeLimitW |
| Discharge | yes | 3 | DischargeLimitW:  - 'Max GridSetpoint / Discharge (W)'  - If discharge must be slower to last whole hour then program calculate this value; After discharge is changed to prev value |
| DisableCharge | yes | 2 | 0 |

Missing options:
- limit battery TargetSOC
- all options for Price<0
