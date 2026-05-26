---
title: "Grafieken"
weight: 40
translationKey: "wykresy"
---

# Grafieken in Home Assistant

GbbOptimizer biedt een interactieve **Batterijprognose**-grafiek die als iframe-kaart in een Home Assistant-dashboard kan worden ingesloten.

## URL van de grafiek

```
https://<adres>/Forecast/IndexChart?PlantId=<PlantId>&PlantToken=<PlantToken>&NoMenu=1&ui-culture=nl
```

Waarbij:
- `<adres>` — het serveradres van GbbOptimizer (zie [Servertabel]({{< relref "/references/mqtt-servers" >}})), zonder `<` of `>`
- `<PlantId>` — {{< glossary "PlantId" >}} van jouw installatie
- `<PlantToken>` — {{< glossary "PlantToken" >}} van jouw installatie

> [!WARNING]
> Als jouw {{< glossary "PlantToken" >}} een **plusteken** (`+`) bevat, vervang dit dan in de URL door `%2b`.
> Als het een **schuine streep** (`/`) bevat, vervang dit dan door `%2f`.

Om de **Donkere modus** in te schakelen, voeg `&DarkMode=1` toe aan het einde van de URL.

## URL-bouwer

Vul de velden in om automatisch een kant-en-klaar adres voor Home Assistant te genereren:

<div class="gbb-url-builder">
  <div class="gbb-field">
    <label for="gbb-server">Serveradres</label>
    <input type="text" id="gbb-server" placeholder="bijv. gbboptimizer.gbbsoft.pl" />
    <small>Zonder https:// — zie <a href="{{< relref "/references/mqtt-servers" >}}">Servertabel</a></small>
  </div>
  <div class="gbb-field">
    <label for="gbb-plantid">PlantId</label>
    <input type="text" id="gbb-plantid" placeholder="bijv. A12345" />
  </div>
  <div class="gbb-field">
    <label for="gbb-planttoken">PlantToken</label>
    <input type="text" id="gbb-planttoken" placeholder="Token uit installatie-instellingen" />
  </div>
  <div class="gbb-field gbb-checkbox">
    <label><input type="checkbox" id="gbb-darkmode" /> Donkere modus (DarkMode)</label>
  </div>
  <button onclick="gbbBuildUrl()" class="gbb-btn">URL genereren</button>
  <div id="gbb-result" style="display:none">
    <label>Gegenereerde URL:</label>
    <div class="gbb-url-box">
      <code id="gbb-url-text"></code>
      <button onclick="gbbCopyUrl()" class="gbb-btn gbb-btn-small">Kopiëren</button>
    </div>
    <details class="gbb-preview-toggle">
      <summary>Voorvertoning (iframe)</summary>
      <iframe id="gbb-iframe" src="" style="width:100%;height:400px;border:1px solid #ccc;margin-top:8px;border-radius:4px;" loading="lazy"></iframe>
    </details>
  </div>
</div>

<script>
function gbbBuildUrl() {
  var server = document.getElementById('gbb-server').value.trim().replace(/^https?:\/\//, '').replace(/\/$/, '');
  var plantId = document.getElementById('gbb-plantid').value.trim();
  var plantToken = document.getElementById('gbb-planttoken').value.trim();
  var darkMode = document.getElementById('gbb-darkmode').checked;

  if (!server || !plantId || !plantToken) {
    alert('Vul alle velden in: Serveradres, PlantId en PlantToken.');
    return;
  }

  var encodedToken = plantToken.replace(/\+/g, '%2b').replace(/\//g, '%2f');
  var url = 'https://' + server + '/Forecast/IndexChart?PlantId=' + plantId + '&PlantToken=' + encodedToken + '&NoMenu=1&ui-culture=nl';
  if (darkMode) url += '&DarkMode=1';

  document.getElementById('gbb-url-text').textContent = url;
  document.getElementById('gbb-iframe').src = url;
  document.getElementById('gbb-result').style.display = 'block';
}

function gbbCopyUrl() {
  var text = document.getElementById('gbb-url-text').textContent;
  navigator.clipboard.writeText(text).then(function() {
    var btn = event.target;
    var orig = btn.textContent;
    btn.textContent = 'Gekopieerd!';
    setTimeout(function() { btn.textContent = orig; }, 1500);
  });
}
</script>

<style>
.gbb-url-builder { background: var(--body-background, #f8f8f8); border: 1px solid var(--hint-color, #ccc); border-radius: 6px; padding: 1.2em 1.4em; margin: 1.2em 0; }
.gbb-field { margin-bottom: 0.8em; }
.gbb-field label { display: block; font-weight: 600; margin-bottom: 0.25em; font-size: 0.9em; }
.gbb-field input[type="text"] { width: 100%; max-width: 480px; padding: 0.4em 0.6em; border: 1px solid #bbb; border-radius: 4px; font-size: 0.95em; box-sizing: border-box; }
.gbb-field small { display: block; color: #666; font-size: 0.8em; margin-top: 0.2em; }
.gbb-checkbox label { font-weight: normal; display: flex; align-items: center; gap: 0.4em; cursor: pointer; }
.gbb-btn { background: #2080c8; color: #fff; border: none; padding: 0.45em 1.1em; border-radius: 4px; cursor: pointer; font-size: 0.95em; margin-top: 0.4em; }
.gbb-btn:hover { background: #1a6aaa; }
.gbb-btn-small { padding: 0.25em 0.7em; font-size: 0.85em; margin-top: 0; margin-left: 0.5em; }
.gbb-url-box { display: flex; align-items: center; background: #fff; border: 1px solid #bbb; border-radius: 4px; padding: 0.5em 0.7em; margin-top: 0.4em; word-break: break-all; }
.gbb-url-box code { flex: 1; font-size: 0.85em; }
#gbb-result label { font-weight: 600; font-size: 0.9em; margin-top: 0.8em; display: block; }
.gbb-preview-toggle { margin-top: 0.8em; }
.gbb-preview-toggle summary { cursor: pointer; font-size: 0.9em; color: #2080c8; }
</style>

## Inbedden in Home Assistant

Kopieer de gegenereerde URL en plak deze in een **Webpage**-kaart (of handmatig als `iframe`):

```yaml
type: iframe
url: "https://<adres>/Forecast/IndexChart?PlantId=<PlantId>&PlantToken=<PlantToken>&NoMenu=1&ui-culture=nl"
aspect_ratio: "16:9"
```

> [!NOTE]
> De grafiek vereist internettoegang. Als Home Assistant in een lokaal netwerk draait zonder toegang tot externe diensten, wordt de grafiek niet geladen.

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
