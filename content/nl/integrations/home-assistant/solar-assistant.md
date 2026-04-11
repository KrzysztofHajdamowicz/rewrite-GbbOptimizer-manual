---
title: "SolarAssistant"
weight: 20
translationKey: "solar-assistant"
---

# SolarAssistant

{{< badge "deye-only" >}}

Integratie van GbbOptimizer met een Deye-omvormer via {{< glossary "SolarAssistant" >}} en Home Assistant.

## Ondersteunde configuraties

- Home Assistant (HA) met SolarAssistant (SA) verbonden met een hybride Deye-omvormer als `inverter_1`

## Vereisten

- Home Assistant met Mosquitto broker
- SolarAssistant geïnstalleerd en verbonden met de Deye-omvormer
- Geconfigureerde [Mosquitto Bridge]({{< relref "/integrations/home-assistant/mosquitto-bridge" >}}) met een topic voor SolarAssistant

## SolarAssistant-configuratie

Ga in de SolarAssistant-instellingen naar **Configuration** -> **Advanced MQTT** en wijzig:

- **Allow setting changes** -> **Enabled**

## Bridge-configuratie

Gebruik in het bestand `/share/mosquitto/GbbOptimizer.conf` de volgende `topic`-regel:

```conf
topic # both 2 solar_assistant/ <PlantId>/solar_assistant/
```

In plaats van de standaard `ha_gbb/`-regel beschreven in [Mosquitto Bridge]({{< relref "/integrations/home-assistant/mosquitto-bridge" >}}).

## MQTT-topics

### Lezen (SolarAssistant -> GbbOptimizer)

| Topic | Beschrijving |
|-------|------|
| `{PlantId}/solar_assistant/total/battery_state_of_charge/state` | {{< glossary "SOC" >}} van de batterij |
| `{PlantId}/solar_assistant/inverter_1/battery_voltage` | Batterijspanning (indien aansturing via V) |
| `{PlantId}/solar_assistant/total/grid_energy_in/state` | Uit het net genomen energie (kWh) |
| `{PlantId}/solar_assistant/total/grid_energy_out/state` | Naar het net gestuurde energie (kWh) |
| `{PlantId}/solar_assistant/total/load_energy/state` | Verbruik (kWh) |
| `{PlantId}/solar_assistant/total/pv_energy/state` | PV-productie (kWh) |
| `{PlantId}/solar_assistant/inverter_1/work_mode/state` | Huidige werkmodus |
| `{PlantId}/solar_assistant/inverter_1/max_charge_current/state` | Maximale laadstroom |

### Schrijven (GbbOptimizer -> SolarAssistant)

| Topic | Beschrijving |
|-------|------|
| `{PlantId}/solar_assistant/inverter_1/capacity_point_{i}/set` | SOC instellen in TimeOfUse |
| `{PlantId}/solar_assistant/inverter_1/voltage_point_{i}/set` | Spanning instellen (indien aansturing via V) |
| `{PlantId}/solar_assistant/inverter_1/grid_charge_point_{i}/set` | Laden uit het net in-/uitschakelen |
| `{PlantId}/solar_assistant/inverter_1/work_mode/set` | Werkmodus wijzigen |
| `{PlantId}/solar_assistant/inverter_1/max_charge_current/set` | Laadstroom wijzigen |

> [!NOTE]
> SolarAssistant laat op dit moment niet toe om op afstand de starttijd of het vermogen (Power) in de TimeOfUse-tabel te wijzigen. Daarom stelt GbbOptimizer alle uurrijen in op dezelfde waarden.

## Verbruik importeren uit SolarAssistant (Solarman/DeyeCloud)

In een Deye-installatie met Solarman of DeyeCloud kun je verbruiksgegevens uit SolarAssistant importeren in plaats van uit de omvormer:

1. Configureer de [Mosquitto Bridge]({{< relref "/integrations/home-assistant/mosquitto-bridge" >}})
2. Voeg de volgende regel toe aan de bridge-configuratie:

```conf
topic # both 2 solar_assistant/total/load_energy/ <PlantId>/solar_assistant/total/load_energy/
```

3. Vink in de installatieparameters de optie **„Verbruiksgegevens worden door HomeAssistant/SolarAssistant verstuurd en niet uit de omvormer opgehaald"** aan

## Meer informatie

- [SolarAssistant MQTT-documentatie](https://solar-assistant.io/help/integration/mqtt)
- [Deye-modusmappings]({{< relref "/references/mode-mappings/deye" >}})
