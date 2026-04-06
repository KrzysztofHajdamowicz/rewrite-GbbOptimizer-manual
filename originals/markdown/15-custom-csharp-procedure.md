## Import remark:

- Procedure must work no longer than 100ms.
- It also cannot interfere with the program's operation

Otherwise will be suspended.

##

## IoT: C# Procedure: App object

### Here is a list of properties in App object (parameter of every IoT C# procedure):

|  |  |  |
| --- | --- | --- |
| Property | Type | Description |
| App.CurrDate | DateTime? | Date when switch must be on or off |
| App.CurrHour | decimal? | Hour when switch must be on or off  (12:30 = 12.5; 12:45 = 12.75) |
| App.CurrForecastIndex | int? | Index in App.Forecast for CurrDate and CurrHour |
| App.StringVariables | Dictionary<string, string?> | String Variables for user (persistent between calls of all procedures) |
| App.DecimalVariables | Dictionary<string, decimal?> | Decimal Variables for user (persistent between calls of all procedures) |

### Forecast:

|  |  |  |
| --- | --- | --- |
| App.Forecast | IForecast[] | Table of Battery Forecast  Forecast[0] - current hour  Forecast[1] - next hour, etc |
| App.Forecast[i].Date | DateTime | Date of forecast |
| App.Forecast[i].DateNo | int | 0 - today, 1 - tomorrow, etc |
| App.Forecast[i].Hour | decimal | Hour of forecast  (12:30 = 12.5; 12:45 = 12.75) |
| App.Forecast[i].HourNo | decimal | Hour of forecast, but counting from start of forecast  Forecast[0].HourNo == 0 always  Forecast[0].HourNo <24: first 24 hours |
| App.Forecast[i].StartBattery\_kWhAC | decimal | kWh in battery after converting to AC on start of hour |
| App.Forecast[i].StartBattery\_kWh | decimal | kWh in bettery in DC on start of hour |
| App.Forecast[i].Prod\_KWhAC | decimal? | Production (PV+Wind) on this hour |
| App.Forecast[i].Loads\_kWhAC | decimal? | Loads on this hour |
| App.Forecast[i].GridCharge\_kWhAC | decimal? | kWh transfered from grid to battery on this hour (on grid site) |
| App.Forecast[i].GridCharge\_kWh | decimal? | kWh transfered from grid to battery on this hour (on battery site) |
| App.Forecast[i].Discharge\_kWhAC | decimal? | kWh transfered from battery to grid on this hour (on grid site) |
| App.Forecast[i].Discharge\_kWh | decimal? | kWh transfered from battery to grid on this hour (on battery site) |
| App.Forecast[i].EndBattery\_kWhAC | decimal? | kWh in battery after converting to AV on end of hour |
| App.Forecast[i].EndBattery\_kWh | decimal? | kWh in battery in DC on end of hour |
| App.Forecast[i].Meteo\_SOC | decimal? | null - no MeteoWarnings, else TargetSOC for MeteoWarning |
| App.Forecast[i].Temperature\_C | decimal? | temperatur (C) on this hour |
| App.Forecast[i].ExtraLoads\_kWh | decimal? | Sum of all ExtraLoads on this hour |
| App.Forecast[i].FromGrid\_kWh | decimal? | kWh from grid on this hour |
| App.Forecast[i].PurchasePrice | decimal? | Purchase price on this hour |
| App.Forecast[i].PurchaseAmount | decimal? | Purchase Amount on this hour |
| App.Forecast[i].ToGrid\_kWh | decimal? | kWh to grid on this hour |
| App.Forecast[i].SalePrice | decimal? | Sales price on this hour |
| App.Forecast[i].SaleAmount | decimal? | Sales Amount on this hour |

###

### Prices:

|  |  |  |
| --- | --- | --- |
| App.Prices | Dictionary(<DateTime Date, decimal Hour>, IPrice) | Table of prices for yesterday, today and next day |
| App.Prices[(d, h)].Day | DateTime | Date of price |
| App.Prices[(d, h)].Hour | decimal | Hour of price  (12:30 = 12.5; 12:45 = 12.75) |
| App.Prices[(d, h)].PurchasePrice | decimal? | Purchase price |
| App.Prices[(d, h)].SalesPrice | decimal? | Sales price |
| App.Prices[(d, h)] .Imported\_PurchasePrice | decimal? | Purchase price imported from price source |
| App.Prices[(d, h)] .Imported\_SalesPrice | decimal? | Sales price imported from price source |

###

### History:

|  |  |  |
| --- | --- | --- |
| App.History | IHistory[] | Table of History data  History[0] - hour before current  History[1] - two hour before current, etc  This is yesterday and today history |
| App.History[i].Date | DateTime | Date of history |
| App.History[i].Hour | decimal | Hour of history  (12:30 = 12.5; 12:45 = 12.75) |
| App.History[i].FromGrid\_kWh | decimal? | kWh from grid on this hour |
| App.History[i].PurchasePrice | decimal? | Purchase Price for this hour |
| App.History[i].PurchaseAmount | decimal? | Purchase Amount for this hour |
| App.History[i].ToGrid\_kWh | decimal? | kWh to grid on this hour |
| App.History[i].SalePrice | decimal? | Sales price for this hour |
| App.History[i].SaleAmount | decimal? | Sales amount for this hour |
| App.History[i].Loads\_kWh | decimal? | kWh of Loads on this hour |
| App.History[i].LoadsPrice | decimal? | Loads energy price on this hour |
| App.History[i].LoadsAmount | decimal? | Loads energy amount on this hour |
| App.History[i].PV\_kWh | decimal? | kWh of PV production on this hour |
| App.History[i].SOC\_Start | decimal? | Start SOC on this hour |
| App.History[i].SOC\_End | decimal? | End SOC on this hour |
| App.History[i].ExtraLoads\_Price | decimal? | ExtraLoads energy price on this hour |
| App.History[i].ExtraLoads\_kWh | decimal? | Sum of all ExtraLoads on this hour |

###

### IoTDevices;

|  |  |  |
| --- | --- | --- |
| App.IoTDevices | Dictionary<string Name, IIoTDevice> | List of IoT devices |
| App.IoTDevices[n].Name | string | Name of device |
| App.IoTDevices[n].IsOn | bool | Current state of switch |

## Special function

|  |  |
| --- | --- |
| Function | description |
| void App.ToLog(string massage) | Put any message to menu Log |
| bool App.IsInLowerPrices(DateTime CurrDate, decimal CorrHour, int LowerHours, bool Purchase) | If given hour is in lower hours of the day? |
| bool App.IsInHigherPrices(DateTime CurrDate, decimal CorrHour, int HigherHours, bool Purchase) |  |

### Following libraried are available:

mscorlib.dll
system.runtime.dll
System.Text.RegularExpressions.dll
system.linq.dll
System.Collections.dll

### Example:

public bool IoTDevice\_0036\_IsOn(IApp App)
{
  return App.IsInLowerPrices(App.CurrDate, App.CurrHour, 3, false)
      || App.Forecast[App.CurrForecastIndex].FromGrid>3;
}
