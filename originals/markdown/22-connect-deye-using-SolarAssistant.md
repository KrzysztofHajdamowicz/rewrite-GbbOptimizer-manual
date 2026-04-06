Zobacz początek konfiguracji [tutaj](https://gbbvictronweb.gbbsoft.pl/Manual?Filters.PageNo=9)

## Obsługiwane konfiguracje:

- HomeAssistant (HA) z SolarAssistant (SA) podłaczone z inwerterem hybrydowym Deye jako "inverter\_1"

## Uwagi:

- W ustawieniach SolarAssistant w "configuration" -> "Advance MQTT": zmień "Allow setting changes" na "Enabled"
- SolarAssistant aktualnie nie pozwala zdalnie zmieniać godziny
  początkowej w tablicy 'TimeOfUse', więc GbbOptimizer ustawia
  wszystkie wiersze godzin na te same wartości.
- SolarAssistant aktualnie także nie poznala zmieniać Power w 'TimeOfUse'.
- W konfiguracji Bridge powinieneś zmienić topic na następujący: **topic # both 2 solar\_assistant/ <plantID>/solar\_assistant/**

##

## HomeAssistant (HA) z SolarAssistant (SA) podłaczone z inwerterem hybrydowym Deye jako "inverter\_1"

GbbOptimizer uzywa następująch ścieżek w mqtt:

Odczyt:

{PlantId}/solar\_assistant/total/battery\_state\_of\_charge/state
albo {PlantId}/solar\_assistant/inverter\_1/battery\_voltage (jeżeli zaznaczono 'Steruj poprzez V a nie przez SOC (Deye)')
{PlantId}/solar\_assistant/total/grid\_energy\_in/state
{PlantId}/solar\_assistant/total/grid\_energy\_out/state
{PlantId}/solar\_assistant/total/load\_energy/state
{PlantId}/solar\_assistant/total/pv\_energy/state
{PlantId}/solar\_assistant/inverter\_1/work\_mode/state
{PlantId}/solar\_assistant/inverter\_1/max\_charge\_current/state

Zapis:

{PlantId}/solar\_assistant/inverter\_1/capacity\_point\_{i}/set
albo {PlantId}/solar\_assistant/inverter\_1/voltage\_point\_{i}/set (jeżeli
zaznaczono 'Steruj poprzez V a nie przez SOC (Deye)')
{PlantId}/solar\_assistant/inverter\_1/grid\_charge\_point\_{i}/set
{PlantId}/solar\_assistant/inverter\_1/work\_mode/set
{PlantId}/solar\_assistant/inverter\_1/max\_charge\_current/set

Więcej informacji o SolarAssistant: <https://solar-assistant.io/help/integration/mqtt>

## Solarman/DeyeCloud: weź Zużycie z SA

W instalacji Deye z Solarman (lub DeyeCloud) Zużycie może być importowane z SA a nie z inwertera:

1. W HA stwórz plik /share/mosquitto/GbbOptimizer.conf, patrz: [Jak zintegrować z HomeAssistant?](https://gbboptimizer10.gbbsoft.pl/Manual?Filters.PageNo=9)
2. W konfiguracji bridge należy dodać nastepujący topic:

**topic # both 2 solar\_assistant/total/load\_energy/ <PlantId>/solar\_assistant/total/load\_energy/**

3. W parametrach instalacji zaznacz "Dane Zużycia są wysyłane z HomeAssistant/SolarAssistant a nie pobierane z invertera"
