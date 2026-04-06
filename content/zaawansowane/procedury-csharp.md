---
title: "Procedury C# IoT"
weight: 10
---

# Procedury C# IoT

GbbOptimizer pozwala tworzyc wlasne procedury w jezyku C#, ktore steruja urzadzeniami IoT na podstawie prognoz, cen energii i historii zuzycia.

> [!WARNING]
> Procedura musi dzialac **nie dluzej niz 100 ms** i nie moze zaklocac pracy programu. W przeciwnym razie zostanie zawieszona.

## Obiekt App

Kazda procedura IoT otrzymuje obiekt `App` jako parametr. Ponizej lista dostepnych wlasciwosci.

### Wlasciwosci glowne

| Wlasciwosc | Typ | Opis |
|------------|-----|------|
| `App.CurrDate` | `DateTime?` | Data, dla ktorej urzadzenie ma byc wlaczone/wylaczone |
| `App.CurrHour` | `decimal?` | Godzina (12:30 = 12.5; 12:45 = 12.75) |
| `App.CurrForecastIndex` | `int?` | Indeks w `App.Forecast` dla biezacej daty i godziny |
| `App.StringVariables` | `Dictionary<string, string?>` | Zmienne tekstowe uzytkownika (trwale miedzy wywolaniami) |
| `App.DecimalVariables` | `Dictionary<string, decimal?>` | Zmienne liczbowe uzytkownika (trwale miedzy wywolaniami) |

### Prognoza (Forecast)

| Wlasciwosc | Typ | Opis |
|------------|-----|------|
| `App.Forecast` | `IForecast[]` | Tablica prognozy baterii. `[0]` = biez. godzina, `[1]` = nast. godzina itd. |
| `.Date` | `DateTime` | Data prognozy |
| `.DateNo` | `int` | 0 = dzisiaj, 1 = jutro itd. |
| `.Hour` | `decimal` | Godzina prognozy |
| `.HourNo` | `decimal` | Godzina liczac od poczatku prognozy (`[0].HourNo == 0` zawsze) |
| `.StartBattery_kWhAC` | `decimal` | kWh w baterii (AC) na poczatku godziny |
| `.StartBattery_kWh` | `decimal` | kWh w baterii (DC) na poczatku godziny |
| `.Prod_KWhAC` | `decimal?` | Produkcja (PV + wiatr) w danej godzinie |
| `.Loads_kWhAC` | `decimal?` | Zuzycie w danej godzinie |
| `.GridCharge_kWhAC` | `decimal?` | kWh z sieci do baterii (strona sieci) |
| `.GridCharge_kWh` | `decimal?` | kWh z sieci do baterii (strona baterii) |
| `.Discharge_kWhAC` | `decimal?` | kWh z baterii do sieci (strona sieci) |
| `.Discharge_kWh` | `decimal?` | kWh z baterii do sieci (strona baterii) |
| `.EndBattery_kWhAC` | `decimal?` | kWh w baterii (AC) na koniec godziny |
| `.EndBattery_kWh` | `decimal?` | kWh w baterii (DC) na koniec godziny |
| `.Meteo_SOC` | `decimal?` | null = brak ostrzezen meteo; wartosc = docelowy SOC dla ostrzezenia |
| `.Temperature_C` | `decimal?` | Temperatura (st. C) w danej godzinie |
| `.ExtraLoads_kWh` | `decimal?` | Suma dodatkowych obciazen |
| `.FromGrid_kWh` | `decimal?` | kWh z sieci |
| `.PurchasePrice` | `decimal?` | Cena zakupu |
| `.PurchaseAmount` | `decimal?` | Kwota zakupu |
| `.ToGrid_kWh` | `decimal?` | kWh do sieci |
| `.SalePrice` | `decimal?` | Cena sprzedazy |
| `.SaleAmount` | `decimal?` | Kwota sprzedazy |

### Ceny (Prices)

| Wlasciwosc | Typ | Opis |
|------------|-----|------|
| `App.Prices` | `Dictionary<(DateTime, decimal), IPrice>` | Ceny za wczoraj, dzisiaj i jutro |
| `.Day` | `DateTime` | Data ceny |
| `.Hour` | `decimal` | Godzina ceny |
| `.PurchasePrice` | `decimal?` | Cena zakupu |
| `.SalesPrice` | `decimal?` | Cena sprzedazy |
| `.Imported_PurchasePrice` | `decimal?` | Cena zakupu zaimportowana ze zrodla cen |
| `.Imported_SalesPrice` | `decimal?` | Cena sprzedazy zaimportowana ze zrodla cen |

### Historia (History)

| Wlasciwosc | Typ | Opis |
|------------|-----|------|
| `App.History` | `IHistory[]` | Dane historyczne. `[0]` = godzina przed biez., `[1]` = dwie godziny przed itd. |
| `.Date` | `DateTime` | Data |
| `.Hour` | `decimal` | Godzina |
| `.FromGrid_kWh` | `decimal?` | kWh z sieci |
| `.PurchasePrice` | `decimal?` | Cena zakupu |
| `.PurchaseAmount` | `decimal?` | Kwota zakupu |
| `.ToGrid_kWh` | `decimal?` | kWh do sieci |
| `.SalePrice` | `decimal?` | Cena sprzedazy |
| `.SaleAmount` | `decimal?` | Kwota sprzedazy |
| `.Loads_kWh` | `decimal?` | Zuzycie (kWh) |
| `.LoadsPrice` | `decimal?` | Cena energii zuzycia |
| `.LoadsAmount` | `decimal?` | Kwota energii zuzycia |
| `.PV_kWh` | `decimal?` | Produkcja PV (kWh) |
| `.SOC_Start` | `decimal?` | SOC na poczatku godziny |
| `.SOC_End` | `decimal?` | SOC na koniec godziny |
| `.ExtraLoads_Price` | `decimal?` | Cena dodatkowych obciazen |
| `.ExtraLoads_kWh` | `decimal?` | Suma dodatkowych obciazen (kWh) |

### Urzadzenia IoT (IoTDevices)

| Wlasciwosc | Typ | Opis |
|------------|-----|------|
| `App.IoTDevices` | `Dictionary<string, IIoTDevice>` | Lista urzadzen IoT |
| `.Name` | `string` | Nazwa urzadzenia |
| `.IsOn` | `bool` | Aktualny stan wlacznika |

## Funkcje specjalne

| Funkcja | Opis |
|---------|------|
| `void App.ToLog(string message)` | Wyswietl wiadomosc w menu Log |
| `bool App.IsInLowerPrices(DateTime CurrDate, decimal CurrHour, int LowerHours, bool Purchase)` | Czy dana godzina jest w najnizszych godzinach dnia? |
| `bool App.IsInHigherPrices(DateTime CurrDate, decimal CurrHour, int HigherHours, bool Purchase)` | Czy dana godzina jest w najwyzszych godzinach dnia? |

## Dostepne biblioteki

- `mscorlib.dll`
- `system.runtime.dll`
- `System.Text.RegularExpressions.dll`
- `system.linq.dll`
- `System.Collections.dll`

## Przyklad

```csharp
public bool IoTDevice_0036_IsOn(IApp App)
{
    return App.IsInLowerPrices(App.CurrDate, App.CurrHour, 3, false)
        || App.Forecast[App.CurrForecastIndex].FromGrid_kWh > 3;
}
```

Ten przyklad wlacza urzadzenie, gdy:
- Biez. godzina jest w 3 najtanszych godzinach dnia (cena sprzedazy), **lub**
- Prognozowany pobor z sieci w biezacej godzinie przekracza 3 kWh
