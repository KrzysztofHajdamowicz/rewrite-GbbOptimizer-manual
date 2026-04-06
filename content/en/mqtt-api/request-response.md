---
title: "Request / Response"
weight: 20
translationKey: "zapytania-odpowiedzi"
---

# MQTT Request and Response

GbbOptimizer supports request/response queries over MQTT. An external program sends a request and GbbOptimizer replies with data.

## Connection

The external program should connect to MQTT with the following parameters:

| Parameter | Value |
|-----------|-------|
| Address | See [MQTT servers]({{< relref "/references/mqtt-servers" >}}) |
| Port | 8883 |
| Username | `{PlantId}` |
| Password | `{PlantToken}` |
| UseTLS | true |
| ClientID | must end with `_{PlantId}` |

## Topics

| Direction | Topic |
|-----------|-------|
| Request → | `{PlantId}/ha_gbb/dataserver/serverrequest` |
| ← Response | `{PlantId}/ha_gbb/dataserver/serverresponse` |

> [!NOTE]
> For backward compatibility the program also handles `{PlantId}/dataserver/serverrequest` and `{PlantId}/dataserver/serverresponse` (not recommended).

## Error Response

Any request may return an error:

```json
{
  "Operation": "xxx",
  "Status": "ERROR",
  "ErrDesc": "error description"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `Operation` | string | Operation from the request |
| `Status` | string | `"ERROR"` |
| `ErrDesc` | string | Human-readable error description |

## Available Operations

{{< mqtt-endpoint name="BatteryForecast_GetChartData" request-topic="{PlantId}/ha_gbb/dataserver/serverrequest" response-topic="{PlantId}/ha_gbb/dataserver/serverresponse" description="Get battery forecast chart data" >}}

**Request:**
```json
{"Operation": "BatteryForecast_GetChartData"}
```

**Response** — array of objects in the `BatteryForecast_GetChartData` field:

| Field | Type | Description |
|-------|------|-------------|
| `Day` | date | Day |
| `Hour` | int (0-23) | Hour |
| `StartBattery_Perc` | decimal | SOC at the start of the hour |
| `StartBattery_kWh` | decimal | kWh at the start (DC) |
| `StartBattery_kWhAC` | decimal | kWh at the start (AC) |
| `PVForecast_Perc` | decimal? | PV forecast (%) |
| `PVForecast_kWh` | decimal? | PV forecast (kWh DC) |
| `PVForecast_kWhAC` | decimal? | PV forecast (kWh AC) |
| `Loads_Perc` | decimal? | Consumption (%) |
| `Loads_kWh` | decimal? | Consumption incl. ExtraLoad (kWh DC) |
| `Loads_kWhAC` | decimal? | Consumption (kWh AC) |
| `GridCharge_Perc` | decimal? | Grid charging (%) |
| `GridCharge_kWh` | decimal? | Grid charging (kWh DC) |
| `GridCharge_kWhAC` | decimal? | Grid charging (kWh AC) |
| `Discharge_Perc` | decimal? | Discharge (%) |
| `Discharge_kWh` | decimal? | Discharge (kWh DC) |
| `Discharge_kWhAC` | decimal? | Discharge (kWh AC) |
| `EndBattery_Perc` | decimal | SOC at the end of the hour |
| `EndBattery_kWh` | decimal | kWh at the end (DC) |
| `EndBattery_kWhAC` | decimal | kWh at the end (AC) |
| `EndBattery_Price` | decimal? | Value of energy in the battery |
| `Profit_Amount` | decimal? | Profit amount |
| `FromGrid_kWh` | decimal? | Grid import |
| `Purchase_Price` | decimal? | Purchase price |
| `Purchase_Amount` | decimal? | Purchase amount |
| `ToGrid_kWh` | decimal? | Grid export |
| `Sale_Price` | decimal? | Sale price |
| `Sale_Amount` | decimal? | Sale amount |
| `Consumption_kWh` | decimal? | Consumption (= Loads_kWh) |
| `Consumption_Price` | decimal? | Consumption price |
| `Consumption_Amount` | decimal? | Consumption amount |
| `ExtraLoadsKW` | decimal? | Extra consumption (total) |
| `ExtraLoadsKW_ElectricVehicle` | decimal? | EV |
| `ExtraLoadsKW_HeatingPump` | decimal? | Heat pump |
| `ExtraLoadsKW_Generic1`–`Generic6` | decimal? | Other 1–6 |

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="History_GetHours" request-topic="{PlantId}/ha_gbb/dataserver/serverrequest" response-topic="{PlantId}/ha_gbb/dataserver/serverresponse" description="Get hourly history from the Profits module" >}}

**Request — form 1** (date range):
```json
{"Operation": "History_GetHours", "FromDate": "2024-01-01", "ToDate": "2024-01-01"}
```

| Field | Type | Description |
|-------|------|-------------|
| `Operation` | string | `"History_GetHours"` |
| `FromDate` | date? | Default: today |
| `ToDate` | date? | Default: today |

**Request — form 2** (period):

| Field | Type | Description |
|-------|------|-------------|
| `Operation` | string | `"History_GetHours"` |
| `Period` | string | `"curr_day"`, `"prev_day"` or `"today_yesterday"` |
| `AddPeriodToProperty` | int? | If 1 → response key with suffix, e.g. `"History_Hours_curr_day"` |

**Response** — array in `History_Hours`:

| Field | Type | Description |
|-------|------|-------------|
| `Hour` | decimal | Hour |
| `Day` | date | Day |
| `FromGrid_kWh` | decimal? | Grid import |
| `FromGrid2_kWh` | decimal? | Net-metered import |
| `PurchaseAmount` | decimal? | Purchase amount |
| `ToGrid_kWh` | decimal? | Grid export |
| `ToGrid2_kWh` | decimal? | Net-metered export |
| `SaleAmount` | decimal? | Sale amount |
| `Consumption_kWh` | decimal? | Consumption |
| `ConsumptionAmount` | decimal? | Consumption amount |
| `ProfitAmount` | decimal? | Profit amount |
| `Solar_kWh` | decimal? | PV production |
| `ToBattery_kWh` | decimal? | To battery |
| `SOC_Min` / `SOC_Max` | decimal? | Min/Max SOC |
| `SOC_Start` / `SOC_End` | decimal? | Start / end SOC |
| `BattChange_kWh` | decimal? | Battery change |
| `LostPower_kWh` | decimal? | Losses |
| `ChargeFromGrid_kWh` | decimal? | Charging from grid |
| `ChargeFromPV_kWh` | decimal? | Charging from PV |
| `DischargeToGrid_kWh` | decimal? | Discharge to grid |
| `DischargeToLoads_kWh` | decimal? | Discharge to loads |
| `Start_kWh` / `End_kWh` | decimal? | Start / end kWh in battery |
| `ValueStartAmount` / `ValueEndAmount` | decimal? | Start / end value |
| `ValueChangeAmount` | decimal? | Value change |

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="History_GetDays" request-topic="{PlantId}/ha_gbb/dataserver/serverrequest" response-topic="{PlantId}/ha_gbb/dataserver/serverresponse" description="Get daily history from the Profits module" >}}

**Request — form 1:**
```json
{"Operation": "History_GetDays", "FromDate": "2024-01-01", "ToDate": "2024-01-03"}
```

**Request — form 2:**

| Field | Type | Description |
|-------|------|-------------|
| `Period` | string | `"curr_month"`, `"prev_month"`, `"curr_year"` or `"prev_year"` |
| `AddPeriodToProperty` | int? | If 1 → suffix in the response key |

**Response** — identical structure to `History_GetHours`, but in the `History_Days` array.

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="History_GetMonths" request-topic="{PlantId}/ha_gbb/dataserver/serverrequest" response-topic="{PlantId}/ha_gbb/dataserver/serverresponse" description="Get monthly history from the Profits module" >}}

**Request — form 1:**
```json
{"Operation": "History_GetMonths", "FromYear": 2024, "FromMonth": 1, "ToYear": 2024, "ToMonth": 2}
```

| Field | Type | Description |
|-------|------|-------------|
| `FromYear` / `FromMonth` | int? | Default: current year/month |
| `ToYear` / `ToMonth` | int? | Default: current year/month |

**Request — form 2:**

| Field | Type | Description |
|-------|------|-------------|
| `Period` | string | `"curr_month"`, `"prev_month"`, `"curr_year"` or `"prev_year"` |

**Response** — identical structure plus `Year` and `Month` fields, in the `History_Months` array.

{{< /mqtt-endpoint >}}
