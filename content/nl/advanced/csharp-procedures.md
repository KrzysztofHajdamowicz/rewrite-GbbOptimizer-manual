---
title: "C# IoT-procedures"
weight: 10
translationKey: "procedury-csharp"
---

# C# IoT-procedures

GbbOptimizer maakt het mogelijk eigen procedures in C# te schrijven die IoT-apparaten aansturen op basis van prognoses, energieprijzen en verbruiksgeschiedenis.

> [!WARNING]
> Een procedure mag **niet langer dan 100 ms** duren en mag de werking van het programma niet verstoren. Anders wordt de procedure opgeschort.

## Object App

Elke IoT-procedure ontvangt het `App`-object als parameter. Hieronder staat een lijst met beschikbare eigenschappen.

### Belangrijkste eigenschappen

| Eigenschap | Type | Beschrijving |
|------------|-----|------|
| `App.CurrDate` | `DateTime?` | Datum waarop het apparaat aan/uit moet worden gezet |
| `App.CurrHour` | `decimal?` | Uur (12:30 = 12.5; 12:45 = 12.75) |
| `App.CurrForecastIndex` | `int?` | Index in `App.Forecast` voor de huidige datum en uur |
| `App.StringVariables` | `Dictionary<string, string?>` | Tekstvariabelen van de gebruiker (persistent tussen aanroepen) |
| `App.DecimalVariables` | `Dictionary<string, decimal?>` | Numerieke variabelen van de gebruiker (persistent tussen aanroepen) |

### Prognose (Forecast)

| Eigenschap | Type | Beschrijving |
|------------|-----|------|
| `App.Forecast` | `IForecast[]` | Array van de batterijprognose. `[0]` = huidig uur, `[1]` = volgend uur enz. |
| `.Date` | `DateTime` | Datum van de prognose |
| `.DateNo` | `int` | 0 = vandaag, 1 = morgen enz. |
| `.Hour` | `decimal` | Uur van de prognose |
| `.HourNo` | `decimal` | Uur geteld vanaf het begin van de prognose (`[0].HourNo == 0` altijd) |
| `.StartBattery_kWhAC` | `decimal` | kWh in de batterij (AC) aan het begin van het uur |
| `.StartBattery_kWh` | `decimal` | kWh in de batterij (DC) aan het begin van het uur |
| `.Prod_KWhAC` | `decimal?` | Productie (PV + wind) in dat uur |
| `.Loads_kWhAC` | `decimal?` | Verbruik in dat uur |
| `.GridCharge_kWhAC` | `decimal?` | kWh uit het net naar de batterij (netzijde) |
| `.GridCharge_kWh` | `decimal?` | kWh uit het net naar de batterij (batterijzijde) |
| `.Discharge_kWhAC` | `decimal?` | kWh uit de batterij naar het net (netzijde) |
| `.Discharge_kWh` | `decimal?` | kWh uit de batterij naar het net (batterijzijde) |
| `.EndBattery_kWhAC` | `decimal?` | kWh in de batterij (AC) aan het einde van het uur |
| `.EndBattery_kWh` | `decimal?` | kWh in de batterij (DC) aan het einde van het uur |
| `.Meteo_SOC` | `decimal?` | null = geen weerswaarschuwingen; waarde = doel-SOC voor de waarschuwing |
| `.Temperature_C` | `decimal?` | Temperatuur (°C) in dat uur |
| `.ExtraLoads_kWh` | `decimal?` | Som van extra verbruik |
| `.FromGrid_kWh` | `decimal?` | kWh uit het net |
| `.PurchasePrice` | `decimal?` | Inkoopprijs |
| `.PurchaseAmount` | `decimal?` | Inkoopbedrag |
| `.ToGrid_kWh` | `decimal?` | kWh naar het net |
| `.SalePrice` | `decimal?` | Verkoopprijs |
| `.SaleAmount` | `decimal?` | Verkoopbedrag |

