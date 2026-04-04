---
title: "Deye"
weight: 20
---

# Deye Integration

## Checklist

Before connecting your Deye inverter:

- [ ] **Work mode** — "Zero export to CT" or "Zero export to Loads" (do not use "Selling First" during discharge)
- [ ] **TimeOfUse** — enabled
- [ ] **TimeOfUse settings** — use percentage-based (not voltage), or map SOC to voltage values
- [ ] **System Work Mode** — configured for all 7 days of the week
- [ ] **Energy pattern** — set to "Load First"
- [ ] **SolarSell** — checked/enabled
- [ ] **Grid charge** — enabled
- [ ] **Grid Start / Battery Restart** — thresholds below {{< glossary "MinSOC" >}} settings
- [ ] **Data transmission** — every **1 minute** (not every 5 minutes)
- [ ] **Copilot** — **disabled**

## Connection Methods

Deye inverters can connect via:
- [DeyeCloud]({{< relref "/integrations/connection-methods/deye-cloud" >}}) {{< badge "recommended" >}}
- [Solarman]({{< relref "/integrations/connection-methods/solarman" >}}) {{< badge "deprecated" >}}
- [GbbConnect2]({{< relref "/integrations/connection-methods/gbb-connect2" >}})
- [Home Assistant + SolarAssistant]({{< relref "/integrations/home-assistant/solar-assistant" >}})

## Mode Mappings

See [Deye Mode Mapping]({{< relref "/reference/mode-mappings/deye" >}}) for how protocol modes translate to Deye register values.
