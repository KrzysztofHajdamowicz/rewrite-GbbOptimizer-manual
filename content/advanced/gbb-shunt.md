---
title: "GbbShunt"
weight: 20
---

# GbbShunt

GbbShunt is a specialized module for managing **lead-acid batteries** through voltage-based regulation rather than {{< glossary "SOC" >}} calculations.

## Functions

1. **SOC Calculation** — calculates SOC based on energy sent and received from the battery
2. **Charge Control** — ends battery charging and discharging when the indicated SOC level is reached

## Configuration Parameters

| Parameter | Description |
|-----------|-------------|
| Enabled | Activate the module |
| Battery minimal SOC | Lower threshold for automatic reset |
| V when SOC is Minimum | Voltage trigger for minimum SOC |
| Battery maximal SOC | Upper threshold for automatic reset |
| V when SOC is Maximum | Voltage trigger for maximum SOC |
| Losses on charge+discharge (%) | Energy loss factor in calculations |
| V during charge battery | Voltage setpoint during charging |
| V during discharge battery | Voltage setpoint during discharging |

## Notes

- SOC automatically resets when calculations exceed 100% or drop below 0%
- Module updates every minute via Solarman connection
- For optimal performance, configure the inverter to transmit data every **1 minute** (default is 5 minutes)

## GbbShunt Monitor

The monitor displays real-time data collected by the GbbShunt module, providing visibility into current battery management operations.
