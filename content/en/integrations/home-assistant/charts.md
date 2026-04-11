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

### Ready-made package — GBB Forecast Downloader

A ready-made Home Assistant package is available that automatically pulls the battery SOC forecast from GbbOptimizer via MQTT and exposes it as a sensor for visualization in **ApexCharts Card**.

![Example battery SOC forecast chart](https://github.com/user-attachments/assets/7e6d2477-d76e-4630-a835-b0d68d7e3699)

The package creates a `sensor.gbb_battery_forecast` sensor that queries the MQTT API for the forecast every 5 minutes and exposes data in its attributes (timestamps + SOC values). The forecast is displayed as a dashed line on an ApexCharts graph.

**Installation:**

1. Make sure you have the [MQTT bridge]({{< relref "/integrations/home-assistant/mosquitto-bridge" >}}) configured
2. Copy the `gbb_battery_forecast.yaml` file to the `/config/packages/` directory in Home Assistant
3. Ensure packages are enabled in `configuration.yaml`:
   ```yaml
   homeassistant:
     packages: !include_dir_named packages
   ```
4. Install **ApexCharts Card** from HACS
5. Restart Home Assistant

Full documentation and YAML file: [HomeAssistant-pull-forecast-from-GbbOptimizer](https://github.com/KrzysztofHajdamowicz/HomeAssistant-pull-forecast-from-GbbOptimizer)
