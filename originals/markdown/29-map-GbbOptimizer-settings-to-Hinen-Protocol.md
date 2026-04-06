# Map Protocol Modes to Hinen settings

---

##

| Protocol Operation | Work Mode | Charge/Discharge  Enable | Charge/Discharge  Start/End | Charge/Discharge  SOC | Charge/Discharge  Rate | AntiBackflow  Enable | AntiBackflow  Limit Rate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal | Self-consumtion | no |  | 100% |  |  |  |
| Charge | Time period control | yes | yes | SOC% | = ChargeLimit/ (MaxInverterChargeDC\_kW or MaxBatteryChargeDC\_kW) \* 100% | no |  |
| Discharge | Time period control | yes | yes | SOC% | = - abs(DischargeLimit)/ (MaxInverterChargeDC\_kW or MaxBatteryChargeDC\_kW) \* 100%    DischargeLimit= 'Max GridSetpoint / Discharge (W)' - If discharge must be slower to last whole hour then program calculate this value | yes | same as Charge/Discharge Rate, but >0 |
| DisableCharge | Time period control | yes | yes | Current SOC | 1% | no |  |
