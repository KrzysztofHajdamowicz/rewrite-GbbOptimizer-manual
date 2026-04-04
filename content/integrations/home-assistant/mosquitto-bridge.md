---
title: "Mosquitto Bridge"
weight: 10
---

# Home Assistant: Mosquitto Bridge Setup

GbbOptimizer connects to Home Assistant through an MQTT bridge using the Mosquitto broker.

## Setup Steps

1. Add a new plant by selecting **"Add new plant with HomeAssistant"**
2. Choose the connection device type for your inverter
3. Save the plant configuration, then **edit** it to generate {{< glossary "PlantId" >}} and {{< glossary "PlantToken" >}}
4. In Home Assistant's **Mosquitto broker** add-on settings, activate **Customize** and set the folder to: `mosquitto`
5. Create the configuration file at `/share/mosquitto/GbbOptimizer.conf`

## Bridge Configuration

```ini
connection GbbOptimizer_<plantID>
remote_username <plantID>
remote_password <plantToken>
address <mqtt_address>:8883
bridge_capath /etc/ssl/certs
topic # both 2 "" <plantID>/
```

Replace:
- `<plantID>` — your numeric Plant ID
- `<plantToken>` — your Plant Token
- `<mqtt_address>` — your [MQTT server address]({{< relref "/reference/mqtt-servers" >}})

## MQTT Explorer Connection

To debug MQTT messages, connect MQTT Explorer with:

| Parameter | Value |
|-----------|-------|
| Encryption (TLS) | Enabled |
| Host | `gbboptimizerX-mqtt.gbbsoft.pl` (X = server number) |
| Port | 8883 |
| Username | `<plantId>` |
| Password | `<plantToken>` |
| Topic filter | `<plantId>/#` |
| Client ID | Must end with `_<plantId>` |
