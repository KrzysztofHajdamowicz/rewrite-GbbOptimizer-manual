---
title: "Gains"
weight: 80
translationKey: "zyski"
---

# Gains

The module collects data from the installation and calculates photovoltaic gains. Import data manually at least once a day or check **Automatically import data from Installation**.

Data is displayed by hour, day, or month:
- Hourly data — stored for **2 months**
- Daily data — stored for **2 years**
- Monthly data — stored **permanently**

## Columns — Profit

| Column | Description |
|--------|-------------|
| Day / Hour | Day and hour |
| Profit value | **= Consumption Value - Inverter Value - (Purchase Value - Battery Value Change) + Sale Value** |
| Profit / Consumption | KPI: Profit value / Consumption kWh |
| Profit / Solar | KPI: Profit value / PV kWh |
| Energy cost | Purchase Value - Sale Value |
| From grid (kWh) | How much drawn from the grid |
| From grid balanced (kWh) | Drawn after hourly balancing (for Poland) |
| Purchase Price | Energy purchase price |
| Purchase Value | From grid [balanced] × Purchase Price + Monthly Cost |
| Purchase / Production | KPI: Purchase Value / Consumption Value |
| (Purchase - Sale) / Production | KPI: what percentage of the energy bill you will pay |
| To grid (kWh) | How much sent to the grid |
| To grid balanced (kWh) | Sent after hourly balancing (for Poland) |
| Sale Price | Energy sale price |
| Sale Value | To grid [balanced] × Sale Price − Value of energy sent to grid |
| Consumption (kWh) | Home electricity consumption |
| Consumption Price | Price of energy consumed by the home (including inverter) |
| Consumption Value | Consumption kWh × Consumption Price |
| Inverter Consumption (kWh) | Electricity consumption by the inverter |
| Inverter Value | Inverter Consumption kWh × Consumption Price |
| Self-consumption | KPI: 1 - (To grid kWh / PV kWh) — how much PV energy does not go to the grid |
| Self-sufficiency | KPI: PV / Consumption — what % of energy from PV covers consumption |
| {{< glossary "RTE" >}} | KPI: To grid kWh / (From grid kWh + PV kWh - Consumption kWh) |
| PV (kWh) | PV production |
| To battery (kWh) | Energy sent to the battery (before DC conversion) |
| min/max/avg SOC (%) | Minimum, maximum, and average battery SOC |

## Columns — Battery Energy Value

| Column | Description |
|--------|-------------|
| Start SOC (%) | Starting SOC (calculated from MinSOC and MaxSOC if not provided by the installation) |
| End SOC (%) | Ending SOC |
| Battery Change (kWh) | >0 charging, <0 discharging — calculated from EndSOC - StartSOC |
| Grid charging (kWh) | Energy used to charge from the grid (AC side) |
| PV charging (kWh) | Energy used to charge from PV (AC side) |
| Charging losses (kWh) | Difference between DC and AC during charging |
| Charging efficiency (%) | 1 - Losses / (Grid charging + PV charging) |
| Discharge to grid (kWh) | Battery energy to grid (AC) |
| Discharge to consumption (kWh) | Battery energy to home (AC) |
| Discharge losses (kWh) | DC/AC difference during discharging |
| Discharge efficiency (%) | 1 - Losses / (Discharge to grid + to consumption) |
| Start / End kWh in battery | Energy in battery above MinSOC |
| Start / End Value | Value of energy in the battery |
| Battery Value Change | Discharging: kWh × Average price (previous hour). Charging: kWh × Purchase Price |
| Average end price | End Value / End kWh in battery |
| MinSOC (%) | Stored value of "Minimum battery SOC %" from installation parameters |

## Columns — Extra Consumption

| Column | Description |
|--------|-------------|
| Extra Consumption Price | Average kWh price: average of 0 (PV), Average battery price and Purchase Price (in usage proportions) |
| Electric vehicle (kWh / value) | Energy and value of EV charging |
| Heat pump (kWh / value) | Energy and value of heat pump |
| Other1 (kWh / value) | Energy and value of "Other1" |
| Other2 (kWh / value) | Energy and value of "Other2" |
