---
title: "Charts"
weight: 40
translationKey: "wykresy"
---

# Charts in Home Assistant

GbbOptimizer provides an interactive **Battery Forecast** chart that can be embedded in a Home Assistant dashboard as an iframe card.

## Chart URL

```
https://<address>/Forecast/IndexChart?PlantId=<PlantId>&PlantToken=<PlantToken>&NoMenu=1&ui-culture=en
```

Where:
- `<address>` — your GbbOptimizer server address (see [Server table]({{< relref "/references/mqtt-servers" >}})), without `<` or `>`
- `<PlantId>` — {{< glossary "PlantId" >}} of your installation
- `<PlantToken>` — {{< glossary "PlantToken" >}} of your installation

> [!WARNING]
> If your {{< glossary "PlantToken" >}} contains a **plus sign** (`+`), replace it in the URL with `%2b`.
> If it contains a **slash** (`/`), replace it with `%2f`.

To enable **Dark Mode**, append `&DarkMode=1` to the end of the URL.

## URL Builder

Fill in the fields to automatically generate a ready-to-use address for Home Assistant:

<div class="gbb-url-builder">
  <div class="gbb-field">
    <label for="gbb-server">Server address</label>
    <input type="text" id="gbb-server" placeholder="e.g. gbboptimizer.gbbsoft.pl" />
    <small>Without https:// — see <a href="{{< relref "/references/mqtt-servers" >}}">Server table</a></small>
  </div>
  <div class="gbb-field">
    <label for="gbb-plantid">PlantId</label>
    <input type="text" id="gbb-plantid" placeholder="e.g. A12345" />
  </div>
  <div class="gbb-field">
    <label for="gbb-planttoken">PlantToken</label>
    <input type="text" id="gbb-planttoken" placeholder="Token from installation settings" />
  </div>
  <div class="gbb-field gbb-checkbox">
    <label><input type="checkbox" id="gbb-darkmode" /> Dark Mode</label>
  </div>
  <button onclick="gbbBuildUrl()" class="gbb-btn">Generate URL</button>
  <div id="gbb-result" style="display:none">
    <label>Generated URL:</label>
    <div class="gbb-url-box">
      <code id="gbb-url-text"></code>
      <button onclick="gbbCopyUrl()" class="gbb-btn gbb-btn-small">Copy</button>
    </div>
    <details class="gbb-preview-toggle">
      <summary>Preview (iframe)</summary>
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
    alert('Please fill in all fields: Server address, PlantId, and PlantToken.');
    return;
  }

  var encodedToken = plantToken.replace(/\+/g, '%2b').replace(/\//g, '%2f');
  var url = 'https://' + server + '/Forecast/IndexChart?PlantId=' + plantId + '&PlantToken=' + encodedToken + '&NoMenu=1&ui-culture=en';
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
    btn.textContent = 'Copied!';
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

## Embedding in Home Assistant

Copy the generated URL and paste it into a **Webpage** card (or manually as an `iframe`):

```yaml
type: iframe
url: "https://<address>/Forecast/IndexChart?PlantId=<PlantId>&PlantToken=<PlantToken>&NoMenu=1&ui-culture=en"
aspect_ratio: "16:9"
```

> [!NOTE]
> The chart requires internet access. If Home Assistant is running on a local network without access to external services, the chart will not load.

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
