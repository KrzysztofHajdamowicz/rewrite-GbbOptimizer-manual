---
title: "Solarman"
weight: 10
---

# Solarman

Solarman to chmurowa metoda połączenia falownika z GbbOptimizer. Dane przechodzą przez serwery Solarman — nie wymaga instalacji dodatkowego oprogramowania.

## Konfiguracja krok po kroku

1. Dodaj instalację: **Dodaj nową instalację z falownikiem połączonym do Solarman**
2. Wypełnij pola do grupy „Solarman" (szczegóły w [Parametry instalacji]({{< relref "/instalacja/parametry-instalacji" >}}))
3. Zaloguj się do serwerów Solarman: wprowadź **email** i **hasło** (te same co do aplikacji Solarman) i naciśnij **Połącz**
4. Wybierz z listy **Wybierz SerialNo falownika** swój falownik
5. Wybierz **Rodzaj falownika**

   > [!WARNING]
   > Nie wolno pomylić rodzaju falownika! Błędny wybór i wysłanie danych wymaga przywrócenia ustawień fabrycznych w falowniku.

6. Naciśnij **Testuj połączenie z falownikiem** — program pobierze aktualny {{< glossary "SOC" >}} z falownika. Sprawdź, czy wartość jest poprawna. W module Log znajdziesz więcej informacji z falownika
7. Kontynuuj wypełnianie pól o bateriach i naciśnij **Kontynuuj w Szybkiej Konfiguracji**

## Sterowanie poprzez napięcie (V) zamiast SOC

Jeśli wolisz sterować baterią przez napięcie zamiast {{< glossary "SOC" >}}:

1. Zaznacz **Steruj poprzez V a nie przez SOC**
2. Naciśnij **Edytuj mapowanie SOC do V**
3. Wprowadź co najmniej **dwa znane pary** SOC i V, aby program utworzył mapowanie. Im więcej par — tym dokładniejsze mapowanie

> [!NOTE]
> Mapowanie jest **proporcjonalne (liniowe)** — program interpoluje na podstawie dwóch najbliższych punktów.

## GbbShunt

GbbShunt to moduł zaprojektowany do sterowania bateriami kwasowo-ołowiowymi. Wykonuje dwie funkcje (normalnie realizowane przez falownik):

- **Oblicza {{< glossary "SOC" >}}** na podstawie energii wysłanej i pobranej z baterii
- **Kończy ładowanie/rozładowanie** po osiągnięciu wskazanego poziomu SOC

### Parametry GbbShunt

Szczegółowy opis parametrów GbbShunt znajdziesz w [Parametry instalacji]({{< relref "/instalacja/parametry-instalacji" >}}).

### Jak GbbShunt oblicza SOC?

1. Na podstawie różnicy między początkową a aktualną energią wysłaną/pobraną z baterii oblicza przyrost energii
2. Po podzieleniu aktualnej energii przez całkowitą pojemność baterii otrzymuje **Wyliczony SOC**
3. Gdy Wyliczony SOC < 0 lub SOC > 100, albo napięcie baterii osiągnie poziomy określone w parametrach — następuje **reset danych**: program zapamiętuje aktualne wartości jako początkowe
4. Przy pierwszym uruchomieniu (lub po przerwie > 12 godzin) program oblicza początkową energię na podstawie SOC pobranego z falownika
5. Obliczenia wykonywane są **co minutę**

### Jak GbbShunt steruje zakończeniem ładowania/rozładowania?

1. Przy wysyłce danych do falownika GbbShunt otrzymuje informację o docelowym SOC na bieżącą godzinę
2. **Ładowanie**: gdy Wyliczony SOC ≥ docelowy SOC — następuje zatrzymanie. Jeśli w tej samej godzinie SOC spadnie poniżej docelowego SOC - 5%, ładowanie zostanie wznowione
3. **Rozładowanie**: gdy Wyliczony SOC ≤ docelowy SOC — następuje zatrzymanie. Jeśli w tej samej godzinie SOC wzrośnie powyżej docelowego SOC + 5%, rozładowanie zostanie wznowione
4. Zakończenie ładowania/rozładowania powoduje wysłanie operacji **Normal** do falownika

> [!NOTE]
> Dobrze, aby falownik wysyłał dane do Solarman **co 1 minutę** (domyślnie co 5 minut). Zmień ten parametr w ustawieniach falownika.
