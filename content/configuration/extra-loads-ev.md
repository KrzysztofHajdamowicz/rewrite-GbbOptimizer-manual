---
title: "Extra Loads / EV"
weight: 70
---

# Extra Loads / EV

Extra Loads represent the variable, unpredictable portion of energy consumption separate from standard household profiles — primarily EV charging and heat pumps.

## Data Flow

```
IoT Meters / EV Chargers → Extra Loads → Gain/Profits → Battery Forecast (main chart)
```

## AutoConverter

AutoConverter identifies consumption spikes and automatically converts them to EV charging categories.

| Parameter | Description |
|-----------|-------------|
| Load threshold (kWh/hour) | Activates conversion when consumption exceeds this value |
| Protected loads (kWh/hour) | Energy that remains classified as standard loads |
| Maximum conversion cap (kWh/hour) | Upper limit for converted energy; excess stays as regular loads |
| ExtraLoads classification | Category destination for converted energy |

AutoConverter runs during the Gain/Profits import process.

## AutoAdd

AutoAdd continuously replenishes ExtraLoads for devices operating on schedules without individual consumption meters.

| Parameter | Description |
|-----------|-------------|
| Disabled | Deactivate this row |
| ExtraLoads type | Category: 0=EV, 1=HeatPump, 2-7=Other |
| Consumption rate | Energy per hour (kWh/hour) |
| Date range | Validity period (FromDate required) |
| Time window | Daily hour range (FromHour, ToHour) |
| Weekly recurrence | Repeat interval in weeks |
| Day selection | Mon-Sun availability flags |

> [!NOTE]
> Enable automatic hourly EV charger data imports and AutoAdd processing through the application settings.
