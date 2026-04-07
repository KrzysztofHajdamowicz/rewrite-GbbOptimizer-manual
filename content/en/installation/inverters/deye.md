---
title: "Deye"
weight: 20
translationKey: "deye"
---

# Deye

{{< badge "deye-only" >}}

Deye hybrid inverters can be connected to GbbOptimizer in several ways. On this page you will find a checklist of inverter settings and a comparison of connection methods.

## Checklist

Before starting GbbOptimizer, verify the following on the Deye inverter:

1. **Operating mode** — `Zero export to CT` or `Zero export to Loads` (not "Selling First"!)

   > [!WARNING]
   > Do not check the operating mode during active discharge — GbbOptimizer temporarily changes the mode.

2. **TimeOfUse** — must be **enabled**
3. **TimeOfUse** — set to **%** (not V), unless an SOC-to-V mapping is defined
4. **System Work Mode** (Schedule) — enabled for **all 7 days** of the week
5. **Energy pattern** — `Load First`
6. **SolarSell / Sell energy** — **checked**
7. **Grid Charge** — `Enable`
8. **Grid Start, Battery Restart** — values **lower than** {{< glossary "MinSOC" >}}
9. **Data upload interval** — every **1 min** (default is every 5 min — needs to be changed)
10. **Copilot** — must be **disabled**

## Connection methods — comparison

The Deye inverter can be connected to GbbOptimizer in four ways:

|  | [Solarman]({{< relref "/installation/connection-methods/solarman" >}}) / [DeyeCloud]({{< relref "/installation/connection-methods/deye-cloud" >}}) | [GbbConnect2]({{< relref "/installation/connection-methods/gbbconnect2" >}}) | [DongleDirect]({{< relref "/installation/connection-methods/dongle-direct" >}}) | HomeAssistant / {{< glossary "SolarAssistant" >}} |
|--|--|--|--|--|
| **Data from GbbOptimizer to inverter** | GbbOptimizer → DeyeCloud → Solarman → Dongle → Inverter | GbbOptimizer → GbbConnect2 → Dongle → Inverter | GbbOptimizer → Dongle → Inverter | GbbOptimizer → HA Automation → Inverter |
| **Data from inverter to GbbOptimizer** | Inverter → Dongle → Solarman → DeyeCloud → GbbOptimizer | Inverter → Dongle → GbbConnect2 → GbbOptimizer | Inverter → Dongle → GbbOptimizer | Inverter → HA Automation → GbbOptimizer |
| **Data from DeyeCloud/Solarman to inverter** | DeyeCloud → Solarman → Dongle → Inverter | DeyeCloud → Solarman → Dongle → Inverter | DeyeCloud → Solarman → GbbOptimizer → Dongle → Inverter | N/A |
| **Data from inverter to DeyeCloud/Solarman** | Inverter → Dongle → Solarman → DeyeCloud | Inverter → Dongle → Solarman → DeyeCloud | Inverter → Dongle → GbbOptimizer → Solarman → DeyeCloud | N/A |
| **Dongle disconnection problem** | Yes | No | Yes | No |
| **Required software** | None | GbbConnect2 on local network | None | HomeAssistant on local network |
| **Data passes through Chinese servers** | Yes | Yes (no, if you block Dongle at firewall) | Your choice | No |
| **Parameter changes from outside home** | Yes | No (but you can use Solarman/DeyeCloud in parallel) | Your choice | Yes |

> [!NOTE]
> Detailed configuration instructions for each method can be found in the [Connection methods]({{< relref "/installation/connection-methods" >}}) section.
