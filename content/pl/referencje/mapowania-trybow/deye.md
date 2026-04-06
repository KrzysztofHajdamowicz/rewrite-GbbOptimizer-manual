---
title: "Deye"
weight: 10
translationKey: "deye"
---

# Mapowanie trybów — Deye

{{< badge "deye-only" >}}

Jak tryby GbbOptimizer przekładają się na ustawienia falownika Deye w zależności od metody połączenia.

## Solarman / DeyeCloud (nowa metoda połączenia)

{{< badge "recommended" >}}

| Operacja | Work Mode | GridCharge (TimeOfUse) | Time (TimeOfUse) | SOC (TimeOfUse) | Power (TimeOfUse) | Charge A | MaxSellPower |
|----------|-----------|----------------------|-----------------|-----------------|-------------------|----------|--------------|
| **Normal** | — | nie | tak | 5%\* | Max Battery Discharge, jeśli brak: Max Inverter Discharge | bez zmian | — |
| **Charge** | — | tak | tak | SOC% | ChargeLimitW, jeśli brak: Max Battery Charge, jeśli brak: Max Inverter Charge | ChargeLimitW, jeśli brak: Max Battery Charge, jeśli brak: Max Inverter Charge | — |
| **Discharge** | SellingFirst (po zakończeniu: powrót do poprzedniej wartości) | nie | tak | SOC% | Max Battery Discharge, jeśli brak: Max Inverter Discharge | bez zmian; KeepSOC: 0W | Max GridSetpoint / Discharge (W); jeśli rozładowanie musi być wolniejsze, program oblicza wartość; po zakończeniu: powrót do poprzedniej wartości |
| **DisableCharge** | — | nie | tak | 5%\* | Max GridSetpoint / Discharge (W) | zmiana na 0 (po zakończeniu: powrót do poprzedniej wartości) | — |

\* 5% można zmienić parametrem **"Default MinSOC after discharge"** w ustawieniach planu rozładowania.

### Cena < 0

- (opcjonalnie) Wyłącz **SolarSell** + włącz **MI export to Grid cutoff**
- (opcjonalnie) Zmień LV1 na 270V — powoduje odłączenie od sieci (off-grid). Po zakończeniu okresu ceny < 0 program przywraca poprzednią wartość LV1.

### Generator

- **On:** Ustaw GEN w TimeOfUse (tylko podczas operacji Charge) + ustaw GenSOC na aktualny SOC + 1
- **PurchasePrice > LimitPrice:** Zmień LV1 na 270V (odłączenie od sieci w celu uruchomienia generatora) lub ustaw NoBatt

### Dodatkowe opcje

- **"Switch off peak-shaving during discharge battery to grid"** — wyłącz Peak-Shaving
- **"Change Mode to 'Zero Export To CT' during charge battery from grid"** — zmień WorkMode
- **"Input Limit (A)"** — Grid Peak Shaving (W)

---

## DeyeCloud (stare API)

{{< badge "deprecated" >}}

| Operacja | Work Mode | GridCharge (TimeOfUse) | Time (TimeOfUse) | SOC (TimeOfUse) | Power (TimeOfUse) | Charge A | MaxSellPower |
|----------|-----------|----------------------|-----------------|-----------------|-------------------|----------|--------------|
| **Normal** | — | nie | tak | 5%\* | Max Battery Discharge | bez zmian | — |
| **Charge** | — | tak | tak | SOC% | ChargeLimitW, jeśli brak: Max Battery Discharge | bez zmian | — |
| **Discharge** | SellingFirst (po zakończeniu: **zmiana na ZeroExportToCT**) | nie | tak | SOC% | Sell Power, jeśli brak: Max Battery Discharge | bez zmian | Max GridSetpoint / Discharge (W); po zakończeniu: MaxSellPower after Discharge |
| **DisableCharge** | — | nie | tak | 5%\* | Max GridSetpoint / Discharge (W) | zmiana na 0 (po zakończeniu: MaxChargePower after Disable battery charge) | — |

\* 5% można zmienić parametrem **"Default MinSOC after discharge"**.

### Cena < 0 (stare API)

- (opcjonalnie) Wyłącz **SolarSell**

### Generator (stare API)

- **On:** Ustaw GEN w TimeOfUse (tylko podczas operacji Charge)

### Dodatkowe opcje (stare API)

- **"Change Mode to 'Zero Export To CT' during charge battery from grid"** — zmień WorkMode

> [!WARNING]
> Stare API DeyeCloud jest przestarzałe i ma ograniczoną funkcjonalność (brak obsługi Peak-Shaving, generatora z LV1, Input Limit). Zalecane jest przejście na nową metodę połączenia.

---

## SolarAssistant

| Operacja | Work Mode | GridCharge (TimeOfUse) | Time (TimeOfUse) | SOC (TimeOfUse) | Charge A |
|----------|-----------|----------------------|-----------------|-----------------|----------|
| **Normal** | — | nie | tak | 5%\* | bez zmian |
| **Charge** | — | tak | tak | SOC% | bez zmian |
| **Discharge** | SellingFirst (po zakończeniu: powrót do poprzedniej wartości) | nie | tak | SOC% | bez zmian |
| **DisableCharge** | — | nie | tak | 5%\* | zmiana na 0 (po zakończeniu: powrót do poprzedniej wartości) |

\* 5% można zmienić parametrem **"Default MinSOC after discharge"**.

> [!NOTE]
> {{< glossary "SolarAssistant" >}} aktualnie nie pozwala zdalnie zmieniać Power w TimeOfUse ani godziny początkowej. Dlatego GbbOptimizer ustawia wszystkie wiersze na te same wartości. Funkcje Price < 0 i Generator nie są dostępne przez SolarAssistant.

Więcej informacji: [Integracja SolarAssistant]({{< relref "/integracje/home-assistant/solar-assistant" >}})
