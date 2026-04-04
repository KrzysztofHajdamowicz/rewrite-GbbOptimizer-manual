---
title: "Data Commands"
weight: 30
---

# Data Commands

Commands to modify GbbOptimizer data via MQTT. All commands return a result on the result topic.

{{< mqtt-topic topic="{PlantId}/ha_gbb/api/result" direction="subscribe" description="Result topic for all data commands. Returns \"OK\" or an error description." >}}

---

{{< mqtt-endpoint name="SetManualPrices" topic="{PlantId}/ha_gbb/api/setmanualprices" direction="publish" description="Set manual electricity prices" >}}

Override electricity prices for specific dates and hours.

### Payload

```json
{
  "Data": [
    {
      "Date": "2024-04-20",
      "StartHour": 20,
      "PurchasePrice": 0.23
    },
    {
      "Date": "2024-04-20",
      "StartHour": 21,
      "PurchasePrice": 0.18
    }
  ]
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `Data` | array | yes | Array of price entries |
| `Data[].Date` | string | yes | Date in `YYYY-MM-DD` format |
| `Data[].StartHour` | number | yes | Hour (0-23) |
| `Data[].PurchasePrice` | number | no | Purchase price override |
| `Data[].SellPrice` | number | no | Sell price override |

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetExtraLoads" topic="{PlantId}/ha_gbb/api/setextraloads" direction="publish" description="Set extra load data (EV, heat pump, etc.)" >}}

### Type Numbers

| TypeNo | Category |
|--------|----------|
| 0 | EV |
| 1 | Heat Pump |
| 2-7 | Other types |

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetRealTemperature" topic="{PlantId}/ha_gbb/api/setrealtemperature" direction="publish" description="Set actual measured temperature" >}}

Provide real temperature data for HP/AirCond forecast improvements.

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetOptimizer" topic="{PlantId}/ha_gbb/api/setoptimizer" direction="publish" description="Set optimizer parameters" >}}

Modify optimizer parameters at runtime via MQTT.

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetCar" topic="{PlantId}/ha_gbb/api/setcar" direction="publish" description="Set car / EV parameters" >}}

Track multiple vehicles via VIN with SOC, charge limits, and location data.

### Payload

```json
{
  "VIN": "WVWZZZ1KZAW123456",
  "SOC": 65,
  "ChargeLimit": 80,
  "Location": "home"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `VIN` | string | Vehicle Identification Number |
| `SOC` | number | Current vehicle battery SOC (%) |
| `ChargeLimit` | number | Target charge limit (%) |
| `Location` | string | Vehicle location |

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetHP" topic="{PlantId}/ha_gbb/api/sethp" direction="publish" description="Set heat pump parameters" >}}

Control heating pump break periods and scheduling.

{{< /mqtt-endpoint >}}
