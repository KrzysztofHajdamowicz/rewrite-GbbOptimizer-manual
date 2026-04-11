---
title: "Requests / Responses"
weight: 20
translationKey: "zapytania-odpowiedzi"
---

# MQTT-requests en -responses

GbbOptimizer ondersteunt request/response-queries via MQTT. Een extern programma stuurt een request en GbbOptimizer antwoordt met de gegevens.

## Verbinding

Het externe programma moet verbinding maken met MQTT met de volgende parameters:

| Parameter | Waarde |
|----------|---------|
| Adres | Zie [MQTT-servers]({{< relref "/references/mqtt-servers" >}}) |
| Poort | 8883 |
| Gebruiker | `{PlantId}` |
| Wachtwoord | `{PlantToken}` |
| UseTLS | true |
| ClientID | moet eindigen op `_{PlantId}` |

## Topics

| Richting | Topic |
|----------|-------|
| Request → | `{PlantId}/ha_gbb/dataserver/serverrequest` |
| ← Response | `{PlantId}/ha_gbb/dataserver/serverresponse` |

> [!NOTE]
> Voor achterwaartse compatibiliteit ondersteunt het programma ook `{PlantId}/dataserver/serverrequest` en `{PlantId}/dataserver/serverresponse` (niet aanbevolen).

## Foutresponse

Elke request kan een fout retourneren:

```json
{
  "Operation": "xxx",
  "Status": "ERROR",
  "ErrDesc": "foutbeschrijving"
}
```

| Veld | Type | Beschrijving |
|------|-----|------|
| `Operation` | string | Operatie uit de request |
| `Status` | string | `"ERROR"` |
| `ErrDesc` | string | Foutbeschrijving voor de gebruiker |

## Beschikbare operaties

{{< mqtt-endpoint name="BatteryForecast_GetChartData" request-topic="{PlantId}/ha_gbb/dataserver/serverrequest" response-topic="{PlantId}/ha_gbb/dataserver/serverresponse" description="Batterijprognosegegevens ophalen" >}}

**Request:**
```json
{"Operation": "BatteryForecast_GetChartData"}
```

**Response** — array van objecten in het veld `BatteryForecast_GetChartData`:

| Veld | Type | Beschrijving |
|------|-----|------|
| `Day` | date | Dag |
| `Hour` | int (0-23) | Uur |
| `StartBattery_Perc` | decimal | SOC aan het begin van het uur |
| `StartBattery_kWh` | decimal | kWh aan het begin (DC) |
| `StartBattery_kWhAC` | decimal | kWh aan het begin (AC) |
| `PVForecast_Perc` | decimal? | PV-prognose (%) |
| `PVForecast_kWh` | decimal? | PV-prognose (kWh DC) |
| `PVForecast_kWhAC` | decimal? | PV-prognose (kWh AC) |
| `Loads_Perc` | decimal? | Verbruik (%) |
| `Loads_kWh` | decimal? | Verbruik met ExtraLoad (kWh DC) |
| `Loads_kWhAC` | decimal? | Verbruik (kWh AC) |
| `GridCharge_Perc` | decimal? | Laden uit het net (%) |
| `GridCharge_kWh` | decimal? | Laden uit het net (kWh DC) |
| `GridCharge_kWhAC` | decimal? | Laden uit het net (kWh AC) |
| `Discharge_Perc` | decimal? | Ontladen (%) |
| `Discharge_kWh` | decimal? | Ontladen (kWh DC) |
| `Discharge_kWhAC` | decimal? | Ontladen (kWh AC) |
| `EndBattery_Perc` | decimal | SOC aan het einde van het uur |
| `EndBattery_kWh` | decimal | kWh aan het einde (DC) |
| `EndBattery_kWhAC` | decimal | kWh aan het einde (AC) |
| `EndBattery_Price` | decimal? | Waarde van de energie in de batterij |
| `Profit_Amount` | decimal? | Winstbedrag |
| `FromGrid_kWh` | decimal? | Import uit het net |
| `Purchase_Price` | decimal? | Inkoopprijs |
| `Purchase_Amount` | decimal? | Inkoopbedrag |
| `ToGrid_kWh` | decimal? | Export naar het net |
| `Sale_Price` | decimal? | Verkoopprijs |
| `Sale_Amount` | decimal? | Verkoopbedrag |
| `Consumption_kWh` | decimal? | Verbruik (= Loads_kWh) |
| `Consumption_Price` | decimal? | Verbruiksprijs |
| `Consumption_Amount` | decimal? | Verbruiksbedrag |
| `ExtraLoadsKW` | decimal? | Extra verbruik (totaal) |
| `ExtraLoadsKW_ElectricVehicle` | decimal? | EV |
| `ExtraLoadsKW_HeatingPump` | decimal? | Warmtepomp |
| `ExtraLoadsKW_Generic1`–`Generic6` | decimal? | Andere 1–6 |

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="History_GetHours" request-topic="{PlantId}/ha_gbb/dataserver/serverrequest" response-topic="{PlantId}/ha_gbb/dataserver/serverresponse" description="Uurgeschiedenis uit de module Winsten ophalen" >}}

