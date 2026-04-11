---
title: "EVCC-topics"
weight: 60
translationKey: "tematy-evcc"
---

# MQTT-topics voor EVCC

Integratie van GbbOptimizer met [evcc.io](https://evcc.io/) via MQTT.

## Configuratie

Maak in de Mosquitto-broker (of HA) een bridge-configuratiebestand:

```
connection GbbOptimizer_<PlantId>
remote_username <PlantId>
remote_password <PlantToken>
address <MQTT-adres>:8883
bridge_capath /etc/ssl/certs
topic # both 2 evcc/loadpoints/ <PlantId>/evcc/site/loadpoints/
```

MQTT-serveradressen — zie [MQTT-servers]({{< relref "/references/mqtt-servers" >}}).

## Gegevens van EVCC naar GbbOptimizer

{{< mqtt-topic topic="{PlantId}/evcc/site/statistic/total/chargedKWh" direction="subscribe" description="Totale door de lader opgenomen energie (kWh)" >}}

## Commando's van GbbOptimizer naar EVCC

{{< mqtt-topic topic="{PlantId}/evcc/loadpoints/{chargerId}/mode" direction="publish" description="Laadmodus: off of now" >}}

{{< mqtt-topic topic="{PlantId}/evcc/loadpoints/{chargerId}/maxCurrent" direction="publish" description="Maximale laadstroom" >}}

{{< mqtt-topic topic="{PlantId}/evcc/loadpoints/{chargerId}/connected" direction="publish" description="Verbindingsstatus van de lader" >}}
