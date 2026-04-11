---
title: "evcc"
weight: 20
translationKey: "evcc"
---

# Integratie met evcc

[evcc.io](https://evcc.io) is software voor slim laden van elektrische voertuigen. GbbOptimizer kan ermee communiceren via MQTT om het laden van de EV te coördineren met de optimalisatie van de thuisbatterij.

## Vereisten

- Werkende evcc-installatie
- Lokale MQTT-broker (Mosquitto in Home Assistant of standalone)
- Geconfigureerde [Mosquitto Bridge]({{< relref "/integrations/home-assistant/mosquitto-bridge" >}})

## Bridge-configuratie

Voeg in het Mosquitto-configuratiebestand (`/share/mosquitto/GbbOptimizer.conf`) `topic`-regels toe voor evcc:

```conf
connection GbbOptimizer_<PlantId>
remote_username <PlantId>
remote_password <PlantToken>
address <mqtt-server-adres>:8883
bridge_capath /etc/ssl/certs
topic # both 2 evcc/loadpoints/ <PlantId>/evcc/site/loadpoints/
```

## MQTT-topics

### Gegevens uit evcc (evcc -> GbbOptimizer)

| Topic | Beschrijving |
|-------|------|
| `{PlantId}/evcc/site/statistic/total/chargedKWh` | Totale naar EV geladen energie (kWh) |

### Commando's vanuit GbbOptimizer (GbbOptimizer -> evcc)

| Topic | Payload | Beschrijving |
|-------|---------|------|
| `{PlantId}/evcc/loadpoints/{chargerId}/mode` | `off` of `now` | Laden in-/uitschakelen |
| `{PlantId}/evcc/loadpoints/{chargerId}/maxCurrent` | getal (A) | Maximale laadstroom |
| `{PlantId}/evcc/loadpoints/{chargerId}/connected` | `true`/`false` | Verbindingsstatus met de lader |

Waarbij `{chargerId}` de identificatie van het laadpunt in evcc is.

> [!NOTE]
> evcc moet worden geconfigureerd voor communicatie via MQTT. Zie de [evcc-documentatie](https://docs.evcc.io/docs/reference/configuration/messaging#mqtt) in de sectie over MQTT.
