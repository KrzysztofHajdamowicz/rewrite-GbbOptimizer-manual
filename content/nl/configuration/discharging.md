---
title: "Ontladen"
weight: 30
translationKey: "rozladowanie"
---

# Ontladen

De ontlaadmodule bepaalt wanneer en hoe energie uit de batterij naar het net wordt gestuurd of wordt gebruikt om het huis te voeden. De sleutelparameter is {{< glossary "GridSetpoint" >}}.

## GridSetpoint — hoe het werkt

De {{< glossary "GridSetpoint" >}} bepaalt hoeveel energie er door de netmeter moet stromen:

- **Positieve waarde** (bijv. +100 W) — het systeem neemt energie uit het net. Overschot uit PV gaat naar de batterij.
- **Negatieve waarde** (bijv. -5000 W) — het systeem exporteert energie naar het net. Eerst uit PV, daarna uit de batterij.

**Voorbeeld 1:** GridSetpoint = +100 W

| Parameter | Waarde |
|----------|---------|
| PV produceert | 2000 W |
| Huis verbruikt | 500 W |
| Uit het net | +100 W |
| **Naar de batterij** | **1600 W** |

**Voorbeeld 2:** GridSetpoint = -5000 W

| Parameter | Waarde |
|----------|---------|
| PV produceert | 2000 W |
| Huis verbruikt | 500 W |
| Naar het net | 5000 W |
| **Uit de batterij** | **3500 W** |

**Voorbeeld 3:** GridSetpoint = -5000 W, veel PV

| Parameter | Waarde |
|----------|---------|
| PV produceert | 6000 W |
| Huis verbruikt | 500 W |
| Naar het net | 5000 W |
| **Naar de batterij** | **500 W** |

Om de batterij tijdens het ontladen te beschermen:
- Stel {{< glossary "MinSOC" >}} in — de batterij zakt niet onder dit niveau
- Vink „Batterij ontladen blokkeren" aan — de batterij zakt niet onder de actuele SOC (maar kan wel worden geladen)

## Eerste stap

Om te beginnen met ontladen:

1. Maak één **ontlaadplan** aan (tenzij er al een bestaat)
2. {{< badge "victron-only" >}} Als „Battery Life" in ESS is ingeschakeld — schakel het uit. Zet het op „Optimized (without BatteryLife)"

## Normaal ontladen

Om normaal ontladen in te stellen voor een geselecteerd uur:

1. Vink **Inschakelen** aan voor het geselecteerde uur
2. Voer **Max GridSetpoint** in — een negatieve waarde, hoeveel W er maximaal naar het net moet gaan
3. *(Optioneel)* Voer **MinSOC** in — begrenzing van het ontladen tot het aangegeven SOC-niveau

> [!NOTE]
> Het programma controleert de actuele SOC van de batterij. Als MinSOC hoger is dan de actuele SOC, stuurt het programma de actuele SOC. Dit voorkomt dat de batterij tot MinSOC wordt geladen in plaats van te worden ontladen.

Om de instellingen voor het huidige uur te testen — klik op **Gegevens nu naar installatie sturen**.

## Uurlijkse taken

Om automatisch elk uur gegevens naar de installatie te sturen:

1. Vink **Taak elk uur uitvoeren** aan
2. {{< badge "victron-only" >}} Voer de huidige MinSOC (uit ESS in Cerbo) in het veld **Standaard MinSOC na ontladen** in
3. {{< badge "victron-only" >}} Voer de huidige GridSetpoint (uit ESS) in het veld **Standaard GridSetpoint na ontladen** in
4. Wijzigingen opslaan

> [!NOTE]
> - Elk uur stuurt het programma alleen ontlaadgegevens voor uren waarbij „Inschakelen" is aangevinkt
> - Na het laatste ontlaaduur herstelt het programma de standaardwaarden
> - De optie „Niet ontladen als verkoopprijs < laatste inkoopprijs" blokkeert ontladen wanneer verkopen niet rendabel zou zijn

## Voorwaardelijk ontladen — wanneer prijs > minimum

Om alleen te ontladen wanneer de verkoopprijs een drempel overschrijdt:

1. Vink **Inschakelen** aan voor het geselecteerde uur
2. Voer **Max GridSetpoint** in (negatieve waarde)
3. *(Optioneel)* Voer **MinSOC** in
4. Vink **Alleen als Prijs > MinVerkoopPrijs** aan
5. Voer de limiet in onder **MinVerkoopPrijs**

## Ontladen / laden van de batterij blokkeren

