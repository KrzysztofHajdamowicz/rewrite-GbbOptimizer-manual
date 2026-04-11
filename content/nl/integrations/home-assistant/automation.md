---
title: "Automatisering"
weight: 30
translationKey: "automatyzacja"
---

# Home Assistant-automatisering

Nadat je de [Mosquitto Bridge]({{< relref "/integrations/home-assistant/mosquitto-bridge" >}}) hebt geconfigureerd, kun je automatiseringen in Home Assistant maken die:

- **Gegevens versturen** van HA-sensoren naar GbbOptimizer
- **Reageren op commando's** ontvangen van GbbOptimizer

## Gegevens naar GbbOptimizer versturen

GbbOptimizer verwacht gegevens op het topic `ha_gbb/sensor` (lokaal in HA; via de bridge wordt het `<PlantId>/ha_gbb/sensor`).

### Verplichte velden

| Veld | Beschrijving |
|------|------|
| `soc_perc` | {{< glossary "SOC" >}} van de batterij in procenten (of `V` als aansturing via spanning is ingesteld) |
| `loads_total_kWh` | Verbruiksteller (kWh, cumulatief) |
| `fromgrid_total_kWh` | Teller van uit het net genomen energie (kWh) |
| `togrid_total_kWh` | Teller van naar het net gestuurde energie (kWh) |
| `pv_total_kWh` | PV-productieteller (kWh) |

### Optionele velden

| Veld | Beschrijving |
|------|------|
| `ev_charge_total_kWh` | EV-laadteller |
| `hp_total_kWh` | Warmtepompteller |
| `other1_total_kWh` ... `other6_total_kWh` | Aanvullende tellers |

### Meerdere PV-installaties

Gebruik het veld `more` om gegevens van meerdere PV-vlakken te versturen:

```json
{
  "pv_total_kWh": 10.5,
  "more": [
    {"number": 2, "pv_total_kWh": 5.2},
    {"number": 3, "pv_total_kWh": 3.1}
  ]
}
```

> [!NOTE]
> De hoofdwaarde `pv_total_kWh` komt overeen met `number: 1`. Gebruik ofwel `pv_total_kWh`, ofwel `number: 1` in `more` — niet beide tegelijk. Het bijbehorende nummer moet zijn geconfigureerd in de PV-vlakinstellingen -> HomeAssistant.

### Voorbeeld van automatisering — gegevens publiceren

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
      payload: >-
        {
          "soc_perc": {{ states.sensor.battery_soc.state | float(-1) }},
          "loads_total_kWh": {{ states.sensor.loads_daily.state | float(-1) }},
          "fromgrid_total_kWh": {{ states.sensor.grid_import_daily.state | float(-1) }},
          "togrid_total_kWh": {{ states.sensor.grid_export_daily.state | float(-1) }},
          "pv_total_kWh": {{ states.sensor.pv_daily.state | float(-1) }}
        }
```

> [!WARNING]
> Waarden kleiner dan 0 worden behandeld als ontbrekende gegevens (null). Tellers mogen worden gereset — je kunt bijvoorbeeld dagelijkse tellers versturen.

### Opmerkingen over gedeeltelijke import

- Je kunt **alleen optionele velden** versturen als de hoofdgegevens (SOC, verbruik enz.) rechtstreeks uit de omvormer worden geïmporteerd. Voeg in dat geval in het menu **IoT** het HomeAssistant-systeem toe en een teller voor elk type optionele gegevens.
- Het veld `pv_total_kWh` kan apart worden verstuurd — het wordt opgeteld bij de PV uit de omvormer als in **PV-prognose** -> **Corrigeren** -> **Bron van daadwerkelijke PV-productie** `HomeAssistant` is ingesteld.

### Opmerkingen voor Solarman / DeyeCloud

- De velden `soc_perc`, `fromgrid_total_kWh` en `togrid_total_kWh` kunnen apart worden verstuurd als de optie **„FromGrid-, ToGrid- en SOC-gegevens worden verzonden via HomeAssistant/SolarAssistant"** is aangevinkt
- Het veld `loads_total_kWh` kan apart worden verstuurd als **„Verbruiksgegevens worden verzonden door HomeAssistant/SolarAssistant"** is aangevinkt

## Commando's van GbbOptimizer ontvangen

GbbOptimizer verstuurt commando's naar de volgende topics (lokaal in HA zonder {{< glossary "PlantId" >}}-prefix):

| Topic | Bewerking |
|-------|----------|
| `ha_gbb/Start_Charge` | Start het laden van de batterij vanuit PV/net tot de ingestelde SOC |
| `ha_gbb/Start_Discharge` | Start het ontladen van de batterij naar het net tot de ingestelde SOC |
| `ha_gbb/Start_DisableCharge` | Laden van de batterij uitschakelen, PV gaat naar huis en net |
| `ha_gbb/Start_Normal` | Terug naar normale werking |
| `ha_gbb/EMS` | Verzameltopic met dezelfde gegevens als de bovenstaande commando's |

### Commando-payload

Elk commando verstuurt JSON met de volgende velden:

| Veld | Type | Beschrijving |
|------|-----|------|
| `Hour` | int | Uur |
| `FromMinute` | int | Beginminuut |
| `ToMinute` | int | Eindminuut |
| `DischargeLimitW` | int | Ontlaadlimiet (W) |
| `ChargeLimitW` | int | Laadlimiet (W) |
| `InputLimitW` | int | Limiet voor opname uit het net (W) |
| `PriceLessZero` | int | 0 = normale prijs, 1 = prijs < 0 |
| `Operation` | string | `"Normal"`, `"Discharge"`, `"DisableCharge"`, `"Charge"` |
| `SOC` | int | Doel-SOC-niveau |
| `V` | float | SOC omgerekend naar spanning (indien aansturing via V) |

### Voorbeeld van automatisering — reageren op een commando

```yaml
alias: mqtt_start_charge
trigger:
  - platform: mqtt
    topic: ha_gbb/Start_Charge
action:
  - service: switch.turn_on
    target:
      entity_id: switch.inverter_charge_from_grid
    data: {}
mode: single
```

> [!NOTE]
> Je moet zelf voor elk commando automatiseringen schrijven, afgestemd op jouw omvormer en configuratie. Het bovenstaande voorbeeld dient alleen ter illustratie.
