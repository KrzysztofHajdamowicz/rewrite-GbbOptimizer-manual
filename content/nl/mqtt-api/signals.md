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
