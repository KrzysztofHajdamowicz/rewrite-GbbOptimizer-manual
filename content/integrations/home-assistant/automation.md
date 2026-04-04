---
title: "Automation"
weight: 30
---

# Home Assistant Automation

GbbOptimizer exchanges data with Home Assistant through MQTT topics for sensor input and command output.

## Data Input (HA → GbbOptimizer)

Publish sensor data to `<plantId>/ha_gbb/sensor` in JSON format.

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| soc | number | Battery State of Charge (%) — or voltage if SOC not available |
| total_loads | number | Total household loads (kWh) |
| grid_import | number | Grid import total (kWh) |
| grid_export | number | Grid export total (kWh) |
| pv_generation | number | PV generation total (kWh) |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| ev_charging | number | EV charger consumption (kWh) |
| heat_pump | number | Heat pump consumption (kWh) |
| additional_meters | number | Additional meter readings (kWh) |

### Notes

- Total counters may reset periodically for daily tracking
- Negative values indicate missing data
- Multiple PV sources use the "more" array structure with numbered entries
- Recommended: trigger MQTT publish every 5 minutes

## Command Output (GbbOptimizer → HA)

GbbOptimizer sends operational commands via these topics:

| Topic | Description |
|-------|-------------|
| `<plantId>/ha_gbb/Start_Charge` | Begin battery charging |
| `<plantId>/ha_gbb/Start_Discharge` | Begin battery discharging |
| `<plantId>/ha_gbb/Start_DisableCharge` | Prevent battery charging |
| `<plantId>/ha_gbb/Start_Normal` | Return to normal operation |

Command payloads include scheduling details, power limits, pricing indicators, and target SOC levels.

## Example Automation

A typical HA automation triggers every 5 minutes to publish sensor data, and a trigger-based automation switches battery priority based on received charge/discharge commands.