Om het ontladen (of laden) van de batterij onder de actuele SOC te blokkeren:

1. Vink **Inschakelen** aan voor het geselecteerde uur
2. {{< badge "victron-only" >}} Voer **Max GridSetpoint** in
3. Vink **Batterij ontladen blokkeren** (of **Batterij laden blokkeren**) aan

> [!NOTE]
> {{< badge "victron-only" >}} Het programma stelt MinSOC in ESS in op de huidige SOC-waarde, wat het ontladen blokkeert maar het laden toestaat. Na dit uur keert MinSOC terug naar de standaardwaarde.

> [!WARNING]
> {{< badge "victron-only" >}} Als je „Batterij ontladen blokkeren" instelt met GridSetpoint = een grote negatieve waarde (bijv. min het totale PV-vermogen), gaat alle energie van PV naar het net en wordt de batterij niet geladen. Dit kan worden gebruikt om **het laden van de batterij uit te stellen**.

## Dynamisch ontladen (Dynamic Discharge — DD)

{{< glossary "Dynamic Discharge" >}} zoekt automatisch uren met de hoogste verkoopprijs en stelt in die uren het ontladen in.

> [!WARNING]
> Gebruik deze functie niet met de **prijsgebaseerde optimizer**!

Om DD te configureren:

1. Voeg minstens één ontlaadperiode toe
2. Voer in **vanaf welk uur** en **hoeveel uren** het programma moet zoeken
   - 24 uur → het beginuur is niet relevant, het programma controleert 24 u vanaf het huidige uur
   - Minder dan 24 uur → het programma controleert vanaf het opgegeven uur. Als de periode voorbij is — controleert het de volgende dag
3. Voer in **hoeveel uren** je wilt ontladen
4. Voer voor alle uren in de periode **Max GridSetpoint** in
5. Om te automatiseren: vink **Taak elk uur uitvoeren** en **DD en DDBD automatisch optimaliseren** aan

Om te testen — klik op **Dynamisch ontladen nu optimaliseren**.

Het programma markeert de uren met de hoogste verkoopprijs en blokkeert de overige. Uren zonder ingevoerde GridSetpoint en uren met ingeschakeld laden worden overgeslagen.

> [!NOTE]
> Als je twee DD-perioden definieert voor dezelfde tijd — vindt de eerste de uren met de hoogste prijzen, zoekt de tweede de volgende hoogste (met uitsluiting van de al gevonden uren).

## Dynamische MinSOC via de optimizer

Om de optimizer uit [Batterijprognose]({{< relref "/configuration/battery-forecast" >}}) dynamisch de MinSOC te laten wijzigen:

1. Vink **Inschakelen** aan (of gebruik DD/DDBD om in te schakelen)
2. Voer **Max GridSetpoint** in
3. Vink **MinSOC optimaliseren via Batterijprognose** aan
4. *(Optioneel)* Voer **MinimalSOC** in — de ondergrens voor ontlading door de optimizer
5. *(Optioneel)* Vink **Alleen als Prijs > MinPrijs** aan en voer **MinPrijs** in

**Voorbeeld:** Het programma ontlaadt de batterij om 21:00 (hoogste verkoopprijs) om tegen 16:00 ruimte te maken voor energie uit PV. De SOC daalt nooit onder MinSOC.

## Dynamisch ontladen blokkeren (DDBD)

**DDBD** (Dynamically Disable Battery Discharge) dwingt het sturen van PV-productie naar het net af totdat de prijs het laagst is — op dat moment is het beter om de batterij uit PV te laden dan te verkopen.

> [!WARNING]
> Gebruik deze functie niet met de **prijsgebaseerde optimizer**!

Om DDBD te configureren:

1. Voeg minstens één periode toe
2. Voer in **vanaf welk uur** en **hoeveel uren** het programma moet zoeken naar de minimale inkoopprijs
3. Voer in **hoeveel uren** je de batterij wilt laden
4. Voer voor alle uren in de periode **Max GridSetpoint** (grote negatieve waarde) in
5. Om te automatiseren: vink **Taak elk uur uitvoeren** en **DD en DDBD automatisch optimaliseren** aan

Om te testen — klik op **Batterij blokkeren nu optimaliseren**.

### DDBD uitschakelen als de batterij niet wordt opgeladen

Het programma kan controleren of de batterij na afloop van DDBD tot het vereiste niveau zal zijn geladen. Zo niet — schakelt het DDBD eenmalig uit.

