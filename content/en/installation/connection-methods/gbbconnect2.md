---
title: "GbbConnect2"
weight: 30
translationKey: "gbbconnect2"
---

# GbbConnect2

{{< glossary "GbbConnect2" >}} is software running on the local network that connects the inverter directly to GbbOptimizer via {{< glossary "ModbusInMqtt" >}}, bypassing cloud servers.

## Requirements

- A computer with **Windows** or a **Docker** container running 24/7 on the local network
- A **Deye** hybrid inverter with a WiFi logger (dongle)
- A fixed IP address for the logger on the local network

## Step-by-step configuration

1. Download and install GbbConnect2: [github.com/gbbsoft/GbbConnect2](https://github.com/gbbsoft/GbbConnect2)
2. In GbbOptimizer, create a new installation of type **GbbConnect2** (or change the type of an existing one)
3. Enter the installation name, review the remaining fields, and **Save**
4. Press **Edit**, then **Generate new Token**
5. Note the {{< glossary "PlantId" >}} and {{< glossary "PlantToken" >}}
6. In GbbConnect2: create a new Plant with the name and type "SolarmanV2"
7. In the **Test and Log** tab, press **Search for Inverters** to find the IP and SerialNumber of the inverter
8. In the **Plants** tab, enter the **IP address** and **SerialNumber** of the logger

   > [!WARNING]
   > The logger under the inverter **must have a fixed IP address** on the local network. Set a DHCP reservation on the router.

9. In the **GbbOptimizer** section, enter the {{< glossary "PlantId" >}} and {{< glossary "PlantToken" >}}
10. Enter the MQTT server address — see [MQTT Servers]({{< relref "/referencje/serwery-mqtt" >}})
11. In the **Parameters** tab, check "Start server after program starts" so that communication starts automatically
12. Press **StartServer**

## Docker version

There is a **GbbConnect2Console** version for Docker:

1. Start with the **Windows** version — test the connection and create a configuration file
2. Switch to the **Docker** version with the same configuration file

> [!NOTE]
> The program should run **24/7** to collect statistical data from the inverter and execute commands from GbbOptimizer.
