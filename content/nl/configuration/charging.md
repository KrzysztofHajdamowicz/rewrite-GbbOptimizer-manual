---
title: "Laden"
weight: 20
translationKey: "ladowanie"
---

# Laden

De module Laden beheert de schema's voor het laden van de batterij uit het net. In het Victron-systeem komt dit overeen met Schedules in de ESS-module.

> [!NOTE]
> {{< badge "victron-only" >}} We gaan ervan uit dat „Self-consumption above limit" op **PV** staat (en niet op „PV & Battery"), omdat we willen dat het schema 's nachts het ontladen van de batterij stopt.

## Tabel uit de installatie ophalen

{{< badge "victron-only" >}} Het programma maakt verbinding met de installatie en haalt 5 schema's (Schedulers) op.

## Wijzigingen van het laden

Je kunt de laadparameters aanpassen:
- Een laadregel **blokkeren / deblokkeren**
- Het **starttijdstip** en de **duur** wijzigen — kolommen „Nieuwe start" en „Nieuwe duur"
- De **SOC-limiet** wijzigen — kolom „Nieuwe SOCLimit"

Na een wijziging:
- **Opslaan** — de wijzigingen worden in het programma opgeslagen, maar niet naar de installatie gestuurd. Maakt het mogelijk scenario's in de [Batterijprognose]({{< relref "/configuration/battery-forecast" >}}) te testen
- **Naar installatie sturen** — de wijzigingen worden opgeslagen en naar de omvormer gestuurd

De knop **Alle nieuwe waarden wissen** reset de kolommen „Nieuwe start", „Nieuwe duur" en „Nieuwe SOCLimit".

## Laadparameters

| Parameter | Omvormer | Beschrijving |
|----------|----------|------|
| Rek het laden uit tot een vol uur | Allen | Verlaagt het laadvermogen zodat het een heel uur duurt. Gebruik dit samen met de volgende optie! |
| Speciale snelheidsberekening wanneer SOC = TargetSOC | Allen | Als SOC ≤ TargetSOC, bereken het laadvermogen dan volgens: PV - Verbruik |
| Modus wisselen naar „Zero Export To CT" tijdens laden uit het net | {{< badge "deye-only" >}} | Voorkomt overbelasting van de netzekering wanneer er tegelijk batterijen laden en grote verbruikers werken. Werkt samen met grid peak-shaving |
| MaxDischarge=0 instellen tijdens het laden | {{< badge "deye-only" >}} | Blokkeert het ontladen van de batterij tijdens het laden. Alleen gebruiken wanneer er niets op Load/Backup is aangesloten |
| MaxDischarge=0 instellen tijdens normaal bedrijf wanneer InkoopPrijs < PrijsInBatterij | {{< badge "deye-only" >}} | Blokkeert het ontladen van de batterij tijdens normaal bedrijf. Alleen gebruiken wanneer er niets op Load/Backup is aangesloten |
| PeakShaving W niet wijzigen tijdens laden | {{< badge "deye-only" >}} | Laat de waarde PeakShaving onveranderd tijdens het laden |

## Instellingen voor de optimizer

Het laden wordt geoptimaliseerd door de [Batterijprognose]({{< relref "/configuration/battery-forecast" >}}), indien:
- Niet geblokkeerd
- „SOCLimit niet optimaliseren via de Batterijprognose" niet is aangevinkt

Opties:
- **Minimale SOCLimit (%)** en **Maximale SOCLimit (%)** — beperken de „Nieuwe SOCLimit"-range (alleen SOC-optimizer)
- **Mag door de Batterijprognose worden geblokkeerd** — de optimizer mag het laden blokkeren om ruimte te maken voor PV

> [!NOTE]
> Het instellen van SOCLimit = 5% blokkeert het ontladen van de batterij.

## Dynamic Charge — dynamische wijziging van het laaduur

Dynamic Charge zoekt automatisch uren met de **laagste inkoopprijs** en verplaatst het laden daarheen.

> [!WARNING]
> Gebruik deze optie niet met de **prijsgebaseerde optimizer**!

Configuratie:

1. Voeg minstens één schema toe
2. Kies welke laadactie je wilt wijzigen
3. Voer in **vanaf welk uur** en **hoeveel uur** het programma moet zoeken
   - 24 uur → het beginuur is niet relevant, het programma controleert 24 u vanaf het huidige uur
   - Minder dan 24 uur → het programma controleert de opgegeven uren. Als de periode voorbij is — controleert het de volgende dag
4. Voer in **hoeveel uren** je wilt laden
5. Opslaan

Voor automatisering — stel een **uurlijkse taak** in (zie hieronder).

Om te testen — klik op **Laden nu optimaliseren**.

Het programma verplaatst het starttijdstip naar minimale prijzen. Als twee ladingen elkaar overlappen — zoekt het programma verschillende uren met minimale prijzen voor elk.

## Dynamic Charge: Laden blokkeren bij lage prijs

Blokkeert het ontladen van de batterij wanneer de prijs te laag is in vergelijking met de prijs van de laatste lading.

> [!WARNING]
> Gebruik deze optie niet met de **prijsgebaseerde optimizer**!

Configuratie:

1. Voeg minstens één regel toe
2. Kies de lading om te wijzigen (mag niet in andere modules worden gebruikt)
3. Voer in **vanaf welk uur** en **hoeveel uur** het programma moet zoeken naar een prijs die lager is dan die van de laatste lading
   - 24 uur → het beginuur is niet relevant
   - Minder dan 24 uur → controleert de opgegeven uren; indien voorbij — de volgende dag
4. Voer in **hoeveel %** bij de prijs van de laatste lading moet worden opgeteld (bijv. 10%)
5. Opslaan

**Hoe het werkt** (voorbeeld: vanaf uur 0, controle 6 u):
1. Zoekt de **prijs van de laatste lading**: vanaf het uur vóór het einde van de periode, terugwerkend. Neemt de laatste lading binnen de periode of de eerste lading vóór de periode
2. Controleert de uren waarin de inkoopprijs < prijs laatste lading + „Procent toevoegen". Zoekt vanaf het begin van de periode (of vanaf het einde van het laden)

> [!NOTE]
> Eén Lading kan in meerdere blokkades worden gebruikt, als de uurperioden elkaar niet overlappen.

> [!WARNING]
> Als je een Lading hebt die dynamisch verandert (bijv. van 0 tot 6), configureer dan het blokkeerschema met **dezelfde periode** (van 0 tot 6) **of langer** (bijv. van 0 tot 9).

## Uurlijkse taak

Om ladingen automatisch te optimaliseren en gegevens elk uur naar de installatie te sturen:

Vink **Ladingen automatisch elk uur optimaliseren en gegevens naar installatie sturen** aan.

## Weeralarmen

De module laadt de batterij automatisch tot 100% (of een andere waarde) wanneer belangrijke weeralarmen naderen.

Configuratie:
1. Voeg een land toe (bijv. Polen met MeteoAlarm of IMGW)
2. Voeg de types alarmen toe waarin je geïnteresseerd bent
3. Geef voor elk type aan **vanaf welk niveau** (dit en hoger) en **welke SOC** moet worden afgedwongen

Wanneer er een alarm van een bepaald type en niveau verschijnt — zal de prijsgebaseerde optimizer het aangegeven SOC-niveau afdwingen voor de duur van het alarm, zelfs ten koste van laden uit het net.
