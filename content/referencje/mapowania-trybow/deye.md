---
title: "Deye"
weight: 10
---

# Mapowanie trybow — Deye

{{< badge "deye-only" >}}

Jak tryby GbbOptimizer przekladaja sie na ustawienia falownika Deye w zaleznosci od metody polaczenia.

## Solarman / DeyeCloud (nowa metoda polaczenia)

{{< badge "recommended" >}}

| Operacja | Work Mode | GridCharge (TimeOfUse) | Time (TimeOfUse) | SOC (TimeOfUse) | Power (TimeOfUse) | Charge A | MaxSellPower |
|----------|-----------|----------------------|-----------------|-----------------|-------------------|----------|--------------|
| **Normal** | — | nie | tak | 5%\* | Max Battery Discharge, jesli brak: Max Inverter Discharge | bez zmian | — |
| **Charge** | — | tak | tak | SOC% | ChargeLimitW, jesli brak: Max Battery Charge, jesli brak: Max Inverter Charge | ChargeLimitW, jesli brak: Max Battery Charge, jesli brak: Max Inverter Charge | — |
| **Discharge** | SellingFirst (po zakonczeniu: powrot do poprzedniej wartosci) | nie | tak | SOC% | Max Battery Discharge, jesli brak: Max Inverter Discharge | bez zmian; KeepSOC: 0W | Max GridSetpoint / Discharge (W); jesli rozladowanie musi byc wolniejsze, program oblicza wartosc; po zakonczeniu: powrot do poprzedniej wartosci |
| **DisableCharge** | — | nie | tak | 5%\* | Max GridSetpoint / Discharge (W) | zmiana na 0 (po zakonczeniu: powrot do poprzedniej wartosci) | — |

\* 5% mozna zmienic parametrem **"Default MinSOC after discharge"** w ustawieniach planu rozladowania.

### Cena < 0

- (opcjonalnie) Wylacz **SolarSell** + wlacz **MI export to Grid cutoff**
- (opcjonalnie) Zmien LV1 na 270V — powoduje odlaczenie od sieci (off-grid). Po zakonczeniu okresu ceny < 0 program przywraca poprzednia wartosc LV1.

### Generator

- **On:** Ustaw GEN w TimeOfUse (tylko podczas operacji Charge) + ustaw GenSOC na aktualny SOC + 1
- **PurchasePrice > LimitPrice:** Zmien LV1 na 270V (odlaczenie od sieci w celu uruchomienia generatora) lub ustaw NoBatt

### Dodatkowe opcje

- **"Switch off peak-shaving during discharge battery to grid"** — wylacz Peak-Shaving
- **"Change Mode to 'Zero Export To CT' during charge battery from grid"** — zmien WorkMode
- **"Input Limit (A)"** — Grid Peak Shaving (W)

---

## DeyeCloud (stare API)

{{< badge "deprecated" >}}

| Operacja | Work Mode | GridCharge (TimeOfUse) | Time (TimeOfUse) | SOC (TimeOfUse) | Power (TimeOfUse) | Charge A | MaxSellPower |
|----------|-----------|----------------------|-----------------|-----------------|-------------------|----------|--------------|
| **Normal** | — | nie | tak | 5%\* | Max Battery Discharge | bez zmian | — |
| **Charge** | — | tak | tak | SOC% | ChargeLimitW, jesli brak: Max Battery Discharge | bez zmian | — |
| **Discharge** | SellingFirst (po zakonczeniu: **zmiana na ZeroExportToCT**) | nie | tak | SOC% | Sell Power, jesli brak: Max Battery Discharge | bez zmian | Max GridSetpoint / Discharge (W); po zakonczeniu: MaxSellPower after Discharge |
| **DisableCharge** | — | nie | tak | 5%\* | Max GridSetpoint / Discharge (W) | zmiana na 0 (po zakonczeniu: MaxChargePower after Disable battery charge) | — |

\* 5% mozna zmienic parametrem **"Default MinSOC after discharge"**.

### Cena < 0 (stare API)

- (opcjonalnie) Wylacz **SolarSell**

### Generator (stare API)

- **On:** Ustaw GEN w TimeOfUse (tylko podczas operacji Charge)

### Dodatkowe opcje (stare API)

- **"Change Mode to 'Zero Export To CT' during charge battery from grid"** — zmien WorkMode

> [!WARNING]
> Stare API DeyeCloud jest przestarzale i ma ograniczona funkcjonalnosc (brak obslugi Peak-Shaving, generatora z LV1, Input Limit). Zalecane jest przejscie na nowa metode polaczenia.

---

## SolarAssistant

| Operacja | Work Mode | GridCharge (TimeOfUse) | Time (TimeOfUse) | SOC (TimeOfUse) | Charge A |
|----------|-----------|----------------------|-----------------|-----------------|----------|
| **Normal** | — | nie | tak | 5%\* | bez zmian |
| **Charge** | — | tak | tak | SOC% | bez zmian |
| **Discharge** | SellingFirst (po zakonczeniu: powrot do poprzedniej wartosci) | nie | tak | SOC% | bez zmian |
| **DisableCharge** | — | nie | tak | 5%\* | zmiana na 0 (po zakonczeniu: powrot do poprzedniej wartosci) |

\* 5% mozna zmienic parametrem **"Default MinSOC after discharge"**.

> [!NOTE]
> {{< glossary "SolarAssistant" >}} aktualnie nie pozwala zdalnie zmieniac Power w TimeOfUse ani godziny poczatkowej. Dlatego GbbOptimizer ustawia wszystkie wiersze na te same wartosci. Funkcje Price < 0 i Generator nie sa dostepne przez SolarAssistant.

Wiecej informacji: [Integracja SolarAssistant]({{< relref "/integracje/home-assistant/solar-assistant" >}})
