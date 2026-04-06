---
title: "Zapytania / Odpowiedzi"
weight: 20
---

# Zapytania i odpowiedzi MQTT

GbbOptimizer obsługuje zapytania request/response przez MQTT. Zewnętrzny program wysyła zapytanie, a GbbOptimizer odpowiada z danymi.

## Połączenie

Zewnętrzny program powinien połączyć się z MQTT z parametrami:

| Parametr | Wartość |
|----------|---------|
| Adres | Patrz [serwery MQTT]({{< relref "/referencje/serwery-mqtt" >}}) |
| Port | 8883 |
| Użytkownik | `{PlantId}` |
| Hasło | `{PlantToken}` |
| UseTLS | true |
| ClientID | musi kończyć się na `_{PlantId}` |

## Tematy

| Kierunek | Temat |
|----------|-------|
| Zapytanie → | `{PlantId}/ha_gbb/dataserver/serverrequest` |
| ← Odpowiedź | `{PlantId}/ha_gbb/dataserver/serverresponse` |

> [!NOTE]
> Dla kompatybilności wstecznej program obsługuje też `{PlantId}/dataserver/serverrequest` i `{PlantId}/dataserver/serverresponse` (nie rekomendowane).

## Odpowiedź z błędem

Każde zapytanie może zwrócić błąd:

```json
{
  "Operation": "xxx",
  "Status": "ERROR",
  "ErrDesc": "opis błędu"
}
```

| Pole | Typ | Opis |
|------|-----|------|
| `Operation` | string | Operacja z zapytania |
| `Status` | string | `"ERROR"` |
| `ErrDesc` | string | Opis błędu dla użytkownika |

## Dostępne operacje

{{< mqtt-endpoint name="BatteryForecast_GetChartData" request-topic="{PlantId}/ha_gbb/dataserver/serverrequest" response-topic="{PlantId}/ha_gbb/dataserver/serverresponse" description="Pobierz dane prognozy baterii" >}}

**Zapytanie:**
```json
{"Operation": "BatteryForecast_GetChartData"}
```

**Odpowiedź** — tablica obiektów w polu `BatteryForecast_GetChartData`:

| Pole | Typ | Opis |
|------|-----|------|
| `Day` | date | Dzień |
| `Hour` | int (0-23) | Godzina |
| `StartBattery_Perc` | decimal | SOC na początku godziny |
| `StartBattery_kWh` | decimal | kWh na początku (DC) |
| `StartBattery_kWhAC` | decimal | kWh na początku (AC) |
| `PVForecast_Perc` | decimal? | Prognoza PV (%) |
| `PVForecast_kWh` | decimal? | Prognoza PV (kWh DC) |
| `PVForecast_kWhAC` | decimal? | Prognoza PV (kWh AC) |
| `Loads_Perc` | decimal? | Zużycie (%) |
| `Loads_kWh` | decimal? | Zużycie z ExtraLoad (kWh DC) |
| `Loads_kWhAC` | decimal? | Zużycie (kWh AC) |
| `GridCharge_Perc` | decimal? | Ładowanie z sieci (%) |
| `GridCharge_kWh` | decimal? | Ładowanie z sieci (kWh DC) |
| `GridCharge_kWhAC` | decimal? | Ładowanie z sieci (kWh AC) |
| `Discharge_Perc` | decimal? | Rozładowanie (%) |
| `Discharge_kWh` | decimal? | Rozładowanie (kWh DC) |
| `Discharge_kWhAC` | decimal? | Rozładowanie (kWh AC) |
| `EndBattery_Perc` | decimal | SOC na koniec godziny |
| `EndBattery_kWh` | decimal | kWh na koniec (DC) |
| `EndBattery_kWhAC` | decimal | kWh na koniec (AC) |
| `EndBattery_Price` | decimal? | Wartość energii w baterii |
| `Profit_Amount` | decimal? | Kwota zysku |
| `FromGrid_kWh` | decimal? | Import z sieci |
| `Purchase_Price` | decimal? | Cena zakupu |
| `Purchase_Amount` | decimal? | Kwota zakupu |
| `ToGrid_kWh` | decimal? | Eksport do sieci |
| `Sale_Price` | decimal? | Cena sprzedaży |
| `Sale_Amount` | decimal? | Kwota sprzedaży |
| `Consumption_kWh` | decimal? | Zużycie (= Loads_kWh) |
| `Consumption_Price` | decimal? | Cena zużycia |
| `Consumption_Amount` | decimal? | Kwota zużycia |
| `ExtraLoadsKW` | decimal? | Extra Zużycie (łącznie) |
| `ExtraLoadsKW_ElectricVehicle` | decimal? | EV |
| `ExtraLoadsKW_HeatingPump` | decimal? | Pompa ciepła |
| `ExtraLoadsKW_Generic1`–`Generic6` | decimal? | Inne 1–6 |

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="History_GetHours" request-topic="{PlantId}/ha_gbb/dataserver/serverrequest" response-topic="{PlantId}/ha_gbb/dataserver/serverresponse" description="Pobierz historię godzinową z modułu Zyski" >}}

