---
title: "Common Errors"
weight: 60
translationKey: "najczestsze-bledy"
---

# Common Errors

A list of the most frequently encountered error messages in GbbOptimizer, their causes, and possible solutions.

## Solarman

| Message | Description |
|---------|-------------|
| `SolarmanError: Solarman timeout!` | Solarman cannot send data to the inverter. Check the local network. |
| `Solarman error: 2101040-device not found` | The inverter is not sending data to Solarman. Check the inverter's network connection. |
| `Response status code: 503 / 500 / 504` | The Solarman API is not working correctly. Problem on Solarman's side — wait and try again. |

## DeyeCloud

| Message | Description |
|---------|-------------|
| `DeyeCloud error: timeout` | DeyeCloud cannot send data to the inverter. Check the local network. |
| `DeyeCloud error: 2104006-device offline` | The inverter is not sending data to DeyeCloud. Check the inverter's network connection. |
| `DeyeCloud error: 2101042-auth no operation permission` | Insufficient permissions for the DeyeCloud account (e.g. account granted by an installer). Contact the installer to obtain full permissions. |

## GbbConnect2

| Message | Description |
|---------|-------------|
| `Mqtt to GbbConnect2: timeout!` | GbbOptimizer cannot connect to the local {{< glossary "GbbConnect2" >}}. Check whether GbbConnect2 is running. |
| `GbbConnect2Error: Connection timed out 192.168.x.xx:8899` | {{< glossary "GbbConnect2" >}} cannot connect to the Deye dongle. Check whether the dongle is on the network. |

## Victron

| Message | Description |
|---------|-------------|
| `Victron Mqtt: timeout! (15 sec)` | GbbOptimizer cannot connect to Cerbo through Victron's MQTT servers. Check the local network and remote access in {{< glossary "VRM" >}}. |
| `Error during checking whether Schedules reached Cerbo successfully` | ESS schedules did not reach Cerbo. Check Cerbo's internet connection. |

## Energy Prices

| Message | Source | Description |
|---------|--------|-------------|
| `Get Prices: The SSL connection could not be established` | ENTSO-E | The ENTSO-E price API is not working. Problem on the provider's side. |
| `Get Prices: Proba polaczenia nie powiodla sie` | ENTSO-E | ENTSO-E API unavailable. |
| `Get Prices: HTTP POST ... Gateway timeout / 502 Bad Gateway` | Tibber | The Tibber price API is not working. |
| `Get Prices: Response status code: 502 (Bad Gateway)` | AU Amber | The Amber price API is not working. |

## Other

| Message | Source | Description |
|---------|--------|-------------|
| `Solcast.com: Too many requests` | Solcast | The 10 daily request limit for Solcast.com has been reached. Wait until midnight. |
| `ERROR from Cache: Response status code: 500` | Pstryk | Error on the Pstryk API side. |
| `B0220-System function downgrade` | Hinen | The Hinen API is being updated. Wait for the update to finish. |

> [!NOTE]
> Error messages are sent by email from the program. Most "timeout" and "device offline" errors are related to local network issues — check the inverter and router connection.
