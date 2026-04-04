---
title: "Solarman"
weight: 10
---

# Solarman Connection

{{< badge "deprecated" >}}

> **Due to ongoing issues with Solarman, it is recommended to use [DeyeCloud]({{< relref "deye-cloud" >}}) as an alternative or additional connection method.**

Solarman is a cloud service that collects data from inverter WiFi dongles. GbbOptimizer can connect through the Solarman API to read data and send commands.

## Known Issues

- Connection timeouts when the inverter fails to transmit data to Solarman
- Local network connectivity problems causing data gaps
- Rate limiting and API availability issues

## Recommendation

Consider switching to:
- **[DeyeCloud]({{< relref "deye-cloud" >}})** — for cloud-based connection
- **[GbbConnect2]({{< relref "gbb-connect2" >}})** — for local, reliable connection
