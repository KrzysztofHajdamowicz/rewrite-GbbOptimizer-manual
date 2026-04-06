---
title: "GoodWe"
weight: 20
---

# Mapowanie trybow — GoodWe

Jak tryby GbbOptimizer przekladaja sie na ustawienia protokolu GoodWe.

## Battery Charge-Discharge

| Operacja | BatteryCDEnable | BatteryCDMode | BatteryCDPW |
|----------|----------------|---------------|-------------|
| **Normal** | nie | — | — |
| **Charge** | tak | 2 | ChargeLimitW |
| **Discharge** | tak | 3 | DischargeLimitW: Max GridSetpoint / Discharge (W). Jesli rozladowanie musi byc wolniejsze, aby trwalo cala godzine — program oblicza odpowiednia wartosc. Po zakonczeniu: powrot do poprzedniej wartosci. |
| **DisableCharge** | tak | 2 | 0 |

## Brakujace opcje

> [!WARNING]
> Protokol GoodWe nie obsluguje:
> - Limitu docelowego {{< glossary "SOC" >}} (TargetSOC)
> - Opcji dla ceny < 0