Parameters:
- **Aantal uren van lading** — hoeveel uren de batterij zou moeten worden geladen
- **Alleen als SOC stijgt met ten minste X %** — vereiste SOC-stijging tijdens de laaduren

> [!NOTE]
> Als het veld „alleen als SOC stijgt..." leeg is, controleert de optimizer niet of de batterij het vereiste niveau bereikt.

## Automatische inschakeling van het ontladen (dag/nacht)

Het programma kan het ontladen automatisch alleen overdag of alleen 's nachts inschakelen, op basis van de tijden van zonsopgang en zonsondergang.

> [!NOTE]
> Vereist dat breedte- en lengtegraad zijn ingesteld in de [installatieparameters]({{< relref "/installation/installation-parameters" >}}).

## Ontlaadparameters

| Parameter | Omvormer | Beschrijving |
|----------|----------|------|
| Ontladen automatisch inschakelen | Allen | Schakel het ontladen (kolom „Inschakelen") alleen overdag of 's nachts in, uit in de overige uren |
| Standaard MinSOC na ontladen (%) | {{< badge "victron-only" >}} | MinSOC die na afloop van het ontladen in de omvormer wordt ingesteld |
| Standaard GridSetpoint na ontladen (W) | {{< badge "victron-only" >}} | GridSetpoint die na afloop van het ontladen in de omvormer wordt ingesteld |
| Rek het ontladen uit tot een vol uur | Allen | Stel GridSetpoint/MaxSellPower zo in dat het ontladen een heel uur duurt |
| Stuur altijd een vaste MinSOC | Allen | Stuur een vaste MinSOC-waarde in plaats van die uit het ontlaadplan. Idee: de ontlaadsnelheid wordt alleen via GridSetpoint gestuurd, minder risico op laden uit het net na het bereiken van TargetSOC |
| Speciale GridSetpoint-berekening wanneer SOC = TargetSOC | Allen | Bij het vasthouden van een constante SOC — stel een kleine GridSetpoint in plaats van de maximale in |
| GridSetpoint verhogen met het voorspelde verbruik | Allen | Voor systemen met het huis aan de netzijde van de omvormer |
| Peak-Shaving uitschakelen tijdens ontladen | {{< badge "deye-only" >}} | Op sommige firmwares blokkeert peak-shaving het ontladen — het programma kan het uitschakelen |
| MaxCharge=0 instellen tijdens ontladen | {{< badge "deye-only" >}} | Blokkeer laden (zelfs toevallig) tijdens een ontlaaduur |
| Als er niets te doen is | {{< badge "victron-only" >}} {{< badge "deye-only" >}} | Wanneer: geen PV, geen laden, geen ontladen, MinSOC < SOC < MaxSOC, geen EV-lading → koppel de omvormer los van het net (of Deye: zet op „NoBatt"). Idee: vermindering van stroomverbruik door de omvormer |

## Verkoopprijs ≤ 0

Speciale bewerkingen wanneer de verkoopprijs negatief of nul is:

### Victron

| Optie | Beschrijving |
|-------|------|
| Loskoppelen van het net | De omvormer schakelt over naar de modus „Inverter only" |
| „DC-coupled PV — feed in excess" uitschakelen | Schakelt de optie uit voor PV aangesloten aan de DC-zijde |
| GridSetpoint instellen indien Prijs ≤ 0 | Bijv. 0 — beperkt het sturen van stroom naar het net |
| Relay 1/2 inschakelen | PV uitschakelen via de Relay1/Relay2-uitgang van de Cerbo |
| Aannemen dat er geen PV is | Het programma gaat ervan uit dat er geen PV werkt in uren met prijs ≤ 0 |

### Solarman (Deye)

| Optie | Beschrijving |
|-------|------|
| Loskoppelen van het net | Wijzigt de minimaal toegestane spanning naar 270 V — Deye koppelt los van het net |
| SolarSell uitschakelen en MI export to Grid cutoff | Schakelt SolarSell en micro-omvormers uit tijdens uren met prijs < 0 |
| Aannemen dat er geen PV is | Zoals hierboven |

### DeyeCloud

| Optie | Beschrijving |
|-------|------|
| SolarSell uitschakelen | Schakelt SolarSell uit tijdens uren met prijs < 0 |
| Aannemen dat er geen PV is | Zoals hierboven |

### HomeAssistant / GbbConnect

| Optie | Beschrijving |
|-------|------|
| Aannemen dat er geen PV is | Het programma gaat ervan uit dat er geen PV werkt in uren met prijs ≤ 0 |
