---
title: "Batterijprognose"
weight: 10
translationKey: "prognoza-baterii"
---

# Batterijprognose

De centrale module van GbbOptimizer. Analyseert de {{< glossary "SOC" >}} van de batterij voor de komende 24 uur (of langer) op basis van PV-lading, netlading, ontlading en verbruik door het huis. Bevat een optimizer die automatisch de laad- en ontlaadparameters kiest.

In deze module kun je:
- De prognose van de batterij-SOC voor de komende 24 uur analyseren
- Zien wanneer de SOC onder of boven de minimale of maximale waarden komt
- Laad- en ontlaadplannen optimaliseren
- Inkoop- en verkoopprijzen en winsten bekijken

## Kolommen van de prognosetabel

De tabel toont gegevens voor de komende 24 uur. Afkortingen: **DC** = gelijkstroom, **AC** = wisselstroom.

### Batterij

| Kolom | Beschrijving |
|---------|------|
| Dag | Dag |
| Uur | Uur op die dag |
| Begin batterij % (kWh) AC/DC | SOC en kWh van de batterij aan het begin van het uur (in AC en DC) |
| PV-prognose (kWh AC) | Prognose van de PV-productie in dat uur |
| PV-prognose % (kWh DC) | Hoeveel kWh van PV naar de batterij gaat (na conversie naar DC), na aftrek van het huishoudelijk verbruik |
| Verbruik +Extra (kWh AC) | Prognose van het huisverbruik (inclusief Extra Verbruik) |
| Verbruik +Extra % (kWh DC) | Hoeveel kWh uit de batterij wordt gehaald om het verbruik minus PV te dekken |
| Laden uit het net (kWh AC) | Hoeveel uit het net wordt gehaald om de batterij te laden |
| Laden uit het net % (kWh DC) | Zoals hierboven, na conversie naar DC |
| Ontladen | Status van het ontlaadplan voor dat uur |
| Ontladen (kWh AC) | Hoeveel uit de batterij naar het net is gestuurd (in AC) |
| Ontladen % (kWh DC) | Hoeveel uit de batterij naar het net is gestuurd (in DC) |
| Einde batterij (kWh AC) | kWh in de batterij aan het einde van het uur. **= Begin AC + PV AC - Verbruik AC + Laden AC - Ontladen AC** |
| Einde batterij % (kWh DC) | SOC en kWh aan het einde van het uur. **= Begin DC + PV DC - Verbruik DC + Laden DC - Ontladen DC** |
| Onder Min | „Ja" = de batterij kan aan het eind onder {{< glossary "MinSOC" >}} zakken |
| Boven Max | „Ja" = de batterij kan aan het eind boven {{< glossary "MaxSOC" >}} komen |

### Winst

| Kolom | Beschrijving |
|---------|------|
| Winstbedrag | **= Verbruiksbedrag - (Inkoopbedrag - Waardeverandering batterij) + Verkoopbedrag - Batterijkostenbedrag** |
| Niet-betaald bedrag voor energie | **= Verkoopbedrag - (Inkoopbedrag - Waardeverandering batterij) - Batterijkostenbedrag** |
| Batterijkostenbedrag | „Kosten van batterijgebruik per kWh" × „Batterijlading kWh" — batterijafschrijving |
| Uit het net (kWh) | Hoeveel uit het net is gehaald in dat uur |
| Inkoopprijs | Inkoopprijs van energie |
| Inkoopbedrag | Uit het net × Inkoopprijs |
| Naar het net (kWh) | Hoeveel naar het net is gestuurd |
| Verkoopprijs | Verkoopprijs van energie |
| Verkoopbedrag | Naar het net × Verkoopprijs |
| Verbruik (kWh) | Huisverbruik |
| Verbruiksprijs | Prijs van de door het huis verbruikte energie |
| Verbruiksbedrag | Verbruik × Verbruiksprijs |

### Waarde van de energie in de batterij

| Kolom | Beschrijving |
|---------|------|
| Batterijlading (kWh) | >0 laden, <0 ontladen — hoeveel energie er naar/uit de batterij is gegaan |
| Laden uit het net (kWh) | Hoeveel van de energie naar de batterij uit het net komt |
| Ontladen (kWh) | Hoeveel energie uit de batterij is gehaald |
| Begin kWh in de batterij | Energie in de batterij aan het begin van het uur (boven MinSOC%) |
| Beginwaarde (PLN) | Waarde van de energie in de batterij aan het begin van het uur |
| Eind kWh in de batterij | Energie in de batterij aan het einde van het uur (boven MinSOC%) |
| Eindwaarde (PLN) | Waarde van de energie in de batterij aan het einde van het uur |
| Waardeverandering (PLN) | **= Eindwaarde - Beginwaarde.** Ontladen: Ontladen kWh × Gemiddelde prijs van het vorige uur. Laden: Laden uit het net kWh × Inkoopprijs |
| Gemiddelde eindprijs (PLN) | Eindwaarde / Eind kWh in de batterij |

## Optimizer

