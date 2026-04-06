---
title: "Tryby falownikow"
weight: 20
---

# Tryby falownikow

GbbOptimizer steruje falownikiem za pomoca czterech podstawowych trybow (operacji protokolu). Kazdy falownik implementuje je w inny sposob — szczegolowe mapowania znajdziesz w sekcji [Mapowania trybow]({{< relref "/referencje/mapowania-trybow" >}}).

## Wymagane dane z falownika

Falownik musi dostarczac nastepujace dane:

| Pole | Opis |
|------|------|
| `soc_perc` | {{< glossary "SOC" >}} baterii w procentach (lub `V` jesli sterowanie przez napiecie) |
| `loads_total_kWh` | Licznik zuzycia (kWh, narastajaco) |
| `fromgrid_total_kWh` | Licznik energii pobranej z sieci (kWh) |
| `togrid_total_kWh` | Licznik energii wyslanej do sieci (kWh) |
| `pv_total_kWh` | Licznik produkcji PV (kWh) |

Opcjonalnie:

| Pole | Opis |
|------|------|
| `ev_charge_total_kWh` | Licznik ladowania EV |
| `hp_total_kWh` | Licznik pompy ciepla |
| `other1_total_kWh` ... `other2_total_kWh` | Inne liczniki |

## Tryby operacji

### Normal

Powrot do normalnej pracy:
- PV zasila dom, potem baterie, potem siec
- Dom zasilany z PV, potem z baterii, potem z sieci

### Charge

Rozpocznij ladowanie baterii z PV i/lub sieci do zadanego poziomu {{< glossary "SOC" >}} z zadana predkoscia (W).

Po osiagnieciu docelowego SOC:
- Nie laduj baterii z sieci
- Nie rozladowuj baterii ponizej docelowego SOC
- Mozna ladowac baterie z PV

### Discharge

Rozpocznij rozladowanie baterii (i PV) do sieci do zadanego poziomu {{< glossary "SOC" >}} z zadana predkoscia (W).

### DisableCharge

Wylacz ladowanie baterii. Energia z PV przesylana jest do domu i sieci.

## Mapowania dla poszczegolnych falownikow

- [Deye (Solarman / DeyeCloud / SolarAssistant)]({{< relref "/referencje/mapowania-trybow/deye" >}})
- [GoodWe]({{< relref "/referencje/mapowania-trybow/goodwe" >}})
- [Hinen]({{< relref "/referencje/mapowania-trybow/hinen" >}})
- [Sofar]({{< relref "/referencje/mapowania-trybow/sofar" >}})
- [Victron (tryb pasywny)]({{< relref "/referencje/mapowania-trybow/victron-pasywny" >}})
