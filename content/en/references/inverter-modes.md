---
title: "Inverter Modes"
weight: 20
translationKey: "tryby-falownikow"
---

# Inverter Modes

GbbOptimizer controls the inverter using four basic modes (protocol operations). Each inverter implements them differently — see the [Mode Mappings]({{< relref "/references/mode-mappings" >}}) section for detailed mappings.

## Required Data from the Inverter

The inverter must provide the following data:

| Field | Description |
|-------|-------------|
| `soc_perc` | Battery {{< glossary "SOC" >}} in percent (or `V` if controlling via voltage) |
| `loads_total_kWh` | Consumption counter (kWh, cumulative) |
| `fromgrid_total_kWh` | Grid import energy counter (kWh) |
| `togrid_total_kWh` | Grid export energy counter (kWh) |
| `pv_total_kWh` | PV production counter (kWh) |

Optionally:

| Field | Description |
|-------|-------------|
| `ev_charge_total_kWh` | EV charging counter |
| `hp_total_kWh` | Heat pump counter |
| `other1_total_kWh` ... `other2_total_kWh` | Other counters |

## Operation Modes

### Normal

Return to normal operation:
- PV powers the home, then the battery, then the grid
- Home is powered from PV, then from battery, then from grid

### Charge

Start charging the battery from PV and/or grid to the specified {{< glossary "SOC" >}} level at the specified rate (W).

After the target SOC is reached:
- Do not charge the battery from the grid
- Do not discharge the battery below the target SOC
- Charging the battery from PV is allowed

### Discharge

Start discharging the battery (and PV) to the grid down to the specified {{< glossary "SOC" >}} level at the specified rate (W).

### DisableCharge

Disable battery charging. Energy from PV is sent to the home and grid.

## Mappings for Individual Inverters

- [Deye (Solarman / DeyeCloud / SolarAssistant)]({{< relref "/references/mode-mappings/deye" >}})
- [GoodWe]({{< relref "/references/mode-mappings/goodwe" >}})
- [Hinen]({{< relref "/references/mode-mappings/hinen" >}})
- [Sofar]({{< relref "/references/mode-mappings/sofar" >}})
- [Victron (passive mode)]({{< relref "/references/mode-mappings/victron-passive" >}})
