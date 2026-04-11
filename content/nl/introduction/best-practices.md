---
title: "Best practices"
weight: 30
translationKey: "najlepsze-praktyki"
---

# Best practices

Adviezen en tips van ervaren GbbOptimizer-gebruikers.

## Geduld

> [!WARNING]
> De meest voorkomende fout van nieuwe gebruikers is te snel de configuratie aanpassen. Het programma heeft tijd nodig om te kalibreren.

GbbOptimizer is een programma dat geduld aanleert. In de eerste week:

- Wordt de {{< glossary "Correction Factor" >}} voor de PV-prognose gekalibreerd
- Verzamelt het verbruiksprofiel historische gegevens
- "Leert" de optimizer jouw installatie kennen

Schakel {{< glossary "Test Mode" >}} niet eerder uit dan na een week. Geef het programma de tijd om gegevens te verzamelen.

## Stel MaxSOC in op 90%

{{< badge "recommended" >}}

Stel {{< glossary "MaxSOC" >}} in op **90%** in plaats van 100%. Waarom?

- Je houdt een **buffer van 10%** over voor onverwachte PV-overschotten (als de prognose te laag is)
- Het PV-overschot gaat niet verloren — het gaat naar de batterij in plaats van tegen een lage verkoopprijs naar het net
- De batterij bereikt minder vaak 100%, wat de levensduur verlengt

### Periodieke volledige lading

Voor de gezondheid van de batterij is het wel verstandig om af en toe tot 100% op te laden. Stel de parameter **„Lijst van dagen in de maand waarop MaxSOC naar 100% wordt gezet"** bijvoorbeeld in op:

```
1, 15
```

Zo wordt de batterij op de 1e en de 15e van elke maand volledig opgeladen (ongeveer 2 uur), wat kalibratie van de {{< glossary "SOC" >}} mogelijk maakt en goed is voor de celchemie. Meer over deze parameter: {{< glossary "Battery Full Date" >}}.

## Wijzig de bron voor de PV-prognose

{{< badge "recommended" >}}

De standaardbron voor de PV-prognose is **forecast.solar**. Overweeg om te schakelen naar **solcast.com**, dat doorgaans nauwkeuriger is:

1. Maak een gratis „Home"-account aan op [solcast.com](https://solcast.com)
2. Voeg je PV-vlakken toe (één account ondersteunt tot twee vlakken)
3. Wijzig in de installatieparameters de bron voor de PV-prognose naar Solcast

> [!NOTE]
> Solcast heeft een limiet op het aantal verzoeken op een gratis account — één „Home"-account ondersteunt maximaal twee PV-vlakken. Als je er meer hebt, heb je extra accounts nodig.

## Minder opties = grotere winst

Hoe minder aanvullende opties er zijn aangevinkt in de parameters van de optimizer, hoe beter het resultaat. Elke extra optie is een bijkomende beperking die de bewegingsruimte van de optimizer verkleint.

Begin met de standaardconfiguratie en voeg alleen opties toe als je daar een concrete reden voor hebt.

## Solarman en Home Assistant — voorkom conflicten

> [!WARNING]
> Als je Solarman gebruikt en tegelijkertijd gegevens uit de omvormer naar Home Assistant importeert, stel `update_interval` dan in op **ten minste 20 seconden**. Te frequent pollen veroorzaakt communicatieconflicten — Solarman en Home Assistant "bijten elkaar" bij de toegang tot de omvormer.

Alternatieve oplossing: stap over van Solarman naar {{< glossary "GbbConnect2" >}}, dat dit probleem niet heeft.

## Verifieer de invoergegevens

Controleer na de initiële configuratie drie belangrijke zaken:

### 1. Prijzen

Zorg dat de [prijzen]({{< relref "/configuration/prices" >}}) correct zijn:
- Zijn de transportkosten meegenomen?
- Is de btw correct?
- Komt de verkoopprijs overeen met jouw tarief?

### 2. PV-prognose

Controleer in de [Batterijprognose]({{< relref "/configuration/battery-forecast" >}}) of de PV-prognose dicht bij de werkelijke productie ligt. Zo niet — wijzig de bron van de prognose.

### 3. Verbruiksprofiel

Verifieer het [verbruiksprofiel]({{< relref "/configuration/consumption-profiles" >}}):
- Komen de waarden overeen met het werkelijke verbruik van je huis?
- Verschillen de weekends van werkdagen (als dat in de praktijk zo is)?

## De testmodus is je vriend

Gebruik {{< glossary "Test Mode" >}} niet alleen in het begin. Schakel hem in elke keer dat je:

- Belangrijke configuratieparameters wijzigt
- De bron van de PV-prognose wijzigt
- Het energietarief wijzigt
- Een nieuw PV-vlak toevoegt

Geef de optimizer een dag of twee om de nieuwe gegevens te verwerken voordat je hem de omvormer laat aansturen.

## Samenvatting

| Praktijk | Prioriteit |
|----------|-----------|
| Wacht een week voordat je de testmodus uitschakelt | {{< badge "required" >}} |
| Controleer de juistheid van prijzen en transportkosten | {{< badge "required" >}} |
| Stel MaxSOC in op 90% | {{< badge "recommended" >}} |
| Schakel de PV-prognose om naar Solcast | {{< badge "recommended" >}} |
| Stel periodiek volledig laden in (bijv. op de 1e en 15e van de maand) | {{< badge "recommended" >}} |
| Minimaliseer het aantal extra opties | {{< badge "recommended" >}} |
