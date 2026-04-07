---
title: "evcc"
weight: 20
translationKey: "evcc"
---

# Integration with evcc

[evcc.io](https://evcc.io) is software for intelligent electric vehicle charging. GbbOptimizer can communicate with it via MQTT to coordinate EV charging with home battery optimization.

## Requirements

- A working evcc installation
- Local MQTT broker (Mosquitto in Home Assistant or standalone)
- Configured [Mosquitto Bridge]({{< relref "/integrations/home-assistant/mosquitto-bridge" >}})

## Bridge Configuration

In the Mosquitto configuration file (`/share/mosquitto/GbbOptimizer.conf`) add `topic` lines for evcc:

```conf
connection GbbOptimizer_<PlantId>
remote_username <PlantId>
remote_password <PlantToken>
address <mqtt-server-address>:8883
bridge_capath /etc/ssl/certs
topic # both 2 evcc/loadpoints/ <PlantId>/evcc/site/loadpoints/
```

## MQTT Topics

### Data from evcc (evcc -> GbbOptimizer)

| Topic | Description |
|-------|-------------|
| `{PlantId}/evcc/site/statistic/total/chargedKWh` | Total energy charged to EV (kWh) |

### Commands from GbbOptimizer (GbbOptimizer -> evcc)

| Topic | Payload | Description |
|-------|---------|-------------|
| `{PlantId}/evcc/loadpoints/{chargerId}/mode` | `off` or `now` | Enable/disable charging |
| `{PlantId}/evcc/loadpoints/{chargerId}/maxCurrent` | number (A) | Maximum charging current |
| `{PlantId}/evcc/loadpoints/{chargerId}/connected` | `true`/`false` | Charger connection status |

Where `{chargerId}` is the charging point identifier in evcc.

> [!NOTE]
> evcc must be configured to communicate via MQTT. Check the [evcc documentation](https://docs.evcc.io/docs/reference/configuration/messaging#mqtt) in the MQTT section.
