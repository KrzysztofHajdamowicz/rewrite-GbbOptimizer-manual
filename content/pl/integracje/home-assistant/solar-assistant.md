---
title: "SolarAssistant"
weight: 20
translationKey: "solar-assistant"
---

# SolarAssistant

{{< badge "deye-only" >}}

Integracja GbbOptimizer z falownikiem Deye przez {{< glossary "SolarAssistant" >}} i Home Assistant.

## Obsługiwane konfiguracje

- Home Assistant (HA) z SolarAssistant (SA) połączonym z hybrydowym falownikiem Deye jako `inverter_1`

## Wymagania

- Home Assistant z Mosquitto broker
- SolarAssistant zainstalowany i połączony z falownikiem Deye
- Skonfigurowany [Mosquitto Bridge]({{< relref "/integracje/home-assistant/mosquitto-bridge" >}}) z topikiem dla SolarAssistant

## Konfiguracja SolarAssistant

W ustawieniach SolarAssistant przejdź do **Configuration** -> **Advanced MQTT** i zmień:

- **Allow setting changes** -> **Enabled**

## Konfiguracja bridge

W pliku `/share/mosquitto/GbbOptimizer.conf` użyj następującej linii `topic`:

```conf
topic # both 2 solar_assistant/ <PlantId>/solar_assistant/
```

Zamiast standardowej linii `ha_gbb/` opisanej w [Mosquitto Bridge]({{< relref "/integracje/home-assistant/mosquitto-bridge" >}}).

## Topiki MQTT

### Odczyt (SolarAssistant -> GbbOptimizer)

| Topik | Opis |
|-------|------|
| `{PlantId}/solar_assistant/total/battery_state_of_charge/state` | {{< glossary "SOC" >}} baterii |
| `{PlantId}/solar_assistant/inverter_1/battery_voltage` | Napięcie baterii (jeśli sterowanie przez V) |
| `{PlantId}/solar_assistant/total/grid_energy_in/state` | Energia pobrana z sieci (kWh) |
| `{PlantId}/solar_assistant/total/grid_energy_out/state` | Energia wysłana do sieci (kWh) |
| `{PlantId}/solar_assistant/total/load_energy/state` | Zużycie (kWh) |
| `{PlantId}/solar_assistant/total/pv_energy/state` | Produkcja PV (kWh) |
| `{PlantId}/solar_assistant/inverter_1/work_mode/state` | Aktualny tryb pracy |
| `{PlantId}/solar_assistant/inverter_1/max_charge_current/state` | Maksymalny prąd ładowania |

### Zapis (GbbOptimizer -> SolarAssistant)

| Topik | Opis |
|-------|------|
| `{PlantId}/solar_assistant/inverter_1/capacity_point_{i}/set` | Ustawienie SOC w TimeOfUse |
| `{PlantId}/solar_assistant/inverter_1/voltage_point_{i}/set` | Ustawienie napięcia (jeśli sterowanie przez V) |
| `{PlantId}/solar_assistant/inverter_1/grid_charge_point_{i}/set` | Włącz/wyłącz ładowanie z sieci |
| `{PlantId}/solar_assistant/inverter_1/work_mode/set` | Zmiana trybu pracy |
| `{PlantId}/solar_assistant/inverter_1/max_charge_current/set` | Zmiana prądu ładowania |

> [!NOTE]
> SolarAssistant aktualnie nie pozwala zdalnie zmieniać godziny początkowej ani mocy (Power) w tablicy TimeOfUse. Dlatego GbbOptimizer ustawia wszystkie wiersze godzin na te same wartości.

## Import zużycia z SolarAssistant (Solarman/DeyeCloud)

W instalacji Deye z Solarman lub DeyeCloud można importować dane zużycia z SolarAssistant zamiast z falownika:

1. Skonfiguruj [Mosquitto Bridge]({{< relref "/integracje/home-assistant/mosquitto-bridge" >}})
2. Dodaj następujący topik do konfiguracji bridge:

```conf
topic # both 2 solar_assistant/total/load_energy/ <PlantId>/solar_assistant/total/load_energy/
```

3. W parametrach instalacji zaznacz opcję **"Dane zużycia są wysłane z HomeAssistant/SolarAssistant a nie pobierane z invertera"**

## Więcej informacji

- [Dokumentacja MQTT SolarAssistant](https://solar-assistant.io/help/integration/mqtt)
- [Mapowania trybów Deye]({{< relref "/referencje/mapowania-trybow/deye" >}})
