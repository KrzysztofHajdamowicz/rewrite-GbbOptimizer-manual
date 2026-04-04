---
title: "Quick Start Guide"
weight: 20
---

# Quick Start Guide

Follow these steps to get GbbOptimizer running with your solar installation.

## Step 1: Create a Plant

1. Register at [gbboptimizer.gbbsoft.pl](https://gbboptimizer.gbbsoft.pl)
2. Click **"Add new plant"** and select your connection type:
   - Victron systems (with or without Home Assistant)
   - Deye hybrid inverters via DeyeCloud
   - Deye hybrid inverters via Solarman
   - Other hybrid inverters via Solarman
   - Deye hybrid inverters via Home Assistant / SolarAssistant
   - SofarSolar inverters via DongleDirect
   - Master-Slave Deye configurations via Solarman
3. Fill in all required fields (marked with **\***)
4. Proceed with **FastSetup**

## Step 2: Configure Prices

Open the **[Prices]({{< relref "/configuration/prices" >}})** module and set up:
- Purchase price (including transportation costs!)
- Sell price
- VAT and other cost factors

> [!WARNING]
> **Important:** Purchase prices **must** include transportation costs. Incorrect prices lead to suboptimal battery management.

## Step 3: Set Up Load Profiles

Open **[Profiles of Loads]({{< relref "/configuration/profiles-of-loads" >}})** and either:
- Enter your household AC loads manually (kWh per hour and weekday)
- Import from your plant data
- Copy-paste from Excel

## Step 4: Wait and Observe (Test Mode)

Your plant starts in **test mode**. During this period:
- The optimizer calculates but does **not** send commands to your inverter
- Load profiles are being learned
- PV forecast correction factor is being calculated

> [!NOTE]
> **Wait approximately one week** before disabling test mode. This allows the system to calibrate.

## Step 5: Go Live

After ~1 week, open **[Battery Forecast]({{< relref "/configuration/battery-forecast" >}})** and disable **Test Mode**. The optimizer will now send commands to your plant.

## Best Practices

- Set **MaxSOC to 90%** — provides buffer for PV forecast inaccuracies
- Switch PV forecast source to **[solcast.com](https://solcast.com)** (free Home account, up to 2 PV fields)
- If using Home Assistant, set **update_interval to 20+ seconds** to prevent Solarman conflicts
- The fewer additional optimizer options selected, the **greater the profits**
- Configure **Battery Full Dates** (e.g., 1st and 15th of month) for periodic full charge cycles