**Zapytanie — forma 1** (zakres dat):
```json
{"Operation": "History_GetHours", "FromDate": "2024-01-01", "ToDate": "2024-01-01"}
```

| Pole | Typ | Opis |
|------|-----|------|
| `Operation` | string | `"History_GetHours"` |
| `FromDate` | date? | Domyślnie: dzisiaj |
| `ToDate` | date? | Domyślnie: dzisiaj |

**Zapytanie — forma 2** (okres):

| Pole | Typ | Opis |
|------|-----|------|
| `Operation` | string | `"History_GetHours"` |
| `Period` | string | `"curr_day"`, `"prev_day"` lub `"today_yesterday"` |
| `AddPeriodToProperty` | int? | Jeśli 1 → klucz odpowiedzi z sufiksem, np. `"History_Hours_curr_day"` |

**Odpowiedź** — tablica w `History_Hours`:

| Pole | Typ | Opis |
|------|-----|------|
| `Hour` | decimal | Godzina |
| `Day` | date | Dzień |
| `FromGrid_kWh` | decimal? | Import z sieci |
| `FromGrid2_kWh` | decimal? | Import zbilansowany |
| `PurchaseAmount` | decimal? | Kwota zakupu |
| `ToGrid_kWh` | decimal? | Eksport do sieci |
| `ToGrid2_kWh` | decimal? | Eksport zbilansowany |
| `SaleAmount` | decimal? | Kwota sprzedaży |
| `Consumption_kWh` | decimal? | Zużycie |
| `ConsumptionAmount` | decimal? | Kwota zużycia |
| `ProfitAmount` | decimal? | Kwota zysku |
| `Solar_kWh` | decimal? | Produkcja PV |
| `ToBattery_kWh` | decimal? | Do baterii |
| `SOC_Min` / `SOC_Max` | decimal? | Min/Max SOC |
| `SOC_Start` / `SOC_End` | decimal? | Pocz/Koń SOC |
| `BattChange_kWh` | decimal? | Zmiana baterii |
| `LostPower_kWh` | decimal? | Straty |
| `ChargeFromGrid_kWh` | decimal? | Ładowanie z sieci |
| `ChargeFromPV_kWh` | decimal? | Ładowanie z PV |
| `DischargeToGrid_kWh` | decimal? | Rozładowanie do sieci |
| `DischargeToLoads_kWh` | decimal? | Rozładowanie do zużycia |
| `Start_kWh` / `End_kWh` | decimal? | Pocz/Koń kWh w baterii |
| `ValueStartAmount` / `ValueEndAmount` | decimal? | Wartość pocz/koń |
| `ValueChangeAmount` | decimal? | Zmiana wartości |

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="History_GetDays" request-topic="{PlantId}/ha_gbb/dataserver/serverrequest" response-topic="{PlantId}/ha_gbb/dataserver/serverresponse" description="Pobierz historię dzienną z modułu Zyski" >}}

**Zapytanie — forma 1:**
```json
{"Operation": "History_GetDays", "FromDate": "2024-01-01", "ToDate": "2024-01-03"}
```

**Zapytanie — forma 2:**

| Pole | Typ | Opis |
|------|-----|------|
| `Period` | string | `"curr_month"`, `"prev_month"`, `"curr_year"` lub `"prev_year"` |
| `AddPeriodToProperty` | int? | Jeśli 1 → sufiks w kluczu odpowiedzi |

**Odpowiedź** — identyczna struktura jak `History_GetHours`, ale w tablicy `History_Days`.

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="History_GetMonths" request-topic="{PlantId}/ha_gbb/dataserver/serverrequest" response-topic="{PlantId}/ha_gbb/dataserver/serverresponse" description="Pobierz historię miesięczną z modułu Zyski" >}}

**Zapytanie — forma 1:**
```json
{"Operation": "History_GetMonths", "FromYear": 2024, "FromMonth": 1, "ToYear": 2024, "ToMonth": 2}
```

| Pole | Typ | Opis |
|------|-----|------|
| `FromYear` / `FromMonth` | int? | Domyślnie: bieżący rok/miesiąc |
| `ToYear` / `ToMonth` | int? | Domyślnie: bieżący rok/miesiąc |

**Zapytanie — forma 2:**

| Pole | Typ | Opis |
|------|-----|------|
| `Period` | string | `"curr_month"`, `"prev_month"`, `"curr_year"` lub `"prev_year"` |

**Odpowiedź** — identyczna struktura + pola `Year` i `Month`, w tablicy `History_Months`.

{{< /mqtt-endpoint >}}
