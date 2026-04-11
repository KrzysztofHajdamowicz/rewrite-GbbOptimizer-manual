---
title: "Hinen"
weight: 50
translationKey: "hinen"
---

# Hinen

Configuratie van de Hinen-omvormer met GbbOptimizer.

## Mapping van GbbOptimizer-modi op Hinen-instellingen

GbbOptimizer stuurt de Hinen-omvormer aan door de juiste **Work Mode** en de laad-/ontlaadparameters in te stellen.

| GbbOptimizer-bewerking | Work Mode | Charge/Discharge Enable | Start/End | SOC | Rate | AntiBackflow Enable | AntiBackflow Limit Rate |
|------------------------|-----------|------------------------|-----------|-----|------|---------------------|------------------------|
| **Normal** | Self-consumption | Nee | — | 100% | — | — | — |
| **Charge** | Time period control | Ja | Ja | Doel-SOC% | `ChargeLimit / (MaxInverterChargeDC of MaxBatteryChargeDC) * 100%` | Nee | — |
| **Discharge** | Time period control | Ja | Ja | Doel-SOC% | `DischargeLimit / (MaxInverterChargeDC of MaxBatteryChargeDC) * 100%` (negatieve waarde) | Ja | Zelfde als Rate, maar > 0 |
| **DisableCharge** | Time period control | Ja | Ja | Actuele SOC | 1% | Nee | — |

### Opmerkingen over de Discharge-bewerking

- De waarde `DischargeLimit` komt overeen met de parameter „Max {{< glossary "GridSetpoint" >}} / Discharge (W)"
- Als de ontlading trager moet om het hele uur te beslaan, corrigeert het programma deze waarde automatisch
- **AntiBackflow** wordt ingeschakeld tijdens het ontladen om de export naar het net te beheersen
