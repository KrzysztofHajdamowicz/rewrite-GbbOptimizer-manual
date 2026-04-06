---
title: "Procedury C# IoT"
weight: 10
---

# Procedury C# IoT

GbbOptimizer pozwala tworzyć własne procedury w języku C#, które sterują urządzeniami IoT na podstawie prognoz, cen energii i historii zużycia.

> [!WARNING]
> Procedura musi działać **nie dłużej niż 100 ms** i nie może zakłócać pracy programu. W przeciwnym razie zostanie zawieszona.

## Obiekt App

Każda procedura IoT otrzymuje obiekt `App` jako parametr. Poniżej lista dostępnych właściwości.

### Właściwości główne

| Właściwość | Typ | Opis |
|------------|-----|------|
| `App.CurrDate` | `DateTime?` | Data, dla której urządzenie ma być włączone/wyłączone |
| `App.CurrHour` | `decimal?` | Godzina (12:30 = 12.5; 12:45 = 12.75) |
| `App.CurrForecastIndex` | `int?` | Indeks w `App.Forecast` dla bieżącej daty i godziny |
| `App.StringVariables` | `Dictionary<string, string?>` | Zmienne tekstowe użytkownika (trwałe między wywołaniami) |
| `App.DecimalVariables` | `Dictionary<string, decimal?>` | Zmienne liczbowe użytkownika (trwałe między wywołaniami) |

### Prognoza (Forecast)

| Właściwość | Typ | Opis |
|------------|-----|------|
| `App.Forecast` | `IForecast[]` | Tablica prognozy baterii. `[0]` = bież. godzina, `[1]` = nast. godzina itd. |
| `.Date` | `DateTime` | Data prognozy |
| `.DateNo` | `int` | 0 = dzisiaj, 1 = jutro itd. |
| `.Hour` | `decimal` | Godzina prognozy |
| `.HourNo` | `decimal` | Godzina licząc od początku prognozy (`[0].HourNo == 0` zawsze) |
| `.StartBattery_kWhAC` | `decimal` | kWh w baterii (AC) na początku godziny |
| `.StartBattery_kWh` | `decimal` | kWh w baterii (DC) na początku godziny |
| `.Prod_KWhAC` | `decimal?` | Produkcja (PV + wiatr) w danej godzinie |
| `.Loads_kWhAC` | `decimal?` | Zużycie w danej godzinie |
| `.GridCharge_kWhAC` | `decimal?` | kWh z sieci do baterii (strona sieci) |
| `.GridCharge_kWh` | `decimal?` | kWh z sieci do baterii (strona baterii) |
| `.Discharge_kWhAC` | `decimal?` | kWh z baterii do sieci (strona sieci) |
| `.Discharge_kWh` | `decimal?` | kWh z baterii do sieci (strona baterii) |
| `.EndBattery_kWhAC` | `decimal?` | kWh w baterii (AC) na koniec godziny |
| `.EndBattery_kWh` | `decimal?` | kWh w baterii (DC) na koniec godziny |
| `.Meteo_SOC` | `decimal?` | null = brak ostrzeżeń meteo; wartość = docelowy SOC dla ostrzeżenia |
| `.Temperature_C` | `decimal?` | Temperatura (st. C) w danej godzinie |
| `.ExtraLoads_kWh` | `decimal?` | Suma dodatkowych obciążeń |
| `.FromGrid_kWh` | `decimal?` | kWh z sieci |
| `.PurchasePrice` | `decimal?` | Cena zakupu |
| `.PurchaseAmount` | `decimal?` | Kwota zakupu |
| `.ToGrid_kWh` | `decimal?` | kWh do sieci |
| `.SalePrice` | `decimal?` | Cena sprzedaży |
| `.SaleAmount` | `decimal?` | Kwota sprzedaży |

### Ceny (Prices)

| Właściwość | Typ | Opis |
|------------|-----|------|
| `App.Prices` | `Dictionary<(DateTime, decimal), IPrice>` | Ceny za wczoraj, dzisiaj i jutro |
| `.Day` | `DateTime` | Data ceny |
| `.Hour` | `decimal` | Godzina ceny |
| `.PurchasePrice` | `decimal?` | Cena zakupu |
| `.SalesPrice` | `decimal?` | Cena sprzedaży |
| `.Imported_PurchasePrice` | `decimal?` | Cena zakupu zaimportowana ze źródła cen |
| `.Imported_SalesPrice` | `decimal?` | Cena sprzedaży zaimportowana ze źródła cen |

### Historia (History)

| Właściwość | Typ | Opis |
|------------|-----|------|
| `App.History` | `IHistory[]` | Dane historyczne. `[0]` = godzina przed bież., `[1]` = dwie godziny przed itd. |
| `.Date` | `DateTime` | Data |
| `.Hour` | `decimal` | Godzina |
| `.FromGrid_kWh` | `decimal?` | kWh z sieci |
| `.PurchasePrice` | `decimal?` | Cena zakupu |
| `.PurchaseAmount` | `decimal?` | Kwota zakupu |
| `.ToGrid_kWh` | `decimal?` | kWh do sieci |
| `.SalePrice` | `decimal?` | Cena sprzedaży |
| `.SaleAmount` | `decimal?` | Kwota sprzedaży |
| `.Loads_kWh` | `decimal?` | Zużycie (kWh) |
| `.LoadsPrice` | `decimal?` | Cena energii zużycia |
| `.LoadsAmount` | `decimal?` | Kwota energii zużycia |
| `.PV_kWh` | `decimal?` | Produkcja PV (kWh) |
| `.SOC_Start` | `decimal?` | SOC na początku godziny |
| `.SOC_End` | `decimal?` | SOC na koniec godziny |
| `.ExtraLoads_Price` | `decimal?` | Cena dodatkowych obciążeń |
| `.ExtraLoads_kWh` | `decimal?` | Suma dodatkowych obciążeń (kWh) |

### Urządzenia IoT (IoTDevices)

| Właściwość | Typ | Opis |
|------------|-----|------|
| `App.IoTDevices` | `Dictionary<string, IIoTDevice>` | Lista urządzeń IoT |
| `.Name` | `string` | Nazwa urządzenia |
| `.IsOn` | `bool` | Aktualny stan włącznika |

## Funkcje specjalne

| Funkcja | Opis |
|---------|------|
| `void App.ToLog(string message)` | Wyświetl wiadomość w menu Log |
| `bool App.IsInLowerPrices(DateTime CurrDate, decimal CurrHour, int LowerHours, bool Purchase)` | Czy dana godzina jest w najniższych godzinach dnia? |
| `bool App.IsInHigherPrices(DateTime CurrDate, decimal CurrHour, int HigherHours, bool Purchase)` | Czy dana godzina jest w najwyższych godzinach dnia? |

## Dostępne biblioteki

- `mscorlib.dll`
- `system.runtime.dll`
- `System.Text.RegularExpressions.dll`
- `system.linq.dll`
- `System.Collections.dll`

## Przykład

```csharp
public bool IoTDevice_0036_IsOn(IApp App)
{
    return App.IsInLowerPrices(App.CurrDate, App.CurrHour, 3, false)
        || App.Forecast[App.CurrForecastIndex].FromGrid_kWh > 3;
}
```

Ten przykład włącza urządzenie, gdy:
- Bież. godzina jest w 3 najtańszych godzinach dnia (cena sprzedaży), **lub**
- Prognozowany pobór z sieci w bieżącej godzinie przekracza 3 kWh
