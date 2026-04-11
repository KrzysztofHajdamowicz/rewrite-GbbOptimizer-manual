---
title: "Victron"
weight: 50
translationKey: "victron-pasywny"
---

# Modusmapping — Victron

{{< badge "victron-only" >}}

Victron-omvormers worden aangestuurd door {{< glossary "ESS" >}} (Energy Storage System) via {{< glossary "VRM" >}} en MQTT.

## ESS-modus

GbbOptimizer stuurt het Victron-systeem aan via ESS-schema's (ESS Schedules) op de Cerbo GX. De schema's bepalen:

- **Werkmodus** — laden, ontladen, normale werking
- **Doel-SOC** — tot welk niveau laden/ontladen
- **Vermogensgrens** — maximaal laad-/ontlaadvermogen
- **Tijdvenster** — uren waarop het schema van toepassing is

## Initiële configuratie

1. Schakel in het {{< glossary "VRM" >}}-portaal externe toegang tot de Cerbo in
2. Stel in {{< glossary "ESS" >}} de modus **„Optimized (without BatteryLife)"** in
3. Zorg ervoor dat GbbOptimizer de juiste VRM-gegevens heeft ({{< glossary "PlantId" >}}, {{< glossary "PlantToken" >}})

> [!NOTE]
> Als **Battery Life** in ESS is ingeschakeld, kan GbbOptimizer de batterij niet volledig aansturen. Schakel het uit en stel in op **„Optimized (without BatteryLife)"**.

## Aansturing

GbbOptimizer communiceert met de Cerbo via de MQTT-servers van Victron. In elke optimalisatiecyclus voert het programma de volgende stappen uit:

1. Leest actuele gegevens (SOC, PV-productie, verbruik, netstatus)
2. Berekent het optimale schema
3. Schrijft de ESS-schema's naar de Cerbo

Gedetailleerde informatie over de Victron MQTT-topics is beschikbaar in de MQTT API-documentatie.

## Meer informatie

- [Victron ESS-documentatie](https://www.victronenergy.com/media/pg/Energy_Storage_System/en/index-en.html)
- [VRM Portal](https://vrm.victronenergy.com/)
