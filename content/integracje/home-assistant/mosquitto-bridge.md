---
title: "Mosquitto Bridge"
weight: 10
---

# Mosquitto Bridge

Aby GbbOptimizer mog komunikowac sie z Home Assistant, nalezy skonfigurowac most (bridge) miedzy lokalnym brokerem Mosquitto w HA a serwerem MQTT GbbOptimizer.

## Wymagania

- Home Assistant z zainstalowanym dodatkiem **Mosquitto broker**
- Aktywna instalacja w GbbOptimizer z przypisanym {{< glossary "PlantId" >}} i {{< glossary "PlantToken" >}}
- Adres serwera MQTT — patrz [Serwery MQTT]({{< relref "/referencje/serwery-mqtt" >}})

## Konfiguracja krok po kroku

### 1. Wlacz folder konfiguracyjny w Mosquitto

W Home Assistant przejdz do **Ustawienia** -> **Dodatki** -> **Mosquitto broker** -> **Konfiguracja**.

Aktywuj opcje **Customize** i ustaw folder na:

```
mosquitto
```

### 2. Utworz plik konfiguracyjny bridge

Utworz plik `/share/mosquitto/GbbOptimizer.conf` z nastepujaca zawartoscia:

```conf
connection GbbOptimizer_<PlantId>
remote_username <PlantId>
remote_password <PlantToken>
address <adres-serwera-mqtt>:8883
bridge_capath /etc/ssl/certs
topic # both 2 ha_gbb/ <PlantId>/ha_gbb/
```

Zamien:
- `<PlantId>` — na Twoj {{< glossary "PlantId" >}}
- `<PlantToken>` — na Twoj {{< glossary "PlantToken" >}}
- `<adres-serwera-mqtt>` — na adres serwera z tabeli [Serwery MQTT]({{< relref "/referencje/serwery-mqtt" >}})

### 3. Zrestartuj Mosquitto

Po zapisaniu pliku zrestartuj dodatek Mosquitto broker w Home Assistant.

> [!NOTE]
> Polaczenie uzywa portu **8883** (MQTT over TLS). Certyfikaty CA sa pobierane z `/etc/ssl/certs` — nie trzeba dodawac wlasnych.

## Jak dziala bridge

Linia `topic` w konfiguracji mapuje topiki:

| Kierunek | Topik lokalny (HA) | Topik zdalny (GbbOptimizer) |
|----------|--------------------|-----------------------------|
| HA -> GbbOptimizer | `ha_gbb/#` | `<PlantId>/ha_gbb/#` |
| GbbOptimizer -> HA | `ha_gbb/#` | `<PlantId>/ha_gbb/#` |

Dzieki temu:
- Dane z czujnikow wyslane na `ha_gbb/sensor` w HA trafiaja do GbbOptimizer jako `<PlantId>/ha_gbb/sensor`
- Komendy z GbbOptimizer (np. `<PlantId>/ha_gbb/Start_Charge`) pojawiaja sie w HA jako `ha_gbb/Start_Charge`

## Bridge dla SolarAssistant

Jesli uzywasz {{< glossary "SolarAssistant" >}}, zmien linie `topic` na:

```conf
topic # both 2 solar_assistant/ <PlantId>/solar_assistant/
```

Wiecej informacji: [SolarAssistant]({{< relref "/integracje/home-assistant/solar-assistant" >}})

## Bridge dla evcc

Jesli integrujesz z evcc, dodaj osobna linie `topic`:

```conf
topic # both 2 evcc/loadpoints/ <PlantId>/evcc/site/loadpoints/
```

Wiecej informacji: [evcc]({{< relref "/integracje/evcc" >}})

> [!WARNING]
> Upewnij sie, ze {{< glossary "PlantId" >}} i {{< glossary "PlantToken" >}} sa poprawne. Bledne dane uwierzytelniajace spowoduja brak polaczenia — sprawdz logi Mosquitto w HA.
