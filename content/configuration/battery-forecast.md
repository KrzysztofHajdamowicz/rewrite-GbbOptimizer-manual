---
title: "Battery Forecast"
weight: 20
---

# Battery Forecast

The Battery Forecast module is the heart of GbbOptimizer. It calculates the optimal charge/discharge plan based on PV forecasts, electricity prices, and load profiles.

## Main Chart

The Battery Forecast page displays a chart showing hourly projections including:
- Battery SOC levels throughout the day
- PV production forecast
- Expected loads
- Grid import/export
- Calculated profit

## Test Mode

> [!WARNING]
> New plants start in **{{< glossary "Test Mode" >}}**. In this mode, the optimizer calculates forecasts but does **not** send any commands to your inverter.

Keep test mode active for approximately **one week** to allow:
- Load profile data to accumulate
- {{< glossary "Correction Factor" >}} to be calculated
- PV forecast accuracy to be validated

To go live, disable Test Mode in this module.

## PV Forecast Source

| Source | Notes |
|--------|-------|
| forecast.solar | Default, no account needed |
| solcast.com | {{< badge "recommended" >}} Better accuracy. Free Home account supports up to 2 PV fields |

## MaxSOC Setting

Set {{< glossary "MaxSOC" >}} to **90%** (recommended). This provides a buffer for PV forecast inaccuracies — if the forecast overestimates solar production, the battery still has headroom.

## Battery Full Dates

Configure specific days for 100% battery charge cycles using {{< glossary "Battery Full Date" >}}. Enter as comma-separated day numbers (e.g., `1, 15` for the 1st and 15th of each month).

## Optimizer Parameters

> [!NOTE]
> **The fewer additional options selected in the optimizer parameters, the greater the profits.** Only enable options you specifically need.
