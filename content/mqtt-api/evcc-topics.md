---
title: "Evcc Topics"
weight: 60
---

# Evcc MQTT Topics

MQTT topics for EV charger integration via [evcc.io](https://evcc.io).

## From evcc → GbbOptimizer

{{< mqtt-topic topic="{PlantId}/evcc/site/statistic/total/chargedKWh" direction="subscribe" description="Total energy charged by the EV charger (kWh)" >}}

## From GbbOptimizer → evcc

{{< mqtt-topic topic="{PlantId}/evcc/loadpoints/{chargerId}/mode" direction="publish" description="Set charger mode: \"off\" or \"now\"" >}}

{{< mqtt-topic topic="{PlantId}/evcc/loadpoints/{chargerId}/maxCurrent" direction="publish" description="Set maximum charging current (A)" >}}

{{< mqtt-topic topic="{PlantId}/evcc/loadpoints/{chargerId}/connected" direction="publish" description="Vehicle connection status" >}}

## Topic Pattern

Replace `{chargerId}` with the specific charger identifier configured in evcc.

The topic mapping uses the pattern: `<plantId>/evcc/loadpoints/{chargerId}/`
