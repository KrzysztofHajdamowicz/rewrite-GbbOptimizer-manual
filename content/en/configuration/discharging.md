---
title: "Discharging"
weight: 30
translationKey: "rozladowanie"
---

# Discharging

The discharging module controls when and how energy from the battery is sent to the grid or used to power the home. The key parameter is {{< glossary "GridSetpoint" >}}.

## GridSetpoint — how it works

{{< glossary "GridSetpoint" >}} determines how much energy should flow through the grid meter:

- **Positive value** (e.g. +100 W) — the system draws energy from the grid. Surplus PV goes to the battery.
- **Negative value** (e.g. -5000 W) — the system exports energy to the grid. First from PV, then from the battery.

**Example 1:** GridSetpoint = +100 W

| Parameter | Value |
|-----------|-------|
| PV producing | 2000 W |
| Home consuming | 500 W |
| From grid | +100 W |
| **To battery** | **1600 W** |

**Example 2:** GridSetpoint = -5000 W

| Parameter | Value |
|-----------|-------|
| PV producing | 2000 W |
| Home consuming | 500 W |
| To grid | 5000 W |
| **From battery** | **3500 W** |

**Example 3:** GridSetpoint = -5000 W, lots of PV

| Parameter | Value |
|-----------|-------|
| PV producing | 6000 W |
| Home consuming | 500 W |
| To grid | 5000 W |
| **To battery** | **500 W** |

To protect the battery during discharging:
- Set {{< glossary "MinSOC" >}} — the battery will not go below this level
- Check "Block battery discharging" — the battery will not go below the current SOC (but can be charged)

## First Step

To start discharging:

1. Create one **Discharge Plan** (if one does not already exist)
2. {{< badge "victron-only" >}} If "Battery Life" is enabled in ESS — disable it. Set it to "Optimized (without BatteryLife)"

## Normal Discharging

To set normal discharging at a selected hour:

1. Check **Enable** for the selected hour
2. Enter **Max GridSetpoint** — a negative value, the maximum W that should go to the grid
3. *(Optional)* Enter **MinSOC** — restricts discharging to the specified SOC level

> [!NOTE]
> The program checks the current battery SOC. If MinSOC is higher than the current SOC, the program will send the current SOC. This prevents the battery from charging to MinSOC instead of discharging.

To test settings for the current hour — press **Send data to installation now**.

## Hourly Tasks

To automatically send data to the installation every hour:

1. Check **Run task every hour**
2. {{< badge "victron-only" >}} Enter the current MinSOC (from ESS in Cerbo) in the **Default MinSOC after discharging** field
3. {{< badge "victron-only" >}} Enter the current GridSetpoint (from ESS) in the **Default GridSetpoint after discharging** field
4. Save changes

> [!NOTE]
> - Every hour the program sends discharging data only for hours with "Enable" checked
> - After the last discharging hour, the program restores the default values
> - The option "Do not discharge if Sale Price < last purchase price" blocks discharging when selling would not be profitable

## Conditional Discharging — when price > minimum

To discharge only when the sale price exceeds a threshold:

1. Check **Enable** for the selected hour
2. Enter **Max GridSetpoint** (negative value)
3. *(Optional)* Enter **MinSOC**
4. Check **Only if Price > MinSalePrice**
5. Enter the limit in **MinSalePrice**

## Blocking battery discharging / charging

To block discharging (or charging) of the battery below the current SOC:

1. Check **Enable** for the selected hour
2. {{< badge "victron-only" >}} Enter **Max GridSetpoint**
3. Check **Block battery discharging** (or **Block battery charging**)

> [!NOTE]
> {{< badge "victron-only" >}} The program sets MinSOC in ESS to the current SOC value, which blocks discharging but allows charging. After that hour, MinSOC returns to the default value.

> [!WARNING]
> {{< badge "victron-only" >}} If you set "Block battery discharging" with GridSetpoint = large negative value (e.g. minus total PV power), all PV energy will go to the grid and the battery will not charge. This can be used to **delay battery charging**.

## Dynamic Discharge (DD)

{{< glossary "Dynamic Discharge" >}} automatically searches for hours with the highest sale price and sets discharging during those hours.

> [!WARNING]
> Do not use this feature with the **price-based optimizer**!

To configure DD:

1. Add at least one discharging period
2. Enter **from what hour** and **how many hours** the program should search
   - 24 hours → start hour is irrelevant, the program checks 24h from the current hour
   - Less than 24h → the program checks from the specified hour. If the period has passed — it checks the next day
3. Enter **how many hours** you want to discharge
4. For all hours in the period — enter **Max GridSetpoint**
5. To automate: check **Run task every hour** and **Automatically optimize DD and DDBD**

To test — press **Optimize dynamic discharging now**.

The program marks hours with the maximum sale price and blocks the rest. It skips hours without a GridSetpoint entered and hours when charging is active.

