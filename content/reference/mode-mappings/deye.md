---
title: "Deye"
weight: 10
---

# Deye Mode Mapping

How GbbOptimizer protocol modes translate to Deye inverter settings.

## Solarman or DeyeCloud (Current Method)

| Mode | Work Mode | Grid Charge | SOC | Power | Notes |
|------|-----------|-------------|-----|-------|-------|
| Normal | — | — | 5% min | — | Default operation |
| Charge | Time of Use | Enabled for period | Target SOC% | Charge power limit | Grid + PV charging |
| Discharge | Selling First | Disabled | Min SOC% | Discharge power | Grid export active |
| DisableCharge | Time of Use | Disabled | Current SOC | 0 W | PV to loads/grid only |

## DeyeCloud Only (Legacy API)

{{< badge "deprecated" >}}

Similar mappings but with limited post-discharge mode handling. Not recommended for new installations.

## SolarAssistant

Simplified parameter mapping for the same four operational modes when using {{< glossary "SolarAssistant" >}} as a bridge.

## Special Scenarios

- **Price < 0** — Generator integration and activation
- **Peak shaving** — Peak load management
- **Zero Export to CT** — Mode transitions for current transformer monitoring