Nadat je op **Optimizer nu uitvoeren** hebt geklikt, kan het programma wijzigen:
- SOCLimit in de module [Laden]({{< relref "/configuration/charging" >}}) (en zelfs het laden blokkeren)
- MinSOC in het [ontlaadplan]({{< relref "/configuration/discharging" >}})
- DDBD (Dynamically Disable Battery Discharge) uitschakelen

### Optimizer 1: Op basis van SOC

**„Laden/ontladen wordt geoptimaliseerd op basis van SOC (met extra optimizers)"**

Deze optimizer probeert:
- Op een bepaald moment 100% (of {{< glossary "MaxSOC" >}}) te bereiken (maar niet te lang)
- De batterij boven {{< glossary "MinSOC" >}} te houden — wat belangrijker is
- Gebruikt de ingestelde laad- en ontlaadmomenten (die moeten vooraf handmatig zijn ingesteld)

> [!NOTE]
> - Kan worden gecombineerd met {{< glossary "Dynamic Discharge" >}} en Dynamic Charge
> - Kan de batterij 's nachts (goedkoop tarief) laden zodat er overdag ruimte is voor PV
> - Kan de batterij bij hoge prijzen ontladen zodat PV hem daarna tot MaxSOC kan laden
> - Als de inkoopprijs < 0, wordt het laden in die uren op MaxSOC gezet

### Optimizer 2: Op basis van prijzen {{< badge "recommended" >}}

**„Laden/ontladen wordt geoptimaliseerd op basis van in- en verkoopprijzen (om de winst te vergroten)"**

Probeert de som in de kolom „Winstbedrag" te maximaliseren — zoekt de beste combinatie van laden/ontladen per uur.

> [!WARNING]
> Na de optimalisatie worden nieuwe instellingen **niet automatisch verzonden** naar de installatie. Controleer de resultaten en klik daarna op **Stuur nieuwe SOCLimit uit Laden naar de installatie**.

> [!NOTE]
> - Moet elk uur worden uitgevoerd
> - Vereist dat de import in de module [Winsten]({{< relref "/configuration/profits" >}}) elk uur wordt uitgevoerd
> - Laden wanneer de energie nooit wordt verbruikt (omdat de prognose 24 uur betreft) is „gratis" — aan het einde van de periode verschijnt vaak overbodig laden. Wacht enkele uren op een betere prognose
> - Elke ingeschakelde extra optie verlaagt de winst!

## Parameters van de prijsgebaseerde optimizer

### SOC

| Parameter | Beschrijving |
|----------|------|
| Ik wil liever meer in de batterij dan minder | Strategie voor situaties waarin verschillende ladingen dezelfde winst opleveren: **Niveau 0** — liever niet laden. **Niveau 1** — liever meer laden. **Niveau 2** — liever meer laden + liever laden dan niet laden (voor het G12w-tarief) |
| Maximale SOC van de batterij (%) | De optimizer probeert deze waarde niet te overschrijden |
| Minimale SOC van de batterij (%) | De optimizer probeert niet onder deze waarde te komen |
| Verhoog Min/Max SOC met X als PV-prognose < Y | Verhoog de reserve in de batterijen wanneer de PV-prognose laag is |
| Dagelijks MaxSOC (100%) afdwingen — UPS | Eenmaal per dag wordt de batterij gedurende 2-3 uur tot 100% geladen |
| ... alleen tijdens optimalisatie van middernacht tot zonsopgang | De afdwinging wordt alleen 's nachts berekend — als de weersverwachting daalt, probeert het programma overdag niet krampachtig 100% te bereiken |
| ... vervang zonsondergang door een vast uur | Bijv. het einde van het goedkope tarief in plaats van zonsondergang |

### Batterijbalancering

