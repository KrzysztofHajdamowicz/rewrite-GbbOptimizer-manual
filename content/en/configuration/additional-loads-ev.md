---
title: "Extra Consumption / EV"
weight: 60
translationKey: "dodatkowe-obciazenia-ev"
---

# Extra Consumption / EV

Extra Consumption is the portion of energy consumption that **does not enter the home average** — for example, charging an electric vehicle or a heat pump. The goal is to separate the unpredictable, variable part from standard consumption.

**Data flow:**
- IoT meters → Extra Consumption → [Gains]({{< relref "/configuration/gains" >}}) → [Battery Forecast]({{< relref "/configuration/battery-forecast" >}})
- EV chargers → Extra Consumption → Gains → Battery Forecast

## AutoConverter

AutoConverter detects peaks in consumption and automatically converts them into vehicle charging (or another type of Extra Consumption).

| Parameter | Description |
|-----------|-------------|
| Consumption limit above which AutoConverter activates (kWh/h) | AutoConverter activates only after this threshold is exceeded |
| Consumption never converted to Extra Consumption | This energy always remains as Consumption |
| Maximum Extra Consumption (kWh/h) | Maximum converted energy (e.g. EV charger power). The rest = Consumption |
| Extra Consumption Type | The type to which the converted energy is directed |

AutoConverter runs during import in the [Gains]({{< relref "/configuration/gains" >}}) module.

## AutoAdd

A mechanism for continuously filling Extra Consumption — for devices that run on a schedule and have no dedicated meter.

| Parameter | Description |
|-----------|-------------|
| Locked | The row is not taken into account |
| Extra Consumption Type | Extra Consumption type filled according to this row |
| Extra Consumption (kWh/h) | Energy consumed per hour |
| FromDay, ToDay | Active period (FromDay must be filled) |
| FromHour, ToHour | Hourly range within the day |
| Mon, ..., Sun | Days of the week |
| Repeat every X weeks | How often the row applies (counting from FromDay) |

> [!NOTE]
> Check **Automatically import data from EV chargers and AutoAdd ExtraLoads every hour** to have AutoAdd run automatically.
