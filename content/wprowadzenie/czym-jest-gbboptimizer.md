---
title: "Czym jest GbbOptimizer"
weight: 10
---

# Czym jest GbbOptimizer

GbbOptimizer (dawniej GbbVictronWeb) to program optymalizujacy wykorzystanie energii w domowej instalacji fotowoltaicznej z magazynem energii (baterią). Analizuje prognozy produkcji PV, profil zużycia energii oraz ceny zakupu i sprzedaży, aby automatycznie sterować falownikiem — decydując kiedy ładować baterię, kiedy rozładowywać i kiedy kupować lub sprzedawać energię z/do sieci.

## Jak to działa

Program działa w chmurze i komunikuje się z falownikiem przez internet. Co godzinę wykonuje obliczenia i wysyła komendy do falownika.

```
┌─────────────────────────────────────────────────────────────────┐
│                       GbbOptimizer (chmura)                     │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   │
│  │ Prognoza PV  │  │  Profil      │  │  Ceny zakupu         │   │
│  │ (Solcast,    │  │  zużycia     │  │  i sprzedaży         │   │
│  │ forecast.    │  │  domu        │  │  (taryfy, giełda)    │   │
│  │  solar)      │  │              │  │                      │   │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬───────────┘   │
│         │                 │                     │               │
│         └─────────────────┼─────────────────────┘               │
│                           │                                     │
│                    ┌──────▼───────┐                             │
│                    │ Optymalizator│                             │
│                    │  (Prognoza   │                             │
│                    │   Baterii)   │                             │
│                    └──────┬───────┘                             │
│                           │                                     │
│              Harmonogram ładowania / rozładowania               │
│              + tryb pracy falownika                             │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                    ┌───────▼────────┐
                    │   Połączenie   │
                    │  (VRM, MQTT,   │
                    │  Solarman,     │
                    │  GbbConnect2)  │
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │   Falownik     │
                    │  hybrydowy     │
                    │  + bateria     │
                    └────────────────┘
```

Każda instalacja ma unikalny {{< glossary "PlantId" >}} i {{< glossary "PlantToken" >}}, które służą do identyfikacji i autoryzacji komunikacji.

## Cztery tryby pracy

Optymalizator przełącza falownik między czterema trybami w zależności od aktualnej sytuacji cenowej i stanu baterii:

| Tryb | Opis |
|------|------|
| **Normal** | Standardowa praca falownika — bateria ładuje się z PV, dom zasilany z PV i baterii. Nadwyżki PV mogą być eksportowane do sieci |
| **Charge** | Ładowanie baterii z sieci. Używane gdy cena zakupu jest niska (np. taryfa nocna, ujemne ceny na giełdzie) |
| **Discharge** | Wymuszone rozładowanie baterii do sieci. Używane gdy cena sprzedaży jest wysoka i opłaca się sprzedać energię |
| **DisableCharge** | Blokada ładowania z PV. Używane aby zostawić miejsce w baterii na późniejsze tanie ładowanie z sieci |

Szczegóły konfiguracji ładowania znajdziesz w [module Ładowanie]({{< relref "/konfiguracja/ladowanie" >}}), a rozładowania w [module Rozładowanie]({{< relref "/konfiguracja/rozladowanie" >}}).

## Optymalizator oparty o ceny

Domyślnie wybierany jest "Optymalizator oparty o ceny". Analizuje on ceny zakupu i sprzedaży energii na najbliższe godziny i planuje:

- **Kiedy ładować** — szuka godzin z najniższą ceną zakupu
- **Kiedy rozładowywać** — szuka godzin z najwyższą ceną sprzedaży
- **Ile ładować** — uwzględnia prognozę PV (żeby nie ładować z sieci tego, co i tak wyprodukuje PV) oraz {{< glossary "MaxSOC" >}} baterii
- **Ile rozładowywać** — uwzględnia prognozę zużycia domu i {{< glossary "MinSOC" >}} baterii

Cały plan wizualizowany jest w module [Prognoza baterii]({{< relref "/konfiguracja/prognoza-baterii" >}}).

## Kluczowe parametry

- {{< glossary "SOC" >}} — aktualny poziom naładowania baterii
- {{< glossary "MinSOC" >}} — minimalny poziom baterii (zabezpieczenie)
- {{< glossary "MaxSOC" >}} — maksymalny poziom ładowania (zalecane 90%)
- {{< glossary "GridSetpoint" >}} — cel mocy wymiany z siecią
- {{< glossary "RTE" >}} — sprawność cyklu ładowania/rozładowania
- {{< glossary "Correction Factor" >}} — współczynnik korygujący prognozę PV (kalibruje się automatycznie przez ~tydzień)

## Wspierane falowniki

GbbOptimizer obsługuje następujące falowniki hybrydowe:

| Falownik | Metody połączenia |
|----------|-------------------|
| **Victron** | VRM Portal (natywnie), Home Assistant |
| **Deye** | DeyeCloud, Solarman, Home Assistant, {{< glossary "GbbConnect2" >}}, {{< glossary "DongleDirect" >}} |
| **GoodWe** | Solarman, Home Assistant, {{< glossary "GbbConnect2" >}} |
| **Afore** | Solarman, {{< glossary "GbbConnect2" >}} |
| **Hinen** | Solarman, {{< glossary "GbbConnect2" >}} |
| **SofarSolar** | {{< glossary "DongleDirect" >}}, {{< glossary "GbbConnect2" >}} |

> [!NOTE]
> Victron to najdłużej wspierany falownik z najpełniejszą integracją. Pozostałe falowniki mają pełne wsparcie trybów ładowania/rozładowania, ale niektóre zaawansowane opcje mogą się różnić.

Szczegóły konfiguracji poszczególnych falowników znajdziesz w sekcji [Instalacja]({{< relref "/instalacja" >}}).

## Co dalej?

- [Szybki start]({{< relref "/wprowadzenie/szybki-start" >}}) — krok po kroku jak uruchomić system
- [Najlepsze praktyki]({{< relref "/wprowadzenie/najlepsze-praktyki" >}}) — porady od doświadczonych użytkowników
- [Ceny]({{< relref "/konfiguracja/ceny" >}}) — konfiguracja cen zakupu i sprzedaży
- [Prognoza baterii]({{< relref "/konfiguracja/prognoza-baterii" >}}) — centralny moduł optymalizatora
