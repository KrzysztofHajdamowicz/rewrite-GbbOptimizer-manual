---
title: "Victron"
weight: 50
---

# Mapowanie trybów — Victron

{{< badge "victron-only" >}}

Falowniki Victron są sterowane przez {{< glossary "ESS" >}} (Energy Storage System) za pośrednictwem {{< glossary "VRM" >}} i MQTT.

## Tryb ESS

GbbOptimizer steruje systemem Victron poprzez harmonogramy ESS (ESS Schedules) na Cerbo GX. Harmonogramy określają:

- **Tryb pracy** — ładowanie, rozładowanie, normalna praca
- **Docelowy SOC** — do jakiego poziomu ładować/rozładowywać
- **Limit mocy** — maksymalna moc ładowania/rozładowania
- **Okno czasowe** — godziny obowiązywania harmonogramu

## Konfiguracja wstępna

1. W portalu {{< glossary "VRM" >}} włącz dostęp zdalny do Cerbo
2. W {{< glossary "ESS" >}} ustaw tryb **"Optimized (without BatteryLife)"**
3. Upewnij się, że GbbOptimizer ma poprawne dane VRM ({{< glossary "PlantId" >}}, {{< glossary "PlantToken" >}})

> [!NOTE]
> Jeśli **Battery Life** jest włączony w ESS, GbbOptimizer nie będzie mógł w pełni kontrolować baterii. Wyłącz go i ustaw na **"Optimized (without BatteryLife)"**.

## Sterowanie

GbbOptimizer komunikuje się z Cerbo przez serwery MQTT Victrona. W każdym cyklu optymalizacji program:

1. Odczytuje aktualne dane (SOC, produkcja PV, zużycie, stan sieci)
2. Oblicza optymalny harmonogram
3. Zapisuje harmonogramy ESS na Cerbo

Szczegółowe informacje o topicach MQTT Victron dostępne są w dokumentacji API MQTT.

## Więcej informacji

- [Dokumentacja Victron ESS](https://www.victronenergy.com/media/pg/Energy_Storage_System/en/index-en.html)
- [VRM Portal](https://vrm.victronenergy.com/)
