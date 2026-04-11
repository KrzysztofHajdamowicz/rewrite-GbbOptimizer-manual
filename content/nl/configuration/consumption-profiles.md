---
title: "Verbruiksprofielen"
weight: 50
translationKey: "profile-zuzycia"
---

# Verbruiksprofielen

Module voor het voorspellen van het energieverbruik van het huis. Het verbruik is onderverdeeld in uren en weekdagen.

## Handmatige invoer

Voer de kWh voor elk uur en elke weekdag rechtstreeks in de tabel in.

## Gegevens uit de installatie importeren

Stel de importperiode in en klik op **Importeren uit installatie**. Het programma berekent het gemiddelde verbruik voor elk uur en elke weekdag op basis van de gegevens uit de omvormer.

### Automatische import

Vink **Gegevens automatisch 's nachts importeren** aan — het programma importeert elke nacht de gegevens van de laatste 28 dagen.

## Handmatige import vanuit Excel

1. Bereid de gegevens in Excel voor: uren in rijen, weekdagen in kolommen
2. Kopieer de gegevens (Ctrl+C)
3. Plak ze in het veld „Jouw profiel"
4. Kies het kolomscheidingsteken en het decimaalteken
5. Klik op **Importeren**

> [!NOTE]
> - Een lege cel = het programma wijzigt de gegevens op die plek niet
> - Je kunt minder dan 24 rijen of 7 kolommen plakken — ontbrekende uren/dagen blijven ongewijzigd
> - Overtollige kolommen en rijen worden genegeerd

## Meerdere profielen

Je kunt meerdere verbruiksprofielen definiëren. Het geselecteerde profiel wordt gebruikt in de [Batterijprognose]({{< relref "/configuration/battery-forecast" >}}) voor het weergeven van gegevens, grafieken en optimalisatie.

## Beperking van de importperiode

In de profielbewerking kun je instellen:
- **Vanaf maand / Vanaf dag** — beperkt de dag waarop de data-import start
- **Tot maand / Tot dag** — beperkt de dag waarop de import eindigt

Handig bijvoorbeeld voor een **vakantieprofiel**, waarbij de import alleen gegevens uit de vakantieperiode moet gebruiken.

Als „Vanaf dag" leeg is — gebruikt het programma de eerste dag van de maand. Als „Tot dag" leeg is — wordt de laatste dag gebruikt.

## Automatische profielwisseling

Om profielen automatisch te wisselen:

1. Definieer ten minste twee profielen met een ingevuld „Vanaf maand"-veld (en optioneel „Vanaf dag"), en een leeg „Tot maand"-veld
2. Vink **Profiel automatisch wisselen op basis van „Vanaf maand/Dag"** aan

> [!NOTE]
> Dit beperkt ook de importperiode voor gegevens uit de installatie!

## Automatisch vakantieprofiel

Definieer een profiel met **zowel** „Vanaf maand/dag" als „Tot maand/dag" ingevuld. Het programma:
- Schakelt het vakantieprofiel in op de startdatum
- Keert een dag na het einde terug naar het normale profiel
