---
title: "Victron"
weight: 50
---

# Mapowanie trybow — Victron

{{< badge "victron-only" >}}

Falowniki Victron sa sterowane przez {{< glossary "ESS" >}} (Energy Storage System) za posrednictwem {{< glossary "VRM" >}} i MQTT.

## Tryb ESS

GbbOptimizer steruje systemem Victron poprzez harmonogramy ESS (ESS Schedules) na Cerbo GX. Harmonogramy okreslaja:

- **Tryb pracy** — ladowanie, rozladowanie, normalna praca
- **Docelowy SOC** — do jakiego poziomu ladowac/rozladowywac
- **Limit mocy** — maksymalna moc ladowania/rozladowania
- **Okno czasowe** — godziny obowiazywania harmonogramu

## Konfiguracja wstepna

1. W {{< glossary "VRM" >}} portal wlacz dostep zdalny do Cerbo
2. W {{< glossary "ESS" >}} ustaw tryb **"Optimized (without BatteryLife)"**
3. Upewnij sie, ze GbbOptimizer ma poprawne dane VRM ({{< glossary "PlantId" >}}, {{< glossary "PlantToken" >}})

> [!NOTE]
> Jesli **Battery Life** jest wlaczony w ESS, GbbOptimizer nie bedzie mogl w pelni kontrolowac baterii. Wylacz go i ustaw na **"Optimized (without BatteryLife)"**.

## Sterowanie

GbbOptimizer komunikuje sie z Cerbo przez serwery MQTT Victrona. W kazdym cyklu optymalizacji program:

1. Odczytuje aktualne dane (SOC, produkcja PV, zuzycie, stan sieci)
2. Oblicza optymalny harmonogram
3. Zapisuje harmonogramy ESS na Cerbo

Szczegolowe informacje o topikach MQTT Victron dostepne sa w dokumentacji API MQTT.

## Wiecej informacji

- [Dokumentacja Victron ESS](https://www.victronenergy.com/media/pg/Energy_Storage_System/en/index-en.html)
- [VRM Portal](https://vrm.victronenergy.com/)
