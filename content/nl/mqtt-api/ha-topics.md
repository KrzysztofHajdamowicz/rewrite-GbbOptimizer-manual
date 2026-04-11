---
title: "Home Assistant-topics"
weight: 40
translationKey: "tematy-ha"
---

# MQTT-topics voor Home Assistant

Topics gebruikt voor communicatie tussen GbbOptimizer en Home Assistant / GbbConnect.

## Gegevens van Home Assistant naar GbbOptimizer

{{< mqtt-topic topic="{PlantId}/ha_gbb/sensor" direction="subscribe" qos="0" description="Gegevens van HA-sensoren — cumulatieve tellers" >}}

**Verplichte velden:**

| Veld | Type | Beschrijving |
|------|-----|------|
| `soc_perc` | decimal | Batterij-SOC (%). Gebruik `V` indien „Aansturing via V" is aangevinkt |
| `loads_total_kWh` | decimal | Verbruik — cumulatieve teller |
| `fromgrid_total_kWh` | decimal | Import uit het net — cumulatieve teller |
| `togrid_total_kWh` | decimal | Export naar het net — cumulatieve teller |
| `pv_total_kWh` | decimal | PV-productie — cumulatieve teller |

**Optionele velden:**

| Veld | Type | Beschrijving |
|------|-----|------|
| `ev_charge_total_kWh` | decimal | EV-laden |
| `hp_total_kWh` | decimal | Warmtepomp |
| `other1_total_kWh` – `other6_total_kWh` | decimal | Andere 1–6 |

**Meerdere PV-bronnen:**

```json
{
  "pv_total_kWh": 123.4,
  "more": [
    {"number": 2, "pv_total_kWh": 56.7},
    {"number": 3, "pv_total_kWh": 89.0}
  ]
}
```

> [!NOTE]
> - Tellers mogen worden gereset — je kunt bijvoorbeeld dagelijkse tellers versturen
> - Waarden < 0 worden behandeld als ontbrekende gegevens
> - Je kunt alleen optionele gegevens versturen als de hoofdgegevens uit de omvormer worden geïmporteerd. Voeg in dat geval het HomeAssistant-systeem toe in het IoT-menu
> - `pv_total_kWh` is hetzelfde als `"more"` met `number=1` — gebruik beide niet tegelijk
> - Solarman/DeyeCloud: afzonderlijke velden (`soc_perc`, `fromgrid_total_kWh`, `togrid_total_kWh`, `loads_total_kWh`) kunnen apart worden verstuurd als de bijbehorende opties zijn aangevinkt in de [installatieparameters]({{< relref "/installation/installation-parameters" >}})

## Commando's van GbbOptimizer naar Home Assistant

GbbOptimizer verstuurt stuurcommando's naar speciale topics:

{{< mqtt-topic topic="{PlantId}/ha_gbb/Start_Charge" direction="publish" description="Start batterijladen tot SOC uit Payload" >}}

{{< mqtt-topic topic="{PlantId}/ha_gbb/Start_Discharge" direction="publish" description="Start batterijontladen naar het net (tot SOC uit Payload)" >}}

{{< mqtt-topic topic="{PlantId}/ha_gbb/Start_DisableCharge" direction="publish" description="Laad de batterij niet — PV naar huis en net" >}}

{{< mqtt-topic topic="{PlantId}/ha_gbb/Start_Normal" direction="publish" description="Terug naar normale werking" >}}

Parallel worden dezelfde gegevens ook verstuurd naar:

{{< mqtt-topic topic="{PlantId}/ha_gbb/EMS" direction="publish" description="Gecombineerd EMS-commando met volledige JSON-payload" >}}

**JSON-payload:**

| Veld | Type | Beschrijving |
|------|-----|------|
| `Hour` | int | Uur |
| `FromMinute` | int | Beginminuut |
| `ToMinute` | int | Eindminuut |
| `DischargeLimitW` | int | Ontlaadlimiet (W) |
| `ChargeLimitW` | int | Laadlimiet (W) |
| `InputLimitW` | int | Importlimiet (W) |
| `PriceLessZero` | int | 0 = normale prijs, 1 = prijs < 0 |
| `Operation` | string | `"Normal"`, `"Discharge"`, `"DisableCharge"` of `"Charge"` |
| `SOC` | int | Doel-SOC |
| `V` | decimal | SOC omgerekend naar V (indien aansturing via V) |

**Voorbeeld:**
```json
{
  "Hour": 22,
  "FromMinute": 0,
  "ToMinute": 59,
  "PriceLessZero": 0,
  "Operation": "Normal",
  "SOC": 90
}
```

## Voorbeeld van HA-automatisering

```yaml
alias: mqtt output_source_priority_battery
trigger:
  - platform: mqtt
    topic: ha_gbb/Start_Charge
action:
  - service: switch.turn_on
    target:
      entity_id: switch.bms_1_output_source_priority_battery
```

## Voorbeeld van het publiceren van gegevens naar MQTT

```yaml
alias: mqtt_publicatie
trigger:
  - platform: time_pattern
    minutes: /5
action:
  - service: mqtt.publish
    data:
      qos: "0"
      retain: false
      topic: ha_gbb/sensor
      payload: >
        {
          "loads_total_kWh": {{ states.sensor.inverter_out_daily_energy.state | float(-1) }},
          "fromgrid_total_kWh": {{ states.sensor.inverter_in_daily_energy.state | float(-1) }},
          "pv_total_kWh": {{ states.sensor.total_daily_energy.state | float(-1) }},
          "soc_perc": {{ states.sensor.battery_soc.state | float(-1) }},
          "togrid_total_kWh": 0
        }
```
