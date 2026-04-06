---
title: "Hinen"
weight: 30
---

# Mapowanie trybow — Hinen

Jak tryby GbbOptimizer przekladaja sie na ustawienia protokolu Hinen.

## Tabela mapowania

| Operacja | Work Mode | Charge/Discharge Enable | Charge/Discharge Start/End | Charge/Discharge SOC | Charge/Discharge Rate | AntiBackflow Enable | AntiBackflow Limit Rate |
|----------|-----------|------------------------|---------------------------|---------------------|----------------------|--------------------|-----------------------|
| **Normal** | Self-consumption | nie | — | 100% | — | — | — |
| **Charge** | Time period control | tak | tak | SOC% | = ChargeLimit / (MaxInverterChargeDC_kW lub MaxBatteryChargeDC_kW) * 100% | nie | — |
| **Discharge** | Time period control | tak | tak | SOC% | = -abs(DischargeLimit) / (MaxInverterChargeDC_kW lub MaxBatteryChargeDC_kW) * 100%. DischargeLimit = Max GridSetpoint / Discharge (W). Jesli rozladowanie musi byc wolniejsze — program oblicza wartosc. | tak | taki sam jak Charge/Discharge Rate, ale > 0 |
| **DisableCharge** | Time period control | tak | tak | aktualny SOC | 1% | nie | — |

## Uwagi

- **Rate** jest wyrazany jako procent maksymalnej mocy falownika (lub baterii), a nie w watach
- W trybie **Normal** system wraca do trybu Self-consumption z SOC = 100% i wylaczonym Charge/Discharge
- W trybie **DisableCharge** SOC jest ustawiany na aktualny poziom, a Rate na minimalne 1%
