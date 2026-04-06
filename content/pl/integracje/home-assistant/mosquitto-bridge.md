---
title: "Mosquitto Bridge"
weight: 10
translationKey: "mosquitto-bridge"
---

# Mosquitto Bridge

Aby GbbOptimizer mógł komunikować się z Home Assistant, należy skonfigurować most (bridge) między lokalnym brokerem Mosquitto w HA a serwerem MQTT GbbOptimizer.

## Wymagania

- Home Assistant z zainstalowanym dodatkiem **Mosquitto broker**
- Aktywna instalacja w GbbOptimizer z przypisanym {{< glossary "PlantId" >}} i {{< glossary "PlantToken" >}}
- Adres serwera MQTT — patrz [Serwery MQTT]({{< relref "/referencje/serwery-mqtt" >}})

## Konfiguracja krok po kroku

### 1. Włącz folder konfiguracyjny w Mosquitto

W Home Assistant przejdź do **Ustawienia** -> **Dodatki** -> **Mosquitto broker** -> **Konfiguracja**.

Aktywuj opcję **Customize** i ustaw folder na:

```
mosquitto
```

### 2. Utwórz plik konfiguracyjny bridge

Utwórz plik `/share/mosquitto/GbbOptimizer.conf` z następującą zawartością:

```conf
connection GbbOptimizer_<PlantId>
remote_username <PlantId>
remote_password <PlantToken>
address <adres-serwera-mqtt>:8883
bridge_capath /etc/ssl/certs
topic # both 2 ha_gbb/ <PlantId>/ha_gbb/
```

Zamień:
- `<PlantId>` — na Twój {{< glossary "PlantId" >}}
- `<PlantToken>` — na Twój {{< glossary "PlantToken" >}}
- `<adres-serwera-mqtt>` — na adres serwera z tabeli [Serwery MQTT]({{< relref "/referencje/serwery-mqtt" >}})

### 3. Zrestartuj Mosquitto

Po zapisaniu pliku zrestartuj dodatek Mosquitto broker w Home Assistant.

> [!NOTE]
> Połączenie używa portu **8883** (MQTT over TLS). Certyfikaty CA są pobierane z `/etc/ssl/certs` — nie trzeba dodawać własnych.

## Jak działa bridge

Linia `topic` w konfiguracji mapuje topiki:

| Kierunek | Topik lokalny (HA) | Topik zdalny (GbbOptimizer) |
|----------|--------------------|-----------------------------|
| HA -> GbbOptimizer | `ha_gbb/#` | `<PlantId>/ha_gbb/#` |
| GbbOptimizer -> HA | `ha_gbb/#` | `<PlantId>/ha_gbb/#` |

Dzięki temu:
- Dane z czujników wysłane na `ha_gbb/sensor` w HA trafiają do GbbOptimizer jako `<PlantId>/ha_gbb/sensor`
- Komendy z GbbOptimizer (np. `<PlantId>/ha_gbb/Start_Charge`) pojawiają się w HA jako `ha_gbb/Start_Charge`

## Bridge dla SolarAssistant

Jeśli używasz {{< glossary "SolarAssistant" >}}, zmień linię `topic` na:

```conf
topic # both 2 solar_assistant/ <PlantId>/solar_assistant/
```

Więcej informacji: [SolarAssistant]({{< relref "/integracje/home-assistant/solar-assistant" >}})

## Bridge dla evcc

Jeśli integrujesz z evcc, dodaj osobną linię `topic`:

```conf
topic # both 2 evcc/loadpoints/ <PlantId>/evcc/site/loadpoints/
```

Więcej informacji: [evcc]({{< relref "/integracje/evcc" >}})

> [!WARNING]
> Upewnij się, że {{< glossary "PlantId" >}} i {{< glossary "PlantToken" >}} są poprawne. Błędne dane uwierzytelniające spowodują brak połączenia — sprawdź logi Mosquitto w HA.
