---
title: "Home Assistant Topics"
weight: 40
translationKey: "tematy-ha"
---

# MQTT Topics for Home Assistant

Topics used for communication between GbbOptimizer and Home Assistant / GbbConnect.

## Data from Home Assistant to GbbOptimizer

{{< mqtt-topic topic="{PlantId}/ha_gbb/sensor" direction="subscribe" qos="0" description="HA sensor data — cumulative counters" >}}

**Required fields:**

| Field | Type | Description |
|-------|------|-------------|
| `soc_perc` | decimal | Battery SOC (%). Use `V` if "Control via V" is checked |
| `loads_total_kWh` | decimal | Consumption — cumulative counter |
| `fromgrid_total_kWh` | decimal | Grid import — cumulative counter |
| `togrid_total_kWh` | decimal | Grid export — cumulative counter |
| `pv_total_kWh` | decimal | PV production — cumulative counter |

**Optional fields:**

| Field | Type | Description |
|-------|------|-------------|
| `ev_charge_total_kWh` | decimal | EV charging |
| `hp_total_kWh` | decimal | Heat pump |
| `other1_total_kWh` – `other6_total_kWh` | decimal | Other 1–6 |

**Multiple PV sources:**

```json
{
  "pv_total_kWh": 123.4,
  "more": [
    {"number": 2, "pv_total_kWh": 56.7},
    {"number": 3, "pv_total_kWh": 89.0}
  ]
}
```

> [!NOTE]
> - Counters may reset — you can send daily counters for example
> - Values < 0 are treated as missing data
> - You can send only optional data if the main data is imported from the inverter. In that case add the HomeAssistant system in the IoT menu
> - `pv_total_kWh` is the same as `"more"` with `number=1` — do not use both at the same time
> - Solarman/DeyeCloud: individual fields (`soc_perc`, `fromgrid_total_kWh`, `togrid_total_kWh`, `loads_total_kWh`) can be sent separately if the corresponding options are checked in [installation parameters]({{< relref "/installation/installation-parameters" >}})

## Commands from GbbOptimizer to Home Assistant

GbbOptimizer sends control commands to dedicated topics:

{{< mqtt-topic topic="{PlantId}/ha_gbb/Start_Charge" direction="publish" description="Start charging battery to SOC from Payload" >}}

{{< mqtt-topic topic="{PlantId}/ha_gbb/Start_Discharge" direction="publish" description="Start discharging battery to grid (to SOC from Payload)" >}}

{{< mqtt-topic topic="{PlantId}/ha_gbb/Start_DisableCharge" direction="publish" description="Do not charge battery — PV to home and grid" >}}

{{< mqtt-topic topic="{PlantId}/ha_gbb/Start_Normal" direction="publish" description="Return to normal operation" >}}

In parallel, the same data is sent to:

{{< mqtt-topic topic="{PlantId}/ha_gbb/EMS" direction="publish" description="Combined EMS command with full JSON payload" >}}

**JSON Payload:**

| Field | Type | Description |
|-------|------|-------------|
| `Hour` | int | Hour |
| `FromMinute` | int | Start minute |
| `ToMinute` | int | End minute |
| `DischargeLimitW` | int | Discharge limit (W) |
| `ChargeLimitW` | int | Charge limit (W) |
| `InputLimitW` | int | Import limit (W) |
| `PriceLessZero` | int | 0 = normal price, 1 = price < 0 |
| `Operation` | string | `"Normal"`, `"Discharge"`, `"DisableCharge"` or `"Charge"` |
| `SOC` | int | Target SOC |
| `V` | decimal | SOC converted to V (if control via V) |

**Example:**
```json
{
  "Hour": 22,
  "FromMinute": 0,
  "ToMinute": 59,
  "PriceLessZero": 0,
  "Operation": "Normal",
  "SOC": 90
}
```

## HA Automation Example

```yaml
alias: mqtt output_source_priority_battery
trigger:
  - platform: mqtt
    topic: ha_gbb/Start_Charge
action:
  - service: switch.turn_on
    target:
      entity_id: switch.bms_1_output_source_priority_battery
```

## Example: Publishing Data to MQTT

```yaml
alias: mqtt_publish
trigger:
  - platform: time_pattern
    minutes: /5
action:
  - service: mqtt.publish
    data:
      qos: "0"
      retain: false
      topic: ha_gbb/sensor
      payload: >
        {
          "loads_total_kWh": {{ states.sensor.inverter_out_daily_energy.state | float(-1) }},
          "fromgrid_total_kWh": {{ states.sensor.inverter_in_daily_energy.state | float(-1) }},
          "pv_total_kWh": {{ states.sensor.total_daily_energy.state | float(-1) }},
          "soc_perc": {{ states.sensor.battery_soc.state | float(-1) }},
          "togrid_total_kWh": 0
        }
```
