---
title: "Hinen"
weight: 30
translationKey: "mapowania-hinen"
---

# Modusmapping — Hinen

Hoe de GbbOptimizer-modi zich vertalen naar de instellingen van het Hinen-protocol.

## Mappingtabel

| Operatie | Work Mode | Charge/Discharge Enable | Charge/Discharge Start/End | Charge/Discharge SOC | Charge/Discharge Rate | AntiBackflow Enable | AntiBackflow Limit Rate |
|----------|-----------|------------------------|---------------------------|---------------------|----------------------|--------------------|-----------------------|
| **Normal** | Self-consumption | nee | — | 100% | — | — | — |
| **Charge** | Time period control | ja | ja | SOC% | = ChargeLimit / (MaxInverterChargeDC_kW of MaxBatteryChargeDC_kW) * 100% | nee | — |
| **Discharge** | Time period control | ja | ja | SOC% | = -abs(DischargeLimit) / (MaxInverterChargeDC_kW of MaxBatteryChargeDC_kW) * 100%. DischargeLimit = Max GridSetpoint / Discharge (W). Als het ontladen langzamer moet — het programma berekent de waarde. | ja | gelijk aan Charge/Discharge Rate, maar > 0 |
| **DisableCharge** | Time period control | ja | ja | huidige SOC | 1% | nee | — |

## Opmerkingen

- **Rate** wordt uitgedrukt als percentage van het maximale vermogen van de omvormer (of batterij), niet in watt
- In de modus **Normal** keert het systeem terug naar Self-consumption met SOC = 100% en Charge/Discharge uitgeschakeld
- In de modus **DisableCharge** wordt SOC ingesteld op het huidige niveau en Rate op het minimum van 1%
