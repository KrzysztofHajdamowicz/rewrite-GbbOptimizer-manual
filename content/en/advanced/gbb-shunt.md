---
title: "GBB Shunt"
weight: 20
translationKey: "gbb-shunt"
---

# GBB Shunt

GBB Shunt is a GbbOptimizer module designed for installations with lead-acid batteries (flooded, gel, AGM).

## What is GBB Shunt?

In installations with lead-acid batteries, the standard {{< glossary "SOC" >}} measurement by the inverter can be inaccurate. GBB Shunt enables more accurate tracking of the battery state of charge based on current measurement through a shunt (coulomb counter).

## Key Features

- **Accurate SOC measurement** — based on current measurement (coulomb counting), not voltage
- **Temperature compensation** — accounts for the effect of temperature on lead-acid battery capacity
- **Battery protection** — prevents deep discharges that shorten the life of lead-acid batteries

## When to Use?

GBB Shunt is recommended if:

- You use lead-acid batteries (not lithium)
- The inverter does not have accurate SOC measurement for lead-acid batteries
- You want to extend battery life through precise cycle control

> [!NOTE]
> Lithium batteries (LiFePO4, Li-ion) with BMS have built-in accurate SOC measurement and do not require the GBB Shunt module.

## Configuration

The GBB Shunt module is configured in the installation settings under the advanced section. It requires:

- Battery capacity (Ah)
- Nominal voltage
- Shunt parameters
