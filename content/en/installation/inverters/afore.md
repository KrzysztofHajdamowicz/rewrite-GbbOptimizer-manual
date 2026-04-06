---
title: "Afore"
weight: 40
translationKey: "afore"
---

# Afore

Configuring an Afore inverter with GbbOptimizer. GbbOptimizer controls the Afore inverter via the {{< glossary "Modbus" >}} protocol.

## GbbOptimizer mode mapping to Afore settings

| Operation | Register | Value | After completion |
|-----------|----------|-------|-----------------|
| **AC charging maximum SOC** | Charging: target {{< glossary "MaxSOC" >}} | — | — |
| **ACCharging start/end time (1-4)** | Charging: array of next 4 periods | — | — |
| **Forced charging start/end time (1-4)** | Charging: array of next 4 periods | — | — |
| **ACCharging power percentage** | Charging: Input Limit | % of MaxBuyPower or MaxBatteryChargeDC | Restore original value |
| **Forced charging power percentage** | Charging: Charge Limit | % of MaxBatteryChargeDC | Restore original value |
| **Minimum SOC for forced discharge** | Discharge: target {{< glossary "MinSOC" >}} | — | — |
| **Forced discharge start time (1-4)** | Discharge: array of next 4 periods | — | — |
| **Power grid power limit percentage** | Discharge: {{< glossary "GridSetpoint" >}} | % of MaxSellPower or MaxBatteryDischargeDC | — |
| **Maximum charging current** | Charge block: sets `0` | — | Restore original value |

## Checklist

- **Timing DChg ON/OFF** = `Enable`
- **PDisChgMax** (Forced discharge power percentage) = `100%`
