---
title: "Battery Forecast"
weight: 10
translationKey: "prognoza-baterii"
---

# Battery Forecast

The central module of GbbOptimizer. It analyzes {{< glossary "SOC" >}} of the battery for the next 24 hours (or more) based on PV charging, grid charging, discharging, and home consumption. It includes an optimizer that automatically selects charging and discharging parameters.

In this module you can:
- Analyze the battery SOC forecast for the next 24 hours
- See when SOC exceeds minimum or maximum values
- Optimize charging and discharging plans
- View purchase and sale prices and profits

## Forecast Table Columns

The table shows data for the next 24 hours. Abbreviations: **DC** = direct current, **AC** = alternating current.

### Battery

| Column | Description |
|--------|-------------|
| Day | Day |
| Hour | Hour of the given day |
| Start battery % (kWh) AC/DC | Battery SOC and kWh at the start of the hour (in AC and DC) |
| PV Forecast (kWh AC) | PV production forecast for this hour |
| PV Forecast % (kWh DC) | How many kWh from PV go to the battery (after DC conversion), after subtracting home consumption |
| Consumption +Extra (kWh AC) | Home consumption forecast (including Extra Consumption) |
| Consumption +Extra % (kWh DC) | How many kWh drawn from the battery to cover consumption minus PV |
| Grid charging (kWh AC) | How much drawn from the grid to charge the battery |
| Grid charging % (kWh DC) | Same as above, after DC conversion |
| Discharging | Discharge Plan status for this hour |
| Discharging (kWh AC) | How much sent from the battery to the grid (in AC) |
| Discharging % (kWh DC) | How much sent from the battery to the grid (in DC) |
| End battery (kWh AC) | kWh in the battery at the end of the hour. **= Start AC + PV AC - Consumption AC + Charging AC - Discharging AC** |
| End battery % (kWh DC) | SOC and kWh at the end of the hour. **= Start DC + PV DC - Consumption DC + Charging DC - Discharging DC** |
| Below Min | "Yes" = end battery may drop below {{< glossary "MinSOC" >}} |
| Above Max | "Yes" = end battery may exceed {{< glossary "MaxSOC" >}} |

### Profit

| Column | Description |
|--------|-------------|
| Profit amount | **= Consumption amount - (Purchase amount - Battery value change) + Sale amount - Battery cost amount** |
| Unpaid energy amount | **= Sale amount - (Purchase amount - Battery value change) - Battery cost amount** |
| Battery cost amount | "Battery usage cost per kWh" × "Battery charging kWh" — battery depreciation |
| From grid (kWh) | How much drawn from the grid in this hour |
| Purchase price | Energy purchase price |
| Purchase amount | From grid × Purchase price |
| To grid (kWh) | How much sent to the grid |
| Sale price | Energy sale price |
| Sale amount | To grid × Sale price |
| Consumption (kWh) | Home consumption |
| Consumption price | Price of energy consumed by the home |
| Consumption amount | Consumption × Consumption price |

### Battery Energy Value

| Column | Description |
|--------|-------------|
| Battery charging (kWh) | >0 charging, <0 discharging — how much energy went to/from the battery |
| Grid charging (kWh) | How much energy sent to the battery comes from the grid |
| Discharging (kWh) | How much energy drawn from the battery |
| Start kWh in battery | Energy in battery at the start of the hour (above MinSOC%) |
| Start value | Value of energy in the battery at the start of the hour |
| End kWh in battery | Energy in battery at the end of the hour (above MinSOC%) |
| End value | Value of energy in the battery at the end of the hour |
| Value change | **= End value - Start value.** Discharging: Discharging kWh × Average price from previous hour. Charging: Grid charging kWh × Purchase price |
| Average end price | End value / End kWh in battery |

## Optimizer

After clicking **Run Optimizer now**, the program can change:
- SOCLimit in the [Charging]({{< relref "/konfiguracja/ladowanie" >}}) module (and even block charging)
- MinSOC in the [Discharging]({{< relref "/konfiguracja/rozladowanie" >}}) Plan
- Disable DDBD (Dynamic Battery Discharge Blocking)

### Optimizer 1: SOC-based

**"Charging/Discharging is optimized based on SOC (with additional optimizers)"**

This optimizer tries to:
- Reach 100% (or {{< glossary "MaxSOC" >}}) at some point (but not for too long)
- Keep the battery above {{< glossary "MinSOC" >}} — which is more important
- Uses the set charging and discharging times (these must be manually configured beforehand)

> [!NOTE]
> - Can be combined with {{< glossary "Dynamic Discharge" >}} and Dynamic Charge
> - Can charge the battery at night (cheap tariff) to leave room for PV during the day
> - Can discharge the battery at high prices so that PV charges it to MaxSOC
> - If the purchase price < 0, charging during those hours is set to MaxSOC

### Optimizer 2: Price-based {{< badge "recommended" >}}

**"Charging/Discharging is optimized based on purchase and sale prices (to increase Profit)"**

Tries to maximize the sum in the "Profit amount" column — finds the best combination of charging/discharging for each hour.

> [!WARNING]
> After optimization, the new settings **are not automatically sent** to the installation. Check the results, then press **Send new SOCLimit from Charging to Installation**.

> [!NOTE]
> - Should be run every hour
> - Requires the import in the [Gains]({{< relref "/konfiguracja/zyski" >}}) module to run every hour
> - Charging when energy is never consumed (because the forecast runs for 24h) is "free" — at the end of the period, excess charging often appears. Wait a few hours for a better forecast
> - Each additional enabled option reduces profits!

