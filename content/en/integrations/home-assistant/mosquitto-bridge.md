---
title: "Mosquitto Bridge"
weight: 10
translationKey: "mosquitto-bridge"
---

# Mosquitto Bridge

For GbbOptimizer to communicate with Home Assistant, you need to configure a bridge between the local Mosquitto broker in HA and the GbbOptimizer MQTT server.

## Requirements

- Home Assistant with the **Mosquitto broker** add-on installed
- An active installation in GbbOptimizer with an assigned {{< glossary "PlantId" >}} and {{< glossary "PlantToken" >}}
- MQTT server address — see [MQTT Servers]({{< relref "/referencje/serwery-mqtt" >}})

## Step-by-Step Configuration

### 1. Enable the configuration folder in Mosquitto

In Home Assistant go to **Settings** -> **Add-ons** -> **Mosquitto broker** -> **Configuration**.

Activate the **Customize** option and set the folder to:

```
mosquitto
```

### 2. Create the bridge configuration file

Create the file `/share/mosquitto/GbbOptimizer.conf` with the following content:

```conf
connection GbbOptimizer_<PlantId>
remote_username <PlantId>
remote_password <PlantToken>
address <mqtt-server-address>:8883
bridge_capath /etc/ssl/certs
topic # both 2 ha_gbb/ <PlantId>/ha_gbb/
```

Replace:
- `<PlantId>` — with your {{< glossary "PlantId" >}}
- `<PlantToken>` — with your {{< glossary "PlantToken" >}}
- `<mqtt-server-address>` — with the server address from the [MQTT Servers]({{< relref "/referencje/serwery-mqtt" >}}) table

### 3. Restart Mosquitto

After saving the file, restart the Mosquitto broker add-on in Home Assistant.

> [!NOTE]
> The connection uses port **8883** (MQTT over TLS). CA certificates are taken from `/etc/ssl/certs` — no need to add your own.

## How the Bridge Works

The `topic` line in the configuration maps topics:

| Direction | Local topic (HA) | Remote topic (GbbOptimizer) |
|-----------|------------------|-----------------------------|
| HA -> GbbOptimizer | `ha_gbb/#` | `<PlantId>/ha_gbb/#` |
| GbbOptimizer -> HA | `ha_gbb/#` | `<PlantId>/ha_gbb/#` |

This means:
- Sensor data sent to `ha_gbb/sensor` in HA reaches GbbOptimizer as `<PlantId>/ha_gbb/sensor`
- Commands from GbbOptimizer (e.g. `<PlantId>/ha_gbb/Start_Charge`) appear in HA as `ha_gbb/Start_Charge`

## Bridge for SolarAssistant

If you use {{< glossary "SolarAssistant" >}}, change the `topic` line to:

```conf
topic # both 2 solar_assistant/ <PlantId>/solar_assistant/
```

More information: [SolarAssistant]({{< relref "/integracje/home-assistant/solar-assistant" >}})

## Bridge for evcc

If you are integrating with evcc, add a separate `topic` line:

```conf
topic # both 2 evcc/loadpoints/ <PlantId>/evcc/site/loadpoints/
```

More information: [evcc]({{< relref "/integracje/evcc" >}})

> [!WARNING]
> Make sure that {{< glossary "PlantId" >}} and {{< glossary "PlantToken" >}} are correct. Incorrect credentials will cause a connection failure — check the Mosquitto logs in HA.
