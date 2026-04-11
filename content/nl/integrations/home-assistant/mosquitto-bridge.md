---
title: "Mosquitto Bridge"
weight: 10
translationKey: "mosquitto-bridge"
---

# Mosquitto Bridge

Om GbbOptimizer met Home Assistant te laten communiceren, moet je een bridge instellen tussen de lokale Mosquitto-broker in HA en de MQTT-server van GbbOptimizer.

## Vereisten

- Home Assistant met de **Mosquitto broker**-add-on geïnstalleerd
- Een actieve installatie in GbbOptimizer met toegewezen {{< glossary "PlantId" >}} en {{< glossary "PlantToken" >}}
- Het MQTT-serveradres — zie [MQTT-servers]({{< relref "/references/mqtt-servers" >}})

## Stap-voor-stap configuratie

### 1. Configuratiemap in Mosquitto inschakelen

Ga in Home Assistant naar **Instellingen** -> **Add-ons** -> **Mosquitto broker** -> **Configuratie**.

Activeer de optie **Customize** en stel de map in op:

```
mosquitto
```

### 2. Maak het bridge-configuratiebestand

Maak het bestand `/share/mosquitto/GbbOptimizer.conf` aan met de volgende inhoud:

```conf
connection GbbOptimizer_<PlantId>
remote_username <PlantId>
remote_password <PlantToken>
address <mqtt-server-adres>:8883
bridge_capath /etc/ssl/certs
topic # both 2 ha_gbb/ <PlantId>/ha_gbb/
```

Vervang:
- `<PlantId>` — door jouw {{< glossary "PlantId" >}}
- `<PlantToken>` — door jouw {{< glossary "PlantToken" >}}
- `<mqtt-server-adres>` — door het serveradres uit de tabel [MQTT-servers]({{< relref "/references/mqtt-servers" >}})

### 3. Herstart Mosquitto

Herstart na het opslaan van het bestand de Mosquitto broker-add-on in Home Assistant.

> [!NOTE]
> De verbinding gebruikt poort **8883** (MQTT over TLS). CA-certificaten worden opgehaald uit `/etc/ssl/certs` — je hoeft geen eigen certificaten toe te voegen.

## Hoe de bridge werkt

De `topic`-regel in de configuratie wijst topics toe:

| Richting | Lokaal topic (HA) | Extern topic (GbbOptimizer) |
|----------|--------------------|-----------------------------|
| HA -> GbbOptimizer | `ha_gbb/#` | `<PlantId>/ha_gbb/#` |
| GbbOptimizer -> HA | `ha_gbb/#` | `<PlantId>/ha_gbb/#` |

Daardoor:
- Sensorgegevens gepubliceerd op `ha_gbb/sensor` in HA komen bij GbbOptimizer aan als `<PlantId>/ha_gbb/sensor`
- Commando's uit GbbOptimizer (bijv. `<PlantId>/ha_gbb/Start_Charge`) verschijnen in HA als `ha_gbb/Start_Charge`

## Bridge voor SolarAssistant

Als je {{< glossary "SolarAssistant" >}} gebruikt, wijzig de `topic`-regel in:

```conf
topic # both 2 solar_assistant/ <PlantId>/solar_assistant/
```

Meer informatie: [SolarAssistant]({{< relref "/integrations/home-assistant/solar-assistant" >}})

## Bridge voor evcc

Als je integreert met evcc, voeg een aparte `topic`-regel toe:

```conf
topic # both 2 evcc/loadpoints/ <PlantId>/evcc/site/loadpoints/
```

Meer informatie: [evcc]({{< relref "/integrations/evcc" >}})

> [!WARNING]
> Zorg ervoor dat {{< glossary "PlantId" >}} en {{< glossary "PlantToken" >}} correct zijn. Verkeerde authenticatiegegevens leiden tot verbindingsproblemen — controleer de Mosquitto-logs in HA.
