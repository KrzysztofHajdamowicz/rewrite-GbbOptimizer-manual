---
title: "GbbConnect2"
weight: 30
---

# GbbConnect2

{{< glossary "GbbConnect2" >}} is a local software application that connects your inverter directly to GbbOptimizer via the {{< glossary "ModbusInMqtt" >}} protocol, bypassing cloud services.

## Setup

1. Download and install GbbConnect2 from GitHub
2. Create a new plant in GbbOptimizer with type **"Plant with GbbConnect2"**
3. Generate a new token — record the {{< glossary "PlantId" >}} and {{< glossary "PlantToken" >}}
4. In GbbConnect2, create a plant and select **"SolarmanV5"**
5. Use **"Search for Inverters"** to find your inverter's IP and serial number
6. Enter the inverter logger IP address and serial number in the Plants tab
7. Input PlantId and PlantToken in the GbbOptimizer section
8. Configure the MQTT server address (see [MQTT Servers]({{< relref "/reference/mqtt-servers" >}}))
9. Enable **"Start server after program starts"**
10. Launch the server

> **GbbConnect2 should run 24/7** to maintain the connection and execute commands from GbbOptimizer.

## Docker Deployment

GbbConnect2Console is available as a Docker image for production deployment. Use the Windows version first for initial testing and configuration, then switch to Docker.

## Protocol

GbbConnect2 communicates with GbbOptimizer using the ModbusInMqtt protocol — see [ModbusInMqtt Reference]({{< relref "/mqtt-api/modbus-in-mqtt" >}}).