| Parameter | Beschrijving |
|----------|------|
| Minimale SOC om als balancering te tellen | SOC waarboven het programma aanneemt dat er balancering plaatsvindt. Als de SOC slechts licht daalt — voer een lagere waarde in |
| Moet minstens (uren) duren | Duur van de balancering |
| Lijst van dagen in de maand voor 3u×100% | Forceer balancering op deze dagen van de maand (gescheiden door komma's) |
| Hoeveel dagen terug controleren 3u×100% | Blokkeert te frequente balancering |
| Na hoeveel dagen opnieuw 3u×100% uitvoeren | Alternatieve afdwinging: elke X dagen vanaf de vorige |
| Handmatig 3u×100% vandaag afdwingen | Eenmalige afdwinging, schakelt zichzelf uit na balancering |
| 3u×100% als prijs < ... voor ten minste ... uur | Balancering afdwingen bij lage inkoopprijs |

### Laden en ontladen

| Parameter | Beschrijving |
|----------|------|
| Batterij laden uit het net | Laat toe om laden uit het net uit te schakelen |
| Batterij ontladen naar het net | Laat toe om ontladen uit te schakelen (of de instellingen uit het ontlaadplan te behouden) |
| Min. prijsverschil voor ontladen naar het net | Minimaal verschil tussen de prijs van de energie in de batterij en de verkoopprijs. Waarde 0 = het programma ontlaadt niet met verlies |
| Niet ontladen wanneer verkoopprijs < X | Blokkeert ontladen bij lage verkoopprijs |
| Niet ontladen wanneer inkoopprijs < X | Blokkeert ontladen — idee: tijdens goedkoop tarief uit het net nemen, batterij uit PV laden, ontladen bij duur tarief |
| Niet uit het net laden wanneer inkoopprijs > X | Blokkeert laden bij een te hoge prijs |

### Import / export uit het net

| Parameter | Beschrijving |
|----------|------|
| Probeer niet uit het net te importeren | De optimizer vermijdt het afnemen uit het net (maar het kan voorkomen). Om dit volledig te blokkeren — vink „Geblokkeerd" aan in de module [Laden]({{< relref "/configuration/charging" >}}) |
| Probeer niet naar het net te exporteren | De optimizer vermijdt export (van PV en batterij) |
| Verkoop niet meer dan de niet-gecorrigeerde 24-uurs PV-prognose | *(Optie voor PL)* Blokkeert de verkoop vanuit de batterij van meer dan met PV is geproduceerd. Rekenkundige kost: O(n) |
| Probeer niet te exporteren wanneer verkoopprijs < 0 | Vermijd export bij negatieve prijzen |

### Overige parameters

| Parameter | Beschrijving |
|----------|------|
| Blokkeer stijgen boven MaxSOC | Forceert ontladen tot MaxSOC |
| Blokkeer dalen onder MinSOC | Forceert laden tot MinSOC |
| Niet uit het net laden wanneer EV zal laden | Tijdens het laden van EV — geen batterij laden uit het net |
| Niet ontladen wanneer EV zal laden | Tijdens het laden van EV — geen batterij ontladen |
| Elke 5 min testen op EV-lading | Automatische detectie van EV-lading en uitschakelen van batterij laden/ontladen. Hoeft niet vooraf ingevoerd te worden |
| Probeer > 24 u te prognosticeren | De optimizer neemt meer uren in beschouwing (tot het einde van de bekende prijzen). Kan zichzelf uitschakelen als het te lang duurt |
| Niet terugvallen op prognose „niets doen" | Schakelt de controle uit of de berekende prognose niet slechter is dan „niets doen" |
| Reken de energiekosten op het moment van laden | Normaal gesproken worden kosten verrekend op het moment van verbruik. Deze optie rekent op het moment van aankoop |
| Min/Max SOC aan het einde van de prognose | Forceer SOC-niveau aan het einde van de prognose |
| Kosten van batterijgebruik per kWh | = Aanschafkosten batterij / (aantal cycli × capaciteit kWh). We raden aan dit leeg te laten |

## Uitvoerplanning

| Tijdsintervallen | Optimizer | Export naar de omvormer |
|-------------------|---------------|----------------------|
| 24 (60 min) | na x:00 | na x:00 (herhaling bij fout) |
| 48 (30 min) | na x:00 en x:30 | na x:00 en x:30 (herhaling bij fout) |
| 96 (15 min) | na x:00 en x:30 | na x:00, x:15, x:30, x:45 |

## Scenario's testen

Om verschillende scenario's te testen:
- Maak meer dan één [Verbruiksprofiel]({{< relref "/configuration/consumption-profiles" >}}) aan
- Maak meer dan één ontlaadplan aan
- Schakel de PV-prognose tijdelijk uit (worstcase-scenario)
- Stel in de module Laden „Nieuwe start", „Nieuwe duur" en „Nieuwe SOCLimit" in zonder naar de installatie te sturen

Kies in de sectie **Filters** het huidige Verbruiksprofiel, het ontlaadplan en schakel optioneel de PV-prognose uit.

## Uurlijkse taken

Zodra handmatige optimalisatie correct werkt — stel de uren voor automatische uitvoering in.

Beste uur (voor de SOC-optimizer): de beginuren van actieve ladingen. Als je een ontlaadplan gebruikt — bij voorkeur elk uur.

Om te starten:
1. Vink **Automatisch klikken op: „Alle gegevens ophalen" en „Optimizer uitvoeren"** aan
2. Vink **... en „Nieuwe SOCLimit naar installatie sturen"** aan
3. Voeg één of meer uren toe

### Extra opties

| Optie | Beschrijving |
|-------|------|
| Ook halverwege het uur uitvoeren | Voor 24 intervallen (60 min): extra uitvoering om x:30. Niet aanbevolen |
| Data eerder naar de omvormer sturen | Stuur eerst de instellingen (berekend een uur eerder), voer daarna de optimizer uit en stuur dan de nieuwe instellingen. Handig wanneer de optimizer 4-5 min duurt. Voor 96 intervallen: altijd aan |
| PV-prognose alleen ophalen tijdens uurlijkse taken | De PV-prognose wordt alleen opgehaald tijdens uurlijkse taken (niet bij „Alle gegevens ophalen"). Maakt het mogelijk om de laatst gebruikte prognose te zien |