### Prijzen (Prices)

| Eigenschap | Type | Beschrijving |
|------------|-----|------|
| `App.Prices` | `Dictionary<(DateTime, decimal), IPrice>` | Prijzen voor gisteren, vandaag en morgen |
| `.Day` | `DateTime` | Datum van de prijs |
| `.Hour` | `decimal` | Uur van de prijs |
| `.PurchasePrice` | `decimal?` | Inkoopprijs |
| `.SalesPrice` | `decimal?` | Verkoopprijs |
| `.Imported_PurchasePrice` | `decimal?` | Uit de prijsbron geïmporteerde inkoopprijs |
| `.Imported_SalesPrice` | `decimal?` | Uit de prijsbron geïmporteerde verkoopprijs |

### Geschiedenis (History)

| Eigenschap | Type | Beschrijving |
|------------|-----|------|
| `App.History` | `IHistory[]` | Historische gegevens. `[0]` = uur vóór het huidige, `[1]` = twee uur eerder enz. |
| `.Date` | `DateTime` | Datum |
| `.Hour` | `decimal` | Uur |
| `.FromGrid_kWh` | `decimal?` | kWh uit het net |
| `.PurchasePrice` | `decimal?` | Inkoopprijs |
| `.PurchaseAmount` | `decimal?` | Inkoopbedrag |
| `.ToGrid_kWh` | `decimal?` | kWh naar het net |
| `.SalePrice` | `decimal?` | Verkoopprijs |
| `.SaleAmount` | `decimal?` | Verkoopbedrag |
| `.Loads_kWh` | `decimal?` | Verbruik (kWh) |
| `.LoadsPrice` | `decimal?` | Prijs van verbruikte energie |
| `.LoadsAmount` | `decimal?` | Bedrag van verbruikte energie |
| `.PV_kWh` | `decimal?` | PV-productie (kWh) |
| `.SOC_Start` | `decimal?` | SOC aan het begin van het uur |
| `.SOC_End` | `decimal?` | SOC aan het einde van het uur |
| `.ExtraLoads_Price` | `decimal?` | Prijs van extra verbruik |
| `.ExtraLoads_kWh` | `decimal?` | Som van extra verbruik (kWh) |

### IoT-apparaten (IoTDevices)

| Eigenschap | Type | Beschrijving |
|------------|-----|------|
| `App.IoTDevices` | `Dictionary<string, IIoTDevice>` | Lijst van IoT-apparaten |
| `.Name` | `string` | Naam van het apparaat |
| `.IsOn` | `bool` | Huidige status van de schakelaar |

## Speciale functies

| Functie | Beschrijving |
|---------|------|
| `void App.ToLog(string message)` | Toon een bericht in het Log-menu |
| `bool App.IsInLowerPrices(DateTime CurrDate, decimal CurrHour, int LowerHours, bool Purchase)` | Valt het gegeven uur in de goedkoopste uren van de dag? |
| `bool App.IsInHigherPrices(DateTime CurrDate, decimal CurrHour, int HigherHours, bool Purchase)` | Valt het gegeven uur in de duurste uren van de dag? |

## Beschikbare libraries

- `mscorlib.dll`
- `system.runtime.dll`
- `System.Text.RegularExpressions.dll`
- `system.linq.dll`
- `System.Collections.dll`

## Voorbeeld

```csharp
public bool IoTDevice_0036_IsOn(IApp App)
{
    return App.IsInLowerPrices(App.CurrDate, App.CurrHour, 3, false)
        || App.Forecast[App.CurrForecastIndex].FromGrid_kWh > 3;
}
```

Dit voorbeeld schakelt het apparaat in wanneer:
- Het huidige uur in de 3 goedkoopste uren van de dag valt (verkoopprijs), **of**
- De voorspelde opname uit het net in het huidige uur meer dan 3 kWh bedraagt
