---
title: "Afore"
weight: 40
translationKey: "afore"
---

# Afore

Configuratie van de Afore-omvormer met GbbOptimizer. GbbOptimizer stuurt de Afore-omvormer aan via het {{< glossary "Modbus" >}}-protocol.

## Mapping van GbbOptimizer-modi op Afore-instellingen

| Bewerking | Register | Waarde | Na afloop |
|----------|---------|---------|----------------|
| **AC charging maximum SOC** | Laden: doel-{{< glossary "MaxSOC" >}} | — | — |
| **ACCharging start/end time (1-4)** | Laden: array van de volgende 4 perioden | — | — |
| **Forced charging start/end time (1-4)** | Laden: array van de volgende 4 perioden | — | — |
| **ACCharging power percentage** | Laden: Input Limit | % van MaxBuyPower of MaxBatteryChargeDC | Oorspronkelijke waarde herstellen |
| **Forced charging power percentage** | Laden: Charge Limit | % van MaxBatteryChargeDC | Oorspronkelijke waarde herstellen |
| **Minimum SOC for forced discharge** | Ontladen: doel-{{< glossary "MinSOC" >}} | — | — |
| **Forced discharge start time (1-4)** | Ontladen: array van de volgende 4 perioden | — | — |
| **Power grid power limit percentage** | Ontladen: {{< glossary "GridSetpoint" >}} | % van MaxSellPower of MaxBatteryDischargeDC | — |
| **Maximum charging current** | Laadblokkering: ingesteld op `0` | — | Oorspronkelijke waarde herstellen |

## Checklist

- **Timing DChg ON/OFF** = `Enable`
- **PDisChgMax** (Forced discharge power percentage) = `100%`
