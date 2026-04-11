---
title: "Datacommando's"
weight: 30
translationKey: "komendy-danych"
---

# MQTT-datacommando's

Commando's waarmee externe programma's gegevens in GbbOptimizer kunnen wijzigen. Elk commando stuurt data naar een speciaal topic en ontvangt het resultaat op `{PlantId}/ha_gbb/api/result`.

## Commandoresultaat

{{< mqtt-topic topic="{PlantId}/ha_gbb/api/result" direction="publish" description="Resultaat van elk datacommando — OK of foutbeschrijving" >}}

| Veld | Type | Beschrijving |
|------|-----|------|
| `OrderId` | string? | Gekopieerd uit de request |
| `Result` | string | `"OK"` of foutbeschrijving |
| `Data` | object | Gegevens uit de oorspronkelijke request |

---

{{< mqtt-endpoint name="SetManualPrices" topic="{PlantId}/ha_gbb/api/setmanualprices" direction="subscribe" description="Handmatige energieprijzen instellen" >}}

| Veld | | Type | Vereist | Beschrijving |
|------|--|-----|---------|------|
| `OrderId` | | string | nee | Tekst die naar het antwoord wordt gekopieerd |
| `Data` | | array | ja | |
| | `Date` | date | ja | Datum van de prijs |
| | `StartHour` | int (0-23) | ja | Beginuur |
| | `StartMinute` | int (0-59) | nee | Minuut (standaard 0) |
| | `PurchasePrice` | decimal | nee | Inkoopprijs |
| | `TransferPrice` | decimal | nee | Transportprijs |
| | `SalePrice` | decimal | nee | Verkoopprijs |

**Voorbeeld:**
```json
{
  "Data": [
    {"Date": "2024-04-20", "StartHour": 20, "PurchasePrice": 0.23}
  ]
}
```

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetExtraLoads" topic="{PlantId}/ha_gbb/api/setextraloads" direction="subscribe" description="Extra verbruik instellen" >}}

| Veld | | Type | Vereist | Beschrijving |
|------|--|-----|---------|------|
| `OrderId` | | string | nee | Tekst die naar het antwoord wordt gekopieerd |
| `Data` | | array | ja | |
| | `Date` | date | ja | Datum (vandaag of morgen) |
| | `StartHour` | int (0-23) | ja | Uur |
| | `StartMinute` | int (0-59) | nee | Minuut (standaard 0) |
| | `TypeNo` | int | ja | 0=EV, 1=Warmtepomp, 2=Andere1, 3=Andere2, ..., 7=Andere6 |
| | `ExtraLoads_kWh` | decimal | ja | kWh |

**Voorbeeld:**
```json
{
  "Data": [
    {"Date": "2024-04-20", "StartHour": 20, "TypeNo": 1, "ExtraLoads_kWh": 1.23}
  ]
}
```

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetRealTemperature" topic="{PlantId}/ha_gbb/api/setrealtemperature" direction="subscribe" description="Werkelijke temperatuur instellen" >}}

| Veld | | Type | Vereist | Beschrijving |
|------|--|-----|---------|------|
| `OrderId` | | string | nee | Tekst die naar het antwoord wordt gekopieerd |
| `Data` | | array | ja | |
| | `Date` | date | ja | Datum (gisteren, vandaag of morgen). Zonder `Hour` — uur uit de datum |
| | `Hour` | int (0-23) | nee | Uur van de temperatuur |
| | `RealTemperature` | decimal | ja | Temperatuur (°C) |

**Voorbeeld:**
```json
{
  "Data": [
    {"Date": "2024-04-20", "Hour": 20, "RealTemperature": 1.23}
  ]
}
```

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetOptimizer" topic="{PlantId}/ha_gbb/api/setoptimizer" direction="subscribe" description="Optimizer-parameters instellen" >}}

| Veld | | Type | Vereist | Beschrijving |
|------|--|-----|---------|------|
| `OrderId` | | string | nee | Tekst die naar het antwoord wordt gekopieerd |
| `Data` | | object | ja | |
| | `Opt2_3x100Request` | int | nee | 0 of 1 — 3h×100% forceren |
| | `CurrentLoadProfileId` | int | nee | ID van het verbruiksprofiel |
| | `CurrentLoadProfileName` | string | nee | Naam van het verbruiksprofiel (niet hoofdlettergevoelig) |

**Voorbeeld:**
```json
{"Data": {"Opt2_3x100Request": 1}}
```

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetCar" topic="{PlantId}/ha_gbb/api/setcar" direction="subscribe" description="Parameters van een EV instellen" >}}

> [!NOTE]
> De auto „HomeAssistant EV Car" moet eerst in het programma worden toegevoegd. Alleen de opgegeven parameters worden gewijzigd — maar het programma vereist actuele waarden voor: `SOC`, `SOC_ChargeLimit`, `IsConnected`, `IsCharging`, `Position_Longitude`, `Position_Latitude`.

| Veld | | Type | Vereist | Beschrijving |
|------|--|-----|---------|------|
| `OrderId` | | string | nee | Tekst die naar het antwoord wordt gekopieerd |
| `Data` | | array | ja | Meerdere auto's kunnen worden bijgewerkt |
| | `VIN` | string | ja | Identificatiesleutel. Nieuwe VIN = nieuwe auto (max. 10) |
| | `BatteryKWh` | decimal | nee | Accucapaciteit van de auto |
| | `ChargeA` | decimal | nee | Standaard laadstroom (A) |
| | `Phases` | int | nee | 1 of 3 fases |
| | `SOC` | int | nee | Huidige SOC |
| | `SOC_ChargeLimit` | int | nee | Doel-SOC |
| | `InService` | bool | nee | Of de auto in onderhoud is |
| | `IsConnected` | bool | nee | Of aangesloten op de lader |
| | `IsCharging` | bool | nee | Of momenteel aan het laden |
| | `Position_Longitude` | double | nee | Lengtegraad |
| | `Position_Latitude` | double | nee | Breedtegraad |

**Voorbeeld:**
```json
{
  "Data": [
    {"VIN": "vin1234", "SOC": 40, "SOC_ChargeLimit": 90}
  ]
}
```

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetHP" topic="{PlantId}/ha_gbb/api/sethp" direction="subscribe" description="Parameters van de warmtepomp instellen" >}}

| Veld | | Type | Vereist | Beschrijving |
|------|--|-----|---------|------|
| `OrderId` | | string | nee | Tekst die naar het antwoord wordt gekopieerd |
| `Data` | | object | ja | Alleen de opgegeven parameters worden gewijzigd |
| | `HPForecast_Break_On` | bool | nee | Onderbreking van de WP: aan/uit |
| | `HPForecast_BreakFromDate` | date | nee | Begindatum van de onderbreking |
| | `HPForecast_BreakFromHour` | int (0-23) | nee | Beginuur |
| | `HPForecast_BreakToDate` | date | nee | Einddatum (inclusief) |
| | `HPForecast_BreakToHour` | int (0-23) | nee | Einduur (inclusief) |

**Voorbeeld:**
```json
{
  "Data": {
    "HPForecast_Break_On": true,
    "HPForecast_BreakToDate": "2026-01-30",
    "HPForecast_BreakToHour": 23
  }
}
```

{{< /mqtt-endpoint >}}
