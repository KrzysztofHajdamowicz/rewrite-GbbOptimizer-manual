---
title: "Wat is GbbOptimizer"
weight: 10
translationKey: "czym-jest-gbboptimizer"
---

# Wat is GbbOptimizer

GbbOptimizer (voorheen GbbVictronWeb) is een programma dat het gebruik van energie in een huishoudelijke zonne-installatie met energieopslag (batterij) optimaliseert. Het analyseert prognoses van PV-productie, het energieverbruiksprofiel en de in- en verkoopprijzen van energie om de omvormer automatisch aan te sturen — en bepaalt wanneer de batterij moet worden opgeladen, wanneer ontladen en wanneer energie van of naar het net moet worden gekocht of verkocht.

## Hoe het werkt

Het programma draait in de cloud en communiceert via internet met de omvormer. Elk uur voert het berekeningen uit en stuurt het commando's naar de omvormer.

```
┌─────────────────────────────────────────────────────────────────┐
│                       GbbOptimizer (cloud)                      │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   │
│  │ PV-prognose  │  │  Verbruiks-  │  │  Inkoop- en          │   │
│  │ (Solcast,    │  │  profiel     │  │  verkoopprijzen      │   │
│  │ forecast.    │  │  van de      │  │  (tarieven, beurs)   │   │
│  │  solar)      │  │  woning      │  │                      │   │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬───────────┘   │
│         │                 │                     │               │
│         └─────────────────┼─────────────────────┘               │
│                           │                                     │
│                    ┌──────▼───────┐                             │
│                    │  Optimizer   │                             │
│                    │  (Batterij-  │                             │
│                    │   prognose)  │                             │
│                    └──────┬───────┘                             │
│                           │                                     │
│              Laad-/ontlaadplanning                              │
│              + bedrijfsmodus van de omvormer                    │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                    ┌───────▼────────┐
                    │   Verbinding   │
                    │  (VRM, MQTT,   │
                    │  Solarman,     │
                    │  GbbConnect2)  │
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │    Hybride     │
                    │   omvormer     │
                    │  + batterij    │
                    └────────────────┘
```

Elke installatie heeft een uniek {{< glossary "PlantId" >}} en {{< glossary "PlantToken" >}} die worden gebruikt voor identificatie en autorisatie van de communicatie.

## Vier bedrijfsmodi

De optimizer schakelt de omvormer tussen vier modi, afhankelijk van de actuele prijssituatie en de batterijstatus:

| Modus | Beschrijving |
|------|------|
| **Normal** | Standaard werking van de omvormer — de batterij wordt opgeladen vanuit PV, het huis wordt gevoed vanuit PV en batterij. PV-overschotten kunnen naar het net worden geëxporteerd |
| **Charge** | De batterij wordt opgeladen vanuit het net. Wordt gebruikt wanneer de inkoopprijs laag is (bijv. nachttarief, negatieve prijzen op de beurs) |
| **Discharge** | Geforceerde ontlading van de batterij naar het net. Wordt gebruikt wanneer de verkoopprijs hoog is en het loont om energie te verkopen |
| **DisableCharge** | PV-lading geblokkeerd. Wordt gebruikt om ruimte in de batterij vrij te houden voor latere goedkope lading vanuit het net |

Details over de laadconfiguratie vind je in de [module Laden]({{< relref "/configuration/charging" >}}) en over ontladen in de [module Ontladen]({{< relref "/configuration/discharging" >}}).

## Prijsgestuurde optimizer

Standaard wordt de "Prijsgestuurde optimizer" geselecteerd. Deze analyseert de in- en verkoopprijzen van energie voor de komende uren en plant:

- **Wanneer laden** — zoekt de uren met de laagste inkoopprijs
- **Wanneer ontladen** — zoekt de uren met de hoogste verkoopprijs
- **Hoeveel laden** — houdt rekening met de PV-prognose (om niet uit het net te laden wat PV sowieso zal produceren) en met de {{< glossary "MaxSOC" >}} van de batterij
- **Hoeveel ontladen** — houdt rekening met de verbruiksprognose van het huis en met de {{< glossary "MinSOC" >}} van de batterij

Het hele plan wordt gevisualiseerd in de module [Batterijprognose]({{< relref "/configuration/battery-forecast" >}}).

## Belangrijkste parameters

- {{< glossary "SOC" >}} — actuele laadtoestand van de batterij
- {{< glossary "MinSOC" >}} — minimaal batterijniveau (beveiliging)
- {{< glossary "MaxSOC" >}} — maximaal laadniveau (aanbevolen 90%)
- {{< glossary "GridSetpoint" >}} — doelwaarde voor het vermogen van uitwisseling met het net
- {{< glossary "RTE" >}} — efficiëntie van de laad-/ontlaadcyclus
- {{< glossary "Correction Factor" >}} — correctiefactor voor de PV-prognose (kalibreert zichzelf automatisch gedurende ~een week)

## Ondersteunde omvormers

GbbOptimizer ondersteunt de volgende hybride omvormers:

| Omvormer | Verbindingsmethoden |
|----------|-------------------|
| **Victron** | VRM Portal (native), Home Assistant |
| **Deye** | DeyeCloud, Solarman, Home Assistant, {{< glossary "GbbConnect2" >}}, {{< glossary "DongleDirect" >}} |
| **GoodWe** | Solarman, Home Assistant, {{< glossary "GbbConnect2" >}} |
| **Afore** | Solarman, {{< glossary "GbbConnect2" >}} |
| **Hinen** | Solarman, {{< glossary "GbbConnect2" >}} |
| **SofarSolar** | {{< glossary "DongleDirect" >}}, {{< glossary "GbbConnect2" >}} |

> [!NOTE]
> Victron is de langst ondersteunde omvormer met de meest complete integratie. De overige omvormers hebben volledige ondersteuning voor laad-/ontlaadmodi, maar sommige geavanceerde opties kunnen verschillen.

Details over de configuratie van individuele omvormers vind je in de sectie [Installatie]({{< relref "/installation" >}}).

## Hoe verder?

- [Snelstart]({{< relref "/introduction/quick-start" >}}) — stap voor stap het systeem in gebruik nemen
- [Best practices]({{< relref "/introduction/best-practices" >}}) — tips van ervaren gebruikers
- [Prijzen]({{< relref "/configuration/prices" >}}) — configuratie van in- en verkoopprijzen
- [Batterijprognose]({{< relref "/configuration/battery-forecast" >}}) — de centrale module van de optimizer
