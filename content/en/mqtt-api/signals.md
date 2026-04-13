---
title: "Signals"
weight: 10
translationKey: "sygnaly"
---

# MQTT Signals

GbbOptimizer sends signals to external programs (e.g. Home Assistant) every hour, based on the forecast for the current hour.

MQTT connection parameters (address, port, TLS, ClientID) — see [Request / Response]({{< relref "/mqtt-api/request-response" >}}).

> [!NOTE]
> - Signals must first be enabled in the [Discharge]({{< relref "/configuration/discharging" >}}) module
> - A given signal is not sent if the "X" parameter is not defined (field empty)

## Binary Signals

External programs can subscribe to the following topics:

{{< mqtt-topic topic="{PlantId}/signals/SOCHigherEqThanX" direction="publish" qos="0" description="\"1\" if SOC ≥ X, otherwise \"0\"" >}}

{{< mqtt-topic topic="{PlantId}/signals/SOCLowerEqThanX" direction="publish" qos="0" description="\"1\" if SOC ≤ X, otherwise \"0\"" >}}

{{< mqtt-topic topic="{PlantId}/signals/SellingPriceHigherEqThanX" direction="publish" qos="0" description="\"1\" if Selling Price ≥ X, otherwise \"0\"" >}}

{{< mqtt-topic topic="{PlantId}/signals/SellingPriceLowerEqThanX" direction="publish" qos="0" description="\"1\" if Selling Price ≤ X, otherwise \"0\"" >}}

{{< mqtt-topic topic="{PlantId}/signals/FromGridHigherEqThanX" direction="publish" qos="0" description="\"1\" if grid import ≥ X, otherwise \"0\"" >}}

{{< mqtt-topic topic="{PlantId}/signals/ToGridHigherEqThanX" direction="publish" qos="0" description="\"1\" if grid export ≥ X, otherwise \"0\"" >}}

## JSON Data

{{< mqtt-topic topic="{PlantId}/signals/data" direction="publish" qos="0" description="Forecast data in JSON format" >}}

| Field | Type | Description |
|-------|------|-------------|
| `SOC` | int | SOC (%) at the start of the hour |
| `SellingPrice` | decimal | Current selling price (absent if no price) |
| `PurchasePrice` | decimal | Current purchase price (absent if no price) |
| `FromGrid_kWh` | decimal | Forecast grid import |
| `ToGrid_kWh` | decimal | Forecast grid export |

## EV Charger Signals

Signals sent by the EV module. External programs (e.g. Home Assistant) can subscribe to these topics to switch EV charging on or off.

> [!NOTE]
> - A "HomeAssistant EV Car" must be added in the program first
> - See also [SetCar]({{< relref "/mqtt-api/data-commands" >}}) for setting EV car parameters

{{< mqtt-endpoint name="EVCharger_On" topic="{PlantId}/signals/EVCharger_On" direction="publish" description="Switch on EV charger" >}}
Payload — JSON:

| Field | Type | Description |
|-------|------|-------------|
| `Name` | string | Name of the HomeAssistant EV Car |
| `ChargeSpeedA` | decimal | Charge speed (A) |
{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="EVCharger_Off" topic="{PlantId}/signals/EVCharger_Off" direction="publish" description="Switch off EV charger" >}}
Payload — JSON:

| Field | Type | Description |
|-------|------|-------------|
| `Name` | string | Name of the HomeAssistant EV Car |
{{< /mqtt-endpoint >}}
