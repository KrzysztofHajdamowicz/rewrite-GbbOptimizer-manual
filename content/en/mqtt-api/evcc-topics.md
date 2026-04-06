---
title: "EVCC Topics"
weight: 60
translationKey: "tematy-evcc"
---

# MQTT Topics for EVCC

GbbOptimizer integration with [evcc.io](https://evcc.io/) via MQTT.

## Configuration

In the Mosquitto (or HA) broker, create a bridge configuration file:

```
connection GbbOptimizer_<PlantId>
remote_username <PlantId>
remote_password <PlantToken>
address <MQTT address>:8883
bridge_capath /etc/ssl/certs
topic # both 2 evcc/loadpoints/ <PlantId>/evcc/site/loadpoints/
```

MQTT server addresses — see [MQTT servers]({{< relref "/references/mqtt-servers" >}}).

## Data from EVCC to GbbOptimizer

{{< mqtt-topic topic="{PlantId}/evcc/site/statistic/total/chargedKWh" direction="subscribe" description="Total energy consumed by the charger (kWh)" >}}

## Commands from GbbOptimizer to EVCC

{{< mqtt-topic topic="{PlantId}/evcc/loadpoints/{chargerId}/mode" direction="publish" description="Charging mode: off or now" >}}

{{< mqtt-topic topic="{PlantId}/evcc/loadpoints/{chargerId}/maxCurrent" direction="publish" description="Maximum charging current" >}}

{{< mqtt-topic topic="{PlantId}/evcc/loadpoints/{chargerId}/connected" direction="publish" description="Charger connection status" >}}
