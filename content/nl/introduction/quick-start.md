---
title: "Snelstart"
weight: 20
translationKey: "szybki-start"
---

# Snelstart

Een stap-voor-stap handleiding om GbbOptimizer voor jouw PV-installatie in gebruik te nemen.

## 1. Maak een account aan en voeg een installatie toe

Ga naar de GbbOptimizer-website en maak een account aan. Voeg vervolgens een nieuwe installatie toe door de juiste optie te kiezen, afhankelijk van jouw omvormer:

| Omvormer | Menu-optie |
|----------|-------------|
| **Victron** (Cerbo GX of ander GX-apparaat) | „Nieuwe installatie met Victron System toevoegen" |
| **Deye** via DeyeCloud | „Nieuwe installatie met een Deye-omvormer verbonden met DeyeCloud toevoegen" |
| **Deye** via Solarman | „Nieuwe installatie met Solarman toevoegen" |
| **Deye** via Home Assistant | „Nieuwe installatie met Home Assistant toevoegen" |
| **Andere omvormer** via Solarman | „Nieuwe installatie met Solarman toevoegen" |
| **Andere omvormer** via Home Assistant | „Nieuwe installatie met Home Assistant toevoegen" |
| **SofarSolar** | „Installatie met DongleDirect (Deye, SofarSolar)" |

> [!NOTE]
> Als je Deye-omvormers in een Master-Slave-opstelling hebt, kies dan „Installatie met Solarman" en voeg de Master toe als hoofdomvormer en de Slave als extra omvormer in de installatieparameters.

Elke installatie krijgt een uniek {{< glossary "PlantId" >}} en {{< glossary "PlantToken" >}}.

## 2. Vul de installatiegegevens in

Vul alle velden (in ieder geval die met een **\***) in het installatieformulier in. Klik daarna op **„Opslaan en doorgaan met FastSetup"**.

{{< glossary "FastSetup" >}} leidt je door de basisconfiguratie:

- Toevoegen van PV-vlakken
- Keuze van de bron voor de PV-prognose
- Basisparameters van de batterij

Klik na het invullen van alle velden op **„Wijzigingen opslaan"**.

## 3. Configureer de prijzen

In de module [Prijzen]({{< relref "/configuration/prices" >}}):

1. Klik op **„Kies tarief van netbeheerder en energieleverancier"**
2. Kies je distributietarief en je leverancierstarief
3. Klik op **„Geselecteerde tarieven importeren"**

Als alternatief kun je de in- en verkoopprijzen handmatig configureren.

> [!WARNING]
> Vergeet niet om de transportkosten (netbeheer) in te stellen voor de inkoopprijzen. Zonder die kosten kan de optimizer de rendabiliteit van laden uit het net niet correct berekenen.

## 4. Configureer het verbruiksprofiel

In de module [Verbruiksprofielen]({{< relref "/configuration/consumption-profiles" >}}) heb je twee opties:

- **Handmatig invoeren** — voer een schatting van het verbruik per uur in
- **Importeren uit de installatie** — wacht ~een week totdat het programma gegevens uit de omvormer verzamelt en het gemiddelde verbruik berekent

> [!NOTE]
> Als je het verbruiksprofiel niet handmatig wilt invoeren, wacht dan een week — het programma verzamelt automatisch gegevens en berekent het profiel. Gedurende die tijd zou {{< glossary "Test Mode" >}} sowieso actief moeten zijn.

## 5. Controleer de PV-prognose

Verifieer in de module [Batterijprognose]({{< relref "/configuration/battery-forecast" >}}) of de PV-prognose dicht bij de werkelijke productie ligt. Zo niet, probeer dan de bron voor de PV-prognose te wijzigen in de installatieparameters.

De {{< glossary "Correction Factor" >}} wordt automatisch gekalibreerd gedurende ongeveer een week werking.

## 6. Wacht in de testmodus

Een nieuwe installatie start in {{< glossary "Test Mode" >}} — de optimizer voert berekeningen uit, maar **stuurt geen commando's naar de omvormer**.

In de eerste week:

- Wordt het verbruiksprofiel bijgewerkt (als automatische import is ingeschakeld)
- Wordt de {{< glossary "Correction Factor" >}} voor de PV-prognose gekalibreerd
- Kun je bekijken wat de optimizer *van plan is* te doen, zonder risico

## 7. Testmodus uitschakelen

Schakel na ~een week, wanneer je zeker weet dat:

- **De prijzen** correct zijn (inclusief alle transportkosten)
- **De PV-prognose** dicht bij de werkelijkheid ligt
- **Het verbruiksprofiel** realistisch is

...de {{< glossary "Test Mode" >}} in de module [Batterijprognose]({{< relref "/configuration/battery-forecast" >}}) uit. Vanaf dat moment begint de optimizer commando's naar de omvormer te sturen.

## Instructievideo's

- [Een Victron-systeem toevoegen aan GbbOptimizer](https://youtu.be/5q6gORx1KUY)
- [Een Deye-omvormer toevoegen via Solarman](https://youtu.be/y8fhh1UecqQ)
- [In- en verkoopprijzen configureren](https://youtu.be/m27uQfO60pc)

## Alleen EV-laadoptimalisatie (zonder PV)

Als je alleen het opladen van een elektrische auto wilt optimaliseren, zonder PV-installatie:

1. Voeg een nieuwe installatie toe van het type **Home Assistant**
2. Vul de velden in:
   - Naam
   - Aansluitingsvermogen — import
   - Aansluitingsvermogen — export → vul **0** in
   - Batterijcapaciteit kWh → vul **0** in
3. Klik op **„Opslaan en doorgaan met FastSetup"**, op deze pagina:
   - Vink **„Eerste PV-vlak toevoegen"** uit
   - Vink **„EV: Automatisch uurlijks gegevens uit EV-laders importeren"** aan
4. Klik op **„Opslaan"** — je wordt naar het menu Prijzen geleid:
   - Kies het tarief van netbeheerder en energieleverancier
   - Klik op **„Geselecteerde tarieven importeren"**
5. Ga naar de module [Extra verbruik / EV]({{< relref "/configuration/ev-additional-loads" >}}):
   - Voeg in de sectie „EV laden" je laadpaal toe
   - Configureer in de sectie „Auto EV laden" de laadvoorwaarden (kies bijv. onder „Voorwaarden" → „Prijs" → 3 laagste inkoopprijzen)

## Hoe verder?

- [Best practices]({{< relref "/introduction/best-practices" >}}) — tips om het maximale uit het systeem te halen
- [Laden]({{< relref "/configuration/charging" >}}) — configuratie van laadschema's
- [Ontladen]({{< relref "/configuration/discharging" >}}) — configuratie van batterijontlading
- [Batterijprognose]({{< relref "/configuration/battery-forecast" >}}) — de centrale module van de optimizer
