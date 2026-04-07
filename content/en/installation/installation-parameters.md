---
title: "Installation parameters"
weight: 10
translationKey: "parametry-instalacji"
---

# Installation parameters

Below are all the configuration parameters for an installation in GbbOptimizer, grouped by topic.

## Type

| Parameter | Unit | Description |
|-----------|------|-------------|
| Type | — | Type of connection to the inverter (Victron, Solarman, GbbConnect2, DongleDirect, SolarAssistant) |
| Time slots per day | — | Number of time slots per day. In Poland, 60 slots apply for individual customers |

## Installation

| Parameter | Unit | Description |
|-----------|------|-------------|
| Name | — | Unique installation name within the account |
| Time zone | — | Time zone of the installation location |
| Maximum grid import power | kW | Grid connection parameter — maximum power drawn from the grid |
| Maximum grid export power | kW | Grid connection parameter — maximum power fed into the grid |
| What % of PV is connected on the DC side? | % | `0%` — all PV connected to AC. `100%` — all PV connected to DC |
| Latitude/Longitude | — | Geographic location of the installation. Used by the Meteo and PV Forecast modules |

## Price sources

| Parameter | Description |
|-----------|-------------|
| Purchase: Tariff for purchase prices | Source of imported energy purchase prices |
| Transmission: Tariff for transmission prices | Source of transmission (transport) prices. Empty = 0 |
| Sale: Tariff for sale prices | Source of imported energy sale prices |

Details of price formulas — in the [Prices]({{< relref "/configuration/prices" >}}) module.

## Battery

| Parameter | Unit | Description |
|-----------|------|-------------|
| Battery capacity (gross) | kWh | Total battery capacity |
| Average battery voltage | V | Used for converting W from A and A from W. Can be approximate |
| Minimum battery {{< glossary "SOC" >}} | % | {{< glossary "MinSOC" >}} — hard reserve. Below this value, energy is used only in emergency situations |
| Maximum inverter charging power (DC) | kW | Maximum charging power on the DC side |
| Maximum inverter discharge power (DC) | kW | Maximum discharge power on the DC side |
| Maximum BMS battery charging power (DC) | kW | Relevant when different from inverter power and PV connected on the DC side |
| Maximum BMS battery discharge power (DC) | kW | Relevant when different from inverter power and PV connected on the DC side |
| Battery charging losses from grid | % | Charging losses (including the BMS SOC accounting method) |
| Battery discharge losses to grid/consumption | % | Discharge losses (including the BMS SOC accounting method) |

## Victron

{{< badge "victron-only" >}}

| Parameter | Description |
|-----------|-------------|
| VRM Portal Id | {{< glossary "VRM" >}} portal identifier. Found in: Cerbo → Settings → VRM Online Portal → VRM Portal ID |
| Installation Id | Number in the VRM page address |
| VRM Login/email | Login to the VRM portal |
| VRM Password | Password to the VRM portal (if not using 2FA) |
| VRM Token | Token for two-factor authentication (2FA) |
| VRM Instance number of VE.Bus System device | Normally the inverter has number `276`, but sometimes another |

## Solarman / DeyeCloud

| Parameter | Applies to | Description |
|-----------|-----------|-------------|
| Login method | — | Email, login, or phone number |
| Email / Login / Phone number | — | Login credentials for Solarman/DeyeCloud |
| Password | — | Password for Solarman/DeyeCloud |
| Remember login credentials | — | Automatic reconnection. Without this, manual login is required (notification email) |
| Select inverter SerialNo | — | After connecting, select the inverter serial number |
| Inverter type | — | Inverter type. **Must not be wrong!** Incorrect selection and data transmission requires a factory reset of the inverter |
| Deye: Add MI/GEN production to PV production | {{< badge "deye-only" >}} | On some firmware versions, production from the GEN input must be added manually |
| Deye: No CT, so don't try to set ZeroToCT | {{< badge "deye-only" >}} | Without CT, the program falls back to ZeroToLoad instead of ZeroToCT after discharge ends |
| Deye: Set inverter time at midnight | {{< badge "deye-only" >}} | Synchronizes the inverter clock at midnight |
| SOC data from HomeAssistant/SolarAssistant | — | Do not fetch {{< glossary "SOC" >}} from the inverter — it will be provided by HA/SA |
| GridImport/GridExport data fetched from | — | Do not fetch GridImport/GridExport from the inverter — data from HomeAssistant or IoT meter |
| Consumption data from HomeAssistant/SolarAssistant | — | Do not fetch Consumption from the inverter — it will be provided by HA/SA |

### Backup connection — DeyeCloud

Applies only to Solarman-type installations. Details on the [DeyeCloud]({{< relref "/installation/connection-methods/deye-cloud" >}}) page.

| Parameter | Description |
|-----------|-------------|
| How the backup connection should be used | **Disabled** / **Enabled** (on Solarman error) / **Backup only** (always DeyeCloud) |
| Login method / Email / Password | Login credentials for DeyeCloud |
| Remember login credentials | Automatic re-login to DeyeCloud |
| Select inverter SerialNo | After connecting, select the serial number |

## Inverter parameters

{{< badge "deye-only" >}}

| Parameter | Description |
|-----------|-------------|
| Control via V, not SOC | Inverter uses voltage (V) instead of SOC in TimeOfUse |
| Also calculate current SOC from V | Calculate current SOC based on voltage. If unchecked — SOC is fetched from the inverter |

## GbbShunt

{{< badge "deye-only" >}} Applies only to Solarman + Deye installations. Details on the [Solarman]({{< relref "/installation/connection-methods/solarman" >}}) page.

| Parameter | Unit | Description |
|-----------|------|-------------|
| Enabled | — | Activates the GbbShunt module |
| Minimum battery SOC / V when SOC → MinSOC | V | Voltage at which SOC will be set to {{< glossary "MinSOC" >}} |
| Maximum battery SOC / V when SOC → MaxSOC | V | Voltage at which SOC will be set to {{< glossary "MaxSOC" >}} |
| Charging + discharging losses | % | Percentage of energy excluded from calculations |
| V during battery charging | V | Voltage sent to TimeOfUse instead of the value calculated from the target SOC |
| V during battery discharging | V | Voltage sent to TimeOfUse instead of the value calculated from the target SOC |

## Technical support

| Parameter | Unit | Description |
|-----------|------|-------------|
| Send email after connection loss | hours | After how many hours without connection the program sends a notification. Empty = no notifications |
| Send email with log errors | — | Sends a log error summary every hour |
| Additional email addresses | — | Additional addresses for notifications. Useful for installers, so the client also receives emails |
| Share installation with technical support | — | Gives technical support access to your installation. Contact on Discord first |
