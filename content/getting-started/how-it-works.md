---
title: "How It Works"
weight: 30
---

# How GbbOptimizer Works

## Architecture Overview

GbbOptimizer runs as a cloud service that connects to your inverter and optimizes battery usage.

```
┌──────────────┐     MQTT/API     ┌────────────────────┐     Modbus/API     ┌───────────┐
│  GbbOptimizer│◄────────────────►│  Connection Layer  │◄──────────────────►│ Inverter  │
│  Cloud       │                  │  (Solarman/Cloud/  │                    │ + Battery │
│              │                  │   GbbConnect2/HA)  │                    │           │
└──────┬───────┘                  └────────────────────┘                    └───────────┘
       │
       │ Fetches
       ▼
┌───────────────┐
│ External Data │
│ - PV Forecast │
│ - Electricity │
│   Prices      │
└───────────────┘
```

## Optimization Cycle

Every hour, GbbOptimizer:

1. **Collects data** — current SOC, PV production, grid import/export, loads
2. **Fetches forecasts** — PV generation forecast, electricity prices
3. **Calculates optimal plan** — determines when to charge, discharge, or idle
4. **Sends commands** — sets the inverter mode for the next period

## Four Operating Modes

GbbOptimizer controls your inverter through four protocol modes:

| Mode | Description |
|------|-------------|
| **Normal** | Standard operation — solar feeds loads, then battery, then grid |
| **Charge** | Active battery charging from grid and/or PV to a target SOC |
| **Discharge** | Battery discharge to grid at controlled power |
| **DisableCharge** | Prevents battery charging from grid; PV goes to loads and grid |

How these modes map to specific inverter register values depends on your hardware. See [Mode Mappings]({{< relref "/reference/mode-mappings" >}}).

## Data Flow

The system collects and processes several types of data:

- **Real-time telemetry** — SOC, voltage, power flows (updated every 1-5 minutes)
- **PV forecast** — from forecast.solar or solcast.com (updated periodically)
- **Electricity prices** — from configured price sources (ENTSO-E, Tibber, Amber, etc.)
- **Load profiles** — learned from historical consumption data
- **Extra loads** — EV charging, heat pumps (from IoT meters or manual entry)

All this feeds into the Battery Forecast algorithm, which produces the hourly optimization plan visible on the main chart.