## Price-based Optimizer Parameters

### SOC

| Parameter | Description |
|-----------|-------------|
| I prefer to have more in the battery than less | Strategy for situations where different charge levels give the same profit: **Level 0** — prefer not to charge. **Level 1** — prefer to charge more. **Level 2** — prefer to charge more + prefer charging over not charging (for G12w tariff) |
| Maximum battery SOC (%) | The optimizer tries not to exceed this value |
| Minimum battery SOC (%) | The optimizer tries not to go below this value |
| Increase Min/Max SOC by X if PV Forecast < Y | Increase battery reserve when PV forecast is low |
| Force MaxSOC (100%) daily — UPS | Once a day for 2–3h the battery is charged to 100% |
| ... only during optimization from midnight to sunrise | Forcing calculated only at night — if the weather forecast drops, the program does not try to reach 100% during the day |
| ... replace sunset with a fixed hour | E.g. the end hour of cheap tariff instead of sunset |

### Battery Balancing

| Parameter | Description |
|-----------|-------------|
| Minimum SOC to consider as balancing | SOC from which the program considers balancing to be in progress. If SOC drops slightly — enter a lower value |
| Must last at least (hours) | Duration of balancing |
| List of days in month for 3h×100% | Force balancing on these days of the month (comma-separated) |
| How many days back to check 3h×100% | Prevents too-frequent balancing |
| After how many days to hold 3h×100% again | Alternative forcing: every X days from the previous one |
| Manually force 3h×100% today | One-time forcing, disables itself after balancing |
| 3h×100% if price < ... for at least ... hours | Force balancing when purchase price is low |

### Charging and Discharging

| Parameter | Description |
|-----------|-------------|
| Battery charging from grid | Allows disabling grid charging |
| Battery discharging to grid | Allows disabling discharging (or keeping the Discharge Plan settings) |
| Min price difference for grid discharging | Minimum difference between battery energy price and sale price. Value 0 = the program does not discharge at a loss |
| Do not discharge when sale price < X | Blocks discharging at low sale price |
| Do not discharge when purchase price < X | Blocks discharging — idea: in cheap tariff draw from grid, charge battery from PV, discharge at expensive tariff |
| Do not charge from grid when purchase price > X | Blocks charging at too high a price |

### Grid Import / Export

| Parameter | Description |
|-----------|-------------|
| Try not to import from grid | The optimizer avoids drawing from the grid (but it may happen). To completely block — check "Locked" in the [Charging]({{< relref "/konfiguracja/ladowanie" >}}) module |
| Try not to export to grid | The optimizer avoids export (from PV and battery) |
| Do not sell more than the non-adjusted 24h PV forecast | *(Option for PL)* Blocks selling more from the battery than was produced from PV. Computation cost: O(n) |
| Try not to export when sale price < 0 | Avoid export at negative prices |

### Other Parameters

| Parameter | Description |
|-----------|-------------|
| Block entry above MaxSOC | Forces discharging to MaxSOC |
| Block drop below MinSOC | Forces charging to MinSOC |
| Do not charge from grid when EV will be charging | During EV charging — no battery charging from grid |
| Do not discharge when EV will be charging | During EV charging — no battery discharging |
| Test EV charging every 5 min | Auto-detection of EV charging and disabling battery charging/discharging. No need to enter in advance |
| Try to forecast > 24h | The optimizer considers more hours (until the end of known prices). May disable itself if it takes too long |
| Do not revert to "do nothing" forecast | Disables checking whether the devised forecast is worse than "do nothing" |
| Calculate energy cost at the time of charging | Normally the cost is settled at the time of consumption. This option settles at the time of purchase |
| Min/Max SOC at the end of forecast | Forcing SOC level at the end of the forecast |
| Battery usage cost per kWh | = Battery purchase cost / (number of cycles × capacity kWh). We recommend leaving it empty |

## Run Schedule

| Time intervals | Optimizer | Export to inverter |
|----------------|-----------|-------------------|
| 24 (60 min) | after x:00 | after x:00 (retry on error) |
| 48 (30 min) | after x:00 and x:30 | after x:00 and x:30 (retry on error) |
| 96 (15 min) | after x:00 and x:30 | after x:00, x:15, x:30, x:45 |

## Testing Scenarios

To test different scenarios:
- Create more than one [Consumption Profile]({{< relref "/konfiguracja/profile-zuzycia" >}})
- Create more than one Discharge Plan
- Temporarily disable the PV forecast (worst case scenario)
- In the Charging module, set "New Start", "New Duration", and "New SOCLimit" without sending to the installation

In the **Filters** section, select the current Consumption Profile, Discharge Plan, and optionally disable the PV forecast.

## Hourly Tasks

When manual optimization works correctly — set the hours for automatic execution.

Best time (for the SOC optimizer): initial hours of active charging. If you use a Discharge Plan — best to run every hour.

To run:
1. Check **Automatically press: "Fetch all data" and "Run Optimizer"**
2. Check **... and "Send new SOCLimit to Installation"**
3. Add one or more hours

### Additional Options

| Option | Description |
|--------|-------------|
| Also run at half-past the hour | For 24 intervals (60 min): additional run at x:30. Not recommended |
| Send data to inverter earlier | First send settings (calculated an hour earlier), then run the optimizer, then send new settings. Useful when the optimizer takes 4–5 min. For 96 intervals: always enabled |
| Fetch PV Forecast only during Hourly Tasks | PV forecast imported only during hourly tasks (not during "Fetch all data"). Allows you to see the last forecast used in optimization |
