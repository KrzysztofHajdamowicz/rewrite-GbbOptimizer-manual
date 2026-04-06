---
title: "Victron"
weight: 10
translationKey: "victron"
---

# Victron

{{< badge "victron-only" >}}

Configuring a Victron inverter with GbbOptimizer requires correct setup of the {{< glossary "ESS" >}} system and the {{< glossary "VRM" >}} portal.

## Checklist

Before starting GbbOptimizer, verify the following settings:

1. **Do not install Beta** firmware
2. **DESS must be disabled**
3. **Schedules** — the "Self-consumption above limit" option should be set to **PV** (not "PV & Battery"). This ensures schedules do not cause battery discharge at night
4. **Battery Life** in {{< glossary "ESS" >}} must be **disabled** — select mode: `Optimized (without BatteryLife)`
5. **Log interval** (in VRM Online Portal) set to **1 min**
6. **VRM permissions** — the user must have **Full Control** enabled
7. **Restart Cerbo** after making changes

> [!WARNING]
> Incorrect Battery Life or Schedules settings can cause unexpected battery discharge at night.

## Victron parameters in GbbOptimizer

A detailed description of Victron parameters (VRM Portal Id, Installation Id, VRM Token, etc.) can be found in the [Installation parameters]({{< relref "/instalacja/parametry-instalacji" >}}) section.

## MQTT topics modified by GbbOptimizer

GbbOptimizer modifies **only** the following topics/properties in the Victron system. The variable `{i}` denotes the schedule number (0-4).

### Charging schedules (Schedules)

| MQTT Topic | Property | Notes |
|------------|----------|-------|
| `settings/0/Settings/CGwacs/BatteryLife/Schedule/Charge/{i}/Day` | Schedule day | |
| `settings/0/Settings/CGwacs/BatteryLife/Schedule/Charge/{i}/Soc` | SOC limit | |
| `settings/0/Settings/CGwacs/BatteryLife/Schedule/Charge/{i}/Start` | Start time | |
| `settings/0/Settings/CGwacs/BatteryLife/Schedule/Charge/{i}/Duration` | Duration | |

### ESS and power control

| MQTT Topic | Property | Notes |
|------------|----------|-------|
| `settings/0/Settings/CGwacs/BatteryLife/MinimumSocLimit` | {{< glossary "ESS" >}} / Minimum SOC | |
| `settings/0/Settings/CGwacs/AcPowerSetPoint` | {{< glossary "ESS" >}} / {{< glossary "GridSetpoint" >}} | |
| `settings/0/Settings/SystemSetup/MaxChargeCurrent` | DVCC / Maximum charging current | |
| `vebus/{257 or other}/Ac/ActiveIn/CurrentLimit` | MultiPlus / Input current limit | |

### Control at negative prices (Price < 0)

| MQTT Topic | Property | Notes |
|------------|----------|-------|
| `system/0/Relay/0/State` | Relay 1 | Activated when price < 0 |
| `system/0/Relay/1/State` | Relay 2 | Activated when price < 0 |
| `vebus/{257 or other}/Mode` | Inverter mode | Activated when price < 0 |
| `settings/0/Settings/CGwacs/OvervoltageFeedIn` | DC-coupled PV — feed in excess | Activated when price < 0 |

> [!NOTE]
> The VE.Bus instance number (default `257`) may differ in your system. Check it in the installation parameters as "VRM Instance number of VE.Bus System device".
