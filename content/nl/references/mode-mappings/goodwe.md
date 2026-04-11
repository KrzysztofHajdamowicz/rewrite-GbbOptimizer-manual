---
title: "GoodWe"
weight: 20
translationKey: "mapowania-goodwe"
---

# Modusmapping — GoodWe

Hoe de GbbOptimizer-modi zich vertalen naar de instellingen van het GoodWe-protocol.

## Battery Charge-Discharge

| Operatie | BatteryCDEnable | BatteryCDMode | BatteryCDPW |
|----------|----------------|---------------|-------------|
| **Normal** | nee | — | — |
| **Charge** | ja | 2 | ChargeLimitW |
| **Discharge** | ja | 3 | DischargeLimitW: Max GridSetpoint / Discharge (W). Als het ontladen langzamer moet gaan om een heel uur te duren, berekent het programma de juiste waarde. Na afloop: terug naar vorige waarde. |
| **DisableCharge** | ja | 2 | 0 |

## Ontbrekende opties

> [!WARNING]
> Het GoodWe-protocol ondersteunt niet:
> - Een limiet voor de doel-{{< glossary "SOC" >}} (TargetSOC)
> - Opties voor prijs < 0
