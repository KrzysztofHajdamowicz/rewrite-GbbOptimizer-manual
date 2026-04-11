---
title: "Installatieparameters"
weight: 10
translationKey: "parametry-instalacji"
---

# Installatieparameters

Hieronder worden alle configuratieparameters van een installatie in GbbOptimizer beschreven, thematisch gegroepeerd.

## Type

| Parameter | Eenheid | Beschrijving |
|----------|-----------|------|
| Type | — | Type verbinding met de omvormer (Victron, Solarman, GbbConnect2, DongleDirect, SolarAssistant) |
| Aantal tijdsintervallen per dag | — | Aantal tijdsintervallen per dag. In Polen geldt 60 intervallen voor particuliere klanten |

## Installatie

| Parameter | Eenheid | Beschrijving |
|----------|-----------|------|
| Naam | — | Unieke naam van de installatie binnen het account |
| Tijdzone | — | Tijdzone van de locatie van de installatie |
| Maximaal importvermogen uit het net | kW | Aansluitparameter — maximaal vermogen dat uit het net kan worden afgenomen |
| Maximaal exportvermogen naar het net | kW | Aansluitparameter — maximaal vermogen dat naar het net kan worden geleverd |
| Welk % PV is aangesloten aan de DC-zijde? | % | `0%` — alle PV aangesloten op AC. `100%` — alle PV aangesloten op DC |
| Breedte-/lengtegraad | — | Geografische locatie van de installatie. Wordt gebruikt door de modules: Meteo en PV-prognoses |

## Prijsbronnen

| Parameter | Beschrijving |
|----------|------|
| Inkoop: Tarief voor inkoopprijzen | Bron van de geïmporteerde inkoopprijzen voor energie |
| Transport: Tarief voor transportprijzen | Bron van de transportprijzen (netbeheer). Leeg = 0 |
| Verkoop: Tarief voor verkoopprijzen | Bron van de geïmporteerde verkoopprijzen voor energie |

Details over de prijsformules — in de module [Prijzen]({{< relref "/configuration/prices" >}}).

## Batterij

| Parameter | Eenheid | Beschrijving |
|----------|-----------|------|
| Batterijcapaciteit (bruto) | kWh | Totale capaciteit van de batterij |
| Gemiddelde batterijspanning | V | Wordt gebruikt om W uit A en A uit W te berekenen. Mag een benadering zijn |
| Minimale {{< glossary "SOC" >}} van de batterij | % | {{< glossary "MinSOC" >}} — harde reserve. Onder deze waarde wordt energie alleen in noodsituaties gebruikt |
| Maximaal laadvermogen van de omvormer (DC) | kW | Maximaal laadvermogen aan de DC-zijde |
| Maximaal ontlaadvermogen van de omvormer (DC) | kW | Maximaal ontlaadvermogen aan de DC-zijde |
| Maximaal BMS-laadvermogen van de batterij (DC) | kW | Relevant wanneer het afwijkt van het omvormervermogen en PV op DC-zijde is aangesloten |
| Maximaal BMS-ontlaadvermogen van de batterij (DC) | kW | Relevant wanneer het afwijkt van het omvormervermogen en PV op DC-zijde is aangesloten |
| Verliezen bij het laden van de batterij uit het net | % | Verliezen bij het laden (inclusief de wijze waarop het BMS de SOC berekent) |
| Verliezen bij het ontladen van de batterij naar het net/verbruik | % | Verliezen bij het ontladen (inclusief de wijze waarop het BMS de SOC berekent) |

## Victron

{{< badge "victron-only" >}}

| Parameter | Beschrijving |
|----------|------|
| VRM Portal Id | Identifier van het {{< glossary "VRM" >}}-portaal. Te vinden in: Cerbo → Settings → VRM Online Portal → VRM Portal ID |
| Installation Id | Nummer in de URL van de VRM-pagina |
| VRM-login/e-mail | Login voor het VRM-portaal |
| VRM-wachtwoord | Wachtwoord voor het VRM-portaal (als je geen 2FA gebruikt) |
| VRM Token | Token voor tweefactorauthenticatie (2FA) |
| VRM Instance-nummer van het VE.Bus System-apparaat | Normaal heeft de omvormer nummer `276`, maar dit kan anders zijn |

## Solarman / DeyeCloud