**Request — vorm 1** (datumbereik):
```json
{"Operation": "History_GetHours", "FromDate": "2024-01-01", "ToDate": "2024-01-01"}
```

| Veld | Type | Beschrijving |
|------|-----|------|
| `Operation` | string | `"History_GetHours"` |
| `FromDate` | date? | Standaard: vandaag |
| `ToDate` | date? | Standaard: vandaag |

**Request — vorm 2** (periode):

| Veld | Type | Beschrijving |
|------|-----|------|
| `Operation` | string | `"History_GetHours"` |
| `Period` | string | `"curr_day"`, `"prev_day"` of `"today_yesterday"` |
| `AddPeriodToProperty` | int? | Indien 1 → responssleutel met suffix, bijv. `"History_Hours_curr_day"` |

**Response** — array in `History_Hours`:

| Veld | Type | Beschrijving |
|------|-----|------|
| `Hour` | decimal | Uur |
| `Day` | date | Dag |
| `FromGrid_kWh` | decimal? | Import uit het net |
| `FromGrid2_kWh` | decimal? | Gesaldeerde import |
| `PurchaseAmount` | decimal? | Inkoopbedrag |
| `ToGrid_kWh` | decimal? | Export naar het net |
| `ToGrid2_kWh` | decimal? | Gesaldeerde export |
| `SaleAmount` | decimal? | Verkoopbedrag |
| `Consumption_kWh` | decimal? | Verbruik |
| `ConsumptionAmount` | decimal? | Verbruiksbedrag |
| `ProfitAmount` | decimal? | Winstbedrag |
| `Solar_kWh` | decimal? | PV-productie |
| `ToBattery_kWh` | decimal? | Naar de batterij |
| `SOC_Min` / `SOC_Max` | decimal? | Min/Max SOC |
| `SOC_Start` / `SOC_End` | decimal? | Begin / eind SOC |
| `BattChange_kWh` | decimal? | Batterijverandering |
| `LostPower_kWh` | decimal? | Verliezen |
| `ChargeFromGrid_kWh` | decimal? | Laden uit het net |
| `ChargeFromPV_kWh` | decimal? | Laden uit PV |
| `DischargeToGrid_kWh` | decimal? | Ontladen naar het net |
| `DischargeToLoads_kWh` | decimal? | Ontladen naar verbruik |
| `Start_kWh` / `End_kWh` | decimal? | Begin / eind kWh in de batterij |
| `ValueStartAmount` / `ValueEndAmount` | decimal? | Beginwaarde / eindwaarde |
| `ValueChangeAmount` | decimal? | Waardeverandering |

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="History_GetDays" request-topic="{PlantId}/ha_gbb/dataserver/serverrequest" response-topic="{PlantId}/ha_gbb/dataserver/serverresponse" description="Daggeschiedenis uit de module Winsten ophalen" >}}

**Request — vorm 1:**
```json
{"Operation": "History_GetDays", "FromDate": "2024-01-01", "ToDate": "2024-01-03"}
```

**Request — vorm 2:**

| Veld | Type | Beschrijving |
|------|-----|------|
| `Period` | string | `"curr_month"`, `"prev_month"`, `"curr_year"` of `"prev_year"` |
| `AddPeriodToProperty` | int? | Indien 1 → suffix in de responssleutel |

**Response** — identieke structuur als `History_GetHours`, maar in de array `History_Days`.

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="History_GetMonths" request-topic="{PlantId}/ha_gbb/dataserver/serverrequest" response-topic="{PlantId}/ha_gbb/dataserver/serverresponse" description="Maandgeschiedenis uit de module Winsten ophalen" >}}

**Request — vorm 1:**
```json
{"Operation": "History_GetMonths", "FromYear": 2024, "FromMonth": 1, "ToYear": 2024, "ToMonth": 2}
```

| Veld | Type | Beschrijving |
|------|-----|------|
| `FromYear` / `FromMonth` | int? | Standaard: huidig jaar/maand |
| `ToYear` / `ToMonth` | int? | Standaard: huidig jaar/maand |

**Request — vorm 2:**

| Veld | Type | Beschrijving |
|------|-----|------|
| `Period` | string | `"curr_month"`, `"prev_month"`, `"curr_year"` of `"prev_year"` |

**Response** — identieke structuur + velden `Year` en `Month`, in de array `History_Months`.

{{< /mqtt-endpoint >}}
