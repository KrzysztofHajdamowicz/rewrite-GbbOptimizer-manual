---
title: "MQTT API Reference"
weight: 40
bookCollapseSection: true
---

# MQTT API Reference

GbbOptimizer uses MQTT as its primary communication protocol. This section provides a complete reference for all MQTT topics, commands, and response formats.

## Connection

| Parameter | Value |
|-----------|-------|
| **Port** | `8883` (TLS) |
| **Username** | Your {{< glossary "PlantId" >}} |
| **Password** | Your {{< glossary "PlantToken" >}} |
| **Client ID** | Must end with `_{PlantId}` |

See [MQTT Server Addresses]({{< relref "/reference/mqtt-servers" >}}) for the server hostname matching your plant instance.

## Topic Structure

All topics are prefixed with your `{PlantId}`. The general pattern is:

```
{PlantId}/category/subcategory
```

## Sections

| Section | Description |
|---------|-------------|
| [Signals]({{< relref "signals" >}}) | Outbound signals (SOC thresholds, price alerts) |
| [Request / Response]({{< relref "request-response" >}}) | Query API for forecast and history data |
| [Data Commands]({{< relref "data-commands" >}}) | Modify prices, loads, optimizer parameters |
| [HA Integration Topics]({{< relref "ha-integration-topics" >}}) | Home Assistant sensor input and command output |
| [ModbusInMqtt]({{< relref "modbus-in-mqtt" >}}) | GbbConnect2 protocol for direct inverter control |
| [Evcc Topics]({{< relref "evcc-topics" >}}) | EV charger integration via evcc.io |
