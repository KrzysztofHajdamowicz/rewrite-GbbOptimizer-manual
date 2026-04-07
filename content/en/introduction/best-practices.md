---
title: "Best practices"
weight: 30
translationKey: "najlepsze-praktyki"
---

# Best practices

Tips and advice from experienced GbbOptimizer users.

## Patience

> [!WARNING]
> The most common mistake of new users is making configuration changes too quickly. The program needs time to calibrate.

GbbOptimizer is a program that teaches patience. During the first week of operation:

- {{< glossary "Correction Factor" >}} for the PV forecast calibrates itself
- The consumption profile collects historical data
- The optimizer "learns" your installation

Do not disable {{< glossary "Test Mode" >}} sooner than after one week. Give the program time to collect data.

## Set MaxSOC to 90%

{{< badge "recommended" >}}

Set {{< glossary "MaxSOC" >}} to **90%** instead of 100%. Why?

- You leave a **10% buffer** for unexpected PV surplus (when the forecast is too low)
- PV surplus is not wasted — it goes into the battery instead of being sold to the grid at a low price
- The battery less often reaches 100%, which extends its lifespan

### Periodic full charging

For battery health, it is worth periodically charging to 100%. Set the parameter **"List of days in the month when MaxSOC should be changed to 100%"** to, for example:

```
1, 15
```

This way, on the 1st and 15th of every month, the battery will charge to full (for about 2 hours), which allows {{< glossary "SOC" >}} calibration and is beneficial for cell chemistry. More about this parameter: {{< glossary "Battery Full Date" >}}.

## Change the PV forecast source

{{< badge "recommended" >}}

The default PV forecast source is **forecast.solar**. Consider switching to **solcast.com**, which is usually more accurate:

1. Create a free "Home" account at [solcast.com](https://solcast.com)
2. Add your PV planes (one account supports up to two planes)
3. In the installation parameters, change the PV forecast source to Solcast

> [!NOTE]
> Solcast has a request limit on the free account — one "Home" account supports a maximum of two PV planes. If you have more, you need additional accounts.

## Fewer options = greater savings

The fewer additional options checked in the optimizer parameters, the better the results. Each additional option is an additional constraint that reduces the optimizer's room to maneuver.

Start with the default configuration and only add options when you have a specific reason.

## Solarman and Home Assistant — avoid conflict

> [!WARNING]
> If you use Solarman and simultaneously import data from the inverter to Home Assistant, set the `update_interval` to **at least 20 seconds**. Too frequent polling causes communication conflicts — Solarman and Home Assistant "fight" for access to the inverter.

Alternative solution: switch from Solarman to {{< glossary "GbbConnect2" >}}, which does not have this problem.

## Verify input data

After initial configuration, check three key elements:

### 1. Prices

Make sure that [prices]({{< relref "/configuration/prices" >}}) are correct:
- Are transport (transmission) costs included?
- Is VAT correct?
- Does the sale price match your tariff?

### 2. PV forecast

Check in the [Battery Forecast]({{< relref "/configuration/battery-forecast" >}}) that the PV forecast is close to actual production. If not — change the forecast source.

### 3. Consumption profile

Verify the [consumption profile]({{< relref "/configuration/consumption-profiles" >}}):
- Do the values correspond to actual home consumption?
- Do weekends differ from working days (if that is the case in reality)?

## Test mode is your friend

Use {{< glossary "Test Mode" >}} not only at the start. Enable it every time you:

- Change significant configuration parameters
- Change the PV forecast source
- Change the energy tariff
- Add a new PV plane

Give the optimizer a day or two to recalculate the new data before letting it control the inverter.

## Summary

| Practice | Priority |
|----------|----------|
| Wait one week before disabling test mode | {{< badge "required" >}} |
| Verify correctness of prices and transport costs | {{< badge "required" >}} |
| Set MaxSOC = 90% | {{< badge "recommended" >}} |
| Change PV forecast to Solcast | {{< badge "recommended" >}} |
| Set periodic charging to 100% (e.g. 1st, 15th of the month) | {{< badge "recommended" >}} |
| Minimize the number of additional options | {{< badge "recommended" >}} |
