---
title: "GbbConnect2 Addon"
weight: 15
translationKey: "gbbconnect2-addon"
---

# GbbConnect2 — Home Assistant Addon

{{< glossary "GbbConnect2" >}} is available as a **Home Assistant addon**, allowing you to run it directly in HA without a separate Windows PC or Docker container.

The addon runs the GbbConnect2Console application and connects the inverter to GbbOptimizer via {{< glossary "ModbusInMqtt" >}}.

## Requirements

- **Home Assistant OS** or **Home Assistant Supervised** (Supervisor required)
- An active GbbOptimizer account with a **GbbConnect2** type installation
- A hybrid inverter with a datalogger (WiFi or Ethernet)
- A **fixed IP address** for the datalogger on the local network

## Installation

### 1. Add the repository

Click the button below to automatically add the repository to Home Assistant:

[![Add repository to Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FKrzysztofHajdamowicz%2Fgbbconnect2-ha-addon)

Or manually:

1. In Home Assistant, go to **Settings** -> **Add-ons** -> **Add-on Store**
2. Click the menu (⋮) in the top right corner -> **Repositories**
3. Add the repository URL:
   ```
   https://github.com/KrzysztofHajdamowicz/gbbconnect2-ha-addon
   ```
4. Click **Add**

### 2. Install the addon

1. In the Add-on Store, search for **GbbConnect2**
2. Click **Install**
3. Wait for the installation to complete

## Configuration

Before starting the addon, prepare the data from GbbOptimizer — see [GbbConnect2 configuration]({{< relref "/installation/connection-methods/gbbconnect2" >}}) (steps 2–5).

In the addon's **Configuration** tab, fill in the fields:

| Field | Description |
|-------|-------------|
| `plant_name` | Installation name (as in GbbOptimizer) |
| `plant_driver_no` | Driver type: `0` = SolarmanV5 (WiFi), `1` = ModBusTCP (Ethernet) |
| `plant_address_ip` | Datalogger IP address on the local network |
| `plant_port_no` | Datalogger port (usually `8899`) |
| `plant_serial_number` | **Datalogger** serial number (not the inverter!) |
| `gbboptimizer_plant_id` | {{< glossary "PlantId" >}} from GbbOptimizer |
| `gbboptimizer_plant_token` | {{< glossary "PlantToken" >}} from GbbOptimizer |
| `gbboptimizer_mqtt_address` | MQTT server address — see [MQTT Servers]({{< relref "/references/mqtt-servers" >}}) |
| `gbboptimizer_mqtt_port` | MQTT port (usually `8883`) |
| `server_autostart` | Automatic server start (recommended: `true`) |

> [!WARNING]
> The datalogger **must have a fixed IP address** on the local network. Set a DHCP reservation on your router.

> [!NOTE]
> The serial number is the **datalogger's** serial number, not the inverter's. Common formats: 17xxxxxxx, 21xxxxxxx, 40xxxxxxx. You can find it using the Windows version of GbbConnect2 (**Search for Inverters** function).

## Starting

1. Go to the addon's **Info** tab
2. Click **Start**
3. Check the **Log** tab — wait for a connection established message
4. In GbbOptimizer, verify that data from the inverter is being received

> [!NOTE]
> The addon should run **24/7** so that GbbOptimizer can collect data and send commands to the inverter.

## Troubleshooting

- **Cannot connect to inverter** — check the datalogger IP address, port, and serial number. Make sure HA can reach the datalogger on the network.
- **Cannot connect to MQTT** — verify the {{< glossary "PlantId" >}}, {{< glossary "PlantToken" >}}, and MQTT server address. Check that port 8883 is not blocked by a firewall.
- **Authentication error** — generate a new token in GbbOptimizer and update the addon configuration.

Enable `is_verbose_log`, `is_driver_log`, and `is_driver_log2` in the configuration for detailed diagnostic logs.
