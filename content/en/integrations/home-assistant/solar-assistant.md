---
title: "SolarAssistant"
weight: 20
translationKey: "solar-assistant"
---

# SolarAssistant

{{< badge "deye-only" >}}

GbbOptimizer integration with the Deye inverter via {{< glossary "SolarAssistant" >}} and Home Assistant.

## Supported Configurations

- Home Assistant (HA) with SolarAssistant (SA) connected to a hybrid Deye inverter as `inverter_1`

## Requirements

- Home Assistant with Mosquitto broker
- SolarAssistant installed and connected to the Deye inverter
- Configured [Mosquitto Bridge]({{< relref "/integracje/home-assistant/mosquitto-bridge" >}}) with a topic for SolarAssistant

## SolarAssistant Configuration

In the SolarAssistant settings go to **Configuration** -> **Advanced MQTT** and change:

- **Allow setting changes** -> **Enabled**

## Bridge Configuration

In the `/share/mosquitto/GbbOptimizer.conf` file use the following `topic` line:

```conf
topic # both 2 solar_assistant/ <PlantId>/solar_assistant/
```

Instead of the standard `ha_gbb/` line described in [Mosquitto Bridge]({{< relref "/integracje/home-assistant/mosquitto-bridge" >}}).

## MQTT Topics

### Read (SolarAssistant -> GbbOptimizer)

| Topic | Description |
|-------|-------------|
| `{PlantId}/solar_assistant/total/battery_state_of_charge/state` | Battery {{< glossary "SOC" >}} |
| `{PlantId}/solar_assistant/inverter_1/battery_voltage` | Battery voltage (if voltage-based control) |
| `{PlantId}/solar_assistant/total/grid_energy_in/state` | Energy drawn from the grid (kWh) |
| `{PlantId}/solar_assistant/total/grid_energy_out/state` | Energy sent to the grid (kWh) |
| `{PlantId}/solar_assistant/total/load_energy/state` | Consumption (kWh) |
| `{PlantId}/solar_assistant/total/pv_energy/state` | PV production (kWh) |
| `{PlantId}/solar_assistant/inverter_1/work_mode/state` | Current operating mode |
| `{PlantId}/solar_assistant/inverter_1/max_charge_current/state` | Maximum charging current |

### Write (GbbOptimizer -> SolarAssistant)

| Topic | Description |
|-------|-------------|
| `{PlantId}/solar_assistant/inverter_1/capacity_point_{i}/set` | Set SOC in TimeOfUse |
| `{PlantId}/solar_assistant/inverter_1/voltage_point_{i}/set` | Set voltage (if voltage-based control) |
| `{PlantId}/solar_assistant/inverter_1/grid_charge_point_{i}/set` | Enable/disable grid charging |
| `{PlantId}/solar_assistant/inverter_1/work_mode/set` | Change operating mode |
| `{PlantId}/solar_assistant/inverter_1/max_charge_current/set` | Change charging current |

> [!NOTE]
> SolarAssistant currently does not allow remotely changing the start time or Power in the TimeOfUse table. Therefore GbbOptimizer sets all hour rows to the same values.

## Importing Consumption Data from SolarAssistant (Solarman/DeyeCloud)

For Deye installations with Solarman or DeyeCloud, consumption data can be imported from SolarAssistant instead of from the inverter:

1. Configure [Mosquitto Bridge]({{< relref "/integracje/home-assistant/mosquitto-bridge" >}})
2. Add the following topic to the bridge configuration:

```conf
topic # both 2 solar_assistant/total/load_energy/ <PlantId>/solar_assistant/total/load_energy/
```

3. In the installation parameters check the option **"Consumption data is sent from HomeAssistant/SolarAssistant and not fetched from the inverter"**

## More Information

- [SolarAssistant MQTT Documentation](https://solar-assistant.io/help/integration/mqtt)
- [Deye Mode Mappings]({{< relref "/referencje/mapowania-trybow/deye" >}})
