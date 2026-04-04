---
title: "Inverter Connection Comparison"
weight: 30
---

# Inverter Connection Comparison

Comparison of the four primary connection methods for Deye inverters.

| Feature | Solarman/DeyeCloud | GbbConnect2 | DongleDirect | Home Assistant |
|---------|-------------------|-------------|--------------|----------------|
| Cloud dependency | Yes | No (local) | Partial | No (local) |
| Disconnection risk | Medium | Low | Low | Low |
| Software required | None | GbbConnect2 (Windows/Docker) | None | Home Assistant + Mosquitto |
| Parameter modification | Full | Full (Modbus) | Full | Via MQTT bridge |
| Data relay to cloud | Built-in | No | Optional | No |
| Setup complexity | Low | Medium | Medium | High |

> [!WARNING]
> **Solarman** is experiencing ongoing reliability issues. Consider [DeyeCloud]({{< relref "/integrations/connection-methods/deye-cloud" >}}) or [GbbConnect2]({{< relref "/integrations/connection-methods/gbb-connect2" >}}) as alternatives.
