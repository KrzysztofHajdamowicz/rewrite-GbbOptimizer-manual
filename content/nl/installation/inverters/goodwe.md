---
title: "GoodWe"
weight: 30
translationKey: "goodwe"
---

# GoodWe

Voor de configuratie van een GoodWe-omvormer met GbbOptimizer moet toegang worden verleend via het SEMS-portaal en moeten er instellingen worden gedaan aan de GbbOptimizer-zijde.

## Stap-voor-stap configuratie

1. Log in op het **SEMS**-portaal (GoodWe)
2. Voeg in het menu **Beheer**, bij de gegevens van je installatie, het e-mailadres `gbbsoft@gbbsoft.pl` toe als **Gast**
3. Voeg in GbbOptimizer een installatie toe met GoodWe, maar **selecteer geen SerialNo** — de lijst moet leeg zijn (met uitzondering van de tekst „SerialNo kiezen")
4. Vink onderaan de pagina **De installatie delen met technische ondersteuning** aan
5. Neem contact op met de technische ondersteuning (bijv. via Discord: `gbbsoft`) en geef het **SerialNo** van je omvormer door
6. De technische ondersteuning selecteert jouw SerialNo

> [!NOTE]
> De configuratie van GoodWe vereist een eenmalige actie van de technische ondersteuning om het serienummer van de omvormer aan jouw installatie te koppelen.

## Toegang via de GoodWe OpenAPI

GbbOptimizer maakt verbinding met de GoodWe-omvormer via de **GoodWe OpenAPI** (SEMS Portal). De toegang wordt geconfigureerd aan de kant van de GbbOptimizer-server — de gebruiker hoeft alleen zijn SEMS-account te delen.

## Checklist

- Zorg dat het e-mailadres `gbbsoft@gbbsoft.pl` toegang heeft als **Gast** tot jouw installatie in SEMS
- Controleer of **De installatie delen met technische ondersteuning** in GbbOptimizer is aangevinkt

## Registers die door GbbOptimizer worden gewijzigd

GbbOptimizer wijzigt de volgende registers van de GoodWe-omvormer:

| Register | Bewerking | Na afloop |
|---------|----------|----------------|
| AC charging maximum SOC | Laden: doel-{{< glossary "MaxSOC" >}} | — |
| ACCharging start/end time (1-4) | Laden: array van de volgende 4 laadperioden | — |
| Forced charging start/end time (1-4) | Laden: array van de volgende 4 laadperioden | — |
| ACCharging power percentage | Laden: Input Limit (% van MaxBuyPower of MaxBatteryChargeDC) | Oorspronkelijke waarde herstellen |
| Forced charging power percentage | Laden: Charge Limit (% van MaxBatteryChargeDC) | Oorspronkelijke waarde herstellen |
| Minimum SOC for forced discharge | Ontladen: doel-{{< glossary "MinSOC" >}} | — |
| Forced discharge start time (1-4) | Ontladen: array van de volgende 4 ontlaadperioden | — |
| Power grid power limit percentage | Ontladen: {{< glossary "GridSetpoint" >}} (% van MaxSellPower of MaxBatteryDischargeDC) | — |
| Maximum charging current | Laadblokkering: ingesteld op `0` | Oorspronkelijke waarde herstellen |

## Vereiste instellingen van de omvormer

- **Timing DChg ON/OFF** = `Enable`
- **PDisChgMax** (Forced discharge power percentage) = `100%`
