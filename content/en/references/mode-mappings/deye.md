---
title: "Deye"
weight: 10
translationKey: "mapowania-deye"
---

# Mode Mapping — Deye

{{< badge "deye-only" >}}

How GbbOptimizer modes translate to Deye inverter settings depending on the connection method.

## Solarman / DeyeCloud (new connection method)

{{< badge "recommended" >}}

| Operation | Work Mode | GridCharge (TimeOfUse) | Time (TimeOfUse) | SOC (TimeOfUse) | Power (TimeOfUse) | Charge A | MaxSellPower |
|-----------|-----------|------------------------|------------------|-----------------|-------------------|----------|--------------|
| **Normal** | — | no | yes | 5%\* | Max Battery Discharge, if absent: Max Inverter Discharge | no change | — |
| **Charge** | — | yes | yes | SOC% | ChargeLimitW, if absent: Max Battery Charge, if absent: Max Inverter Charge | ChargeLimitW, if absent: Max Battery Charge, if absent: Max Inverter Charge | — |
| **Discharge** | SellingFirst (on completion: restore previous value) | no | yes | SOC% | Max Battery Discharge, if absent: Max Inverter Discharge | no change; KeepSOC: 0W | Max GridSetpoint / Discharge (W); if discharge must be slower the program calculates a value; on completion: restore previous value |
| **DisableCharge** | — | no | yes | 5%\* | Max GridSetpoint / Discharge (W) | changed to 0 (on completion: restore previous value) | — |

\* 5% can be changed with the **"Default MinSOC after discharge"** parameter in discharge plan settings.

### Price < 0

- (optional) Disable **SolarSell** + enable **MI export to Grid cutoff**
- (optional) Change LV1 to 270V — causes disconnection from grid (off-grid). After the price < 0 period the program restores the previous LV1 value.

### Generator

- **On:** Set GEN in TimeOfUse (only during Charge operation) + set GenSOC to current SOC + 1
- **PurchasePrice > LimitPrice:** Change LV1 to 270V (disconnect from grid to start generator) or set NoBatt

### Additional Options

- **"Switch off peak-shaving during discharge battery to grid"** — disable Peak-Shaving
- **"Change Mode to 'Zero Export To CT' during charge battery from grid"** — change WorkMode
- **"Input Limit (A)"** — Grid Peak Shaving (W)

---

## DeyeCloud (old API)

{{< badge "deprecated" >}}

| Operation | Work Mode | GridCharge (TimeOfUse) | Time (TimeOfUse) | SOC (TimeOfUse) | Power (TimeOfUse) | Charge A | MaxSellPower |
|-----------|-----------|------------------------|------------------|-----------------|-------------------|----------|--------------|
| **Normal** | — | no | yes | 5%\* | Max Battery Discharge | no change | — |
| **Charge** | — | yes | yes | SOC% | ChargeLimitW, if absent: Max Battery Discharge | no change | — |
| **Discharge** | SellingFirst (on completion: **change to ZeroExportToCT**) | no | yes | SOC% | Sell Power, if absent: Max Battery Discharge | no change | Max GridSetpoint / Discharge (W); on completion: MaxSellPower after Discharge |
| **DisableCharge** | — | no | yes | 5%\* | Max GridSetpoint / Discharge (W) | changed to 0 (on completion: MaxChargePower after Disable battery charge) | — |

\* 5% can be changed with the **"Default MinSOC after discharge"** parameter.

### Price < 0 (old API)

- (optional) Disable **SolarSell**

### Generator (old API)

- **On:** Set GEN in TimeOfUse (only during Charge operation)

### Additional Options (old API)

- **"Change Mode to 'Zero Export To CT' during charge battery from grid"** — change WorkMode

> [!WARNING]
> The old DeyeCloud API is deprecated and has limited functionality (no Peak-Shaving, LV1 generator, or Input Limit support). Migrating to the new connection method is recommended.

---

## SolarAssistant

| Operation | Work Mode | GridCharge (TimeOfUse) | Time (TimeOfUse) | SOC (TimeOfUse) | Charge A |
|-----------|-----------|------------------------|------------------|-----------------|----------|
| **Normal** | — | no | yes | 5%\* | no change |
| **Charge** | — | yes | yes | SOC% | no change |
| **Discharge** | SellingFirst (on completion: restore previous value) | no | yes | SOC% | no change |
| **DisableCharge** | — | no | yes | 5%\* | changed to 0 (on completion: restore previous value) |

\* 5% can be changed with the **"Default MinSOC after discharge"** parameter.

> [!NOTE]
> {{< glossary "SolarAssistant" >}} currently does not allow remotely changing Power in TimeOfUse or the start time. Therefore GbbOptimizer sets all rows to the same values. The Price < 0 and Generator features are not available through SolarAssistant.

More information: [SolarAssistant Integration]({{< relref "/integrations/home-assistant/solar-assistant" >}})
