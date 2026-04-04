---
title: "Victron"
weight: 10
---

# Victron Integration

## Checklist

Before connecting your Victron system to GbbOptimizer, verify:

- [ ] **No beta firmware** — use stable firmware only
- [ ] **DESS disabled** — Disable DESS (Dynamic ESS)
- [ ] **Scheduler configured** — "Self-consumption above limit" set to **PV** (not "PV & Battery")
- [ ] **Battery Life disabled** — turn off Battery Life feature
- [ ] **Log interval** — set to **1 minute**
- [ ] **Full Control enabled** — enable in {{< glossary "VRM" >}} portal
- [ ] **Cerbo restarted** — restart after configuration changes

## VRM Portal Setup

Enter your {{< glossary "VRM" >}} Portal credentials in the Plant section:
- VRM Portal ID
- Login email
- Password

## Topics Modified by GbbOptimizer

GbbOptimizer only modifies these specific Victron/{{< glossary "ESS" >}} properties:

| Property | Description |
|----------|-------------|
| Charging Schedules (1-5) | Day, SOC limit, start time, duration |
| ESS/Minimum SOC | MinimumSocLimit |
| ESS/Grid setpoint | AcPowerSetPoint |
| Relay 1 & 2 states | Triggered when Price < 0 |
| Inverter mode | Changed when Price < 0 |
| DC-coupled PV feed-in excess | Overvoltage feed-in setting |
| MultiPlus input current limiting | Grid import power limit |
| DVCC max charge current | Battery charge current limit |

These are the **only** properties modified by the application, ensuring predictable system behavior.
