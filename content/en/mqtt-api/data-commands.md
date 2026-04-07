---
title: "Data Commands"
weight: 30
translationKey: "komendy-danych"
---

# MQTT Data Commands

Commands that allow external programs to modify data in GbbOptimizer. Each command sends data to a dedicated topic and receives a result on `{PlantId}/ha_gbb/api/result`.

## Command Result

{{< mqtt-topic topic="{PlantId}/ha_gbb/api/result" direction="publish" description="Result of each data command — OK or error description" >}}

| Field | Type | Description |
|-------|------|-------------|
| `OrderId` | string? | Copied from the request |
| `Result` | string | `"OK"` or error description |
| `Data` | object | Data from the original request |

---

{{< mqtt-endpoint name="SetManualPrices" topic="{PlantId}/ha_gbb/api/setmanualprices" direction="subscribe" description="Set manual energy prices" >}}

| Field | | Type | Required | Description |
|-------|--|------|----------|-------------|
| `OrderId` | | string | no | Text copied to the response |
| `Data` | | array | yes | |
| | `Date` | date | yes | Price date |
| | `StartHour` | int (0-23) | yes | Start hour |
| | `StartMinute` | int (0-59) | no | Minute (default 0) |
| | `PurchasePrice` | decimal | no | Purchase price |
| | `TransferPrice` | decimal | no | Transfer price |
| | `SalePrice` | decimal | no | Sale price |

**Example:**
```json
{
  "Data": [
    {"Date": "2024-04-20", "StartHour": 20, "PurchasePrice": 0.23}
  ]
}
```

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetExtraLoads" topic="{PlantId}/ha_gbb/api/setextraloads" direction="subscribe" description="Set Extra Consumption" >}}

| Field | | Type | Required | Description |
|-------|--|------|----------|-------------|
| `OrderId` | | string | no | Text copied to the response |
| `Data` | | array | yes | |
| | `Date` | date | yes | Date (today or tomorrow) |
| | `StartHour` | int (0-23) | yes | Hour |
| | `StartMinute` | int (0-59) | no | Minute (default 0) |
| | `TypeNo` | int | yes | 0=EV, 1=Heat pump, 2=Other1, 3=Other2, ..., 7=Other6 |
| | `ExtraLoads_kWh` | decimal | yes | kWh |

**Example:**
```json
{
  "Data": [
    {"Date": "2024-04-20", "StartHour": 20, "TypeNo": 1, "ExtraLoads_kWh": 1.23}
  ]
}
```

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetRealTemperature" topic="{PlantId}/ha_gbb/api/setrealtemperature" direction="subscribe" description="Set real temperature" >}}

| Field | | Type | Required | Description |
|-------|--|------|----------|-------------|
| `OrderId` | | string | no | Text copied to the response |
| `Data` | | array | yes | |
| | `Date` | date | yes | Date (yesterday, today, or tomorrow). If `Hour` is absent — hour taken from the date |
| | `Hour` | int (0-23) | no | Temperature hour |
| | `RealTemperature` | decimal | yes | Temperature (°C) |

**Example:**
```json
{
  "Data": [
    {"Date": "2024-04-20", "Hour": 20, "RealTemperature": 1.23}
  ]
}
```

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetOptimizer" topic="{PlantId}/ha_gbb/api/setoptimizer" direction="subscribe" description="Set optimizer parameters" >}}

| Field | | Type | Required | Description |
|-------|--|------|----------|-------------|
| `OrderId` | | string | no | Text copied to the response |
| `Data` | | object | yes | |
| | `Opt2_3x100Request` | int | no | 0 or 1 — force 3h×100% |
| | `CurrentLoadProfileId` | int | no | Consumption Profile ID |
| | `CurrentLoadProfileName` | string | no | Consumption Profile name (case insensitive) |

**Example:**
```json
{"Data": {"Opt2_3x100Request": 1}}
```

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetCar" topic="{PlantId}/ha_gbb/api/setcar" direction="subscribe" description="Set EV car parameters" >}}

> [!NOTE]
> The "HomeAssistant EV Car" must be added in the program first. Only the provided parameters are updated — but the program requires current values for: `SOC`, `SOC_ChargeLimit`, `IsConnected`, `IsCharging`, `Position_Longitude`, `Position_Latitude`.

| Field | | Type | Required | Description |
|-------|--|------|----------|-------------|
| `OrderId` | | string | no | Text copied to the response |
| `Data` | | array | yes | Multiple cars can be updated |
| | `VIN` | string | yes | Identification key. New VIN = new car (max 10) |
| | `BatteryKWh` | decimal | no | Car battery capacity |
| | `ChargeA` | decimal | no | Default charging current (A) |
| | `Phases` | int | no | 1 or 3 phases |
| | `SOC` | int | no | Current SOC |
| | `SOC_ChargeLimit` | int | no | Target SOC |
| | `InService` | bool | no | Whether the car is in service |
| | `IsConnected` | bool | no | Whether connected to charger |
| | `IsCharging` | bool | no | Whether currently charging |
| | `Position_Longitude` | double | no | Longitude |
| | `Position_Latitude` | double | no | Latitude |

**Example:**
```json
{
  "Data": [
    {"VIN": "vin1234", "SOC": 40, "SOC_ChargeLimit": 90}
  ]
}
```

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetHP" topic="{PlantId}/ha_gbb/api/sethp" direction="subscribe" description="Set heat pump parameters" >}}

| Field | | Type | Required | Description |
|-------|--|------|----------|-------------|
| `OrderId` | | string | no | Text copied to the response |
| `Data` | | object | yes | Only provided parameters are changed |
| | `HPForecast_Break_On` | bool | no | Heat pump break: enable/disable |
| | `HPForecast_BreakFromDate` | date | no | Break start date |
| | `HPForecast_BreakFromHour` | int (0-23) | no | Break start hour |
| | `HPForecast_BreakToDate` | date | no | Break end date (inclusive) |
| | `HPForecast_BreakToHour` | int (0-23) | no | Break end hour (inclusive) |

**Example:**
```json
{
  "Data": {
    "HPForecast_Break_On": true,
    "HPForecast_BreakToDate": "2026-01-30",
    "HPForecast_BreakToHour": 23
  }
}
```

{{< /mqtt-endpoint >}}
