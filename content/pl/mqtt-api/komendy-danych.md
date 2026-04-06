---
title: "Komendy danych"
weight: 30
translationKey: "komendy-danych"
---

# Komendy danych MQTT

Komendy pozwalające zewnętrznym programom zmieniać dane w GbbOptimizer. Każda komenda wysyła dane na dedykowany temat i otrzymuje wynik na `{PlantId}/ha_gbb/api/result`.

## Wynik komend

{{< mqtt-topic topic="{PlantId}/ha_gbb/api/result" direction="publish" description="Wynik każdej komendy danych — OK lub opis błędu" >}}

| Pole | Typ | Opis |
|------|-----|------|
| `OrderId` | string? | Skopiowany z zapytania |
| `Result` | string | `"OK"` lub opis błędu |
| `Data` | object | Dane z oryginalnego zapytania |

---

{{< mqtt-endpoint name="SetManualPrices" topic="{PlantId}/ha_gbb/api/setmanualprices" direction="subscribe" description="Ustaw ręczne ceny energii" >}}

| Pole | | Typ | Wymagane | Opis |
|------|--|-----|---------|------|
| `OrderId` | | string | nie | Tekst skopiowany do odpowiedzi |
| `Data` | | tablica | tak | |
| | `Date` | date | tak | Data ceny |
| | `StartHour` | int (0-23) | tak | Godzina rozpoczęcia |
| | `StartMinute` | int (0-59) | nie | Minuta (domyślnie 0) |
| | `PurchasePrice` | decimal | nie | Cena zakupu |
| | `TransferPrice` | decimal | nie | Cena przesyłu |
| | `SalePrice` | decimal | nie | Cena sprzedaży |

**Przykład:**
```json
{
  "Data": [
    {"Date": "2024-04-20", "StartHour": 20, "PurchasePrice": 0.23}
  ]
}
```

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetExtraLoads" topic="{PlantId}/ha_gbb/api/setextraloads" direction="subscribe" description="Ustaw Extra Zużycie" >}}

| Pole | | Typ | Wymagane | Opis |
|------|--|-----|---------|------|
| `OrderId` | | string | nie | Tekst skopiowany do odpowiedzi |
| `Data` | | tablica | tak | |
| | `Date` | date | tak | Data (dzisiaj lub jutro) |
| | `StartHour` | int (0-23) | tak | Godzina |
| | `StartMinute` | int (0-59) | nie | Minuta (domyślnie 0) |
| | `TypeNo` | int | tak | 0=EV, 1=Pompa ciepła, 2=Inne1, 3=Inne2, ..., 7=Inne6 |
| | `ExtraLoads_kWh` | decimal | tak | kWh |

**Przykład:**
```json
{
  "Data": [
    {"Date": "2024-04-20", "StartHour": 20, "TypeNo": 1, "ExtraLoads_kWh": 1.23}
  ]
}
```

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetRealTemperature" topic="{PlantId}/ha_gbb/api/setrealtemperature" direction="subscribe" description="Ustaw rzeczywistą temperaturę" >}}

| Pole | | Typ | Wymagane | Opis |
|------|--|-----|---------|------|
| `OrderId` | | string | nie | Tekst skopiowany do odpowiedzi |
| `Data` | | tablica | tak | |
| | `Date` | date | tak | Data (wczoraj, dzisiaj lub jutro). Jeśli brak `Hour` — godzina z daty |
| | `Hour` | int (0-23) | nie | Godzina temperatury |
| | `RealTemperature` | decimal | tak | Temperatura (°C) |

**Przykład:**
```json
{
  "Data": [
    {"Date": "2024-04-20", "Hour": 20, "RealTemperature": 1.23}
  ]
}
```

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetOptimizer" topic="{PlantId}/ha_gbb/api/setoptimizer" direction="subscribe" description="Ustaw parametry optymalizatora" >}}

| Pole | | Typ | Wymagane | Opis |
|------|--|-----|---------|------|
| `OrderId` | | string | nie | Tekst skopiowany do odpowiedzi |
| `Data` | | obiekt | tak | |
| | `Opt2_3x100Request` | int | nie | 0 lub 1 — wymuszenie 3h×100% |
| | `CurrentLoadProfileId` | int | nie | ID Profilu Zużycia |
| | `CurrentLoadProfileName` | string | nie | Nazwa Profilu Zużycia (wielkość liter nieistotna) |

**Przykład:**
```json
{"Data": {"Opt2_3x100Request": 1}}
```

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetCar" topic="{PlantId}/ha_gbb/api/setcar" direction="subscribe" description="Ustaw parametry samochodu EV" >}}

> [!NOTE]
> Samochód „HomeAssistant EV Car" musi być najpierw dodany w programie. Zmieniane są tylko podane parametry — ale program wymaga aktualnych: `SOC`, `SOC_ChargeLimit`, `IsConnected`, `IsCharging`, `Position_Longitude`, `Position_Latitude`.

| Pole | | Typ | Wymagane | Opis |
|------|--|-----|---------|------|
| `OrderId` | | string | nie | Tekst skopiowany do odpowiedzi |
| `Data` | | tablica | tak | Można aktualizować wiele samochodów |
| | `VIN` | string | tak | Klucz identyfikacyjny. Nowy VIN = nowy samochód (max 10) |
| | `BatteryKWh` | decimal | nie | Pojemność baterii samochodu |
| | `ChargeA` | decimal | nie | Domyślny prąd ładowania (A) |
| | `Phases` | int | nie | 1 lub 3 fazy |
| | `SOC` | int | nie | Aktualny SOC |
| | `SOC_ChargeLimit` | int | nie | Docelowy SOC |
| | `InService` | bool | nie | Czy samochód jest w serwisie |
| | `IsConnected` | bool | nie | Czy podłączony do ładowarki |
| | `IsCharging` | bool | nie | Czy aktualnie się ładuje |
| | `Position_Longitude` | double | nie | Długość geograficzna |
| | `Position_Latitude` | double | nie | Szerokość geograficzna |

**Przykład:**
```json
{
  "Data": [
    {"VIN": "vin1234", "SOC": 40, "SOC_ChargeLimit": 90}
  ]
}
```

{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="SetHP" topic="{PlantId}/ha_gbb/api/sethp" direction="subscribe" description="Ustaw parametry pompy ciepła" >}}

| Pole | | Typ | Wymagane | Opis |
|------|--|-----|---------|------|
| `OrderId` | | string | nie | Tekst skopiowany do odpowiedzi |
| `Data` | | obiekt | tak | Zmieniane tylko podane parametry |
| | `HPForecast_Break_On` | bool | nie | Przerwa w pracy PC: włącz/wyłącz |
| | `HPForecast_BreakFromDate` | date | nie | Data rozpoczęcia przerwy |
| | `HPForecast_BreakFromHour` | int (0-23) | nie | Godzina rozpoczęcia |
| | `HPForecast_BreakToDate` | date | nie | Data zakończenia (włączńie) |
| | `HPForecast_BreakToHour` | int (0-23) | nie | Godzina zakończenia (włączńie) |

**Przykład:**
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
