---
title: "Consumption Profiles"
weight: 50
translationKey: "profile-zuzycia"
---

# Consumption Profiles

The module for forecasting home energy consumption. Consumption is divided by hour and day of the week.

## Manual Entry

Enter kWh for each hour and day of the week directly in the table.

## Importing Data from Installation

Set the import period and press **Import from Installation**. The program calculates the average consumption for each hour and day of the week based on data from the inverter.

### Automatic Import

Check **Automatically import data at night** — the program imports data from the last 28 days every night.

## Manual Import from Excel

1. Prepare data in Excel: hours in rows, days of the week in columns
2. Copy the data (Ctrl+C)
3. Paste into the "Your profile" field
4. Select the column separator and decimal separator
5. Press **Import**

> [!NOTE]
> - Empty cell = the program does not change data in that position
> - You can paste fewer than 24 rows or 7 columns — missing hours/days will not be changed
> - Extra columns and rows are ignored

## Multiple Profiles

You can define multiple consumption profiles. The selected profile is used in [Battery Forecast]({{< relref "/configuration/battery-forecast" >}}) for displaying data, charts, and optimization.

## Restricting the Import Period

In the profile editor you can set:
- **From month / From day** — restricts the start day of the data import
- **To month / To day** — restricts the end day of the import

Useful for example for a **holiday profile**, where the import should use data only from the holiday period.

If "From day" is empty — the program uses the first day of the month. If "To day" is empty — it uses the last day.

## Automatic Profile Switching

To automatically switch profiles:

1. Define at least two profiles with the "From month" field filled in (and optionally "From day"), with "To month" left empty
2. Check **Automatically change profile based on "From month/day" fields**

> [!NOTE]
> This also restricts the data import period from the installation!

## Automatic Holiday Profile

Define a profile with **both** "From month/day" and "To month/day" fields filled in. The program:
- Activates the holiday profile on the start date
- Returns to the normal profile the day after the end date
