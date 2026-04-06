---
title: "evcc"
weight: 20
---

# Integracja z evcc

[evcc.io](https://evcc.io) to oprogramowanie do inteligentnego ładowania pojazdów elektrycznych. GbbOptimizer może się z nim komunikować przez MQTT, aby koordynować ładowanie EV z optymalizacją baterii domowej.

## Wymagania

- Działająca instalacja evcc
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
| `{PlantId}/evcc/site/statistic/total/chargedKWh` | Całkowita energia załadowana do EV (kWh) |

### Komendy z GbbOptimizer (GbbOptimizer -> evcc)

| Topik | Payload | Opis |
|-------|---------|------|
| `{PlantId}/evcc/loadpoints/{chargerId}/mode` | `off` lub `now` | Włącz/wyłącz ładowanie |
| `{PlantId}/evcc/loadpoints/{chargerId}/maxCurrent` | liczba (A) | Maksymalny prąd ładowania |
| `{PlantId}/evcc/loadpoints/{chargerId}/connected` | `true`/`false` | Stan połączenia z ładowarką |

Gdzie `{chargerId}` to identyfikator punktu ładowania w evcc.

> [!NOTE]
> evcc musi być skonfigurowane do komunikacji przez MQTT. Sprawdź [dokumentację evcc](https://docs.evcc.io/docs/reference/configuration/messaging#mqtt) w sekcji dotyczącej MQTT.
