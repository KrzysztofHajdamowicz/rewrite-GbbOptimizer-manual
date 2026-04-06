---
title: "Prices"
weight: 40
translationKey: "ceny"
---

# Prices

The energy purchase and sale price configuration module. Price data sources are set in [installation parameters]({{< relref "/instalacja/parametry-instalacji" >}}); the remaining parameters are configured here.

## Purchase Price

**Formula:**

```
Purchase Price = (Imported Price × Multiplier + Transmission Price + Transport Cost) × VAT/100
                 + (Monthly Costs / number of hours in the month)
```

| Component | Description |
|-----------|-------------|
| Imported Price | **Fixed** → 0. **Dependent on imported prices and transport costs** → price from the source specified in installation parameters. **Dependent on sale prices** → Sale Price |
| Multiplier | "Multiply imported Purchase Prices by" |
| Transmission Price | Price from the source specified in installation parameters (item "Transmission: Tariff for transmission prices"). 0 if none specified |
| Transport Cost | Price from the table under the "Change Transport Costs / fixed Purchase Prices" button |
| Monthly Costs | Sum of fixed purchase costs — spread evenly across all hours in the month |

## Sale Price

**Formula:**

```
Sale Price = (Imported Price × Multiplier + Additional Charges) × VAT/100
             × Multiplier2 × DailyPercent
```

| Component | Description |
|-----------|-------------|
| Imported Price | If "There is only one fixed Sale Price" is checked → fixed value. Otherwise → price from the source specified in installation parameters |
| Multiplier | "Multiply imported Sale Prices by" |
| Additional Charge | Table under the "Change additional charges for Sale Prices" button |
| Multiplier2 | Table under the "Change additional multiplier2 for Sale Prices" button |
| DailyPercent | 1 + Percent/100 from sunrise to sunset (if enabled) |
