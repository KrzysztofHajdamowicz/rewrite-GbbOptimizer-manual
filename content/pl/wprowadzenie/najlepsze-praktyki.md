---
title: "Najlepsze praktyki"
weight: 30
translationKey: "najlepsze-praktyki"
---

# Najlepsze praktyki

Porady i wskazówki od doświadczonych użytkowników GbbOptimizer.

## Cierpliwość

> [!WARNING]
> Najczęstszy błąd nowych użytkowników to zbyt szybkie zmiany konfiguracji. Program potrzebuje czasu na kalibrację.

GbbOptimizer to program, który uczy cierpliwości. Przez pierwszy tydzień pracy:

- {{< glossary "Correction Factor" >}} dla prognozy PV się kalibruje
- Profil zużycia zbiera dane historyczne
- Optymalizator "uczy się" Twojej instalacji

Nie wyłączaj {{< glossary "Test Mode" >}} wcześniej niż po tygodniu. Daj programowi czas na zebranie danych.

## Ustaw MaxSOC na 90%

{{< badge "recommended" >}}

Ustaw {{< glossary "MaxSOC" >}} na **90%** zamiast 100%. Dlaczego?

- Zostawiasz **bufor 10%** na nieprzewidzianą nadwyżkę PV (gdy prognoza jest za niska)
- Nadwyżka PV nie jest marnowana — trafia do baterii zamiast do sieci po niskiej cenie sprzedaży
- Bateria rzadziej osiąga 100%, co wydłuża jej żywotność

### Okresowe pełne ładowanie

Dla zdrowia baterii warto jednak okresowo ładować do 100%. Ustaw parametr **„Lista dni w miesiącu kiedy MaxSOC ma być zmieniony na 100%”** np. na:

```
1, 15
```

Dzięki temu 1. i 15. dnia każdego miesiąca bateria naładuje się do pełna (na około 2h), co pozwala na kalibrację {{< glossary "SOC" >}} i jest korzystne dla chemii ogniw. Więcej o tym parametrze: {{< glossary "Battery Full Date" >}}.

## Zmień źródło prognozy PV

{{< badge "recommended" >}}

Domyślne źródło prognozy PV to **forecast.solar**. Rozważ zmianę na **solcast.com**, które jest zazwyczaj dokładniejsze:

1. Załóż darmowe konto „Home” na [solcast.com](https://solcast.com)
2. Dodaj swoje płaszczyzny PV (jedno konto obsługuje do dwóch płaszczyzn)
3. W parametrach instalacji zmień źródło prognozy PV na Solcast

> [!NOTE]
> Solcast ma limit zapytań na darmowym koncie — jedno konto „Home” obsługuje maksymalnie dwie płaszczyzny PV. Jeśli masz więcej, potrzebujesz dodatkowych kont.

## Mniej opcji = większe zyski

Im mniej dodatkowych opcji zaznaczonych w parametrach optymalizatora, tym lepsze wyniki. Każda dodatkowa opcja to dodatkowe ograniczenie, które zmniejsza pole manewru optymalizatora.

Zacznij od konfiguracji domyślnej i dodawaj opcje tylko wtedy, gdy masz konkretny powód.

## Solarman i Home Assistant — unikaj konfliktu

> [!WARNING]
> Jeśli korzystasz z Solarman i jednocześnie importujesz dane z falownika do Home Assistant, ustaw `update_interval` na **co najmniej 20 sekund**. Zbyt częste odpytywanie powoduje konflikty komunikacji — Solarman i Home Assistant "gryzą się" o dostęp do falownika.

Alternatywne rozwiązanie: przejdź z Solarman na {{< glossary "GbbConnect2" >}}, który nie ma tego problemu.

## Weryfikuj dane wejściowe

Po początkowej konfiguracji sprawdź trzy kluczowe elementy:

### 1. Ceny

Upewnij się, że [ceny]({{< relref "/konfiguracja/ceny" >}}) są prawidłowe:
- Czy uwzględniono koszty transportu (przesyłu)?
- Czy VAT jest prawidłowy?
- Czy cena sprzedaży odpowiada Twojej taryfie?

### 2. Prognoza PV

Sprawdź w [Prognozie baterii]({{< relref "/konfiguracja/prognoza-baterii" >}}), czy prognoza PV jest zbliżona do rzeczywistej produkcji. Jeśli nie — zmień źródło prognozy.

### 3. Profil zużycia

Zweryfikuj [profil zużycia]({{< relref "/konfiguracja/profile-zuzycia" >}}):
- Czy wartości odpowiadają rzeczywistemu zużyciu domu?
- Czy weekendy różnią się od dni roboczych (jeśli tak jest w rzeczywistości)?

## Tryb testowy to Twój przyjaciel

Używaj {{< glossary "Test Mode" >}} nie tylko na początku. Włączaj go za każdym razem, gdy:

- Zmieniasz istotne parametry konfiguracji
- Zmieniasz źródło prognozy PV
- Zmieniasz taryfę energetyczną
- Dodajesz nową płaszczyznę PV

Daj optymalizatorowi dzień lub dwa na przeliczenie nowych danych, zanim pozwolisz mu sterować falownikiem.

## Podsumowanie

| Praktyka | Priorytet |
|----------|-----------|
| Poczekaj tydzień przed wyłączeniem trybu testowego | {{< badge "required" >}} |
| Sprawdź poprawność cen i kosztów transportu | {{< badge "required" >}} |
| Ustaw MaxSOC = 90% | {{< badge "recommended" >}} |
| Zmień prognozę PV na Solcast | {{< badge "recommended" >}} |
| Ustaw peryodyczne ładowanie do 100% (np. 1, 15 dnia miesiąca) | {{< badge "recommended" >}} |
| Minimalizuj liczbę dodatkowych opcji | {{< badge "recommended" >}} |
