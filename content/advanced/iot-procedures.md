---
title: "IoT C# Procedures"
weight: 10
---

# IoT C# Procedures

GbbOptimizer supports custom C# procedures that run in the IoT context, enabling advanced automation scenarios.

## App Object

The `App` object is passed as a parameter to all IoT procedures and provides access to system data.

### Date/Time Properties

| Property | Type | Description |
|----------|------|-------------|
| `App.CurrDate` | DateTime | Current date |
| `App.CurrHour` | int | Current hour |
| `App.CurrForecastIndex` | int | Matching position in forecast data |

### User Variables

Two persistent variable collections that survive across procedure calls:
- **String variables** — dictionary of string values
- **Decimal variables** — dictionary of decimal values

### Forecast Data

The forecast array contains hourly battery projections:
- Index `[0]` = current hour
- Subsequent indices = future hours

Each entry includes: battery state (AC/DC), production, loads, grid transfers, and pricing.

### Price Information

Historical and projected pricing data keyed by date and hour, including purchase and sales prices.

### History Records

Historical data spanning yesterday and today, indexed from the most recent hour backward.

### IoT Devices

Dictionary of connected devices and their switch states.

## Utility Functions

| Function | Description |
|----------|-------------|
| `App.ToLog(message)` | Write debug output to the log |
| `App.IsInLowerPrices(...)` | Check if current price is in lower price range |
| `App.IsInHigherPrices(...)` | Check if current price is in higher price range |

## Constraints

> **Procedure must execute in under 100ms** and cannot interfere with program operation.
