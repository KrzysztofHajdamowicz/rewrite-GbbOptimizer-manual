---
title: "Heat Pump / Air Conditioning"
weight: 70
translationKey: "pompa-ciepla"
---

# Heat Pump / Air Conditioning Forecast

The module for forecasting heat pump (HP) or air conditioning consumption based on outdoor temperature.

## Why a Separate Module?

Heat pumps and air conditioning (like EV chargers) do not operate according to the rhythm of the day — they depend on temperature. It is therefore better to **exclude them from the average** in the [Consumption Profiles]({{< relref "/konfiguracja/profile-zuzycia" >}}) module and place them in [Extra Consumption]({{< relref "/konfiguracja/dodatkowe-obciazenia-ev" >}}).

## Step-by-Step Configuration

1. Enter **latitude and longitude** in [installation parameters]({{< relref "/instalacja/parametry-instalacji" >}})
2. Import the weather forecast
3. Press **HP Parameters** and enter the kWh consumption of the pump/AC for each hour (minimum 2 values for different temperatures)
4. Press **Calculate HP forecast** and check the results
5. Press **Export HP forecast to Extra Consumption module** (menu: Consumption Profiles → Extra Consumption → Filter: "Type" = "Heat Pump")
6. Enable hourly tasks: **Import weather forecast**, **Calculate HP forecast**, **Export HP forecast to Extra Consumption module**

## HP Parameters — Temperature vs. Consumption Table

For each hour, enter how many kWh the HP/AC consumes at a given outdoor temperature.

Tips:
- You can fill in only the first column — the **Copy Tool** at the bottom lets you copy data between columns
- You do not need to fill in all temperatures (from -20°C to +40°C). **A minimum of 2 values** is sufficient — the program automatically interpolates the rest proportionally
- The more data, the more accurate the forecast
- Data can be supplemented throughout the year as observations are collected

> [!NOTE]
> Example: Enter consumption only for the hours and temperatures you know — e.g. 10°C, 0°C, and -5°C.
