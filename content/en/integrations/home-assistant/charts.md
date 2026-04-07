---
title: "Charts"
weight: 40
translationKey: "wykresy"
---

# Charts in Home Assistant

GbbOptimizer provides interactive charts (PV production, consumption, SOC, energy prices, etc.) via its web interface. These can be embedded in a Home Assistant dashboard.

## Embedding Charts

Use the **Webpage** (or **iFrame**) card in the HA dashboard:

1. Go to the HA dashboard -> **Edit** -> **Add card**
2. Select the **Webpage** card (or a manual card of type `iframe`)
3. In the URL field paste the chart address from GbbOptimizer

```yaml
type: iframe
url: "https://<server>.gbbsoft.pl/Charts?PlantId=<PlantId>"
aspect_ratio: "16:9"
```

Replace `<server>` and `<PlantId>` with the appropriate values for your installation.

> [!NOTE]
> Charts require internet access. If Home Assistant is running on a local network without access to external services, the charts will not load.

## Alternative — Custom Charts from MQTT Data

If you prefer to create charts locally, you can use data transmitted via MQTT (see [Automation]({{< relref "/integrations/home-assistant/automation" >}})) combined with cards such as:

- **ApexCharts Card** (HACS)
- **Mini Graph Card** (HACS)
- Built-in HA history cards
