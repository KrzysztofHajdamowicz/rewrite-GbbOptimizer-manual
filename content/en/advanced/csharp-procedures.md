---
title: "C# IoT Procedures"
weight: 10
translationKey: "procedury-csharp"
---

# C# IoT Procedures

GbbOptimizer allows you to create custom procedures in C# that control IoT devices based on forecasts, energy prices, and consumption history.

> [!WARNING]
> A procedure must run in **no more than 100 ms** and must not interfere with the program's operation. Otherwise it will be suspended.

## The App Object

Each IoT procedure receives an `App` object as a parameter. The available properties are listed below.

### Main Properties

| Property | Type | Description |
|----------|------|-------------|
| `App.CurrDate` | `DateTime?` | Date for which the device should be turned on/off |
| `App.CurrHour` | `decimal?` | Hour (12:30 = 12.5; 12:45 = 12.75) |
| `App.CurrForecastIndex` | `int?` | Index in `App.Forecast` for the current date and hour |
| `App.StringVariables` | `Dictionary<string, string?>` | User string variables (persistent between calls) |
| `App.DecimalVariables` | `Dictionary<string, decimal?>` | User numeric variables (persistent between calls) |

### Forecast

| Property | Type | Description |
|----------|------|-------------|
| `App.Forecast` | `IForecast[]` | Battery forecast array. `[0]` = current hour, `[1]` = next hour, etc. |
| `.Date` | `DateTime` | Forecast date |
| `.DateNo` | `int` | 0 = today, 1 = tomorrow, etc. |
| `.Hour` | `decimal` | Forecast hour |
| `.HourNo` | `decimal` | Hour counted from the start of the forecast (`[0].HourNo == 0` always) |
| `.StartBattery_kWhAC` | `decimal` | kWh in battery (AC) at the start of the hour |
| `.StartBattery_kWh` | `decimal` | kWh in battery (DC) at the start of the hour |
| `.Prod_KWhAC` | `decimal?` | Production (PV + wind) in the given hour |
| `.Loads_kWhAC` | `decimal?` | Consumption in the given hour |
| `.GridCharge_kWhAC` | `decimal?` | kWh from grid to battery (grid side) |
| `.GridCharge_kWh` | `decimal?` | kWh from grid to battery (battery side) |
| `.Discharge_kWhAC` | `decimal?` | kWh from battery to grid (grid side) |
| `.Discharge_kWh` | `decimal?` | kWh from battery to grid (battery side) |
| `.EndBattery_kWhAC` | `decimal?` | kWh in battery (AC) at the end of the hour |
| `.EndBattery_kWh` | `decimal?` | kWh in battery (DC) at the end of the hour |
| `.Meteo_SOC` | `decimal?` | null = no weather warnings; value = target SOC for the warning |
| `.Temperature_C` | `decimal?` | Temperature (°C) in the given hour |
| `.ExtraLoads_kWh` | `decimal?` | Total extra loads |
| `.FromGrid_kWh` | `decimal?` | kWh from grid |
| `.PurchasePrice` | `decimal?` | Purchase price |
| `.PurchaseAmount` | `decimal?` | Purchase amount |
| `.ToGrid_kWh` | `decimal?` | kWh to grid |
| `.SalePrice` | `decimal?` | Sale price |
| `.SaleAmount` | `decimal?` | Sale amount |

### Prices

| Property | Type | Description |
|----------|------|-------------|
| `App.Prices` | `Dictionary<(DateTime, decimal), IPrice>` | Prices for yesterday, today, and tomorrow |
| `.Day` | `DateTime` | Price date |
| `.Hour` | `decimal` | Price hour |
| `.PurchasePrice` | `decimal?` | Purchase price |
| `.SalesPrice` | `decimal?` | Sale price |
| `.Imported_PurchasePrice` | `decimal?` | Purchase price imported from price source |
| `.Imported_SalesPrice` | `decimal?` | Sale price imported from price source |

### History

| Property | Type | Description |
|----------|------|-------------|
| `App.History` | `IHistory[]` | Historical data. `[0]` = hour before current, `[1]` = two hours before, etc. |
| `.Date` | `DateTime` | Date |
| `.Hour` | `decimal` | Hour |
| `.FromGrid_kWh` | `decimal?` | kWh from grid |
| `.PurchasePrice` | `decimal?` | Purchase price |
| `.PurchaseAmount` | `decimal?` | Purchase amount |
| `.ToGrid_kWh` | `decimal?` | kWh to grid |
| `.SalePrice` | `decimal?` | Sale price |
| `.SaleAmount` | `decimal?` | Sale amount |
| `.Loads_kWh` | `decimal?` | Consumption (kWh) |
| `.LoadsPrice` | `decimal?` | Consumption energy price |
| `.LoadsAmount` | `decimal?` | Consumption energy amount |
| `.PV_kWh` | `decimal?` | PV production (kWh) |
| `.SOC_Start` | `decimal?` | SOC at the start of the hour |
| `.SOC_End` | `decimal?` | SOC at the end of the hour |
| `.ExtraLoads_Price` | `decimal?` | Extra loads price |
| `.ExtraLoads_kWh` | `decimal?` | Total extra loads (kWh) |

### IoT Devices

| Property | Type | Description |
|----------|------|-------------|
| `App.IoTDevices` | `Dictionary<string, IIoTDevice>` | List of IoT devices |
| `.Name` | `string` | Device name |
| `.IsOn` | `bool` | Current switch state |

## Special Functions

| Function | Description |
|----------|-------------|
| `void App.ToLog(string message)` | Display a message in the Log menu |
| `bool App.IsInLowerPrices(DateTime CurrDate, decimal CurrHour, int LowerHours, bool Purchase)` | Is the given hour among the lowest-price hours of the day? |
| `bool App.IsInHigherPrices(DateTime CurrDate, decimal CurrHour, int HigherHours, bool Purchase)` | Is the given hour among the highest-price hours of the day? |

## Available Libraries

- `mscorlib.dll`
- `system.runtime.dll`
- `System.Text.RegularExpressions.dll`
- `system.linq.dll`
- `System.Collections.dll`

## Example

```csharp
public bool IoTDevice_0036_IsOn(IApp App)
{
    return App.IsInLowerPrices(App.CurrDate, App.CurrHour, 3, false)
        || App.Forecast[App.CurrForecastIndex].FromGrid_kWh > 3;
}
```

This example turns the device on when:
- The current hour is among the 3 cheapest hours of the day (sale price), **or**
- The forecast grid import in the current hour exceeds 3 kWh
