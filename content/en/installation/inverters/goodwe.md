---
title: "GoodWe"
weight: 30
translationKey: "goodwe"
---

# GoodWe

Configuring a GoodWe inverter with GbbOptimizer requires granting access through the SEMS portal and configuring on the GbbOptimizer side.

## Step-by-step configuration

1. Log in to the **SEMS** portal (GoodWe)
2. In the **Management** menu, in your plant data, add the email `gbbsoft@gbbsoft.pl` as a **Guest**
3. In GbbOptimizer, add an installation with GoodWe, but **do not select a SerialNo** — the list should be empty (except for the "Select SerialNo" label)
4. At the bottom of the page, check **Share installation with technical support**
5. Contact technical support (e.g. via Discord: `gbbsoft`) and provide your inverter's **SerialNo**
6. Technical support will select your SerialNo

> [!NOTE]
> GoodWe configuration requires a one-time technical support intervention to link the inverter serial number to your installation.

## Access via GoodWe OpenAPI

GbbOptimizer connects to the GoodWe inverter via **GoodWe OpenAPI** (SEMS Portal). Access is configured on the GbbOptimizer server side — the user only needs to share their SEMS account.

## Checklist

- Make sure the email `gbbsoft@gbbsoft.pl` has **Guest** access to your plant in SEMS
- Verify that **Share installation with technical support** is checked in GbbOptimizer

## Registers modified by GbbOptimizer

GbbOptimizer modifies the following GoodWe inverter registers:

| Register | Operation | After completion |
|----------|-----------|-----------------|
| AC charging maximum SOC | Charging: target {{< glossary "MaxSOC" >}} | — |
| ACCharging start/end time (1-4) | Charging: array of next 4 charging periods | — |
| Forced charging start/end time (1-4) | Charging: array of next 4 charging periods | — |
| ACCharging power percentage | Charging: Input Limit (% of MaxBuyPower or MaxBatteryChargeDC) | Restore original value |
| Forced charging power percentage | Charging: Charge Limit (% of MaxBatteryChargeDC) | Restore original value |
| Minimum SOC for forced discharge | Discharge: target {{< glossary "MinSOC" >}} | — |
| Forced discharge start time (1-4) | Discharge: array of next 4 discharge periods | — |
| Power grid power limit percentage | Discharge: {{< glossary "GridSetpoint" >}} (% of MaxSellPower or MaxBatteryDischargeDC) | — |
| Maximum charging current | Charge block: sets `0` | Restore original value |

## Required inverter settings

- **Timing DChg ON/OFF** = `Enable`
- **PDisChgMax** (Forced discharge power percentage) = `100%`
