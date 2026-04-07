---
title: "Victron"
weight: 50
translationKey: "victron-pasywny"
---

# Mode Mapping — Victron

{{< badge "victron-only" >}}

Victron inverters are controlled through {{< glossary "ESS" >}} (Energy Storage System) via {{< glossary "VRM" >}} and MQTT.

## ESS Mode

GbbOptimizer controls the Victron system through ESS Schedules on the Cerbo GX. Schedules define:

- **Operating mode** — charging, discharging, normal operation
- **Target SOC** — the level to charge/discharge to
- **Power limit** — maximum charging/discharging power
- **Time window** — hours during which the schedule is active

## Prerequisites

1. In the {{< glossary "VRM" >}} portal, enable remote access to Cerbo
2. In {{< glossary "ESS" >}}, set the mode to **"Optimized (without BatteryLife)"**
3. Ensure GbbOptimizer has correct VRM data ({{< glossary "PlantId" >}}, {{< glossary "PlantToken" >}})

> [!NOTE]
> If **Battery Life** is enabled in ESS, GbbOptimizer will not be able to fully control the battery. Disable it and set to **"Optimized (without BatteryLife)"**.

## Control

GbbOptimizer communicates with Cerbo through Victron's MQTT servers. In each optimization cycle the program:

1. Reads current data (SOC, PV production, consumption, grid status)
2. Calculates the optimal schedule
3. Writes ESS schedules to Cerbo

Detailed information about Victron MQTT topics is available in the MQTT API documentation.

## Further Reading

- [Victron ESS Documentation](https://www.victronenergy.com/media/pg/Energy_Storage_System/en/index-en.html)
- [VRM Portal](https://vrm.victronenergy.com/)
