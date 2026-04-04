---
title: "Prices"
weight: 50
---

# Prices

The Prices module configures how GbbOptimizer calculates electricity purchase and sale prices. Accurate pricing is critical for optimal battery management.

> [!WARNING]
> **Purchase prices must include transportation costs.** Incorrect pricing leads to suboptimal charge/discharge decisions.

## Purchase Price Formula

```
Purchase Price = (Imported Price × Multiplier + Transport Price + Transport Costs) × VAT_Tax / 100
                 + (MonthCosts / hours in month)
```

| Component | Description |
|-----------|-------------|
| Imported Price | Zero for fixed pricing; imported from source when price-dependent |
| Multiplier | Scaling factor applied to imported purchase prices |
| Transport Price | Imported from selected source, or zero if not configured |
| Transport Costs | From the transportation costs / fixed prices editing table |
| VAT_Tax | Value Added Tax percentage |
| MonthCosts | Fixed monthly charges distributed equally across all hours |

## Sale Price Formula

```
Sale Price = (Imported Price × Multiplier + Extra Sale Tax) × VAT_Tax_Factor / 100
             × SalesFactor2 × DayPerc
```

| Component | Description |
|-----------|-------------|
| Imported Price | Fixed value or sourced from selected price zone/tariff |
| Multiplier | Scaling factor for imported sale prices |
| Extra Sale Tax | From an editable table |
| VAT_Tax_Factor | VAT factor for sales |
| SalesFactor2 | Extra sales factor from a configurable table |
| DayPerc | Percentage adjustment from sunrise to sunset (when enabled) |

## Price Sources

GbbOptimizer supports importing prices from various sources including:
- ENTSO-E (European energy exchange)
- Tibber
- Amber
- Pstryk
- Manual price entry

## Manual Price Override

You can set manual prices via the web interface or via MQTT — see [Set Manual Prices]({{< relref "/mqtt-api/data-commands#endpoint-setmanualprices" >}}).
