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