> [!NOTE]
> If you define two DD periods for the same time — the first finds hours with the highest prices, the second searches for the next highest (excluding already found ones).

## Dynamic MinSOC by the Optimizer

To have the optimizer in {{< relref "/configuration/battery-forecast" >}} dynamically change MinSOC:

1. Check **Enable** (or use DD/DDBD to enable)
2. Enter **Max GridSetpoint**
3. Check **Optimize MinSOC by Battery Forecast**
4. *(Optional)* Enter **MinimalSOC** — lower discharging limit by the optimizer
5. *(Optional)* Check **Only if Price > MinPrice** and enter **MinPrice**

**Example:** The program discharges the battery at 21:00 (highest sale price) to make room for PV energy by 16:00. SOC never drops below MinSOC.

## Dynamic Battery Discharge Blocking (DDBD)

**DDBD** (Dynamically Disable Battery Discharge) forces PV production to be sent to the grid until the price is at its lowest — at which point it is better to charge the battery from PV rather than sell.

> [!WARNING]
> Do not use this feature with the **price-based optimizer**!

To configure DDBD:

1. Add at least one period
2. Enter **from what hour** and **how many hours** the program should search for the minimum purchase price
3. Enter **how many hours** you want to charge the battery
4. For all hours in the period — enter **Max GridSetpoint** (large negative value)
5. To automate: check **Run task every hour** and **Automatically optimize DD and DDBD**

To test — press **Optimize battery blocking now**.

### Disable DDBD if battery will not be charged

The program can check whether, after the DDBD period ends, the battery will be charged to the required level. If not — it disables DDBD once.

Parameters:
- **Number of charging hours** — how many hours the battery should charge
- **Only if SOC increases by at least X %** — required SOC increase during charging hours

> [!NOTE]
> If the "only if SOC increases..." field is empty, the optimizer does not check whether the battery will be charged to the required level.

## Automatic discharging activation (day/night)

The program can automatically enable discharging only during the day or only at night, based on sunrise and sunset times.

> [!NOTE]
> Requires latitude and longitude to be set in [installation parameters]({{< relref "/installation/installation-parameters" >}}).

## Discharging Parameters

| Parameter | Inverter | Description |
|-----------|----------|-------------|
| Automatically enable Discharging | All | Enable discharging (column "Enable") only during day or night, disable during remaining hours |
| Default MinSOC after discharging (%) | {{< badge "victron-only" >}} | MinSOC set in the inverter after discharging ends |
| Default GridSetpoint after discharging (W) | {{< badge "victron-only" >}} | GridSetpoint set in the inverter after discharging ends |
| Stretch discharging to a full hour | All | Set GridSetpoint/MaxSellPower so that discharging lasts the full hour |
| Always send fixed MinSOC | All | Send a fixed MinSOC value instead of the value from the Discharge Plan. Idea: discharging speed controlled only by GridSetpoint, lower risk of charging from grid after reaching TargetSOC |
| Special GridSetpoint calculation when SOC = TargetSOC | All | While maintaining a fixed SOC — set a small GridSetpoint instead of the maximum |
| Increase GridSetpoint by forecasted Consumption | All | For systems where the home is on the inverter grid side |
| Disable Peak-Shaving during discharging | {{< badge "deye-only" >}} | In some firmware, peak-shaving blocks discharging — the program can disable it |
| Set MaxCharge=0 during discharging | {{< badge "deye-only" >}} | Block charging (even accidental) during the discharging hour |
| If there is nothing to do | {{< badge "victron-only" >}} {{< badge "deye-only" >}} | When: no PV, no charging, no discharging, MinSOC < SOC < MaxSOC, no EV charging → disconnect inverter from grid (or Deye: set "NoBatt"). Idea: reduce inverter power consumption |

## Sale Price ≤ 0

Special operations when the sale price is negative or equal to 0:

### Victron

| Option | Description |
|--------|-------------|
| Disconnect from grid | Inverter enters "Inverter only" mode |
| Disable "DC-coupled PV — feed in excess" | Disables the option for PV connected on the DC side |
| Set GridSetpoint if Price ≤ 0 | E.g. 0 — limits energy export to the grid |
| Enable Relay 1/2 | Disabling PV via the Cerbo Relay1/Relay2 output |
| Assume no PV | The program assumes PV is not operating during hours with price ≤ 0 |

### Solarman (Deye)

| Option | Description |
|--------|-------------|
| Disconnect from grid | Changes the allowed minimum voltage to 270 V — Deye disconnects from the grid |
| Disable SolarSell and MI export to Grid cutoff | Disables SolarSell and microinverters during hours with price < 0 |
| Assume no PV | Same as above |

### DeyeCloud

| Option | Description |
|--------|-------------|
| Disable SolarSell | Disables SolarSell during hours with price < 0 |
| Assume no PV | Same as above |

### HomeAssistant / GbbConnect

| Option | Description |
|--------|-------------|
| Assume no PV | The program assumes PV is not operating during hours with price ≤ 0 |
