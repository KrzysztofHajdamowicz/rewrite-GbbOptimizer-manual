---
title: "Hinen"
weight: 30
---

# Hinen Mode Mapping

| Mode | Work Mode | Charge/Discharge | SOC | Rate | AntiBackflow |
|------|-----------|------------------|-----|------|-------------|
| Normal | Self-consumption | Disabled | — | — | — |
| Charge | Time period control | Charge enabled | Target SOC% | SOC-based calculation | Optional |
| Discharge | Time period control | Discharge enabled | Min SOC% | Dynamic adjustment | Enable + limit |
| DisableCharge | Time period control | Charge enabled | Current SOC | 1% rate | Optional |

## Discharge Formula

```
DischargeLimit = Max GridSetpoint / Discharge (W)
```

Adaptive calculations apply when discharge duration must extend across full hours.
