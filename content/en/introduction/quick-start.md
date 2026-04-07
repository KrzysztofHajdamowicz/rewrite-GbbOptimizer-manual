---
title: "Quick start"
weight: 20
translationKey: "szybki-start"
---

# Quick start

A step-by-step guide on how to set up GbbOptimizer for your photovoltaic installation.

## 1. Create an account and add an installation

Go to the GbbOptimizer website and create an account. Then add a new installation by selecting the appropriate option depending on your inverter:

| Inverter | Menu option |
|----------|-------------|
| **Victron** (Cerbo GX or other GX module) | "Add new installation with Victron System" |
| **Deye** via DeyeCloud | "Add new installation with Deye inverter connected to DeyeCloud" |
| **Deye** via Solarman | "Add new installation with Solarman" |
| **Deye** via Home Assistant | "Add new installation with Home Assistant" |
| **Other inverter** via Solarman | "Add new installation with Solarman" |
| **Other inverter** via Home Assistant | "Add new installation with Home Assistant" |
| **SofarSolar** | "Installation with DongleDirect (Deye, SofarSolar)" |

> [!NOTE]
> If you have Deye inverters in a Master-Slave setup, select "Installation with Solarman" and add Master as the primary inverter and Slave as an additional one in the installation parameters.

Each installation receives a unique {{< glossary "PlantId" >}} and {{< glossary "PlantToken" >}}.

## 2. Fill in the installation data

Fill in all fields (at least those marked with an asterisk **\***) in the installation form. After filling in, press **"Save and continue in Quick Setup"**.

{{< glossary "FastSetup" >}} will guide you through the basic configuration:

- Adding PV planes
- Selecting the PV forecast source
- Basic battery parameters

After filling in all fields, press **"Save changes"**.

## 3. Configure prices

In the [Prices]({{< relref "/configuration/prices" >}}) module:

1. Click **"Select distributor and energy supplier tariff"**
2. Select your distribution tariff and energy supplier tariff
3. Press **"Import selected tariffs"**

Alternatively, manually configure purchase and sale prices.

> [!WARNING]
> Remember to set transport (transmission) costs for purchase prices. Without them, the optimizer will not correctly calculate the profitability of grid charging.

## 4. Configure the consumption profile

In the [Consumption profiles]({{< relref "/configuration/consumption-profiles" >}}) module you have two options:

- **Manual entry** — enter estimated consumption for each hour
- **Import from installation** — wait ~one week for the program to collect data from the inverter and calculate average consumption

> [!NOTE]
> If you don't want to enter the consumption profile manually, wait a week — the program will automatically collect data and calculate the profile. In the meantime, {{< glossary "Test Mode" >}} should still be running.

## 5. Check the PV forecast

Verify in the [Battery Forecast]({{< relref "/configuration/battery-forecast" >}}) module that the PV forecast is close to actual production. If not, try changing the PV forecast source in the installation parameters.

{{< glossary "Correction Factor" >}} auto-calibrates over approximately one week of operation.

## 6. Wait in test mode

A new installation starts in {{< glossary "Test Mode" >}} — the optimizer performs calculations but **does not send commands to the inverter**.

During the first week:

- The consumption profile will be updated (if automatic import is enabled)
- {{< glossary "Correction Factor" >}} for the PV forecast calibrates itself
- You can observe what the optimizer *plans* to do, without risk

## 7. Disable test mode

After ~one week, once you have confirmed that:

- **Prices** are correct (with all transport costs)
- **PV forecast** is close to reality
- **Consumption profile** is reasonable

...disable {{< glossary "Test Mode" >}} in the [Battery Forecast]({{< relref "/configuration/battery-forecast" >}}) module. From this point on, the optimizer will start sending commands to the inverter.

## Instructional videos

- [Adding a Victron system to GbbOptimizer](https://youtu.be/5q6gORx1KUY)
- [Adding a Deye inverter via Solarman](https://youtu.be/y8fhh1UecqQ)
- [Configuring purchase and sale prices](https://youtu.be/m27uQfO60pc)

## EV charging optimization only (without PV)

If you want to optimize only electric vehicle charging, without a PV installation:

1. Add a new installation of type **Home Assistant**
2. Fill in the fields:
   - Name
   - Grid connection power — import
   - Grid connection power — export → enter **0**
   - Battery capacity kWh → enter **0**
3. Press **"Save and continue in Quick Setup"**, on this page:
   - Uncheck **"Add first PV Plane"**
   - Check **"EV: Automatically import data from EV chargers every hour"**
4. Press **"Save"** — you will be taken to the Prices menu:
   - Select the distributor and energy supplier tariff
   - Press **"Import selected tariffs"**
5. Go to the [Extra Consumption / EV]({{< relref "/configuration/additional-loads-ev" >}}) module:
   - In the "EV Charging" section, add your charger
   - In the "EV AutoCharging" section, configure charging conditions (e.g. in "Conditions" select "Price" → 3 lowest purchase prices)

## What's next?

- [Best practices]({{< relref "/introduction/best-practices" >}}) — tips on getting the most out of the system
- [Charging]({{< relref "/configuration/charging" >}}) — configuring charging schedules
- [Discharge]({{< relref "/configuration/discharging" >}}) — configuring battery discharge
- [Battery Forecast]({{< relref "/configuration/battery-forecast" >}}) — the central optimizer module
