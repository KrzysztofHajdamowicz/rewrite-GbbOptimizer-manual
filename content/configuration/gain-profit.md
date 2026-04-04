---
title: "Gain / Profit"
weight: 90
---

# Gain / Profit

The Gain/Profit module collects plant data and provides performance analytics at hourly, daily, and monthly granularity.

## Data Collection

Data can be collected:
- **Automatically** — enable "Automatically import data from Plant"
- **Manually** — import at least daily

## Data Retention

| Granularity | Retention |
|-------------|-----------|
| Hourly | 2 months |
| Daily | 2 years |
| Monthly | Indefinite |

## Key Metrics

### Financial

| Column | Description |
|--------|-------------|
| Profit Amount | Consumption minus inverter output, adjusted for purchases, sales, and battery changes |
| Profit / Cons | KPI: profit per consumption unit |
| Profit / Solar | KPI: profit per solar generation unit |
| Purchase Amount | Grid acquisition costs |
| Sale Amount | Grid export revenue |
| Consumption Amount | Household energy costs |

### Grid Energy

| Column | Description |
|--------|-------------|
| From Grid (kWh) | Total grid imports |
| From Grid balance (kWh) | Grid imports with optional Polish hour-balancing |
| To Grid (kWh) | Total grid exports |
| To Grid balance (kWh) | Grid exports with optional balancing |

### Efficiency

| Column | Description |
|--------|-------------|
| {{< glossary "Self-Consumption" >}} | Percentage of solar energy used locally |
| {{< glossary "Self-Sufficiency" >}} | Percentage of consumption covered by solar |
| {{< glossary "RTE" >}} | Battery round-trip efficiency |
| Lost power (kWh) | System conversion losses |
| Efficiency (%) | Overall system efficiency |

### Battery

| Column | Description |
|--------|-------------|
| SOC min / max / avg | State of Charge statistics |
| Charge from Grid / Solar | Energy flowing into battery by source |
| Discharge flows | Energy flowing out of battery |

### Extra Loads

Individual tracking for EV, Heat Pump, and Generic sources — consumption in kWh and cost allocation based on blended energy pricing.
