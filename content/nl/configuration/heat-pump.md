---
title: "Warmtepomp / airco"
weight: 70
translationKey: "pompa-ciepla"
---

# Prognose warmtepomp / airco

Module voor het voorspellen van het verbruik van een warmtepomp (WP) of airco op basis van de buitentemperatuur.

## Waarom een aparte module?

Warmtepompen en airco's werken (net als EV-laders) niet volgens het dagritme — ze hangen af van de temperatuur. Daarom is het beter om ze **uit te sluiten van het gemiddelde** in de module [Verbruiksprofielen]({{< relref "/configuration/consumption-profiles" >}}) en ze onder te brengen in [Extra verbruik]({{< relref "/configuration/ev-additional-loads" >}}).

## Stap-voor-stap configuratie

1. Voer **breedte- en lengtegraad** in in de [installatieparameters]({{< relref "/installation/installation-parameters" >}})
2. Importeer de weersvoorspelling
3. Klik op **WP-parameters** en voer het kWh-verbruik van de WP/airco in voor elk uur (minimaal 2 waarden voor verschillende temperaturen)
4. Klik op **WP-prognose berekenen** en controleer de resultaten
5. Klik op **WP-prognose exporteren naar module Extra verbruik** (menu: Verbruiksprofielen → Extra verbruik → Filter: „Type" = „Warmtepomp")
6. Schakel uurlijkse taken in: **Weersvoorspelling importeren**, **WP-prognose berekenen**, **WP-prognose exporteren naar module Extra verbruik**

## WP-parameters — tabel temperatuur vs. verbruik

Geef voor elk uur aan hoeveel kWh de WP/airco verbruikt bij de betreffende buitentemperatuur.

Tips:
- Je kunt alleen de eerste kolom invullen — met de **Kopieertool** onderaan kun je gegevens tussen kolommen kopiëren
- Het is niet nodig alle temperaturen in te vullen (van -20°C tot +40°C). **Minstens 2 waarden** volstaan — het programma interpoleert automatisch de rest proportioneel
- Hoe meer gegevens, hoe nauwkeuriger de prognose
- Je kunt de gegevens in de loop van het jaar aanvullen, naarmate je meer waarnemingen verzamelt

> [!NOTE]
> Voorbeeld: Voer alleen het verbruik in voor de uren en temperaturen die je kent — bijv. 10°C, 0°C en -5°C.
