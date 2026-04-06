---
title: "Szybki start"
weight: 20
translationKey: "szybki-start"
---

# Szybki start

Przewodnik krok po kroku, jak uruchomić GbbOptimizer dla Twojej instalacji fotowoltaicznej.

## 1. Załóż konto i utwórz instalację

Wejdź na stronę GbbOptimizer i załóż konto. Następnie dodaj nową instalację wybierając odpowiednią opcję w zależności od Twojego falownika:

| Falownik | Opcja w menu |
|----------|-------------|
| **Victron** (Cerbo GX lub inny moduł GX) | „Dodaj nową instalację z Victron System" |
| **Deye** przez DeyeCloud | „Dodaj nową instalację z inwerterem Deye podłączonym do DeyeCloud" |
| **Deye** przez Solarman | „Dodaj nową instalację z Solarman" |
| **Deye** przez Home Assistant | „Dodaj nową instalację z Home Assistant" |
| **Inny falownik** przez Solarman | „Dodaj nową instalację z Solarman" |
| **Inny falownik** przez Home Assistant | „Dodaj nową instalację z Home Assistant" |
| **SofarSolar** | „Instalacja z DongleDirect (Deye, SofarSolar)" |

> [!NOTE]
> Jeżeli masz falowniki Deye w układzie Master-Slave, wybierz „Instalacja z Solarman" i dodaj Master jako główny falownik, a Slave jako dodatkowy w parametrach instalacji.

Każda instalacja otrzymuje unikalny {{< glossary "PlantId" >}} i {{< glossary "PlantToken" >}}.

## 2. Wypełnij dane instalacji

Wypełnij wszystkie pola (przynajmniej te oznaczone gwiazdką **\***) w formularzu instalacji. Po wypełnieniu naciśnij **„Zapisz i kontynuj w Szybkiej Konfiguracji"**.

{{< glossary "FastSetup" >}} przeprowadzi Cię przez podstawową konfigurację:

- Dodanie płaszczyzn PV
- Wybór źródła prognozy PV
- Podstawowe parametry baterii

Po wypełnieniu wszystkich pól naciśnij **„Zapisz zmiany"**.

## 3. Skonfiguruj ceny

W module [Ceny]({{< relref "/konfiguracja/ceny" >}}):

1. Kliknij **„Wybierz taryfę dystrybutora i sprzedawcy energii"**
2. Wybierz swoją taryfę dystrybucji i taryfę dostawcy energii
3. Naciśnij **„Importuj wybrane taryfy"**

Alternatywnie, ręcznie skonfiguruj ceny zakupu i sprzedaży.

> [!WARNING]
> Pamiętaj o ustawieniu kosztów transportu (przesyłu) dla cen zakupu. Bez nich optymalizator nie będzie prawidłowo obliczał opłacalności ładowania z sieci.

## 4. Skonfiguruj profil zużycia

W module [Profile zużycia]({{< relref "/konfiguracja/profile-zuzycia" >}}) masz dwie opcje:

- **Ręczne wprowadzenie** — wpisz szacunkowe zużycie dla każdej godziny
- **Import z instalacji** — poczekaj ~tydzień, aż program zbierze dane z falownika i obliczy średnie zużycie

> [!NOTE]
> Jeśli nie chcesz wprowadzać profilu zużycia ręcznie, poczekaj tydzień — program automatycznie zbierze dane i obliczy profil. W tym czasie i tak powinien działać {{< glossary "Test Mode" >}}.

## 5. Sprawdź prognozę PV

Zweryfikuj w module [Prognoza baterii]({{< relref "/konfiguracja/prognoza-baterii" >}}), czy prognoza PV jest zbliżona do rzeczywistej produkcji. Jeżeli nie, spróbuj zmienić źródło prognozy PV w parametrach instalacji.

{{< glossary "Correction Factor" >}} kalibruje się automatycznie przez około tydzień pracy.

## 6. Poczekaj w trybie testowym

Nowa instalacja startuje w {{< glossary "Test Mode" >}} — optymalizator wykonuje obliczenia, ale **nie wysyła komendy do falownika**.

Przez pierwszy tydzień:

- Profil zużycia się zaktualizuje (jeśli włączono automatyczny import)
- {{< glossary "Correction Factor" >}} dla prognozy PV kalibruje się
- Możesz obserwować, co optymalizator *planuje* robić, bez ryzyka

## 7. Wyłącz tryb testowy

Po ~tygodniu, gdy upewnisz się, że:

- **Ceny** są prawidłowe (ze wszystkimi kosztami transportu)
- **Prognoza PV** jest zbliżona do rzeczywistości
- **Profil zużycia** jest sensowny

...wyłącz {{< glossary "Test Mode" >}} w module [Prognoza baterii]({{< relref "/konfiguracja/prognoza-baterii" >}}). Od tego momentu optymalizator zacznie wysyłać komendy do falownika.

## Filmy instruktażowe

- [Dodawanie systemu Victron do GbbOptimizer](https://youtu.be/5q6gORx1KUY)
- [Dodawanie falownika Deye przez Solarman](https://youtu.be/y8fhh1UecqQ)
- [Konfigurowanie cen zakupu i sprzedaży](https://youtu.be/m27uQfO60pc)

## Tylko optymalizacja ładowania EV (bez fotowoltaiki)

Jeśli chcesz optymalizować tylko ładowanie samochodu elektrycznego, bez instalacji PV:

1. Dodaj nową instalację typu **Home Assistant**
2. Wypełnij pola:
   - Nazwa
   - Moc przyłącza — pobieranie
   - Moc przyłącza — wysyłanie → wpisz **0**
   - Pojemność kWh baterii → wpisz **0**
3. Naciśnij **„Zapisz i kontynuj w Szybkiej Konfiguracji"**, na tej stronie:
   - Odznacz **„Dodaj pierwszą Płaszczyznę PV"**
   - Zaznacz **„EV: Automatycznie importuj dane z ładowarek EV co godzinę"**
4. Naciśnij **„Zapisz"** — zostaniesz przeniesiony do menu Ceny:
   - Wybierz taryfę dystrybutora i sprzedawcy energii
   - Naciśnij **„Importuj wybrane taryfy"**
5. Przejdź do modułu [Extra Zużycie / EV]({{< relref "/konfiguracja/dodatkowe-obciazenia-ev" >}}):
   - W sekcji „Ładowanie EV" dodaj swoją ładowarkę
   - W sekcji „AutoŁadowanie EV" skonfiguruj warunki ładowania (np. w „Warunki" wybierz „Cena" → 3 najniższe ceny zakupu)

## Co dalej?

- [Najlepsze praktyki]({{< relref "/wprowadzenie/najlepsze-praktyki" >}}) — porady, jak wyciągnąć z systemu maksimum
- [Ładowanie]({{< relref "/konfiguracja/ladowanie" >}}) — konfiguracja harmonogramów ładowania
- [Rozładowanie]({{< relref "/konfiguracja/rozladowanie" >}}) — konfiguracja rozładowania baterii
- [Prognoza baterii]({{< relref "/konfiguracja/prognoza-baterii" >}}) — centralny moduł optymalizatora
