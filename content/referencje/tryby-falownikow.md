---
title: "Tryby falowników"
weight: 20
---

# Tryby falowników

GbbOptimizer steruje falownikiem za pomocą czterech podstawowych trybów (operacji protokołu). Każdy falownik implementuje je w inny sposób — szczegółowe mapowania znajdziesz w sekcji [Mapowania trybów]({{< relref "/referencje/mapowania-trybow" >}}).

## Wymagane dane z falownika

Falownik musi dostarczać następujące dane:

| Pole | Opis |
|------|------|
| `soc_perc` | {{< glossary "SOC" >}} baterii w procentach (lub `V` jeśli sterowanie przez napięcie) |
| `loads_total_kWh` | Licznik zużycia (kWh, narastająco) |
| `fromgrid_total_kWh` | Licznik energii pobranej z sieci (kWh) |
| `togrid_total_kWh` | Licznik energii wysłanej do sieci (kWh) |
| `pv_total_kWh` | Licznik produkcji PV (kWh) |

Opcjonalnie:

| Pole | Opis |
|------|------|
| `ev_charge_total_kWh` | Licznik ładowania EV |
| `hp_total_kWh` | Licznik pompy ciepła |
| `other1_total_kWh` ... `other2_total_kWh` | Inne liczniki |

## Tryby operacji

### Normal

Powrót do normalnej pracy:
- PV zasila dom, potem baterie, potem sieć
- Dom zasilany z PV, potem z baterii, potem z sieci

### Charge

Rozpocznij ładowanie baterii z PV i/lub sieci do zadanego poziomu {{< glossary "SOC" >}} z zadaną prędkością (W).

Po osiągnięciu docelowego SOC:
- Nie ładuj baterii z sieci
- Nie rozładowuj baterii poniżej docelowego SOC
- Można ładować baterie z PV

### Discharge

Rozpocznij rozładowanie baterii (i PV) do sieci do zadanego poziomu {{< glossary "SOC" >}} z zadaną prędkością (W).

### DisableCharge

Wyłącz ładowanie baterii. Energia z PV przesyłana jest do domu i sieci.

## Mapowania dla poszczególnych falowników

- [Deye (Solarman / DeyeCloud / SolarAssistant)]({{< relref "/referencje/mapowania-trybow/deye" >}})
- [GoodWe]({{< relref "/referencje/mapowania-trybow/goodwe" >}})
- [Hinen]({{< relref "/referencje/mapowania-trybow/hinen" >}})
- [Sofar]({{< relref "/referencje/mapowania-trybow/sofar" >}})
- [Victron (tryb pasywny)]({{< relref "/referencje/mapowania-trybow/victron-pasywny" >}})
