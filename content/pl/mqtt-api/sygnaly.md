---
title: "Sygnały"
weight: 10
translationKey: "sygnaly"
---

# Sygnały MQTT

GbbOptimizer wysyła sygnały do zewnętrznych programów (np. Home Assistant) co godzinę, na podstawie prognozy dla bieżącej godziny.

Parametry połączenia z MQTT (adres, port, TLS, ClientID) — patrz [Zapytania / Odpowiedzi]({{< relref "/mqtt-api/zapytania-odpowiedzi" >}}).

> [!NOTE]
> - Sygnały muszą być najpierw włączone w module [Rozładowanie]({{< relref "/konfiguracja/rozladowanie" >}})
> - Dany sygnał nie jest wysyłany, jeśli parametr „X" nie jest zdefiniowany (pole puste)

## Sygnały binarne

Zewnętrzny program może subskrybować następujące tematy:

{{< mqtt-topic topic="{PlantId}/signals/SOCHigherEqThanX" direction="publish" qos="0" description="\"1\" jeśli SOC ≥ X, w przeciwnym razie \"0\"" >}}

{{< mqtt-topic topic="{PlantId}/signals/SOCLowerEqThanX" direction="publish" qos="0" description="\"1\" jeśli SOC ≤ X, w przeciwnym razie \"0\"" >}}

{{< mqtt-topic topic="{PlantId}/signals/SellingPriceHigherEqThanX" direction="publish" qos="0" description="\"1\" jeśli Cena Sprzedaży ≥ X, w przeciwnym razie \"0\"" >}}

{{< mqtt-topic topic="{PlantId}/signals/SellingPriceLowerEqThanX" direction="publish" qos="0" description="\"1\" jeśli Cena Sprzedaży ≤ X, w przeciwnym razie \"0\"" >}}

{{< mqtt-topic topic="{PlantId}/signals/FromGridHigherEqThanX" direction="publish" qos="0" description="\"1\" jeśli import z sieci ≥ X, w przeciwnym razie \"0\"" >}}

{{< mqtt-topic topic="{PlantId}/signals/ToGridHigherEqThanX" direction="publish" qos="0" description="\"1\" jeśli eksport do sieci ≥ X, w przeciwnym razie \"0\"" >}}

## Dane JSON

{{< mqtt-topic topic="{PlantId}/signals/data" direction="publish" qos="0" description="Dane prognozy w formacie JSON" >}}

| Pole | Typ | Opis |
|------|-----|------|
| `SOC` | int | SOC (%) na początku godziny |
| `SellingPrice` | decimal | Bieżąca cena sprzedaży (brak jeśli nie ma ceny) |
| `PurchasePrice` | decimal | Bieżąca cena zakupu (brak jeśli nie ma ceny) |
| `FromGrid_kWh` | decimal | Prognozowany import z sieci |
| `ToGrid_kWh` | decimal | Prognozowany eksport do sieci |

## Sygnały ładowarki EV

Sygnały wysyłane przez moduł EV. Zewnętrzne programy (np. Home Assistant) mogą subskrybować te tematy, aby włączać lub wyłączać ładowanie EV.

> [!NOTE]
> - Samochód „HomeAssistant EV Car" musi być najpierw dodany w programie
> - Patrz także [SetCar]({{< relref "/mqtt-api/komendy-danych" >}}) — ustawianie parametrów samochodu EV

{{< mqtt-endpoint name="EVCharger_On" topic="{PlantId}/signals/EVCharger_On" direction="publish" description="Włącz ładowarkę EV" >}}
Payload — JSON:

| Pole | Typ | Opis |
|------|-----|------|
| `Name` | string | Nazwa samochodu HomeAssistant EV Car |
| `ChargeSpeedA` | decimal | Prędkość ładowania (A) |
{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="EVCharger_Off" topic="{PlantId}/signals/EVCharger_Off" direction="publish" description="Wyłącz ładowarkę EV" >}}
Payload — JSON:

| Pole | Typ | Opis |
|------|-----|------|
| `Name` | string | Nazwa samochodu HomeAssistant EV Car |
{{< /mqtt-endpoint >}}
