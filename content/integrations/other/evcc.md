---
title: "Evcc.io"
weight: 10
---

# Evcc.io Integration

GbbOptimizer integrates with [evcc.io](https://evcc.io) for EV charger control via MQTT.

## Setup

You need a Mosquitto broker or Home Assistant's MQTT service. Configure the MQTT bridge as described in [Mosquitto Bridge]({{< relref "/integrations/home-assistant/mosquitto-bridge" >}}).

## MQTT Topics

### From evcc → GbbOptimizer

| Topic | Description |
|-------|-------------|
| `<plantId>/evcc/site/statistic/total/chargedKWh` | Total energy charged |

### From GbbOptimizer → evcc

| Topic | Description |
|-------|-------------|
| `<plantId>/evcc/loadpoints/{chargerId}/mode` | Charger mode: `"off"` or `"now"` |
| `<plantId>/evcc/loadpoints/{chargerId}/maxCurrent` | Maximum charging current |
| `<plantId>/evcc/loadpoints/{chargerId}/connected` | Connection status |

See also: [Evcc MQTT Topics]({{< relref "/mqtt-api/evcc-topics" >}}) for the full API reference.
