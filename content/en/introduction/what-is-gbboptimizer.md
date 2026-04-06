---
title: "What is GbbOptimizer"
weight: 10
translationKey: "czym-jest-gbboptimizer"
---

# What is GbbOptimizer

GbbOptimizer (formerly GbbVictronWeb) is a program that optimizes energy use in a home photovoltaic installation with an energy storage system (battery). It analyzes PV production forecasts, energy consumption profiles, and purchase and sale prices to automatically control the inverter — deciding when to charge the battery, when to discharge it, and when to buy or sell energy from/to the grid.

## How it works

The program runs in the cloud and communicates with the inverter over the internet. It performs calculations every hour and sends commands to the inverter.

```
┌─────────────────────────────────────────────────────────────────┐
│                       GbbOptimizer (cloud)                      │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   │
│  │ PV Forecast  │  │  Consumption │  │  Purchase and sale   │   │
│  │ (Solcast,    │  │  profile     │  │  prices              │   │
│  │ forecast.    │  │  (home)      │  │  (tariffs, exchange) │   │
│  │  solar)      │  │              │  │                      │   │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬───────────┘   │
│         │                 │                     │               │
│         └─────────────────┼─────────────────────┘               │
│                           │                                     │
│                    ┌──────▼───────┐                             │
│                    │  Optimizer   │                             │
│                    │  (Battery    │                             │
│                    │   Forecast)  │                             │
│                    └──────┬───────┘                             │
│                           │                                     │
│              Charge / discharge schedule                        │
│              + inverter operating mode                          │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                    ┌───────▼────────┐
                    │   Connection   │
                    │  (VRM, MQTT,   │
                    │  Solarman,     │
                    │  GbbConnect2)  │
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │    Hybrid      │
                    │   inverter     │
                    │  + battery     │
                    └────────────────┘
```

Each installation has a unique {{< glossary "PlantId" >}} and {{< glossary "PlantToken" >}}, which are used to identify and authorize communication.

## Four operating modes

The optimizer switches the inverter between four modes depending on the current price situation and battery state:

| Mode | Description |
|------|-------------|
| **Normal** | Standard inverter operation — battery charges from PV, home powered from PV and battery. PV surpluses can be exported to the grid |
| **Charge** | Charging the battery from the grid. Used when the purchase price is low (e.g. night tariff, negative exchange prices) |
| **Discharge** | Forced battery discharge to the grid. Used when the sale price is high and it is profitable to sell energy |
| **DisableCharge** | Block charging from PV. Used to leave room in the battery for later cheap grid charging |

Configuration details for charging can be found in the [Charging module]({{< relref "/konfiguracja/ladowanie" >}}), and for discharging in the [Discharge module]({{< relref "/konfiguracja/rozladowanie" >}}).

## Price-based optimizer

By default, the "Price-based optimizer" is selected. It analyzes purchase and sale prices for the coming hours and plans:

- **When to charge** — looks for hours with the lowest purchase price
- **When to discharge** — looks for hours with the highest sale price
- **How much to charge** — takes into account the PV forecast (to avoid grid-charging what PV will produce anyway) and the battery's {{< glossary "MaxSOC" >}}
- **How much to discharge** — takes into account the home consumption forecast and the battery's {{< glossary "MinSOC" >}}

The entire plan is visualized in the [Battery Forecast]({{< relref "/konfiguracja/prognoza-baterii" >}}) module.

## Key parameters

- {{< glossary "SOC" >}} — current battery charge level
- {{< glossary "MinSOC" >}} — minimum battery level (protection)
- {{< glossary "MaxSOC" >}} — maximum charge level (recommended 90%)
- {{< glossary "GridSetpoint" >}} — target grid exchange power
- {{< glossary "RTE" >}} — round-trip efficiency of the charge/discharge cycle
- {{< glossary "Correction Factor" >}} — coefficient correcting the PV forecast (auto-calibrates over ~one week)

## Supported inverters

GbbOptimizer supports the following hybrid inverters:

| Inverter | Connection methods |
|----------|--------------------|
| **Victron** | VRM Portal (native), Home Assistant |
| **Deye** | DeyeCloud, Solarman, Home Assistant, {{< glossary "GbbConnect2" >}}, {{< glossary "DongleDirect" >}} |
| **GoodWe** | Solarman, Home Assistant, {{< glossary "GbbConnect2" >}} |
| **Afore** | Solarman, {{< glossary "GbbConnect2" >}} |
| **Hinen** | Solarman, {{< glossary "GbbConnect2" >}} |
| **SofarSolar** | {{< glossary "DongleDirect" >}}, {{< glossary "GbbConnect2" >}} |

> [!NOTE]
> Victron is the longest-supported inverter with the most complete integration. Other inverters have full support for charge/discharge modes, but some advanced options may differ.

Configuration details for individual inverters can be found in the [Installation]({{< relref "/installation" >}}) section.

## What's next?

- [Quick start]({{< relref "/introduction/quick-start" >}}) — step by step how to set up the system
- [Best practices]({{< relref "/introduction/best-practices" >}}) — tips from experienced users
- [Prices]({{< relref "/konfiguracja/ceny" >}}) — configuring purchase and sale prices
- [Battery Forecast]({{< relref "/konfiguracja/prognoza-baterii" >}}) — the central optimizer module
