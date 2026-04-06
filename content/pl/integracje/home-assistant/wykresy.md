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
