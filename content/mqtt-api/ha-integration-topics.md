---
title: "HA Integration Topics"
weight: 40
---

# Home Assistant Integration Topics

MQTT topics used for bidirectional communication between Home Assistant and GbbOptimizer.

## Sensor Input (HA → GbbOptimizer)

{{< mqtt-endpoint name="Sensor Data" topic="{PlantId}/ha_gbb/sensor" direction="publish" description="Send inverter sensor data from Home Assistant" >}}

Home Assistant publishes inverter telemetry data in JSON format. This is the primary data input channel.

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `soc` | number | Battery SOC (%) or voltage |
| `total_loads` | number | Total household loads (kWh) |
| `grid_import` | number | Grid import total (kWh) |
| `grid_export` | number | Grid export total (kWh) |
| `pv_generation` | number | PV generation total (kWh) |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `ev_charging` | number | EV charger consumption (kWh) |
| `heat_pump` | number | Heat pump consumption (kWh) |
| `more` | array | Multiple PV sources with numbered entries |

### Notes

- Negative values indicate missing data
- Total counters may reset periodically for daily tracking
- Optional data imports only function when properly configured in the IoT menu
- Special handling exists for Solarman/DeyeCloud regarding SOC and grid data sources

{{< /mqtt-endpoint >}}

## Command Output (GbbOptimizer → HA)

{{< mqtt-topic topic="{PlantId}/ha_gbb/Start_Charge" direction="subscribe" description="Command to start battery charging. Payload includes scheduling, power limits, and target SOC." >}}

{{< mqtt-topic topic="{PlantId}/ha_gbb/Start_Discharge" direction="subscribe" description="Command to start battery discharging. Payload includes power limits and price indicators." >}}

{{< mqtt-topic topic="{PlantId}/ha_gbb/Start_DisableCharge" direction="subscribe" description="Command to prevent battery charging from grid." >}}

{{< mqtt-topic topic="{PlantId}/ha_gbb/Start_Normal" direction="subscribe" description="Command to return to normal operation mode." >}}
