---
title: "Grafieken"
weight: 40
translationKey: "wykresy"
---

# Grafieken in Home Assistant

GbbOptimizer biedt interactieve grafieken (PV-productie, verbruik, SOC, energieprijzen enz.) via de webinterface. Je kunt ze inbedden in een Home Assistant-dashboard.

## Grafieken inbedden

Gebruik de **Webpage**-kaart (of **iFrame**) in een HA-dashboard:

1. Ga naar het HA-dashboard -> **Bewerken** -> **Kaart toevoegen**
2. Kies de kaart **Webpage** (of een handmatige `iframe`-kaart)
3. Plak het grafieken-URL van GbbOptimizer in het URL-veld

```yaml
type: iframe
url: "https://<server>.gbbsoft.pl/Charts?PlantId=<PlantId>"
aspect_ratio: "16:9"
```

Vervang `<server>` en `<PlantId>` door de juiste waarden voor jouw installatie.

> [!NOTE]
> De grafieken vereisen internettoegang. Als Home Assistant in een lokaal netwerk draait zonder toegang tot externe diensten, worden de grafieken niet geladen.

## Alternatief — eigen grafieken uit MQTT-data

Als je liever lokale grafieken maakt, kun je de via MQTT verzonden gegevens gebruiken (zie [Automatisering]({{< relref "/integrations/home-assistant/automation" >}})) in combinatie met kaarten zoals:

- **ApexCharts Card** (HACS)
- **Mini Graph Card** (HACS)
- Ingebouwde HA-historiekkaarten

### Kant-en-klaar pakket — GBB Forecast Downloader

Er is een kant-en-klaar Home Assistant-pakket beschikbaar dat automatisch de batterij-SOC-prognose ophaalt uit GbbOptimizer via MQTT en beschikbaar stelt als sensor voor visualisatie in **ApexCharts Card**.

![Voorbeeld batterij-SOC-prognose grafiek](https://github.com/user-attachments/assets/7e6d2477-d76e-4630-a835-b0d68d7e3699)

Het pakket maakt een `sensor.gbb_battery_forecast`-sensor aan die elke 5 minuten de MQTT-API bevraagt voor de prognose en de gegevens beschikbaar stelt in attributen (timestamps + SOC-waarden). De prognose wordt weergegeven als een stippellijn op een ApexCharts-grafiek.

**Installatie:**

1. Zorg dat je de [MQTT-bridge]({{< relref "/integrations/home-assistant/mosquitto-bridge" >}}) hebt geconfigureerd
2. Kopieer het bestand `gbb_battery_forecast.yaml` naar de map `/config/packages/` in Home Assistant
3. Zorg dat packages zijn ingeschakeld in `configuration.yaml`:
   ```yaml
   homeassistant:
     packages: !include_dir_named packages
   ```
4. Installeer **ApexCharts Card** via HACS
5. Herstart Home Assistant

Volledige documentatie en YAML-bestand: [HomeAssistant-pull-forecast-from-GbbOptimizer](https://github.com/KrzysztofHajdamowicz/HomeAssistant-pull-forecast-from-GbbOptimizer)
