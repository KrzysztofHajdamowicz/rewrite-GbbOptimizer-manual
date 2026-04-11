---
title: "Wykresy"
weight: 40
translationKey: "wykresy"
---

# Wykresy w Home Assistant

GbbOptimizer udostępnia interaktywne wykresy (produkcja PV, zużycie, SOC, ceny energii itp.) przez interfejs webowy. Można je osadzić w dashboardzie Home Assistant.

## Osadzanie wykresów

Użyj karty **Webpage** (lub **iFrame**) w dashboardzie HA:

1. Przejdź do dashboardu HA -> **Edytuj** -> **Dodaj kartę**
2. Wybierz kartę **Webpage** (lub kartę ręczną typu `iframe`)
3. W polu URL wklej adres wykresów z GbbOptimizer

```yaml
type: iframe
url: "https://<serwer>.gbbsoft.pl/Charts?PlantId=<PlantId>"
aspect_ratio: "16:9"
```

Zamień `<serwer>` i `<PlantId>` na odpowiednie wartości Twojej instalacji.

> [!NOTE]
> Wykresy wymagają dostępu do internetu. Jeśli Home Assistant działa w sieci lokalnej bez dostępu do zewnętrznych usług, wykresy nie będą się ładować.

## Alternatywa — własne wykresy z danych MQTT

Jeśli wolisz tworzyć wykresy lokalnie, możesz użyć danych przesyłanych przez MQTT (patrz [Automatyzacja]({{< relref "/integracje/home-assistant/automatyzacja" >}})) w połączeniu z kartami typu:

- **ApexCharts Card** (HACS)
- **Mini Graph Card** (HACS)
- Wbudowane karty historii HA

### Gotowy pakiet — GBB Forecast Downloader

Dostępny jest gotowy pakiet Home Assistant, który automatycznie pobiera prognozę SOC baterii z GbbOptimizera przez MQTT i udostępnia ją jako sensor do wizualizacji w **ApexCharts Card**.

![Przykładowy wykres prognozy SOC baterii](https://github.com/user-attachments/assets/7e6d2477-d76e-4630-a835-b0d68d7e3699)

Pakiet tworzy sensor `sensor.gbb_battery_forecast`, który co 5 minut odpytuje API MQTT o prognozę i udostępnia dane w atrybutach (timestampy + wartości SOC). Prognoza wyświetlana jest jako linia przerywana na wykresie ApexCharts.

**Instalacja:**

1. Upewnij się, że masz skonfigurowany [most MQTT]({{< relref "/integracje/home-assistant/mosquitto-bridge" >}})
2. Skopiuj plik `gbb_battery_forecast.yaml` do katalogu `/config/packages/` w Home Assistant
3. Upewnij się, że packages są włączone w `configuration.yaml`:
   ```yaml
   homeassistant:
     packages: !include_dir_named packages
   ```
4. Zainstaluj **ApexCharts Card** z HACS
5. Zrestartuj Home Assistant

Pełna dokumentacja i plik YAML: [HomeAssistant-pull-forecast-from-GbbOptimizer](https://github.com/KrzysztofHajdamowicz/HomeAssistant-pull-forecast-from-GbbOptimizer)
