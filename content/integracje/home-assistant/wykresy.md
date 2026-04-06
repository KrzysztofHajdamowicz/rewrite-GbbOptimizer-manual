---
title: "Wykresy"
weight: 40
---

# Wykresy w Home Assistant

GbbOptimizer udostepnia interaktywne wykresy (produkcja PV, zuzycie, SOC, ceny energii itp.) przez interfejs webowy. Mozna je osadzic w dashboardzie Home Assistant.

## Osadzanie wykresow

Uzyj karty **Webpage** (lub **iFrame**) w dashboardzie HA:

1. Przejdz do dashboardu HA -> **Edytuj** -> **Dodaj karte**
2. Wybierz karte **Webpage** (lub karte reczna typu `iframe`)
3. W polu URL wklej adres wykresow z GbbOptimizer

```yaml
type: iframe
url: "https://<serwer>.gbbsoft.pl/Charts?PlantId=<PlantId>"
aspect_ratio: "16:9"
```

Zamien `<serwer>` i `<PlantId>` na odpowiednie wartosci Twojej instalacji.

> [!NOTE]
> Wykresy wymagaja dostepu do internetu. Jesli Home Assistant dziala w sieci lokalnej bez dostepu do zewnetrznych uslug, wykresy nie beda sie ladowac.

## Alternatywa — wlasne wykresy z danych MQTT

Jesli wolisz tworzyc wykresy lokalnie, mozesz uzyc danych przesylanych przez MQTT (patrz [Automatyzacja]({{< relref "/integracje/home-assistant/automatyzacja" >}})) w polaczeniu z kartami typu:

- **ApexCharts Card** (HACS)
- **Mini Graph Card** (HACS)
- Wbudowane karty historii HA
