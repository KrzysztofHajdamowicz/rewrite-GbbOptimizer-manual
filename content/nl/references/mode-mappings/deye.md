---
title: "Deye"
weight: 10
translationKey: "mapowania-deye"
---

# Modusmapping — Deye

{{< badge "deye-only" >}}

Hoe de GbbOptimizer-modi zich vertalen naar de instellingen van de Deye-omvormer, afhankelijk van de verbindingsmethode.

## Solarman / DeyeCloud (nieuwe verbindingsmethode)

{{< badge "recommended" >}}

| Operatie | Work Mode | GridCharge (TimeOfUse) | Time (TimeOfUse) | SOC (TimeOfUse) | Power (TimeOfUse) | Charge A | MaxSellPower |
|----------|-----------|----------------------|-----------------|-----------------|-------------------|----------|--------------|
| **Normal** | — | nee | ja | 5%\* | Max Battery Discharge, anders: Max Inverter Discharge | ongewijzigd | — |
| **Charge** | — | ja | ja | SOC% | ChargeLimitW, anders: Max Battery Charge, anders: Max Inverter Charge | ChargeLimitW, anders: Max Battery Charge, anders: Max Inverter Charge | — |
| **Discharge** | SellingFirst (na afloop: terug naar vorige waarde) | nee | ja | SOC% | Max Battery Discharge, anders: Max Inverter Discharge | ongewijzigd; KeepSOC: 0W | Max GridSetpoint / Discharge (W); als ontladen langzamer moet, berekent het programma de waarde; na afloop: terug naar vorige waarde |
| **DisableCharge** | — | nee | ja | 5%\* | Max GridSetpoint / Discharge (W) | wijzigt naar 0 (na afloop: terug naar vorige waarde) | — |

\* 5% kan worden gewijzigd met de parameter **„Default MinSOC after discharge"** in de instellingen van het ontlaadschema.

### Prijs < 0

- (optioneel) Schakel **SolarSell** uit + schakel **MI export to Grid cutoff** in
- (optioneel) Wijzig LV1 naar 270 V — dit ontkoppelt van het net (off-grid). Na het einde van de periode met prijs < 0 herstelt het programma de vorige LV1-waarde.

### Generator

- **On:** Zet GEN in TimeOfUse (alleen tijdens Charge-operatie) + stel GenSOC in op huidige SOC + 1
- **PurchasePrice > LimitPrice:** Wijzig LV1 naar 270 V (ontkoppeling van het net om de generator te starten) of stel NoBatt in

### Extra opties

- **„Switch off peak-shaving during discharge battery to grid"** — schakel Peak-Shaving uit
- **„Change Mode to 'Zero Export To CT' during charge battery from grid"** — wijzig WorkMode
- **„Input Limit (A)"** — Grid Peak Shaving (W)

---

## DeyeCloud (oude API)

{{< badge "deprecated" >}}

| Operatie | Work Mode | GridCharge (TimeOfUse) | Time (TimeOfUse) | SOC (TimeOfUse) | Power (TimeOfUse) | Charge A | MaxSellPower |
|----------|-----------|----------------------|-----------------|-----------------|-------------------|----------|--------------|
| **Normal** | — | nee | ja | 5%\* | Max Battery Discharge | ongewijzigd | — |
| **Charge** | — | ja | ja | SOC% | ChargeLimitW, anders: Max Battery Discharge | ongewijzigd | — |
| **Discharge** | SellingFirst (na afloop: **wijziging naar ZeroExportToCT**) | nee | ja | SOC% | Sell Power, anders: Max Battery Discharge | ongewijzigd | Max GridSetpoint / Discharge (W); na afloop: MaxSellPower after Discharge |
| **DisableCharge** | — | nee | ja | 5%\* | Max GridSetpoint / Discharge (W) | wijzigt naar 0 (na afloop: MaxChargePower after Disable battery charge) | — |

\* 5% kan worden gewijzigd met de parameter **„Default MinSOC after discharge"**.

### Prijs < 0 (oude API)

- (optioneel) Schakel **SolarSell** uit

### Generator (oude API)

- **On:** Zet GEN in TimeOfUse (alleen tijdens Charge-operatie)

### Extra opties (oude API)

- **„Change Mode to 'Zero Export To CT' during charge battery from grid"** — wijzig WorkMode

> [!WARNING]
> De oude DeyeCloud-API is verouderd en heeft beperkte functionaliteit (geen ondersteuning voor Peak-Shaving, generator met LV1, Input Limit). Overschakelen naar de nieuwe verbindingsmethode wordt aanbevolen.

---

## SolarAssistant

| Operatie | Work Mode | GridCharge (TimeOfUse) | Time (TimeOfUse) | SOC (TimeOfUse) | Charge A |
|----------|-----------|----------------------|-----------------|-----------------|----------|
| **Normal** | — | nee | ja | 5%\* | ongewijzigd |
| **Charge** | — | ja | ja | SOC% | ongewijzigd |
| **Discharge** | SellingFirst (na afloop: terug naar vorige waarde) | nee | ja | SOC% | ongewijzigd |
| **DisableCharge** | — | nee | ja | 5%\* | wijzigt naar 0 (na afloop: terug naar vorige waarde) |

\* 5% kan worden gewijzigd met de parameter **„Default MinSOC after discharge"**.

> [!NOTE]
> {{< glossary "SolarAssistant" >}} laat op dit moment niet toe om op afstand Power in TimeOfUse of de starttijd te wijzigen. Daarom stelt GbbOptimizer alle rijen op dezelfde waarden in. De functies Price < 0 en Generator zijn niet beschikbaar via SolarAssistant.

Meer informatie: [Integratie met SolarAssistant]({{< relref "/integrations/home-assistant/solar-assistant" >}})
