---
title: "Winsten"
weight: 80
translationKey: "zyski"
---

# Winsten

Deze module verzamelt gegevens uit de installatie en berekent de opbrengsten van de PV. Importeer handmatig ten minste één keer per dag, of vink **Gegevens automatisch uit installatie importeren** aan.

Gegevens worden weergegeven per uur, dag of maand:
- Uurgegevens — **2 maanden** bewaard
- Daggegevens — **2 jaar** bewaard
- Maandgegevens — **voor altijd** bewaard

## Kolommen — Winst

| Kolom | Beschrijving |
|---------|------|
| Dag / Uur | Dag en uur |
| Winstwaarde | **= Verbruikswaarde - Omvormerwaarde - (Inkoopwaarde - Waardeverandering batterij) + Verkoopwaarde** |
| Winst / Verbruik | KPI: Winstwaarde / Verbruik kWh |
| Profit / Solar | KPI: Winstwaarde / PV kWh |
| Energiekosten | Inkoopwaarde - Verkoopwaarde |
| Uit het net (kWh) | Hoeveel uit het net is genomen |
| Uit het net gesaldeerd (kWh) | Genomen na saldering per uur (voor Polen) |
| Inkoopprijs | Inkoopprijs van energie |
| Inkoopwaarde | Uit het net [gesaldeerd] × Inkoopprijs + Maandelijkse kosten |
| Inkoop / Productie | KPI: Inkoopwaarde / Verbruikswaarde |
| (Inkoop - Verkoop) / Productie | KPI: welk percentage van je energierekening je betaalt |
| Naar het net (kWh) | Hoeveel naar het net is gestuurd |
| Naar het net gesaldeerd (kWh) | Gestuurd na saldering per uur (voor Polen) |
| Verkoopprijs | Verkoopprijs van energie |
| Verkoopwaarde | Naar het net [gesaldeerd] × Verkoopprijs − Waarde van de naar het net gestuurde energie |
| Verbruik (kWh) | Stroomverbruik door het huis |
| Verbruiksprijs | Prijs van de door het huis verbruikte energie (inclusief de omvormer) |
| Verbruikswaarde | Verbruik kWh × Verbruiksprijs |
| Omvormerverbruik (kWh) | Stroomverbruik van de omvormer |
| Omvormerwaarde | Omvormerverbruik kWh × Verbruiksprijs |
| Zelfconsumptie | KPI: 1 - (Naar het net kWh / PV kWh) — hoeveel PV-energie niet naar het net gaat |
| Zelfvoorziening | KPI: PV / Verbruik — hoeveel % van de energie uit PV het verbruik dekt |
| {{< glossary "RTE" >}} | KPI: Naar het net kWh / (Uit het net kWh + PV kWh - Verbruik kWh) |
| PV (kWh) | PV-productie |
| Naar de batterij (kWh) | Energie verstuurd naar de batterij (voor conversie naar DC) |
| min/max/gem SOC (%) | Minimale, maximale en gemiddelde SOC van de batterij |

## Kolommen — Waarde van de energie in de batterij

| Kolom | Beschrijving |
|---------|------|
| Begin SOC (%) | Begin-SOC (berekend uit MinSOC en MaxSOC, als de installatie dit niet aanlevert) |
| Eind SOC (%) | Eind-SOC |
| Batterijverandering (kWh) | >0 laden, <0 ontladen — berekend uit EindSOC - BeginSOC |
| Laden uit het net (kWh) | Energie gebruikt voor laden uit het net (AC-zijde) |
| Laden uit PV (kWh) | Energie gebruikt voor laden uit PV (AC-zijde) |
| Verliezen bij laden (kWh) | Verschil tussen DC en AC tijdens laden |
| Laadrendement (%) | 1 - Verliezen / (Laden uit het net + uit PV) |
| Ontladen naar het net (kWh) | Energie uit de batterij naar het net (AC) |
| Ontladen naar verbruik (kWh) | Energie uit de batterij naar het huis (AC) |
| Verliezen bij ontladen (kWh) | Verschil DC/AC tijdens ontladen |
| Ontlaadrendement (%) | 1 - Verliezen / (Ontladen naar het net + naar verbruik) |
| Begin / Eind kWh in de batterij | Energie in de batterij boven MinSOC |
| Begin / Eind Waarde (PLN) | Waarde van de energie in de batterij |
| Waardeverandering batterij (PLN) | Ontladen: kWh × Gemiddelde prijs (vorig uur). Laden: kWh × Inkoopprijs |
| Gemiddelde eindprijs (PLN) | Eindwaarde / Eind kWh in de batterij |
| MinSOC (%) | Onthouden waarde „Minimale SOC batterij %" uit de installatieparameters |

## Kolommen — Extra verbruik

| Kolom | Beschrijving |
|---------|------|
| Prijs Extra verbruik (PLN) | Gemiddelde prijs per kWh: gemiddelde van 0 (PV), de gemiddelde batterijprijs en de inkoopprijs (in verhouding van gebruik) |
| Elektrische auto (kWh / PLN) | Energie en waarde van het EV-laden |
| Warmtepomp (kWh / PLN) | Energie en waarde van de warmtepomp |
| Andere1 (kWh / PLN) | Energie en waarde van „Andere1" |
| Andere2 (kWh / PLN) | Energie en waarde van „Andere2" |
