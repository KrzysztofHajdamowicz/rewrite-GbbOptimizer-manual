---
title: "SolarAssistant"
weight: 20
---

# Home Assistant with SolarAssistant

This guide covers connecting GbbOptimizer to Home Assistant via {{< glossary "SolarAssistant" >}} with a Deye Hybrid inverter.

## Prerequisites

In SolarAssistant's advanced MQTT configuration, set **"Allow setting changes"** to **Enabled**.

## MQTT Topics — Read (Data from Inverter)

| Data | Topic |
|------|-------|
| Battery SOC | `{PlantId}/solar_assistant/total/battery_state_of_charge/state` |
| Battery voltage | (alternative if SOC option disabled) |
| Grid energy in | `total/grid_energy_in/state` |
| Grid energy out | `grid_energy_out/state` |
| Load energy | `total/load_energy/state` |
| PV energy | `total/pv_energy/state` |
| Inverter work mode | `inverter_1/work_mode/state` |
| Max charge current | `max_charge_current/state` |

## MQTT Topics — Write (Commands to Inverter)

| Control | Topic |
|---------|-------|
| Capacity points | `capacity_point_{i}/set` |
| Voltage points | `voltage_point_{i}/set` (voltage mode) |
| Grid charge settings | `grid_charge_point_{i}/set` |
| Work mode | `work_mode/set` |
| Max charge current | `max_charge_current/set` |

## Load Data Import

For Solarman/DeyeCloud plants, loads can be imported from SolarAssistant by configuring the bridge topic as `solar_assistant/total/load_energy/` and selecting the option in plant properties.
