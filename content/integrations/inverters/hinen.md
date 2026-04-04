---
title: "Hinen"
weight: 50
---

# Hinen Integration

## Mode Mappings

See [Hinen Mode Mapping]({{< relref "/reference/mode-mappings/hinen" >}}) for the full protocol mode to register mapping.

| Mode | Work Mode | Description |
|------|-----------|-------------|
| Normal | Self-consumption | No charge/discharge control |
| Charge | Time period control | Scheduled charging with SOC-based rate |
| Discharge | Time period control | Scheduled discharging with dynamic rate |
| DisableCharge | Time period control | Restricts charging to current SOC at 1% rate |
