---
title: "Automatyzacja"
weight: 30
translationKey: "automatyzacja"
---

# Automatyzacja Home Assistant

Po skonfigurowaniu [Mosquitto Bridge]({{< relref "/integracje/home-assistant/mosquitto-bridge" >}}) możesz tworzyć automatyzacje w Home Assistant, które:

- **Wysyłają dane** z czujników HA do GbbOptimizer
- **Reagują na komendy** otrzymane z GbbOptimizer

## Wysyłanie danych do GbbOptimizer

GbbOptimizer oczekuje danych na topiku `ha_gbb/sensor` (lokalnie w HA; przez bridge trafia jako `<PlantId>/ha_gbb/sensor`).

### Wymagane pola

| Pole | Opis |
|------|------|
| `soc_perc` | {{< glossary "SOC" >}} baterii w procentach (lub `V` jeśli zaznaczono sterowanie przez napięcie) |
| `loads_total_kWh` | Licznik zużycia (kWh, narastająco) |
| `fromgrid_total_kWh` | Licznik energii pobranej z sieci (kWh) |
| `togrid_total_kWh` | Licznik energii wysłanej do sieci (kWh) |
| `pv_total_kWh` | Licznik produkcji PV (kWh) |

### Pola opcjonalne

| Pole | Opis |
|------|------|
| `ev_charge_total_kWh` | Licznik ładowania EV |
| `hp_total_kWh` | Licznik pompy ciepła |
| `other1_total_kWh` ... `other6_total_kWh` | Dodatkowe liczniki |

### Wiele instalacji PV

Aby wysłać dane z kilku płaszczyzn PV, użyj pola `more`:

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
> Główne `pv_total_kWh` odpowiada `number: 1`. Używaj albo `pv_total_kWh`, albo `number: 1` w `more` — nie obu jednocześnie. Odpowiedni numer musi być skonfigurowany w ustawieniach Płaszczyzny PV -> HomeAssistant.

### Przykład automatyzacji — publikacja danych

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
> Wartości mniejsze od 0 są traktowane jako brak danych (null). Liczniki mogą się zerować — można przesyłać np. liczniki dzienne.

### Uwagi dotyczące częściowego importu danych

- Można wysyłać **tylko pola opcjonalne**, jeśli główne dane (SOC, zużycie itp.) są importowane bezpośrednio z falownika. W takim przypadku w menu **IoT** dodaj system HomeAssistant i licznik dla każdego typu danych opcjonalnych.
- Pole `pv_total_kWh` można wysyłać osobno — zostanie dodane do PV z falownika, jeśli w **Prognoza PV** -> **Popraw** -> **Źródło danych rzeczywistej produkcji PV** ustawiono `HomeAssistant`.

### Uwagi dla Solarman / DeyeCloud

- Pola `soc_perc`, `fromgrid_total_kWh` i `togrid_total_kWh` można wysyłać oddzielnie, jeśli zaznaczono opcję **"Dane FromGrid, ToGrid i SOC są wysyłane przez HomeAssistant/SolarAssistant"**
- Pole `loads_total_kWh` można przesyłać oddzielnie, jeśli zaznaczono **"Dane Zużycia są wysyłane z HomeAssistant/SolarAssistant"**

## Odbieranie komend z GbbOptimizer

GbbOptimizer wysyła komendy na następujące topiki (lokalnie w HA bez prefixu {{< glossary "PlantId" >}}):

| Topik | Operacja |
|-------|----------|
| `ha_gbb/Start_Charge` | Rozpocznij ładowanie baterii z PV/sieci do zadanego SOC |
| `ha_gbb/Start_Discharge` | Rozpocznij rozładowanie baterii do sieci do zadanego SOC |
| `ha_gbb/Start_DisableCharge` | Wyłącz ładowanie baterii, PV idzie do domu i sieci |
| `ha_gbb/Start_Normal` | Powrót do normalnej pracy |
| `ha_gbb/EMS` | Zbiorczy topik z tymi samymi danymi co powyższe komendy |

### Payload komend

Każda komenda wysyła JSON z następującymi polami:

| Pole | Typ | Opis |
|------|-----|------|
| `Hour` | int | Godzina |
| `FromMinute` | int | Minuta początkowa |
| `ToMinute` | int | Minuta końcowa |
| `DischargeLimitW` | int | Limit rozładowania (W) |
| `ChargeLimitW` | int | Limit ładowania (W) |
| `InputLimitW` | int | Limit poboru z sieci (W) |
| `PriceLessZero` | int | 0 = cena normalna, 1 = cena < 0 |
| `Operation` | string | `"Normal"`, `"Discharge"`, `"DisableCharge"`, `"Charge"` |
| `SOC` | int | Docelowy poziom SOC |
| `V` | float | SOC przeliczone na napięcie (jeśli sterowanie przez V) |

### Przykład automatyzacji — reakcja na komendę

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
> Musisz samodzielnie napisać automatyzacje dla każdej komendy, dostosowane do Twojego falownika i konfiguracji. Powyższy przykład jest tylko ilustracja.
