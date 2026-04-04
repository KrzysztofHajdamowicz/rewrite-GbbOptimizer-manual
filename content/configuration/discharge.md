---
title: "Discharge"
weight: 40
---

# Discharge Configuration

The Discharge module controls how and when your battery exports energy to the grid.

## GridSetpoint

{{< glossary "GridSetpoint" >}} determines how much power flows to the grid during normal operation (excluding charging moments or excess power situations):

- **Positive values** — draw power from the grid
- **Negative values** — export power to the grid

## Creating a Discharge Plan

1. Enable the discharge plan
2. Disable **Battery Life** mode if active (Victron)
3. Set {{< glossary "GridSetpoint" >}} (a negative watt value for grid export)
4. Optionally set a {{< glossary "MinSOC" >}} limit

## Job Every Hour

Enable **"Run job every hour"** for automatic hourly discharge management:

| Parameter | Description |
|-----------|-------------|
| Default MinSOC | Floor SOC below which discharge stops |
| Default GridSetpoint | Standard grid export power |

The program blocks further discharge if MinSOC exceeds the current battery state.

## Conditional Discharge by Price

Enable discharge only when the **sell price meets a minimum threshold**:

> Discharge when sell price ≥ MinSellPrice

This prevents selling energy at unfavorable prices.

## Disable Battery Discharge

This option prevents battery discharge below the current SOC without transferring power to the grid. PV charging continues, protecting battery reserves.

## Dynamic Discharge

{{< glossary "Dynamic Discharge" >}} is an advanced feature that enables real-time discharge scheduling based on sale price fluctuations rather than fixed time windows.

Instead of predefined discharge periods, the system continuously evaluates electricity prices and adjusts discharge behavior dynamically to maximize revenue.