| Parameter | Van toepassing | Beschrijving |
|----------|---------|------|
| Inlogmethode | — | E-mail, login of telefoonnummer |
| E-mail / Login / Telefoonnummer | — | Inloggegevens voor Solarman/DeyeCloud |
| Wachtwoord | — | Wachtwoord voor Solarman/DeyeCloud |
| Inloggegevens onthouden | — | Automatisch opnieuw verbinden. Zonder dit is handmatig inloggen vereist (e-mailmelding) |
| SerialNo van de omvormer kiezen | — | Kies na verbinding het serienummer van de omvormer |
| Type omvormer | — | Type omvormer. **Mag niet verkeerd zijn!** Een verkeerde keuze en het verzenden van gegevens vereist een fabrieksreset van de omvormer |
| Deye: MI/GEN-productie bij PV-productie optellen | {{< badge "deye-only" >}} | Op sommige firmwareversies moet de productie van de GEN-ingang handmatig worden opgeteld |
| Deye: Er is geen CT, dus probeer ZeroToCT niet in te stellen | {{< badge "deye-only" >}} | Bij ontbrekende CT keert het programma na de ontlading terug naar ZeroToLoad in plaats van ZeroToCT |
| Deye: Tijd van de omvormer om middernacht instellen | {{< badge "deye-only" >}} | Synchroniseert de klok van de omvormer om middernacht |
| SOC-gegevens uit HomeAssistant/SolarAssistant | — | Haal de {{< glossary "SOC" >}} niet op uit de omvormer — wordt aangeleverd door HA/SA |
| GridIn/GridOut-gegevens opgehaald uit | — | Haal GridIn/GridOut niet op uit de omvormer — gegevens uit HomeAssistant of een IoT-meter |
| Verbruiksgegevens uit HomeAssistant/SolarAssistant | — | Haal het verbruik niet op uit de omvormer — wordt aangeleverd door HA/SA |

### Back-upverbinding — DeyeCloud

Alleen van toepassing op installaties van het type Solarman. Details op de pagina [DeyeCloud]({{< relref "/installation/connection-methods/deye-cloud" >}}).

| Parameter | Beschrijving |
|----------|------|
| Hoe de back-upverbinding moet worden gebruikt | **Uitgeschakeld** / **Ingeschakeld** (bij Solarman-fout) / **Alleen back-up** (altijd DeyeCloud) |
| Inlogmethode / E-mail / Wachtwoord | Inloggegevens voor DeyeCloud |
| Inloggegevens onthouden | Automatisch opnieuw inloggen bij DeyeCloud |
| SerialNo van de omvormer kiezen | Kies na verbinding het serienummer |

## Omvormerparameters

{{< badge "deye-only" >}}

| Parameter | Beschrijving |
|----------|------|
| Besturen via V, niet via SOC | De omvormer gebruikt spanning (V) in plaats van SOC in TimeOfUse |
| Bereken ook de actuele SOC uit V | Bereken de actuele SOC op basis van de spanning. Als dit niet is aangevinkt — wordt de SOC uit de omvormer gelezen |

## GbbShunt

{{< badge "deye-only" >}} Alleen van toepassing op Solarman + Deye-installaties. Details op de pagina [Solarman]({{< relref "/installation/connection-methods/solarman" >}}).

| Parameter | Eenheid | Beschrijving |
|----------|-----------|------|
| Ingeschakeld | — | Activeert de GbbShunt-module |
| Minimale SOC van de batterij / V waarbij SOC → MinSOC | V | Spanning waarbij de SOC op {{< glossary "MinSOC" >}} wordt gezet |
| Maximale SOC van de batterij / V waarbij SOC → MaxSOC | V | Spanning waarbij de SOC op {{< glossary "MaxSOC" >}} wordt gezet |
| Verliezen bij laden + ontladen | % | Percentage energie dat in de berekeningen wordt genegeerd |
| V tijdens het laden van de batterij | V | Spanning die naar TimeOfUse wordt gestuurd in plaats van de uit de doel-SOC berekende waarde |
| V tijdens het ontladen van de batterij | V | Spanning die naar TimeOfUse wordt gestuurd in plaats van de uit de doel-SOC berekende waarde |

## Technische ondersteuning

| Parameter | Eenheid | Beschrijving |
|----------|-----------|------|
| E-mail sturen bij verlies van verbinding | uren | Na hoeveel uur zonder verbinding het programma een melding verstuurt. Leeg = geen meldingen |
| E-mail met fouten uit het logboek sturen | — | Verstuurt elk uur een overzicht van fouten uit het logboek |
| Extra e-mailadressen | — | Extra adressen voor meldingen. Handig voor installateurs, zodat de klant ook e-mails ontvangt |
| De installatie delen met technische ondersteuning | — | Geeft de technische ondersteuning toegang tot jouw installatie. Neem eerst contact op via Discord |
