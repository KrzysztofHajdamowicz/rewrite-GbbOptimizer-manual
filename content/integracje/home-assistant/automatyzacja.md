---
title: "Automatyzacja"
weight: 30
---

# Automatyzacja Home Assistant

Po skonfigurowaniu [Mosquitto Bridge]({{< relref "/integracje/home-assistant/mosquitto-bridge" >}}) mozesz tworzyc automatyzacje w Home Assistant, ktore:

- **Wysylaja dane** z czujnikow HA do GbbOptimizer
- **Reaguja na komendy** otrzymane z GbbOptimizer

## Wysylanie danych do GbbOptimizer

GbbOptimizer oczekuje danych na topiku `ha_gbb/sensor` (lokalnie w HA; przez bridge trafia jako `<PlantId>/ha_gbb/sensor`).

### Wymagane pola

| Pole | Opis |
|------|------|
| `soc_perc` | {{< glossary "SOC" >}} baterii w procentach (lub `V` jesli zaznaczono sterowanie przez napiecie) |
| `loads_total_kWh` | Licznik zuzycia (kWh, narastajaco) |
| `fromgrid_total_kWh` | Licznik energii pobranej z sieci (kWh) |
| `togrid_total_kWh` | Licznik energii wyslnej do sieci (kWh) |
| `pv_total_kWh` | Licznik produkcji PV (kWh) |

### Pola opcjonalne

| Pole | Opis |
|------|------|
| `ev_charge_total_kWh` | Licznik ladowania EV |
| `hp_total_kWh` | Licznik pompy ciepla |
| `other1_total_kWh` ... `other6_total_kWh` | Dodatkowe liczniki |

### Wiele instalacji PV

Aby wyslac dane z kilku plaszczyzn PV, uzyj pola `more`:

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
> Glowne `pv_total_kWh` odpowiada `number: 1`. Uzywaj albo `pv_total_kWh`, albo `number: 1` w `more` — nie obu jednoczesnie. Odpowiedni numer musi byc skonfigurowany w ustawieniach Plaszczyzny PV -> HomeAssistant.

### Przyklad automatyzacji — publikacja danych

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
> Wartosci mniejsze od 0 sa traktowane jako brak danych (null). Liczniki moga sie zerowac — mozna przesylac np. liczniki dzienne.

### Uwagi dotyczace czesciowego importu danych

- Mozna wysylac **tylko pola opcjonalne**, jesli glowne dane (SOC, zuzycie itp.) sa importowane bezposrednio z falownika. W takim przypadku w menu **IoT** dodaj system HomeAssistant i licznik dla kazdego typu danych opcjonalnych.
- Pole `pv_total_kWh` mozna wysylac osobno — zostanie dodane do PV z falownika, jesli w **Prognoza PV** -> **Popraw** -> **Zrodlo danych rzeczywistej produkcji PV** ustawiono `HomeAssistant`.

### Uwagi dla Solarman / DeyeCloud

- Pola `soc_perc`, `fromgrid_total_kWh` i `togrid_total_kWh` mozna wysylac oddzielnie, jesli zaznaczono opcje **"Dane FromGrid, ToGrid i SOC sa wyslane przez HomeAssistant/SolarAssistant"**
- Pole `loads_total_kWh` mozna przesylac oddzielnie, jesli zaznaczono **"Dane Zuzycia sa wyslane z HomeAssistant/SolarAssistant"**

## Odbieranie komend z GbbOptimizer

GbbOptimizer wysyla komendy na nastepujace topiki (lokalnie w HA bez prefixu {{< glossary "PlantId" >}}):

| Topik | Operacja |
|-------|----------|
| `ha_gbb/Start_Charge` | Rozpocznij ladowanie baterii z PV/sieci do zadanego SOC |
| `ha_gbb/Start_Discharge` | Rozpocznij rozladowanie baterii do sieci do zadanego SOC |
| `ha_gbb/Start_DisableCharge` | Wylacz ladowanie baterii, PV idzie do domu i sieci |
| `ha_gbb/Start_Normal` | Powrot do normalnej pracy |
| `ha_gbb/EMS` | Zbiorczy topik z tymi samymi danymi co powyzsze komendy |

### Payload komend

Kazda komenda wysyla JSON z nastepujacymi polami:

| Pole | Typ | Opis |
|------|-----|------|
| `Hour` | int | Godzina |
| `FromMinute` | int | Minuta poczatkowa |
| `ToMinute` | int | Minuta koncowa |
| `DischargeLimitW` | int | Limit rozladowania (W) |
| `ChargeLimitW` | int | Limit ladowania (W) |
| `InputLimitW` | int | Limit poboru z sieci (W) |
| `PriceLessZero` | int | 0 = cena normalna, 1 = cena < 0 |
| `Operation` | string | `"Normal"`, `"Discharge"`, `"DisableCharge"`, `"Charge"` |
| `SOC` | int | Docelowy poziom SOC |
| `V` | float | SOC przeliczone na napiecie (jesli sterowanie przez V) |

### Przyklad automatyzacji — reakcja na komende

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
> Musisz samodzielnie napisac automatyzacje dla kazdej komendy, dostosowane do Twojego falownika i konfiguracji. Powyzszy przyklad jest tylko ilustracja.
