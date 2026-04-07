---
title: "Tematy Home Assistant"
weight: 40
translationKey: "tematy-ha"
---

# Tematy MQTT dla Home Assistant

Tematy używane do komunikacji między GbbOptimizer a Home Assistant / GbbConnect.

## Dane z Home Assistant do GbbOptimizer

{{< mqtt-topic topic="{PlantId}/ha_gbb/sensor" direction="subscribe" qos="0" description="Dane z czujników HA — liczniki narastające" >}}

**Wymagane pola:**

| Pole | Typ | Opis |
|------|-----|------|
| `soc_perc` | decimal | SOC baterii (%). Użyj `V` jeśli zaznaczono „Steruj poprzez V” |
| `loads_total_kWh` | decimal | Zużycie — licznik narastający |
| `fromgrid_total_kWh` | decimal | Import z sieci — licznik narastający |
| `togrid_total_kWh` | decimal | Eksport do sieci — licznik narastający |
| `pv_total_kWh` | decimal | Produkcja PV — licznik narastający |

**Opcjonalne pola:**

| Pole | Typ | Opis |
|------|-----|------|
| `ev_charge_total_kWh` | decimal | Ładowanie EV |
| `hp_total_kWh` | decimal | Pompa ciepła |
| `other1_total_kWh` – `other6_total_kWh` | decimal | Inne 1–6 |

**Wiele źródeł PV:**

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
> - Liczniki mogą się zerować — można przesyłać np. liczniki dzienne
> - Wartości < 0 są traktowane jako brak danych
> - Można wysyłać tylko dane opcjonalne, jeśli główne dane importowane są z falownika. W takim przypadku dodaj system HomeAssistant w menu IoT
> - `pv_total_kWh` to to samo co `"more"` z `number=1` — nie używaj obu jednocześnie
> - Solarman/DeyeCloud: poszczególne pola (`soc_perc`, `fromgrid_total_kWh`, `togrid_total_kWh`, `loads_total_kWh`) mogą być wysyłane oddzielnie, jeśli zaznaczono odpowiednie opcje w [parametrach instalacji]({{< relref "/instalacja/parametry-instalacji" >}})

## Komendy z GbbOptimizer do Home Assistant

GbbOptimizer wysyła komendy sterujące na dedykowane tematy:

{{< mqtt-topic topic="{PlantId}/ha_gbb/Start_Charge" direction="publish" description="Rozpocznij ładowanie baterii do SOC z Payload" >}}

{{< mqtt-topic topic="{PlantId}/ha_gbb/Start_Discharge" direction="publish" description="Rozpocznij rozładowanie baterii do sieci (do SOC z Payload)" >}}

{{< mqtt-topic topic="{PlantId}/ha_gbb/Start_DisableCharge" direction="publish" description="Nie ładuj baterii — PV do domu i sieci" >}}

{{< mqtt-topic topic="{PlantId}/ha_gbb/Start_Normal" direction="publish" description="Powrót do normalnej pracy" >}}

Równolegle te same dane wysyłane są na:

{{< mqtt-topic topic="{PlantId}/ha_gbb/EMS" direction="publish" description="Zbiorcza komenda EMS z pełnym payloadem JSON" >}}

**Payload JSON:**

| Pole | Typ | Opis |
|------|-----|------|
| `Hour` | int | Godzina |
| `FromMinute` | int | Minuta rozpoczęcia |
| `ToMinute` | int | Minuta zakończenia |
| `DischargeLimitW` | int | Limit rozładowania (W) |
| `ChargeLimitW` | int | Limit ładowania (W) |
| `InputLimitW` | int | Limit importu (W) |
| `PriceLessZero` | int | 0 = normalna cena, 1 = cena < 0 |
| `Operation` | string | `"Normal"`, `"Discharge"`, `"DisableCharge"` lub `"Charge"` |
| `SOC` | int | Docelowy SOC |
| `V` | decimal | SOC skonwertowany na V (jeśli sterowanie przez V) |

**Przykład:**
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

## Przykład automatyzacji HA

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

## Przykład publikowania danych do MQTT

```yaml
alias: mqtt_publikacja
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
