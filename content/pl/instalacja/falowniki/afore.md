---
title: "Afore"
weight: 40
translationKey: "afore"
---

# Afore

Konfiguracja falownika Afore z GbbOptimizer. GbbOptimizer steruje falownikiem Afore przez protokół {{< glossary "Modbus" >}}.

## Mapowanie trybów GbbOptimizer na ustawienia Afore

| Operacja | Rejestr | Wartość | Po zakończeniu |
|----------|---------|---------|----------------|
| **AC charging maximum SOC** | Ładowanie: docelowy {{< glossary "MaxSOC" >}} | — | — |
| **ACCharging start/end time (1-4)** | Ładowanie: tablica następnych 4 okresów | — | — |
| **Forced charging start/end time (1-4)** | Ładowanie: tablica następnych 4 okresów | — | — |
| **ACCharging power percentage** | Ładowanie: Input Limit | % z MaxBuyPower lub MaxBatteryChargeDC | Przywrócenie oryginalnej wartości |
| **Forced charging power percentage** | Ładowanie: Charge Limit | % z MaxBatteryChargeDC | Przywrócenie oryginalnej wartości |
| **Minimum SOC for forced discharge** | Rozładowanie: docelowy {{< glossary "MinSOC" >}} | — | — |
| **Forced discharge start time (1-4)** | Rozładowanie: tablica następnych 4 okresów | — | — |
| **Power grid power limit percentage** | Rozładowanie: {{< glossary "GridSetpoint" >}} | % z MaxSellPower lub MaxBatteryDischargeDC | — |
| **Maximum charging current** | Blokada ładowania: ustawia `0` | — | Przywrócenie oryginalnej wartości |

## Lista kontrolna

- **Timing DChg ON/OFF** = `Enable`
- **PDisChgMax** (Forced discharge power percentage) = `100%`
