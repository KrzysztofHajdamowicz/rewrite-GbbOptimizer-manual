---
title: "Charge"
weight: 30
---

# Charge Configuration

The Charge module controls battery charging schedules and SOC limits.

## Charging Schedules (Victron)

For Victron systems, charging is managed through ESS Schedules — part of the {{< glossary "ESS" >}} module in Victron/Cerbo.

> [!NOTE]
> **Important:** Set "Self-consumption above limit" to **PV** (not "PV & Battery") so the scheduler stops discharging the battery at night.

### Getting Schedules from Cerbo

1. Enter your {{< glossary "VRM" >}} Portal ID, login email, and password in the Plant section
2. Press **"Get from Cerbo"**
3. The system imports up to 5 schedules from your Cerbo device

### Modifying Schedules

For each schedule, you can adjust:

| Parameter | Description |
|-----------|-------------|
| Enable/Disable | Toggle individual schedules |
| Start hour | When charging begins (hour values only) |
| Duration | How long to charge (in hours) |
| SOC Limit | Target {{< glossary "SOC" >}} — charging stops when reached |

You can save changes locally for testing, or send them directly to the plant.

## Charging for Deye / Other Inverters

For non-Victron inverters, charging is controlled through the optimizer's protocol modes. The system automatically sets:

- Time-of-use charging periods
- Target SOC percentage
- Maximum charge current/power

See [Mode Mappings]({{< relref "/reference/mode-mappings" >}}) for how charge commands translate to your specific inverter settings.
