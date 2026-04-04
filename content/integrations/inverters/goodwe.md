---
title: "Goodwe"
weight: 30
---

# Goodwe Integration

## Setup

1. In the **SEMS** program, go to Management menu and add `gbbsoft@gbbsoft.pl` as a **Guest** to your Power Plant data
2. Add the Goodwe installation in GbbOptimizer — do **not** select SerialNumber yet (leave the list empty)
3. Enable **"Share Technical Support Installation"** at the bottom of the page
4. Contact the developer on [Discord](https://discord.gg/XEhNSqQ6Jj) (user: gbbsoft) with your inverter's SerialNo
5. The developer will configure the appropriate SerialNo in your installation

## Mode Mappings

| Mode | BatteryCDMode | Power Parameter |
|------|---------------|-----------------|
| Normal | — | No charge/discharge |
| Charge | 2 | ChargeLimitW |
| Discharge | 3 | DischargeLimitW = Max GridSetpoint / Discharge (W) |
| DisableCharge | 2 | Power = 0 W |

> **Note:** "Limit battery TargetSOC" and "all options for Price<0" are **not yet implemented** for Goodwe.

See [Goodwe Mode Mapping]({{< relref "/reference/mode-mappings/goodwe" >}}) for details.
