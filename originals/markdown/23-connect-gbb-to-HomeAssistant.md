## Uwagi:

- W HA, w opcjach Mosquitto broker: aktywować Customize i ustawic folder: mosquitto
- W HA stwórz plik /share/mosquitto/GbbOptimizer.conf
  connection GbbOptimizer\_<plantID>
  remote\_username <plantID>
  remote\_password <plantToken>
  address <adres mqtt [patrz tutaj](https://gbboptimizer10.gbbsoft.pl/Manual?PageNo=14)>:8883
  bridge\_capath /etc/ssl/certs
  **topic # both 2 ha\_gbb/ <plantID>/ha\_gbb/**
- Powinieneś napisać samodzielnie jak komendy z/do GbbOptimizer są przesyłane do/z Inwertera.
- Możesz użyć HA Automation jak opisano ponizej

## Do pobrania

- Opis implementacji od jednego z użytkowników (SeMoi) (PL): [HA\_z\_Automation.rtf](https://www.gbbsoft.pl/!download/GbbOptimizer/HA_z_Automation.rtf) (v0.02)

## Odczytywanie danych w mqtt przez GbbOptimizer:

Program czeka na dane w mqtt pod topikiem: <plantId>/ha\_gbb/sensor.

W Payload powinny się znaleźć następujące dane (to są liczniki narastające)

- "soc\_perc" (lub "V" jeżeli zaznaczono 'Steruj poprzez V a nie przez SOC (Deye)')
- "loads\_total\_kWh"
- "fromgrid\_total\_kWh"
- "togrid\_total\_kWh"
- "pv\_total\_kWh"

Następujące dane są opcjonalne:

- "ev\_charge\_total\_kWh"
- "hp\_total\_kWh"
- "other1\_total\_kWh"
- "other2\_total\_kWh"
- "other3\_total\_kWh"
- "other4\_total\_kWh"
- "other5\_total\_kWh"
- "other6\_total\_kWh"

Jeżeli chcesz wysłac więcej niż jeden PV możesz uzyć dodatkowo następujących pól:

- "more": [ {"number":2, "pv\_total\_kWh":xxx}, {"number": 3, "pv\_total\_kWh":xxx}, ... ]

Uwagi:

- Liczniki mogą się zerować od czasu do czasu, więc można przesyłać np: liczniki dzienne
- Wartości<0 są traktowane jak null: brak danych, czekamy na dane
- Można wysyłać tylko dane opcjonalne (jedna lub więcej), jeżeli
  główne dane importowane są z inwertera. W takim przypadku w menu IoT
  nalezy dodać system HomeAssistent i licznik dla kazdego rodzaju danych
  opcjonalnych, które maja być zaimportowane.
- Mozna wysyłać pv\_total\_kWh, wtedy zostanie to dodane do PV
  zaimportowane z inwertera, jezeli w menu 'Prognoza PV' -> przycisk
  'Popraw' dla jednej z 'Płaszczyzn PV' -> 'Źródło danych
  rzeczywistej produkcji PV'='HomeAssistant'
- Jezeli wysyłasz "more" to odpowiedni numer musi byc skonfigurowany w PłaszczyznaPV -> HomeAssistant
- główne pv\_total\_kWh to jest to samo co "more" z number=1, więc można użyć albo pv\_total\_kWh albo number=1, ale nie obu.

- Solarman/DeyeCloud: W głównych danych „soc\_perc”,
  „fromgrid\_total\_kWh” i „togrid\_total\_kWh” można wysyłać oddzielnie,
  jeśli zaznaczono opcję „Dane FromGrid, ToGrid i SOC są wysyłane przez
  HomeAssistant/SolarAssistant (nie importowane z falownika)”.
- Solarman/DeyeCloud: W głównych danych można przesyłać
  "fromgrid\_total\_kWh", "togrid\_total\_kWh", jeżeli zaznaczono "Dane ZSieci
  i DoSieci są pobierane z HomeAssistant/SolarAssistant"
- Solarman/DeyeCloud: W głównych danych można
  przesyłać "loads\_total\_kWh", jeżeli zaznaczono "Dane Zużycia są
  wysyłane z HomeAssistant/SolarAssistant a nie pobierane z invertera"

## Przykład konfiguracji do publikowania danych w mqtt:

> alias: mqtt\_publikacja
> trigger:
>   - platform: time\_pattern
>     minutes: /5
> action:
>   - service: mqtt.publish
>     data:
>       qos: "0"
>       retain: false
>       payload: |2-
>                 {
>
> "loads\_total\_kWh": {{ states.sensor.easun\_out\_total\_daily\_energy.state |
> float(-1)  }},
>
> "fromgrid\_total\_kWh": {{ states.sensor.easun\_in\_total\_daily\_energy.state
> | float(-1)  }},
>
> "pv\_total\_kWh": {{ states.sensor.total\_daily\_energy\_offgrid.state |
> float(-1) }},
>
> "soc\_perc": {{ states.sensor.easun\_battery\_soc.state | float(-1) }},
>                   "togrid\_total\_kWh": 0,
>                 }
>       topic: ha\_gbb/sensor

## Komendy otrzymane z GbbOptimizer:

Program wysyła następujące topiki:

- <plantid>/ha\_gbb/Start\_Charge - rozpocznij ładowanie baterii z
  PV lub z sieci aż do SOC umieszczonego w Payload (patrz niżej). Kiedy
  poziom SOC zostanie osiągnięty: nie ładuj baterii z sieci, nie
  rozładowuj baterii, możesz ładować baterie z PV
- <plantid>/ha\_gbb/Start\_Discharge - rozpocznij rozładowanie baterii do sieci (do poziomie SOC z Payload)
- <plantid>/ha\_gbb/Start\_DisableCharge - nie ładuj baterii, przesyłaj energię z PV do homu i sieci
- <plantid>/ha\_gbb/Start\_Normal - powrót do normalnej pracy (PV
  przesyłane jest do homu, potem do baterii i na końcu do sieci, Hom
  zapilany jest z PV potem z baterii, a na końcu z sieci)

Równolegle program wysyła tą samą zawartość na topik:

- <plantid>/ha\_gbb/EMS

Jako Payload program wysyłan dane w postaci JSON z następującymi
informacjami: {"Hour":22, "FromMinute":0, "ToMinute":59,
"PriceLessZero":0, "Operation":"Normal", "SOC":90}

- Hour
- FromMinute
- ToMinute
- DischargeLimitW
- ChargeLimitW
- InputLimitW
- PriceLessZero: 0 - normalna cena, 1- cena<0
- Operation: "Normal", "Discharge", "DisableCharge", "Charge"
- SOC: SOC poziom SOC do ładowania/rozładowania
- V: SOC przekonwertowane do V (jeżeli zaznaczono 'Steruj poprzez V a nie przez SOC (Deye)')

## Przykład mqtt trigger:

> alias: mqtt output\_source\_priority\_battery
> description: ""
> trigger:
>   - platform: mqtt
>     topic: ha\_gbb/Start\_Charge
> condition: []
> action:
>   - service: switch.turn\_on
>     target:
>       entity\_id: switch.bms\_1\_output\_source\_priority\_battery
>     data: {}
> mode: single
