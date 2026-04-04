---
title: "Passive / Victron"
weight: 40
---

# Passive Mode Mapping (Victron)

For Victron systems in passive mode (`StorageMode = 3 = PassiveMode`, `ManagementMode = 1 = Manual`).

## Parameters

| Abbreviation | Meaning |
|-------------|---------|
| Gdes | Grid setpoint (default) |
| Blo | Battery low limit |
| Bup | Battery high limit |
| Gdzup | Grid high setpoint |
| Gdzlo | Grid low setpoint |

## Mode Mapping

| Mode | Grid Setpoint | Battery Charge | Battery Discharge | Buy Power | Sell Power |
|------|--------------|----------------|-------------------|-----------|------------|
| Normal | Gdes (default from Discharge menu) | Limit applies | Limit applies | Managed | Managed |
| Charge | Gdzup (grid high) | Charge limit | Disabled | Input limit | — |
| Discharge | Gdzlo (grid low) | Disabled | Battery low limit | — | Sell power limit |
| DisableCharge | — | Disabled | Disabled | Managed | Managed |

This mapping requires systems supporting five parameters for full control.
