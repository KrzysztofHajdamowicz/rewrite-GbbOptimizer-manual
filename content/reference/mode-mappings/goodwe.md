---
title: "Goodwe"
weight: 20
---

# Goodwe Mode Mapping

| Mode | BatteryCDMode | Power Parameter | Notes |
|------|---------------|-----------------|-------|
| Normal | — | — | No charge/discharge enabled |
| Charge | 2 | ChargeLimitW | Active charging to target SOC |
| Discharge | 3 | DischargeLimitW | Auto-recalculates if discharge extends across full hour |
| DisableCharge | 2 | 0 W | Prevents charging |

> **Not yet implemented:** "limit battery TargetSOC" and "all options for Price<0"

The discharge mode uses the formula: `DischargeLimitW = Max GridSetpoint / Discharge (W)`

If discharge must extend across a full hour period, the program automatically recalculates the power values.
