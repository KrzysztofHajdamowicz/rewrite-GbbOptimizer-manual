---
title: "Plant Parameters"
weight: 10
---

# Plant Parameters

The Plant Parameters module contains the core settings for your solar installation.

## Basic Settings

| Parameter | Description |
|-----------|-------------|
| Plant name | Descriptive name for your installation |
| Timezone | Your local timezone |
| Location | Geographic coordinates (latitude/longitude) for PV forecasting |
| Max buy power from grid (W) | Maximum power your grid connection allows for import |
| Max sell power to grid (W) | Maximum power your grid connection allows for export |

## Battery Settings

| Parameter | Description |
|-----------|-------------|
| Battery kWh (brutto) | Total battery capacity in kWh |
| Average voltage | Battery nominal voltage |
| {{< glossary "MinSOC" >}} | Minimum allowed State of Charge |
| Charge power limit (W) | Maximum charging power for the inverter |
| Discharge power limit (W) | Maximum discharging power for the inverter |

## Connection Configuration

Depending on your plant type, you will need to configure connection credentials:

- **Victron** — VRM Portal ID, login email, and password
- **Solarman / DeyeCloud** — Account credentials and device serial number
- **GbbConnect2** — PlantId and PlantToken (generated after saving the plant)
- **Home Assistant** — MQTT bridge configuration (see [Mosquitto Bridge]({{< relref "/integrations/home-assistant/mosquitto-bridge" >}}))

## PV Configuration

- **PV production split** — Allocate production between DC and AC sides
- **Loss calculations** — Configure charging/discharging conversion losses

## Monitoring

- **Email notifications** — Receive alerts on connection failures and errors
- **Share with support** — Grant the developer access to your plant for troubleshooting

## Advanced Options

- **Backup connection** — Configure a secondary connection method in case the primary fails
- **{{< glossary "Battery Full Date" >}}** — Set days of the month for 100% SOC targets (e.g., `1, 15`)
