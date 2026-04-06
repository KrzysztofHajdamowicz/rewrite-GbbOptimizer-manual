---
title: "SolarAssistant"
weight: 20
---

# SolarAssistant

{{< badge "deye-only" >}}

Integracja GbbOptimizer z falownikiem Deye przez {{< glossary "SolarAssistant" >}} i Home Assistant.

## Obslugiwane konfiguracje

- Home Assistant (HA) z SolarAssistant (SA) polaczonym z hybrydowym falownikiem Deye jako `inverter_1`

## Wymagania

- Home Assistant z Mosquitto broker
- SolarAssistant zainstalowany i polaczony z falownikiem Deye
- Skonfigurowany [Mosquitto Bridge]({{< relref "/integracje/home-assistant/mosquitto-bridge" >}}) z topikiem dla SolarAssistant

## Konfiguracja SolarAssistant

W ustawieniach SolarAssistant przejdz do **Configuration** -> **Advanced MQTT** i zmien:

- **Allow setting changes** -> **Enabled**

## Konfiguracja bridge

W pliku `/share/mosquitto/GbbOptimizer.conf` uzyj nastepujacej linii `topic`:

```conf
topic # both 2 solar_assistant/ <PlantId>/solar_assistant/
```

Zamiast standardowej linii `ha_gbb/` opisanej w [Mosquitto Bridge]({{< relref "/integracje/home-assistant/mosquitto-bridge" >}}).

## Topiki MQTT

### Odczyt (SolarAssistant -> GbbOptimizer)

| Topik | Opis |
|-------|------|
| `{PlantId}/solar_assistant/total/battery_state_of_charge/state` | {{< glossary "SOC" >}} baterii |
| `{PlantId}/solar_assistant/inverter_1/battery_voltage` | Napiecie baterii (jesli sterowanie przez V) |
| `{PlantId}/solar_assistant/total/grid_energy_in/state` | Energia pobrana z sieci (kWh) |
| `{PlantId}/solar_assistant/total/grid_energy_out/state` | Energia wyslana do sieci (kWh) |
| `{PlantId}/solar_assistant/total/load_energy/state` | Zuzycie (kWh) |
| `{PlantId}/solar_assistant/total/pv_energy/state` | Produkcja PV (kWh) |
| `{PlantId}/solar_assistant/inverter_1/work_mode/state` | Aktualny tryb pracy |
| `{PlantId}/solar_assistant/inverter_1/max_charge_current/state` | Maksymalny prad ladowania |

### Zapis (GbbOptimizer -> SolarAssistant)

| Topik | Opis |
|-------|------|
| `{PlantId}/solar_assistant/inverter_1/capacity_point_{i}/set` | Ustawienie SOC w TimeOfUse |
| `{PlantId}/solar_assistant/inverter_1/voltage_point_{i}/set` | Ustawienie napiecia (jesli sterowanie przez V) |
| `{PlantId}/solar_assistant/inverter_1/grid_charge_point_{i}/set` | Wlacz/wylacz ladowanie z sieci |
| `{PlantId}/solar_assistant/inverter_1/work_mode/set` | Zmiana trybu pracy |
| `{PlantId}/solar_assistant/inverter_1/max_charge_current/set` | Zmiana pradu ladowania |

> [!NOTE]
> SolarAssistant aktualnie nie pozwala zdalnie zmieniac godziny poczatkowej ani mocy (Power) w tablicy TimeOfUse. Dlatego GbbOptimizer ustawia wszystkie wiersze godzin na te same wartosci.

## Import zuzycia z SolarAssistant (Solarman/DeyeCloud)

W instalacji Deye z Solarman lub DeyeCloud mozna importowac dane zuzycia z SolarAssistant zamiast z falownika:

1. Skonfiguruj [Mosquitto Bridge]({{< relref "/integracje/home-assistant/mosquitto-bridge" >}})
2. Dodaj nastepujacy topik do konfiguracji bridge:

```conf
topic # both 2 solar_assistant/total/load_energy/ <PlantId>/solar_assistant/total/load_energy/
```

3. W parametrach instalacji zaznacz opcje **"Dane Zuzycia sa wyslane z HomeAssistant/SolarAssistant a nie pobierane z invertera"**

## Wiecej informacji

- [Dokumentacja MQTT SolarAssistant](https://solar-assistant.io/help/integration/mqtt)
- [Mapowania trybow Deye]({{< relref "/referencje/mapowania-trybow/deye" >}})
