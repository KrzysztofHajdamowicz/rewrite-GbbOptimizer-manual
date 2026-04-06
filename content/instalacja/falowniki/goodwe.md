---
title: "GoodWe"
weight: 30
---

# GoodWe

Konfiguracja falownika GoodWe z GbbOptimizer wymaga udostępnienia dostępu przez portal SEMS oraz konfiguracji po stronie GbbOptimizer.

## Konfiguracja krok po kroku

1. Zaloguj się do portalu **SEMS** (GoodWe)
2. W menu **Zarządzanie**, w danych swojej elektrowni, dodaj email `gbbsoft@gbbsoft.pl` jako **Gość**
3. W GbbOptimizer dodaj instalację z GoodWe, ale **nie wybieraj SerialNo** — lista powinna być pusta (z wyjątkiem napisu „Wybierz SerialNo”)
4. Na końcu strony zaznacz **Udostępnij instalację pomocy technicznej**
5. Skontaktuj się z pomocą techniczną (np. przez Discord: `gbbsoft`) i podaj **SerialNo** swojego falownika
6. Pomoc techniczna wybierze Twój SerialNo

> [!NOTE]
> Konfiguracja GoodWe wymaga jednorazowej interwencji pomocy technicznej w celu powiązania numeru seryjnego falownika z Twoją instalacją.

## Dostęp przez GoodWe OpenAPI

GbbOptimizer łączy się z falownikiem GoodWe przez **GoodWe OpenAPI** (SEMS Portal). Dostęp jest konfigurowany po stronie serwera GbbOptimizer — użytkownik musi jedynie udostępnić swoje konto SEMS.

## Lista kontrolna

- Upewnij się, że email `gbbsoft@gbbsoft.pl` ma dostęp jako **Gość** do Twojej elektrowni w SEMS
- Sprawdź, czy **Udostępnij instalację pomocy technicznej** jest zaznaczone w GbbOptimizer

## Rejestry zmieniane przez GbbOptimizer

GbbOptimizer modyfikuje następujące rejestry falownika GoodWe:

| Rejestr | Operacja | Po zakończeniu |
|---------|----------|----------------|
| AC charging maximum SOC | Ładowanie: docelowy {{< glossary "MaxSOC" >}} | — |
| ACCharging start/end time (1-4) | Ładowanie: tablica następnych 4 okresów ładowania | — |
| Forced charging start/end time (1-4) | Ładowanie: tablica następnych 4 okresów ładowania | — |
| ACCharging power percentage | Ładowanie: Input Limit (% z MaxBuyPower lub MaxBatteryChargeDC) | Przywrócenie oryginalnej wartości |
| Forced charging power percentage | Ładowanie: Charge Limit (% z MaxBatteryChargeDC) | Przywrócenie oryginalnej wartości |
| Minimum SOC for forced discharge | Rozładowanie: docelowy {{< glossary "MinSOC" >}} | — |
| Forced discharge start time (1-4) | Rozładowanie: tablica następnych 4 okresów rozładowania | — |
| Power grid power limit percentage | Rozładowanie: {{< glossary "GridSetpoint" >}} (% z MaxSellPower lub MaxBatteryDischargeDC) | — |
| Maximum charging current | Blokada ładowania: ustawia `0` | Przywrócenie oryginalnej wartości |

## Wymagane ustawienia falownika

- **Timing DChg ON/OFF** = `Enable`
- **PDisChgMax** (Forced discharge power percentage) = `100%`
