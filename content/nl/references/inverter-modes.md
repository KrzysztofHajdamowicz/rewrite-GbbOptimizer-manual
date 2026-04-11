---
title: "Omvormermodi"
weight: 20
translationKey: "tryby-falownikow"
---

# Omvormermodi

GbbOptimizer stuurt de omvormer aan met vier basismodi (protocoloperaties). Elke omvormer implementeert deze op zijn eigen manier — gedetailleerde mappings vind je in de sectie [Modusmappings]({{< relref "/references/mode-mappings" >}}).

## Vereiste gegevens uit de omvormer

De omvormer moet de volgende gegevens leveren:

| Veld | Beschrijving |
|------|------|
| `soc_perc` | {{< glossary "SOC" >}} van de batterij in procenten (of `V` als aansturing via spanning) |
| `loads_total_kWh` | Verbruiksteller (kWh, cumulatief) |
| `fromgrid_total_kWh` | Teller van uit het net genomen energie (kWh) |
| `togrid_total_kWh` | Teller van naar het net gestuurde energie (kWh) |
| `pv_total_kWh` | PV-productieteller (kWh) |

Optioneel:

| Veld | Beschrijving |
|------|------|
| `ev_charge_total_kWh` | EV-laadteller |
| `hp_total_kWh` | Warmtepompteller |
| `other1_total_kWh` ... `other2_total_kWh` | Andere tellers |

## Operatiemodi

### Normal

Terug naar normale werking:
- PV voedt het huis, daarna de batterij, daarna het net
- Het huis wordt gevoed uit PV, daarna uit de batterij, daarna uit het net

### Charge

Start het laden van de batterij vanuit PV en/of het net tot de ingestelde {{< glossary "SOC" >}}-waarde met de ingestelde snelheid (W).

Nadat de doel-SOC is bereikt:
- De batterij wordt niet uit het net geladen
- De batterij wordt niet onder de doel-SOC ontladen
- De batterij kan uit PV worden geladen

### Discharge

Start het ontladen van de batterij (en PV) naar het net tot de ingestelde {{< glossary "SOC" >}}-waarde met de ingestelde snelheid (W).

### DisableCharge

Schakel het laden van de batterij uit. Energie uit PV wordt naar huis en net gestuurd.

## Mappings voor de afzonderlijke omvormers

- [Deye (Solarman / DeyeCloud / SolarAssistant)]({{< relref "/references/mode-mappings/deye" >}})
- [GoodWe]({{< relref "/references/mode-mappings/goodwe" >}})
- [Hinen]({{< relref "/references/mode-mappings/hinen" >}})
- [Sofar]({{< relref "/references/mode-mappings/sofar" >}})
- [Victron (Passive Mode)]({{< relref "/references/mode-mappings/victron-passive" >}})
