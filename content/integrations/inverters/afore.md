---
title: "Afore"
weight: 40
---

# Afore Integration

## Register Parameters

GbbOptimizer controls Afore inverters through the following registers:

| Parameter | Purpose | Notes |
|-----------|---------|-------|
| AC charging max SOC | Battery upper limit | Target value |
| AC Charging schedule | Time-based charging | 4-period table |
| Forced charging schedule | Override charging times | 4-period table |
| Charging power % | Input limiting | Based on max buy power |
| Discharge schedule | Timed discharge | 4-period table |
| Grid power limit % | Export control | Based on sell power capacity |
| Charge current | Battery protection | Set to 0 to disable |

## Requirements

- **Timing Discharge ON/OFF** = Enable
- **Forced discharge power percentage** = 100%
