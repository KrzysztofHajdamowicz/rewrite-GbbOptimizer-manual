---
title: "evcc"
weight: 20
---

# Integracja z evcc

[evcc.io](https://evcc.io) to oprogramowanie do inteligentnego ladowania pojazdow elektrycznych. GbbOptimizer moze sie z nim komunikowac przez MQTT, aby koordynowac ladowanie EV z optymalizacja baterii domowej.

## Wymagania

- Dzialajaca instalacja evcc
- Lokalny broker MQTT (Mosquitto w Home Assistant lub samodzielny)
- Skonfigurowany [Mosquitto Bridge]({{< relref "/integracje/home-assistant/mosquitto-bridge" >}})

## Konfiguracja bridge

W pliku konfiguracyjnym Mosquitto (`/share/mosquitto/GbbOptimizer.conf`) dodaj linie `topic` dla evcc:

```conf
connection GbbOptimizer_<PlantId>
remote_username <PlantId>
remote_password <PlantToken>
address <adres-serwera-mqtt>:8883
bridge_capath /etc/ssl/certs
topic # both 2 evcc/loadpoints/ <PlantId>/evcc/site/loadpoints/
```

## Topiki MQTT

### Dane z evcc (evcc -> GbbOptimizer)

| Topik | Opis |
|-------|------|
| `{PlantId}/evcc/site/statistic/total/chargedKWh` | Calkowita energia zaladowana do EV (kWh) |

### Komendy z GbbOptimizer (GbbOptimizer -> evcc)

| Topik | Payload | Opis |
|-------|---------|------|
| `{PlantId}/evcc/loadpoints/{chargerId}/mode` | `off` lub `now` | Wlacz/wylacz ladowanie |
| `{PlantId}/evcc/loadpoints/{chargerId}/maxCurrent` | liczba (A) | Maksymalny prad ladowania |
| `{PlantId}/evcc/loadpoints/{chargerId}/connected` | `true`/`false` | Stan polaczenia z ladowarka |

Gdzie `{chargerId}` to identyfikator punktu ladowania w evcc.

> [!NOTE]
> evcc musi byc skonfigurowane do komunikacji przez MQTT. Sprawdz [dokumentacje evcc](https://docs.evcc.io/docs/reference/configuration/messaging#mqtt) w sekcji dotyczacej MQTT.
