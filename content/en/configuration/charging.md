---
title: "Charging"
weight: 20
translationKey: "ladowanie"
---

# Charging

The charging module manages battery charging schedules from the grid. In Victron systems it controls the Schedules in the ESS module.

> [!NOTE]
> {{< badge "victron-only" >}} We assume that "Self-consumption above limit" is set to **PV** (not "PV & Battery"), because we want the schedule to stop battery discharging at night.

## Fetch Schedule from Installation

{{< badge "victron-only" >}} The program connects to the installation and retrieves 5 schedules (Schedulers).

## Charging Changes

You can modify the charging parameters:
- **Lock / unlock** a charging row
- Change the **start time** and **duration** — columns "New Start" and "New Duration"
- Change the **SOC limit** — column "New SOCLimit"

After making changes:
- **Save** — changes are saved in the program but not sent to the installation. This lets you test scenarios in [Battery Forecast]({{< relref "/konfiguracja/prognoza-baterii" >}})
- **Send to Installation** — changes are saved and sent to the inverter

The **Clear all new values** button resets the "New Start", "New Duration", and "New SOCLimit" columns.

## Charging Parameters

| Parameter | Inverter | Description |
|-----------|----------|-------------|
| Stretch charging to a full hour | All | Reduces charging power so it lasts the full hour. Use together with the next option! |
| Special speed calculation when SOC = TargetSOC | All | If SOC ≤ TargetSOC, calculate charging power using the formula: PV - Consumption |
| Switch mode to "Zero Export To CT" during grid charging | {{< badge "deye-only" >}} | Prevents grid protection overload when batteries are charging simultaneously with heavy loads running. Works with grid peak-shaving |
| Set MaxDischarge=0 during charging | {{< badge "deye-only" >}} | Blocks battery discharging during charging. Use only when nothing is connected to Load/Backup |
| Set MaxDischarge=0 during normal operation when PurchasePrice < BatteryPrice | {{< badge "deye-only" >}} | Blocks battery discharging during normal operation. Use only when nothing is connected to Load/Backup |
| Do not change PeakShaving W during charging | {{< badge "deye-only" >}} | Leaves the PeakShaving value unchanged during charging |

## Optimizer Settings

Charging is optimized by [Battery Forecast]({{< relref "/konfiguracja/prognoza-baterii" >}}) if:
- It is not locked
- "Do not optimize SOCLimit by Battery Forecast" is not checked

Options:
- **Minimum SOCLimit (%)** and **Maximum SOCLimit (%)** — restricts the range of "New SOCLimit" (SOC optimizer only)
- **Can be blocked by Battery Forecast** — the optimizer can block charging to make room for PV

> [!NOTE]
> Setting SOCLimit = 5% blocks battery discharging.

## Dynamic Charge — dynamic charging time adjustment

Dynamic Charge automatically searches for hours with the **lowest purchase price** and moves charging there.

> [!WARNING]
> Do not use this option with the **price-based optimizer**!

Configuration:

1. Add at least one schedule
2. Select which Charging entry you want to change
3. Enter **from what hour** and **how many hours** the program should search
   - 24 hours → start hour is irrelevant, the program checks 24h from the current hour
   - Less than 24h → the program checks the specified hours. If the period has passed — it checks the next day
4. Enter **how many hours** you want to charge
5. Save

To automate — set up an **Hourly Task** (see below).

To test — press **Optimize Charging now**.

The program moves the start time to minimum-price hours. If two charging entries have overlapping periods — the program searches for different minimum-price hours for each.

## Dynamic Charge: Blocking charging at low prices

Blocks battery discharging when the price is too low compared to the last charging price.

> [!WARNING]
> Do not use this option with the **price-based optimizer**!

Configuration:

1. Add at least one row
2. Select the Charging entry to change (should not be used in other modules)
3. Enter **from what hour** and **how many hours** the program should look for a price lower than the last charging price
   - 24 hours → start hour is irrelevant
   - Less than 24h → checks the specified hours; if they have passed — checks the next day
4. Enter **what percentage** to add to the last charging price (e.g. 10%)
5. Save

**How it works** (example: from hour 0, checking 6h):
1. Searches for the **last charging price**: from the hour before the end of the period, backwards. Retrieves the last charging in the period or the first charging before the period
2. Checks hours where the purchase price < last charging price + "Add percentage". Searches from the start of the period (or from the end of charging)

> [!NOTE]
> One Charging entry can be used in multiple blocks, as long as the hourly periods do not overlap.

> [!WARNING]
> If you have a Charging entry that changes dynamically (e.g. from 0 to 6), configure the blocking schedule for the **same period** (from 0 to 6) **or longer** (e.g. from 0 to 9).

## Hourly Task

To automatically optimize charging and send data to the installation every hour:

Check **Automatically optimize Charging every hour and send information to the Installation**.

## Weather Alerts

The module automatically charges the batteries to 100% (or another value) when significant weather alerts are issued.

Configuration:
1. Add a country (e.g. Poland from MeteoAlarm or IMGW)
2. Add the types of alerts you are interested in
3. For each type, specify **from what level** (that level and above) and **what SOC** to enforce

When an alert of the given type and level appears — the price-based optimizer will enforce the specified SOC level for the duration of the alert, even at the cost of charging from the grid.
