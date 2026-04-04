---
title: "Request / Response"
weight: 20
---

# Request / Response API

Query GbbOptimizer for forecast and history data using the request/response pattern.

## Topics

{{< mqtt-topic topic="{PlantId}/ha_gbb/dataserver/serverrequest" direction="publish" description="Send requests to GbbOptimizer" >}}

{{< mqtt-topic topic="{PlantId}/ha_gbb/dataserver/serverresponse" direction="subscribe" description="Receive responses from GbbOptimizer" >}}

> **Legacy topics** (not recommended): `{PlantId}/dataserver/serverrequest` and `{PlantId}/dataserver/serverresponse`

---

## Endpoints

{{< mqtt-endpoint name="BatteryForecast_GetChartData" request-topic="{PlantId}/ha_gbb/dataserver/serverrequest" response-topic="{PlantId}/ha_gbb/dataserver/serverresponse" description="Get battery forecast chart data" >}}

Returns hourly battery forecast data including SOC levels, PV production, loads, grid activity, and profit projections.

### Request

```json
{
  "command": "BatteryForecast_GetChartData"
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `SOC` | number[] | Hourly SOC projection (%) |
| `BatteryAC` | number[] | Battery AC power (W) |
| `BatteryDC` | number[] | Battery DC power (W) |
| `PV` | number[] | PV forecast (kWh) |
| `Loads` | number[] | Expected loads (kWh) |
| `FromGrid` | number[] | Grid import (kWh) |
| `ToGrid` | number[] | Grid export (kWh) |
| `Profit` | number[] | Hourly profit |

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="History_GetHours" request-topic="{PlantId}/ha_gbb/dataserver/serverrequest" response-topic="{PlantId}/ha_gbb/dataserver/serverresponse" description="Get hourly history data" >}}

Returns hourly history from the Gain/Profits module.

### Request

```json
{
  "command": "History_GetHours",
  "fromDate": "2024-04-01",
  "toDate": "2024-04-02"
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `FromGrid` | number | Grid import (kWh) |
| `ToGrid` | number | Grid export (kWh) |
| `Consumption` | number | Total consumption (kWh) |
| `Profit` | number | Calculated profit |
| `SOC` | number | Battery SOC (%) |

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="History_GetDays" request-topic="{PlantId}/ha_gbb/dataserver/serverrequest" response-topic="{PlantId}/ha_gbb/dataserver/serverresponse" description="Get daily history data" >}}

Returns daily history data. Supports date range or period parameters.

### Request (date range)

```json
{
  "command": "History_GetDays",
  "fromDate": "2024-04-01",
  "toDate": "2024-04-30"
}
```

### Request (period)

```json
{
  "command": "History_GetDays",
  "period": "current_day"
}
```

Supported periods: `current_day`, `previous_day`, `current_year`, `previous_year`

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="History_GetMonths" request-topic="{PlantId}/ha_gbb/dataserver/serverrequest" response-topic="{PlantId}/ha_gbb/dataserver/serverresponse" description="Get monthly history data" >}}

Returns monthly aggregated history.

### Request

```json
{
  "command": "History_GetMonths",
  "fromYear": 2024,
  "fromMonth": 1,
  "toYear": 2024,
  "toMonth": 12
}
```

{{< /mqtt-endpoint >}}
