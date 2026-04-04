---
title: "Inverter Modes"
weight: 60
---

# Inverter Operating Modes

GbbOptimizer uses four protocol modes to control inverters. Each mode maps to specific register values depending on the inverter brand.

## Protocol Modes

| Mode | Description |
|------|-------------|
| **Normal** | Standard operation — solar feeds loads first, then battery, then grid. No active charge/discharge control. |
| **Charge** | Active battery charging from grid and/or PV to a target {{< glossary "SOC" >}} at a specified power rate. |
| **Discharge** | Battery discharge to grid at controlled power. Sells energy at current grid price. |
| **DisableCharge** | Prevents battery charging from grid. PV goes to loads and grid only. |

## Mode Mapping by Inverter

Each inverter brand implements these modes differently through specific register values:

- [Deye Mode Mapping]({{< relref "mode-mappings/deye" >}})
- [Goodwe Mode Mapping]({{< relref "mode-mappings/goodwe" >}})
- [Hinen Mode Mapping]({{< relref "mode-mappings/hinen" >}})
- [Passive / Victron Mode Mapping]({{< relref "mode-mappings/passive-victron" >}})

## Special Conditions

- **Price < 0** — When electricity prices go negative, special handling activates (relay switching, mode changes)
- **Generator integration** — Generator activation and management
- **Peak shaving** — Load management during peak periods
- **Zero Export to CT** — Prevents grid export via current transformer monitoring
