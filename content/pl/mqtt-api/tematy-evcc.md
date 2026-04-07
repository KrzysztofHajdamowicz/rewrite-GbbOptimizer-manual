---
title: "Tematy EVCC"
weight: 60
translationKey: "tematy-evcc"
---

# Tematy MQTT dla EVCC

Integracja GbbOptimizer z [evcc.io](https://evcc.io/) przez MQTT.

## Konfiguracja

W brokerze Mosquitto (lub HA) stwórz plik konfiguracji bridge:

```
connection GbbOptimizer_<PlantId>
remote_username <PlantId>
remote_password <PlantToken>
address <adres MQTT>:8883
bridge_capath /etc/ssl/certs
topic # both 2 evcc/loadpoints/ <PlantId>/evcc/site/loadpoints/
```

Adresy serwerów MQTT — patrz [serwery MQTT]({{< relref "/referencje/serwery-mqtt" >}}).

## Dane z EVCC do GbbOptimizer

{{< mqtt-topic topic="{PlantId}/evcc/site/statistic/total/chargedKWh" direction="subscribe" description="Całkowita energia pobrana przez ładowarkę (kWh)" >}}

## Komendy z GbbOptimizer do EVCC

{{< mqtt-topic topic="{PlantId}/evcc/loadpoints/{chargerId}/mode" direction="publish" description="Tryb ładowania: off lub now" >}}

{{< mqtt-topic topic="{PlantId}/evcc/loadpoints/{chargerId}/maxCurrent" direction="publish" description="Maksymalny prąd ładowania" >}}

{{< mqtt-topic topic="{PlantId}/evcc/loadpoints/{chargerId}/connected" direction="publish" description="Status połączenia ładowarki" >}}
