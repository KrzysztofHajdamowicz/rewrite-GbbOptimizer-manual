---
title: "Signalen"
weight: 10
translationKey: "sygnaly"
---

# MQTT-signalen

GbbOptimizer verstuurt elk uur signalen naar externe programma's (bijv. Home Assistant) op basis van de prognose voor het lopende uur.

MQTT-verbindingsparameters (adres, poort, TLS, ClientID) — zie [Requests / Responses]({{< relref "/mqtt-api/requests-responses" >}}).

> [!NOTE]
> - Signalen moeten eerst worden ingeschakeld in de module [Ontladen]({{< relref "/configuration/discharging" >}})
> - Een signaal wordt niet verstuurd als de parameter „X" niet is gedefinieerd (veld leeg)

## Binaire signalen

Een extern programma kan de volgende topics abonneren:

{{< mqtt-topic topic="{PlantId}/signals/SOCHigherEqThanX" direction="publish" qos="0" description="\"1\" als SOC ≥ X, anders \"0\"" >}}

{{< mqtt-topic topic="{PlantId}/signals/SOCLowerEqThanX" direction="publish" qos="0" description="\"1\" als SOC ≤ X, anders \"0\"" >}}

{{< mqtt-topic topic="{PlantId}/signals/SellingPriceHigherEqThanX" direction="publish" qos="0" description="\"1\" als Verkoopprijs ≥ X, anders \"0\"" >}}

{{< mqtt-topic topic="{PlantId}/signals/SellingPriceLowerEqThanX" direction="publish" qos="0" description="\"1\" als Verkoopprijs ≤ X, anders \"0\"" >}}

{{< mqtt-topic topic="{PlantId}/signals/FromGridHigherEqThanX" direction="publish" qos="0" description="\"1\" als import uit het net ≥ X, anders \"0\"" >}}

{{< mqtt-topic topic="{PlantId}/signals/ToGridHigherEqThanX" direction="publish" qos="0" description="\"1\" als export naar het net ≥ X, anders \"0\"" >}}

## JSON-gegevens

{{< mqtt-topic topic="{PlantId}/signals/data" direction="publish" qos="0" description="Prognosegegevens in JSON-formaat" >}}

| Veld | Type | Beschrijving |
|------|-----|------|
| `SOC` | int | SOC (%) aan het begin van het uur |
| `SellingPrice` | decimal | Huidige verkoopprijs (ontbreekt als er geen prijs is) |
| `PurchasePrice` | decimal | Huidige inkoopprijs (ontbreekt als er geen prijs is) |
| `FromGrid_kWh` | decimal | Voorspelde import uit het net |
| `ToGrid_kWh` | decimal | Voorspelde export naar het net |

## EV-ladersignalen

Signalen verzonden door de EV-module. Externe programma's (bijv. Home Assistant) kunnen deze topics abonneren om het laden van een EV in of uit te schakelen.

> [!NOTE]
> - Een „HomeAssistant EV Car" moet eerst in het programma worden toegevoegd
> - Zie ook [SetCar]({{< relref "/mqtt-api/data-commands" >}}) voor het instellen van EV-autoparameters

{{< mqtt-endpoint name="EVCharger_On" topic="{PlantId}/signals/EVCharger_On" direction="publish" description="EV-lader inschakelen" >}}
Payload — JSON:

| Veld | Type | Beschrijving |
|------|------|--------------|
| `Name` | string | Naam van de HomeAssistant EV Car |
| `ChargeSpeedA` | decimal | Laadsnelheid (A) |
{{< /mqtt-endpoint >}}

{{< mqtt-endpoint name="EVCharger_Off" topic="{PlantId}/signals/EVCharger_Off" direction="publish" description="EV-lader uitschakelen" >}}
Payload — JSON:

| Veld | Type | Beschrijving |
|------|------|--------------|
| `Name` | string | Naam van de HomeAssistant EV Car |
{{< /mqtt-endpoint >}}
