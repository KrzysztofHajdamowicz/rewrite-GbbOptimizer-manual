---
title: "Automation"
weight: 30
translationKey: "automatyzacja"
---

# Home Assistant Automation

After configuring the [Mosquitto Bridge]({{< relref "/integrations/home-assistant/mosquitto-bridge" >}}) you can create automations in Home Assistant that:

- **Send data** from HA sensors to GbbOptimizer
- **React to commands** received from GbbOptimizer

## Sending Data to GbbOptimizer

GbbOptimizer expects data on the topic `ha_gbb/sensor` (locally in HA; via bridge it arrives as `<PlantId>/ha_gbb/sensor`).

### Required Fields

| Field | Description |
|-------|-------------|
| `soc_perc` | Battery {{< glossary "SOC" >}} in percent (or `V` if voltage-based control is selected) |
| `loads_total_kWh` | Consumption meter (kWh, cumulative) |
| `fromgrid_total_kWh` | Energy drawn from grid meter (kWh) |
| `togrid_total_kWh` | Energy sent to grid meter (kWh) |
| `pv_total_kWh` | PV production meter (kWh) |

### Optional Fields

| Field | Description |
|-------|-------------|
| `ev_charge_total_kWh` | EV charging meter |
| `hp_total_kWh` | Heat pump meter |
| `other1_total_kWh` ... `other6_total_kWh` | Additional meters |

### Multiple PV Arrays

To send data from multiple PV arrays, use the `more` field:

```json
{
  "pv_total_kWh": 10.5,
  "more": [
    {"number": 2, "pv_total_kWh": 5.2},
    {"number": 3, "pv_total_kWh": 3.1}
  ]
}
```

> [!NOTE]
> The main `pv_total_kWh` corresponds to `number: 1`. Use either `pv_total_kWh` or `number: 1` in `more` — not both at the same time. The corresponding number must be configured in the PV Array -> HomeAssistant settings.

### Example Automation — Data Publishing

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
      payload: >-
        {
          "soc_perc": {{ states.sensor.battery_soc.state | float(-1) }},
          "loads_total_kWh": {{ states.sensor.loads_daily.state | float(-1) }},
          "fromgrid_total_kWh": {{ states.sensor.grid_import_daily.state | float(-1) }},
          "togrid_total_kWh": {{ states.sensor.grid_export_daily.state | float(-1) }},
          "pv_total_kWh": {{ states.sensor.pv_daily.state | float(-1) }}
        }
```

> [!WARNING]
> Values less than 0 are treated as missing data (null). Meters may reset — you can send daily meters for example.

### Notes on Partial Data Import

- You can send **only optional fields** if the main data (SOC, consumption, etc.) is imported directly from the inverter. In that case, in the **IoT** menu add a HomeAssistant system and a meter for each type of optional data.
- The `pv_total_kWh` field can be sent separately — it will be added to PV from the inverter if **PV Forecast** -> **Correct** -> **Source of actual PV production data** is set to `HomeAssistant`.

### Notes for Solarman / DeyeCloud

- The `soc_perc`, `fromgrid_total_kWh`, and `togrid_total_kWh` fields can be sent separately if the option **"FromGrid, ToGrid and SOC data is sent via HomeAssistant/SolarAssistant"** is checked
- The `loads_total_kWh` field can be sent separately if **"Consumption data is sent from HomeAssistant/SolarAssistant"** is checked

## Receiving Commands from GbbOptimizer

GbbOptimizer sends commands to the following topics (locally in HA without the {{< glossary "PlantId" >}} prefix):

| Topic | Operation |
|-------|-----------|
| `ha_gbb/Start_Charge` | Start charging the battery from PV/grid to a target SOC |
| `ha_gbb/Start_Discharge` | Start discharging the battery to the grid to a target SOC |
| `ha_gbb/Start_DisableCharge` | Disable battery charging, PV goes to home and grid |
| `ha_gbb/Start_Normal` | Return to normal operation |
| `ha_gbb/EMS` | Combined topic with the same data as the above commands |

### Command Payload

Each command sends JSON with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `Hour` | int | Hour |
| `FromMinute` | int | Start minute |
| `ToMinute` | int | End minute |
| `DischargeLimitW` | int | Discharge limit (W) |
| `ChargeLimitW` | int | Charge limit (W) |
| `InputLimitW` | int | Grid input limit (W) |
| `PriceLessZero` | int | 0 = normal price, 1 = price < 0 |
| `Operation` | string | `"Normal"`, `"Discharge"`, `"DisableCharge"`, `"Charge"` |
| `SOC` | int | Target SOC level |
| `V` | float | SOC converted to voltage (if voltage-based control) |

### Example Automation — Responding to a Command

```yaml
alias: mqtt_start_charge
trigger:
  - platform: mqtt
    topic: ha_gbb/Start_Charge
action:
  - service: switch.turn_on
    target:
      entity_id: switch.inverter_charge_from_grid
    data: {}
mode: single
```

> [!NOTE]
> You need to write automations for each command yourself, adapted to your inverter and configuration. The example above is for illustration purposes only.
