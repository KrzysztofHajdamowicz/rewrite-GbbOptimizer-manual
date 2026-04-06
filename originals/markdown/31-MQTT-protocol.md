## Mqtt

GbbOptimizer (ex. GbbVictronWeb) uses Mqtt protocol to receive requests from external program (e.g. Home Assistant).

External program should connect to Mqtt with:

- Address: [see here](https://gbboptimizer.gbbsoft.pl/Manual?PageNo=14)
- Port: 8883
- User: {PlantId}
- Password: {PlantToken}
- UseTTL: true
- ClientID should end with: \_{PlantId}

# 1. Signals send from mqtt to external program:

- Signals must be first enable in 'Discharge Plan' module.
- Data are calculated based on forecast for current hour.
- Signals are send every hour.
- Given signal is not send if "X" is not defined in "Discharge Plan" (field is empty in form)

External program can subscribe to following signals:

|  |  |
| --- | --- |
| Topic | Payload |
| {PlantId}/signals/SOCHigherEqThanX | "1" if SOC >= x, otherwise "0" |
| {PlantId}/signals/SOCLowerEqThanX | "1" if SOC <= x, otherwise "0" |
| {PlantId}/signals/SellingPriceHigherEqThanX | "1" if SellingPrice >= x, otherwise "0" |
| {PlantId}/signals/SellingPriceLowerEqThanX | "1" if SellingPrice <= x, otherwise "0" |
| {PlantId}/signals/FromGridHigherEqThanX | "1" if FromGrid >= x, otherwise "0" |
| {PlantId}/signals/ToGridHigherEqThanX | "1" if ToGrid >= x, otherwise "0" |

Program also send json data on topic: {PlantId}/signals/data

|  |  |  |
| --- | --- | --- |
| Key | Type | Value |
| SOC | int | SOC value (%) on start of hour |
| SellingPrice | decimal | Current SellingPrice (missing if no price) |
| PurchasePrice | decimal | Current PurchasePrice (missing if no price) |
| FromGrid\_kWh | decimal | Forecasted FromGrid |
| ToGrid\_kWh | decimal | Forecasted ToGrid\_kWh |

# 2. Requests to program by mqtt:

- Send requests to {PlantId}/ha\_gbb/dataserver/serverrequest
- Listen for answers on {PlantId}/ha\_gbb/dataserver/serverresponse

For compatible with previous versions program also support following (not recommended):

- Send requests to {PlantId}/dataserver/serverrequest
- Listen for answers on {PlantId}/dataserver/serverresponse

## Response with error

For every request there can be response with error:

{"Operation": “xxx”, "Status": “ERROR”, "ErrDesc": “any description of error”}

| Key | Type | Value |
| --- | --- | --- |
| Operation | String | operation from request |
| Status | String | “ERROR” |
| ErrDesc | String | Any description of error for user. |

##

## Operation BatteryForecast\_GetChartData

Return information about battery forecast.

###

### Request from External Program:

{"Operation": "BatteryForecast\_GetChartData"}

| Key | Type | Value |
| --- | --- | --- |
| Operation | String | “BatteryForecast\_GetChartData” |

###

### Response from GbbOptimizer

{"Operation": "BatteryForecast\_GetChartData", "Status": “OK”,
"BatteryForecast\_GetChartData": [ {"Hour": 7, "StartBattery\_Perc": 13.5,
...}, ...]}

| Key |  | Type | Value |
| --- | --- | --- | --- |
| Operation |  | String | “BatteryForecast\_GetChartData” |
| Status |  | String | “OK” |
| BatteryForecast\_GetChartData |  | Table |  |
|  | Day | date |  |
|  | Hour | Integer 0-23 |  |
|  | StartBattery\_Perc | decimal |  |
|  | StartBattery\_kWh | decimal |  |
|  | StartBattery\_kWhAC | decimal |  |
|  | PVForecast\_Perc | decimal, optional |  |
|  | PVForecast\_kWh | decimal, optional |  |
|  | PVForecast\_kWhAC | decimal, optional |  |
|  | Loads\_Perc | decimal, optional |  |
|  | Loads\_kWh | decimal, optional | with ExtraLoad |
|  | Loads\_kWhAC | decimal, optional |  |
|  | GridCharge\_Perc | decimal, optional |  |
|  | GridCharge\_kWh | decimal, optional |  |
|  | GridCharge\_kWhAC | decimal, optional |  |
|  | Discharge\_Perc | decimal, optional |  |
|  | Discharge\_kWh | decimal, optional |  |
|  | Discharge\_kWhAC | decimal, optional |  |
|  | EndBattery\_Perc | decimal |  |
|  | EndBattery\_kWh | decimal |  |
|  | EndBattery\_kWhAC | decimal |  |
|  | EndBattery\_Price | decimal, optional |  |
|  | Profit\_Amount | decimal, optional |  |
|  | FromGrid\_kWh | decimal, optional |  |
|  | Purchase\_Price | decimal, optional |  |
|  | Purchase\_Amount | decimal, optional |  |
|  | ToGrid\_kWh | decimal, optional |  |
|  | Sale\_Price | decimal, optional |  |
|  | Sale\_Amount | decimal, optional |  |
|  | Consumption\_kWh | decimal, optional | the same as Loads\_kWh |
|  | Consumption\_Price | decimal, optional |  |
|  | Consumption\_Amount | decimal, optional |  |
|  | ExtraLoadsKW | decimal, optional |  |
|  | ExtraLoadsKW\_ElectricVehicle | decimal, optional |  |
|  | ExtraLoadsKW\_HeatingPump | decimal, optional |  |
|  | ExtraLoadsKW\_Generic1 | decimal, optional |  |
|  | ExtraLoadsKW\_Generic2 | decimal, optional |  |
|  | ExtraLoadsKW\_Generic3 | decimal, optional |  |
|  | ExtraLoadsKW\_Generic4 | decimal, optional |  |
|  | ExtraLoadsKW\_Generic5 | decimal, optional |  |
|  | ExtraLoadsKW\_Generic6 | decimal, optional |  |

##

## Operation History\_GetHours

Returns information about hour history from Gain/Profits module.

###

### Request from External Program:

{"Operation": "History\_GetHours", "FromDate": "2024-01-01", "ToDate": "2024-01-01"}

| Key | Type | Value | Remarks |
| --- | --- | --- | --- |
| Operation | String | “History\_GetDays” |  |
| FromDate | Date, optional | "2024-01-01" | if omitted: today |
| ToDate | Date, optional | "2024-01-01" | if omitted: today |

Second form:

| Key | Type | Value | Remarks |
| --- | --- | --- | --- |
| Operation | String | “History\_GetHours” |  |
| Period | String | "curr\_day" or "prev\_day" or "today\_yesterday" |  |
| AddPeriodToProperty | int, optional | 1 | if 1 then in responce "History\_Hours" will be sufixed with "\_[Period]", eg. "History\_Hour\_curr\_day" |

###

### Response from GbbOptimizer

{"Operation": "History\_GetHours", "Status": “OK”, "History\_Hours": [ {"Day": ...]}

| Key |  | Type | Value |
| --- | --- | --- | --- |
| Operation |  | String | “History\_GetDays” |
| Status |  | String | “OK” |
| Period | String, optional |  |  |
| FromDate | Date | "2024-01-01" |  |
| ToDate | Date | "2024-01-03" |  |
| History\_Hours |  | Table |  |
|  | Hour | decimal |  |
|  | Day | date |  |
|  | FromGrid\_kWh | decimal, optional |  |
|  | FromGrid2\_kWh | decimal, optional |  |
|  | PurchaseAmount | decimal, optional |  |
|  | ToGrid\_kWh | decimal, optional |  |
|  | ToGrid2\_kWh | decimal, optional |  |
|  | SaleAmount | decimal, optional |  |
|  | Consumption\_kWh | decimal, optional |  |
|  | ConsumptionAmount | decimal, optional |  |
|  | ProfitAmount | decimal, optional |  |
|  | Solar\_kWh | decimal, optional |  |
|  | ToBattery\_kWh | decimal, optional |  |
|  | SOC\_Min | decimal, optional |  |
|  | SOC\_Max | decimal, optional |  |
|  | SOC\_Start | decimal, optional |  |
|  | SOC\_End | decimal, optional |  |
|  | BattChange\_kWh | decimal, optional |  |
|  | LostPower\_kWh | decimal, optional |  |
|  | ChargeFromGrid\_kWh | decimal, optional |  |
|  | ChargeFromPV\_kWh | decimal, optional |  |
|  | DischargeToGrid\_kWh | decimal, optional |  |
|  | DischargeToLoads\_kWh | decimal, optional |  |
|  | Start\_kWh | decimal, optional |  |
|  | End\_kWh | decimal, optional |  |
|  | ValueStartAmount | decimal, optional |  |
|  | ValueEndAmount | decimal, optional |  |
|  | ValueChangeAmount | decimal, optional |  |

##

## Operation History\_GetDays

Returns information about day history from Gain/Profits module.

###

### Request from External Program:

{"Operation": "History\_GetDays", "FromDate": "2024-01-01", "ToDate": "2024-01-03"}

| Key | Type | Value | Remarks |
| --- | --- | --- | --- |
| Operation | String | “History\_GetDays” |  |
| FromDate | Date, optional | "2024-01-01" | if omitted: today |
| ToDate | Date, optional | "2024-01-03" | if omitted: today |

Second form:

| Key | Type | Value | Remarks |
| --- | --- | --- | --- |
| Operation | String | “History\_GetDays” |  |
| Period | String | "curr\_month" or "prev\_month" or "curr\_year" or "prev\_year" |  |
| AddPeriodToProperty | int, optional | 1 | if 1 then in responce "History\_Days" will be sufixed with "\_[Period]", eg. "History\_Days\_prev\_month" |

###

### Response from GbbOptimizer

{"Operation": "History\_GetDays", "Status": “OK”, "History\_Days": [ {"Day": ...]}

| Key |  | Type | Value |
| --- | --- | --- | --- |
| Operation |  | String | “History\_GetDays” |
| Status |  | String | “OK” |
| Period | String, optional |  |  |
| FromDate | Date | "2024-01-01" |  |
| ToDate | Date | "2024-01-03" |  |
| History\_Days |  | Table |  |
|  | Day | date |  |
|  | FromGrid\_kWh | decimal, optional |  |
|  | FromGrid2\_kWh | decimal, optional |  |
|  | PurchaseAmount | decimal, optional |  |
|  | ToGrid\_kWh | decimal, optional |  |
|  | ToGrid2\_kWh | decimal, optional |  |
|  | SaleAmount | decimal, optional |  |
|  | Consumption\_kWh | decimal, optional |  |
|  | ConsumptionAmount | decimal, optional |  |
|  | ProfitAmount | decimal, optional |  |
|  | Solar\_kWh | decimal, optional |  |
|  | ToBattery\_kWh | decimal, optional |  |
|  | SOC\_Min | decimal, optional |  |
|  | SOC\_Max | decimal, optional |  |
|  | SOC\_Start | decimal, optional |  |
|  | SOC\_End | decimal, optional |  |
|  | BattChange\_kWh | decimal, optional |  |
|  | LostPower\_kWh | decimal, optional |  |
|  | ChargeFromGrid\_kWh | decimal, optional |  |
|  | ChargeFromPV\_kWh | decimal, optional |  |
|  | DischargeToGrid\_kWh | decimal, optional |  |
|  | DischargeToLoads\_kWh | decimal, optional |  |
|  | Start\_kWh | decimal, optional |  |
|  | End\_kWh | decimal, optional |  |
|  | ValueStartAmount | decimal, optional |  |
|  | ValueEndAmount | decimal, optional |  |
|  | ValueChangeAmount | decimal, optional |  |

##

## Operation History\_GetMonths

Returns information about month history from Gain/Profits module.

###

### Request from External Program:

{"Operation": "History\_GetMonths", "FromYear": 2024, "FromMonth": 1, "ToYear": 2024, "ToMonth": 2}

| Key | Type | Value | Remarks |
| --- | --- | --- | --- |
| Operation | String | “History\_GetMonths” |  |
| FromYear | int, optional | 2024 | if omitted: current year |
| FromMonth | int, optional | 1 | if omitted: current month |
| ToYear | int, optional | 2024 | if omitted: current year |
| ToMonth | int, optional | 2 | if omitted: current month |

Second form:

| Key | Type | Value | Remarks |
| --- | --- | --- | --- |
| Operation | String | “History\_GetMonths” |  |
| Period | String | "curr\_month" or "prev\_month" or "curr\_year" or "prev\_year" |  |
| AddPeriodToProperty | int, optional | 1 | if 1 then in responce "History\_Months" will be sufixed with "\_[Period]", eg: "History\_Months\_prev\_month" |

###

### Response from GbbOptimizer

{"Operation": "History\_GetMonths", "Status": “OK”, "History\_Months": [ {"Year": ...]}

| Key |  | Type | Value |
| --- | --- | --- | --- |
| Operation |  | String | “History\_GetMonths” |
| Status |  | String | “OK” |
| Period |  | String |  |
| FromYear |  | String | 2024 |
| FromMonth |  | int | 1 |
| ToYear |  | int | 2024 |
| ToMonth |  | int | 2 |
| History\_Month |  | Table |  |
|  | Day | date | First day of month |
|  | Year | int |  |
|  | Month | int |  |
|  | FromGrid\_kWh | decimal, optional |  |
|  | FromGrid2\_kWh | decimal, optional |  |
|  | PurchaseAmount | decimal, optional |  |
|  | ToGrid\_kWh | decimal, optional |  |
|  | ToGrid2\_kWh | decimal, optional |  |
|  | SaleAmount | decimal, optional |  |
|  | Consumption\_kWh | decimal, optional |  |
|  | ConsumptionAmount | decimal, optional |  |
|  | ProfitAmount | decimal, optional |  |
|  | Solar\_kWh | decimal, optional |  |
|  | ToBattery\_kWh | decimal, optional |  |
|  | SOC\_Min | decimal, optional |  |
|  | SOC\_Max | decimal, optional |  |
|  | SOC\_Start | decimal, optional |  |
|  | SOC\_End | decimal, optional |  |
|  | BattChange\_kWh | decimal, optional |  |
|  | LostPower\_kWh | decimal, optional |  |
|  | ChargeFromGrid\_kWh | decimal, optional |  |
|  | ChargeFromPV\_kWh | decimal, optional |  |
|  | DischargeToGrid\_kWh | decimal, optional |  |
|  | DischargeToLoads\_kWh | decimal, optional |  |
|  | Start\_kWh | decimal, optional |  |
|  | End\_kWh | decimal, optional |  |
|  | ValueStartAmount | decimal, optional |  |
|  | ValueEndAmount | decimal, optional |  |
|  | ValueChangeAmount | decimal, optional |

# 3. Changes data in program

## Change manual prices

Topic with data send to program: {plantId}/ha\_gbb/api/setmanualprices

Payload:

|  |  |  |  |
| --- | --- | --- | --- |
| Key |  | type | remarks |
| OrderId |  | string(255), optional | Any text copied from request to answer |
| Data |  | table |  |
|  | Date | Date, required | Date of price |
|  | StartHour | int, hour (0-23), required | Start hour of price |
|  | StartMinute | int, minute (0-59), optional | Start minute of hour, if missing then 0 |
|  | PurchasePrice | decimal, optional |  |
|  | TransferPrice | decimal, optional |  |
|  | SalePrice | decimal, optional |  |

example:

{ "Data": [ {"Date": "2024-04-20", "StartHour": 20, "PurchasePrice": 0.23} ] }

## Change extra loads

Topic with data send to program: {plantId}/ha\_gbb/api/setextraloads

Payload:

|  |  |  |  |
| --- | --- | --- | --- |
| Key |  | type | remarks |
| OrderId |  | string(255), optional | Any text copied from request to answer |
| Data |  | table |  |
|  | Date | Date, required | Date of extra loads (today or tomorrow) |
|  | StartHour | int, hour (0-23), required | Start hour of extra loads |
|  | StartMinute | int, minute (0-59), optional | Start minute of hour, if missing then 0 |
|  | TypeNo | int, required | 0 - EV, 1 - HeatPump, 2 - Other1, 3 - Other2, ..., 7 - Other6 |
|  | ExtraLoads\_kWh | decimal, required | kWh |

example:

{ "Data": [ {"Date": "2024-04-20", "StartHour": 20, "TypeNo": 1, "ExtraLoads": 1.23} ] }

## Change real temperature

Topic with data send to program: {plantId}/ha\_gbb/api/setrealtemperature

Payload:

|  |  |  |  |
| --- | --- | --- | --- |
| Key |  | type | remarks |
| OrderId |  | string(255), optional | Any text copied from request to answer |
| Data |  | table |  |
|  | Date | Date, required | Date of extra loads (yesterday, today or tomorrow)  If Hour is not present than hour is taken from Date, otherwise time (hour and minutes) are ignored |
|  | Hour | int, hour (0-23), optional | Hour of temperature |
|  | RealTemperature | decimal, required | stC |

example:

{ "Data": [ {"Date": "2024-04-20", "Hour": 20, "RealTemperature": 1.23} ] }

## Set optimizer parameters

Topic with data send to program: {plantId}/ha\_gbb/api/setoptimizer

Payload:

|  |  |  |  |
| --- | --- | --- | --- |
| Key |  | type | remarks |
| OrderId |  | string(255), optional | Any text copied from request to answer |
| Data |  | object |  |
|  | Opt2\_3x100Request | int, optional | 0 or 1 |
|  | CurrentLoadProfileId | int, optional | Id of LoadProfile |
|  | CurrentLoadProfileName | string, optional | Name of LoadProfile (case are not important) |

example:

{ "Data": {"Opt2\_3x100Request": 1} }

## Set car parameters

Topic with data send to program: {plantId}/ha\_gbb/api/setcar

Remark: 'HomeAssistant EV Car' must be added first (one)

Remark2: only given parameters are changed, so in different payload
different parameters can be changes. But program required following
information to be up to
date: SOC, SOC\_ChargeLimit, IsConnected, IsCharging,
Position\_Longitude, Position\_Latitude

Payload:

|  |  |  |  |
| --- | --- | --- | --- |
| Key |  | type | remarks |
| OrderId |  | string(255), optional | Any text copied from request to answer |
| Data |  | Table | More then one car can be update |
|  | VIN | string, required | Key to search existing car. If new VIN than new car is added (up to 10 cars) |
|  | BatteryKWh | decimal, optional | Car battery size |
|  | ChargeA | decimal, optional | Default car charge A |
|  | Phases | int, optional | 1 or 3 phases of charge |
|  | SOC | int, optional | Current SOC |
|  | SOC\_ChargeLimit | int, optional | Target SOC |
|  | InService | bool, optional | is car in service? |
|  | IsConnected | bool, optional | is car connected to charge? |
|  | IsCharging | bool, optional | is car is cahrging now? |
|  | Position\_Longitude, Position\_Latitude | double, optional | Current car position |

example:

{ "Data": [ {"VIN":"vin1234", "SOC":40, "SOC\_ChargeLimit": 90} ], [ {"VIN":"vin4321", "InService": true] }

## Set HP parameters

Topic with data send to program: {plantId}/ha\_gbb/api/sethp

Remark: only given parameters are changed.

Payload:

|  |  |  |  |
| --- | --- | --- | --- |
| Key |  | type | remarks |
| OrderId |  | string(255), optional | Any text copied from request to answer |
| Data |  | object |  |
|  | HPForecast\_Break\_On | bool, optional | HP doesn't work: on/off |
|  | HPForecast\_BreakFromDate | date, optional | Start Date |
|  | HPForecast\_BreakFromHour | int, optional | Start Hour (0-23) |
|  | HPForecast\_BreakToDate | date, optional | End Date (included) |
|  | HPForecast\_BreakToHour | int, optional | End Hour (included) (0-23) |

example:

{ "Data": {"HPForecast\_Break\_On":true, "HPForecast\_BreakToDate":"2026-01-30", "HPForecast\_BreakToHour": 23} }

##

## Result of changes

After every change in data (eg. {plantid}/ha\_gbb/api/setmanualprices)
program send info on this topic with OK or error description.

Topic with data send from program: {plantid}/ha\_gbb/api/result

Payload:

|  |  |  |
| --- | --- | --- |
| Key | type | remarks |
| OrderId | string(255), optional | Any text copied from request to answer |
| Result | string(255) | OK or error description |
| Data |  | Data from original request |
