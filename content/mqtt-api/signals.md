---
title: "Signals"
weight: 10
---

# MQTT Signals

Signals are sent by GbbOptimizer to external programs (like Home Assistant) based on forecast data. They must be enabled in the **Discharge Plan** module and are sent hourly.

## Signal Topics

{{< mqtt-topic topic="{PlantId}/signals/SOCHigherEqThanX" direction="subscribe" description="Emitted when battery SOC ≥ threshold X. Payload: \"1\" if true, \"0\" if false." >}}

{{< mqtt-topic topic="{PlantId}/signals/SOCLowerEqThanX" direction="subscribe" description="Emitted when battery SOC ≤ threshold X. Payload: \"1\" if true, \"0\" if false." >}}

{{< mqtt-topic topic="{PlantId}/signals/SellingPriceHigherEqThanX" direction="subscribe" description="Emitted when selling price ≥ threshold X. Payload: \"1\" if true, \"0\" if false." >}}

{{< mqtt-topic topic="{PlantId}/signals/SellingPriceLowerEqThanX" direction="subscribe" description="Emitted when selling price ≤ threshold X. Payload: \"1\" if true, \"0\" if false." >}}

{{< mqtt-topic topic="{PlantId}/signals/FromGridHigherEqThanX" direction="subscribe" description="Emitted when grid import ≥ threshold X. Payload: \"1\" if true, \"0\" if false." >}}

{{< mqtt-topic topic="{PlantId}/signals/ToGridHigherEqThanX" direction="subscribe" description="Emitted when grid export ≥ threshold X. Payload: \"1\" if true, \"0\" if false." >}}

## Signal Data

{{< mqtt-topic topic="{PlantId}/signals/data" direction="subscribe" description="JSON payload with current signal values." >}}

### Payload

```json
{
  "SOC": 75,
  "SellingPrice": 0.15,
  "PurchasePrice": 0.23,
  "FromGrid_kWh": 1.2,
  "ToGrid_kWh": 3.5
}
```

| Field | Type | Description |
|-------|------|-------------|
| `SOC` | number | Current battery State of Charge (%) |
| `SellingPrice` | number | Current electricity selling price |
| `PurchasePrice` | number | Current electricity purchase price |
| `FromGrid_kWh` | number | Energy imported from grid (kWh) |
| `ToGrid_kWh` | number | Energy exported to grid (kWh) |
