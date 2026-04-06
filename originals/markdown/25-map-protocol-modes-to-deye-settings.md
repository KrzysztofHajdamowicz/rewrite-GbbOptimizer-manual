# Map Protocol Modes to Deye settings

---

## Solarman or DeyeCloud (with new connection method):

| Protocol Operation | Work Mode | GridCharge in TimeOfUse | Time in TimeOfUse | SOC in TimeOfUse | Power in TimeOfUse | Charge A (Amper) | MaxSellPower |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal |  | no | yes | 5%\* | 'Max Battery Discharge', if missing: 'Max Inverter Discharge' | no change |  |
| Charge |  | yes | yes | SOC% | ChargeLimitW, if missing: 'Max Battery Charge', if missing 'Max Inverter Charge' | ChargeLimitW, if missing: 'Max Battery Charge', if missing 'Max Inverter Charge' |  |
| Discharge | SellingFirst**,** after finish: is changed to previous value | no | yes | SOC% | 'Max Battery Discharge', if missing: 'Max Inverter Discharge' | no change  KeepSOC: 0W | - 'Max GridSetpoint / Discharge (W)'  - If discharge must be slower to last whole hour then program calculate this value; After discharge is changed to prev value |
| DisableCharge |  | no | yes | 5%\* | -'Max GridSetpoint / Discharge (W)' | change to 0, after finish: is changed to previous value |  |

(\*) 5% can be change to other value - parameter 'Default MinSOC after discharge' in 'Discharge Plan'.

Price<0:

- (optional): switch off 'SolarSell' + switch on 'MI export to Grid cutoff'
- (optional): change LV1 to 270V, this causes disconnect from
  grid (off-grid). When Price<0 has finished then program setup
  LV1 to previous value

Generator:

- On: Set GEN in TimeOfUser (only during Operation="Charge") + Set GenSOC to CurrSOC+1
- PurchasePrice>LimitPrice: change LV1 to 270V (disconnect from grid to start generator) or set NoBatt

Others:

- "Switch off peak-shaving during discharge battery to grid": switch off Peak-Shaving
- "Change Mode to 'Zero Export To CT' during charge battery from grid": change WorkMode
- "Input Limit (A)": Grid Peak Shaving (W)

---

## DeyeCloud only (old, limited DeyeCloud API, depreciated)

##

| Protocol Operation | Work Mode | GridCharge in TimeOfUse | Time in TimeOfUse | SOC in TimeOfUse | Power in TimeOfUse | Charge A (Amper) | MaxSellPower |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Normal |  | no | yes | 5%\* | Max Battery Discharge | no change |  |
| Charge |  | yes | yes | SOC% | ChargeLimitW, if missing: Max Battery Discharge | no change |  |
| Discharge | SellingFirst**,** after finish: is **changed to ZeroExportToCT** | no | yes | SOC% | Sell Power, if missing: Max Battery Discharge | no change | - 'Max GridSetpoint / Discharge (W)'  - If discharge must be slower to last whole hour then program calculate this value; After discharge is changed to 'MaxSellPower after 'Discharge'' |
| DisableCharge |  | no | yes | 5%\* | -'Max GridSetpoint / Discharge (W)' | change to 0, after finish: is changed to 'MaxChargePower after 'Disable battery charge' |  |

(\*) 5% can be change to other value - parameter 'Default MinSOC after discharge' in 'Discharge Plan'.

## Price<0:

- (optional): switch off 'SolarSell' ~~+ switch on 'MI export to Grid cutoff'~~
- ~~(optional): change LV1 to 270V, this causes disconnect from
  grid (off-grid). When Price<0 has finished then program setup
  LV1 to previous value~~

Generator:

- On: Set GEN in TimeOfUser (only during Operation="Charge")
- ~~PurchasePrice>LimitPrice: change LV1 to 270V (disconnect from grid to start generator) or set NoBatt~~

Others:

- ~~"Switch off peak-shaving during discharge battery to grid": switch off Peak-Shaving~~
- "Change Mode to 'Zero Export To CT' during charge battery from grid": change WorkMode
- ~~"Input Limit (A)": Grid Peak Shaving (W)~~

---

## SolarAssistant only:

| Protocol Operation | Work Mode | GridCharge in TimeOfUse | Time in TimeOfUse | SOC in TimeOfUse | ~~Power in TimeOfUse (\*\*)~~ | Charge A (Amper) |
| --- | --- | --- | --- | --- | --- | --- |
| Normal |  | no | yes | 5%\* | ~~-**'**Default Gridsetpoint after discharge (W)**'**~~ | no change |
| Charge |  | **yes** | yes | SOC% | ~~ChargeLimitW~~ | no change |
| Discharge | **SellingFirst,** after finish: is changed to previous value | no | yes | SOC% | ~~- 'Max GridSetpoint / Discharge (W)'~~ | no change |
| DisableCharge |  | no | yes | 5%\* | ~~- 'Max GridSetpoint / Discharge (W)'~~ | **change to 0**, after finish: is changed to previous value |

(\*) 5% can be change to other value - parameter 'Default MinSOC after discharge' in 'Discharge Plan'.

## ~~Price<0:~~

- ~~(optional): switch off 'SolarSell' + switch on 'MI export to Grid cutoff'~~
- ~~(optional): change LV1 to 270V, this causes disconnect from
  grid (off-grid). When Price<0 has finished then program setup
  LV1 to previous value~~

~~Generator:~~

- ~~On: Set GEN in TimeOfUser (only during Operation="Charge")~~
- ~~PurchasePrice>LimitPrice: change LV1 to 270V (disconnect from grid to start generator) or set NoBatt~~

---
