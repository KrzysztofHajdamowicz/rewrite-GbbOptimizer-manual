---
title: "Wykresy"
weight: 40
translationKey: "wykresy"
---

# Wykresy w Home Assistant

GbbOptimizer udostępnia interaktywny wykres **Prognozy Baterii**, który można osadzić w dashboardzie Home Assistant jako kartę iframe.

## Adres wykresu

```
https://<adres>/Forecast/IndexChart?PlantId=<PlantId>&PlantToken=<PlantToken>&NoMenu=1&ui-culture=pl
```

Gdzie:
- `<adres>` — adres serwera GbbOptimizer (patrz [Tabela serwerów]({{< relref "/referencje/serwery-mqtt" >}})), bez `<` ani `>`
- `<PlantId>` — {{< glossary "PlantId" >}} Twojej instalacji
- `<PlantToken>` — {{< glossary "PlantToken" >}} Twojej instalacji

> [!WARNING]
> Jeżeli Twój {{< glossary "PlantToken" >}} zawiera znak **plus** (`+`), zastąp go w URL ciągiem `%2b`.
> Jeżeli zawiera **ukośnik** (`/`), zastąp go ciągiem `%2f`.

Aby włączyć **Tryb Ciemny**, dodaj na końcu adresu: `&DarkMode=1`

## Generator URL

Wypełnij pola, aby automatycznie wygenerować gotowy adres do wklejenia w Home Assistant:

<div class="gbb-url-builder">
  <div class="gbb-field">
    <label for="gbb-server">Adres serwera</label>
    <input type="text" id="gbb-server" placeholder="np. gbboptimizer.gbbsoft.pl" />
    <small>Bez https:// — patrz <a href="{{< relref "/referencje/serwery-mqtt" >}}">Tabela serwerów</a></small>
  </div>
  <div class="gbb-field">
    <label for="gbb-plantid">PlantId</label>
    <input type="text" id="gbb-plantid" placeholder="np. A12345" />
  </div>
  <div class="gbb-field">
    <label for="gbb-planttoken">PlantToken</label>
    <input type="text" id="gbb-planttoken" placeholder="Token z ustawień instalacji" />
  </div>
  <div class="gbb-field gbb-checkbox">
    <label><input type="checkbox" id="gbb-darkmode" /> Tryb Ciemny (DarkMode)</label>
  </div>
  <button onclick="gbbBuildUrl()" class="gbb-btn">Generuj URL</button>
  <div id="gbb-result" style="display:none">
    <label>Wygenerowany URL:</label>
    <div class="gbb-url-box">
      <code id="gbb-url-text"></code>
      <button onclick="gbbCopyUrl()" class="gbb-btn gbb-btn-small">Kopiuj</button>
    </div>
    <details class="gbb-preview-toggle">
      <summary>Podgląd (iframe)</summary>
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
    alert('Wypełnij wszystkie pola: Adres serwera, PlantId i PlantToken.');
    return;
  }

  var encodedToken = plantToken.replace(/\+/g, '%2b').replace(/\//g, '%2f');
  var url = 'https://' + server + '/Forecast/IndexChart?PlantId=' + plantId + '&PlantToken=' + encodedToken + '&NoMenu=1&ui-culture=pl';
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
    btn.textContent = 'Skopiowano!';
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

## Osadzanie w Home Assistant

Skopiuj wygenerowany URL i wklej go w karcie **Webpage** (lub ręcznie jako `iframe`):

```yaml
type: iframe
url: "https://<adres>/Forecast/IndexChart?PlantId=<PlantId>&PlantToken=<PlantToken>&NoMenu=1&ui-culture=pl"
aspect_ratio: "16:9"
```

> [!NOTE]
> Wykres wymaga dostępu do internetu. Jeśli Home Assistant działa w sieci lokalnej bez dostępu do zewnętrznych usług, wykres nie będzie się ładować.

## Alternatywa — własne wykresy z danych MQTT

Jeśli wolisz tworzyć wykresy lokalnie, możesz użyć danych przesyłanych przez MQTT (patrz [Automatyzacja]({{< relref "/integracje/home-assistant/automatyzacja" >}})) w połączeniu z kartami typu:

- **ApexCharts Card** (HACS)
- **Mini Graph Card** (HACS)
- Wbudowane karty historii HA

### Gotowy pakiet — GBB Forecast Downloader

Dostępny jest gotowy pakiet Home Assistant, który automatycznie pobiera prognozę SOC baterii z GbbOptimizera przez MQTT i udostępnia ją jako sensor do wizualizacji w **ApexCharts Card**.

![Przykładowy wykres prognozy SOC baterii](https://github.com/user-attachments/assets/7e6d2477-d76e-4630-a835-b0d68d7e3699)

Pakiet tworzy sensor `sensor.gbb_battery_forecast`, który co 5 minut odpytuje API MQTT o prognozę i udostępnia dane w atrybutach (timestampy + wartości SOC). Prognoza wyświetlana jest jako linia przerywana na wykresie ApexCharts.

**Instalacja:**

1. Upewnij się, że masz skonfigurowany [most MQTT]({{< relref "/integracje/home-assistant/mosquitto-bridge" >}})
2. Skopiuj plik `gbb_battery_forecast.yaml` do katalogu `/config/packages/` w Home Assistant
3. Upewnij się, że packages są włączone w `configuration.yaml`:
   ```yaml
   homeassistant:
     packages: !include_dir_named packages
   ```
4. Zainstaluj **ApexCharts Card** z HACS
5. Zrestartuj Home Assistant

Pełna dokumentacja i plik YAML: [HomeAssistant-pull-forecast-from-GbbOptimizer](https://github.com/KrzysztofHajdamowicz/HomeAssistant-pull-forecast-from-GbbOptimizer)
