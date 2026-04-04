---
title: "Welcome"
weight: 10
---

# Welcome to GbbOptimizer

**GbbOptimizer** (formerly GbbVictronWeb) is a plant optimization program for managing hybrid inverter systems with battery storage and price-based energy optimization.

## What is a Plant?

A **Plant** represents one physical solar installation — either:
- A **Victron** system (Cerbo GX or other GX module)
- A **Deye** hybrid inverter system
- Another supported hybrid inverter (Goodwe, Afore, Hinen, Sofar)

## How Does It Work?

GbbOptimizer connects to your inverter (via cloud APIs, MQTT, or local dongles) and optimizes battery charge/discharge cycles based on:

1. **Electricity prices** — buys energy when cheap, sells when expensive
2. **PV forecast** — predicts solar generation using forecast.solar or solcast.com
3. **Load profiles** — learns your household consumption patterns
4. **Battery state** — manages SOC (State of Charge) within safe limits

The optimizer runs hourly, calculating the optimal charge/discharge plan for the next hours and sending commands to your inverter.

## Supported Connection Methods

| Method | Inverters | Notes |
|--------|-----------|-------|
| Solarman | Deye, others | {{< badge "deprecated" >}} Use DeyeCloud instead |
| DeyeCloud | Deye | Recommended for Deye inverters |
| GbbConnect2 | Deye, others | Local dongle, ModbusInMqtt protocol |
| DongleDirect | Sofar | Redirects dongle to GbbOptimizer server |
| Home Assistant | All via HA | MQTT bridge integration |
| Victron VRM | Victron | Via VRM Portal API |
| Tuya | Tuya-compatible | Via Tuya Cloud API |
| Supla | Supla-compatible | Via Supla platform |
| Evcc.io | EV chargers | MQTT-based EV charger control |

## Community

Join the [GbbOptimizer Discord](https://discord.gg/XEhNSqQ6Jj) for support and discussion.
