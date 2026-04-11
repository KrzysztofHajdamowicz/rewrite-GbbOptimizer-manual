---
title: "MQTT-servers"
weight: 50
translationKey: "serwery-mqtt"
---

# MQTT-servers

GbbOptimizer gebruikt meerdere MQTT-servers voor communicatie met omvormers en integraties. Welke server aan jouw installatie is toegewezen, hangt af van de {{< glossary "PlantId" >}}-prefix.

## Servertabel

| Applicatieserver | MQTT-server | PlantId-prefix |
|-----------------|-------------|----------------|
| gbboptimizer.gbbsoft.pl | gbboptimizer-mqtt.gbbsoft.pl | (geen) |
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

## De server uit PlantId afleiden

De {{< glossary "PlantId" >}}-prefix (eerste letter) geeft aan welke server jouw installatie gebruikt:

- PlantId beginnend met **J** (bijv. `J1234`) -> server `gbboptimizer10-mqtt.gbbsoft.pl`
- PlantId beginnend met een **cijfer** (bijv. `1234`) -> server `gbboptimizer-mqtt.gbbsoft.pl`

## Poort en versleuteling

Alle MQTT-servers gebruiken:

- **Poort:** 8883
- **Versleuteling:** TLS/SSL
- **Authenticatie:** {{< glossary "PlantId" >}} (als gebruikersnaam) en {{< glossary "PlantToken" >}} (als wachtwoord)
