---
title: "MQTT Servers"
weight: 50
translationKey: "serwery-mqtt"
---

# MQTT Servers

GbbOptimizer uses multiple MQTT servers to communicate with inverters and integrations. The server assigned to your installation depends on the {{< glossary "PlantId" >}} prefix.

## Server Table

| Application Server | MQTT Server | PlantId Prefix |
|-------------------|-------------|----------------|
| gbboptimizer.gbbsoft.pl | gbboptimizer-mqtt.gbbsoft.pl | (none) |
| gbboptimizer2.gbbsoft.pl | gbboptimizer2-mqtt.gbbsoft.pl | B |
| gbboptimizer3.gbbsoft.pl | gbboptimizer3-mqtt.gbbsoft.pl | C |
| gbboptimizer4.gbbsoft.pl | gbboptimizer4-mqtt.gbbsoft.pl | D |
| gbboptimizer5.gbbsoft.pl | gbboptimizer5-mqtt.gbbsoft.pl | E |
| gbboptimizer6.gbbsoft.pl | gbboptimizer6-mqtt.gbbsoft.pl | F |
| gbboptimizer7.gbbsoft.pl | gbboptimizer7-mqtt.gbbsoft.pl | G |
| gbboptimizer8.gbbsoft.pl | gbboptimizer8-mqtt.gbbsoft.pl | H |
| gbboptimizer9.gbbsoft.pl | gbboptimizer9-mqtt.gbbsoft.pl | I |
| gbboptimizer10.gbbsoft.pl | gbboptimizer10-mqtt.gbbsoft.pl | J |
| gbboptimizer11.gbbsoft.pl | gbboptimizer11-mqtt.gbbsoft.pl | K |
| gbboptimizer12.gbbsoft.pl | gbboptimizer12-mqtt.gbbsoft.pl | L |
| gbboptimizer13.gbbsoft.pl | gbboptimizer13-mqtt.gbbsoft.pl | M |
| gbboptimizer14.gbbsoft.pl | gbboptimizer14-mqtt.gbbsoft.pl | N |
| gbboptimizer15.gbbsoft.pl | gbboptimizer15-mqtt.gbbsoft.pl | O |
| gbboptimizer16.gbbsoft.pl | gbboptimizer16-mqtt.gbbsoft.pl | P |
| gbboptimizer17.gbbsoft.pl | gbboptimizer17-mqtt.gbbsoft.pl | Q |
| gbboptimizer18.gbbsoft.pl | gbboptimizer18-mqtt.gbbsoft.pl | R |
| gbboptimizer19.gbbsoft.pl | gbboptimizer19-mqtt.gbbsoft.pl | S |
| gbboptimizer20.gbbsoft.pl | gbboptimizer20-mqtt.gbbsoft.pl | T |

## How to Determine Your Server from PlantId

The {{< glossary "PlantId" >}} prefix (first letter) indicates which server your installation uses:

- PlantId starting with **J** (e.g. `J1234`) -> server `gbboptimizer10-mqtt.gbbsoft.pl`
- PlantId starting with a **digit** (e.g. `1234`) -> server `gbboptimizer-mqtt.gbbsoft.pl`

## Port and Encryption

All MQTT servers use:

- **Port:** 8883
- **Encryption:** TLS/SSL
- **Authentication:** {{< glossary "PlantId" >}} (as username) and {{< glossary "PlantToken" >}} (as password)
