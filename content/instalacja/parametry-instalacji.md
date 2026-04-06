---
title: "Parametry instalacji"
weight: 10
---

# Parametry instalacji

Poniżej opisane są wszystkie parametry konfiguracyjne instalacji w GbbOptimizer, pogrupowane tematycznie.

## Typ

| Parametr | Jednostka | Opis |
|----------|-----------|------|
| Typ | — | Typ połączenia z falownikiem (Victron, Solarman, GbbConnect2, DongleDirect, SolarAssistant) |
| Przedziałów czasu dziennie | — | Liczba przedziałów czasu dziennie. W Polsce obowiązuje 60 przedziałów dla klientów indywidualnych |

## Instalacja

| Parametr | Jednostka | Opis |
|----------|-----------|------|
| Nazwa | — | Unikalna nazwa instalacji w ramach konta |
| Strefa czasowa | — | Strefa czasowa lokalizacji instalacji |
| Maksymalna moc pobierania z sieci | kW | Parametr przyłącza — maksymalna moc pobierana z sieci |
| Maksymalna moc wysyłania do sieci | kW | Parametr przyłącza — maksymalna moc oddawana do sieci |
| Jaki % PV jest podłączony po stronie DC? | % | `0%` — wszystkie PV podłączone do AC. `100%` — wszystkie PV podłączone do DC |
| Szerokość/Długość geograficzna | — | Położenie geograficzne instalacji. Używane przez moduły: Meteo i Prognozy PV |

## Źródła cen

| Parametr | Opis |
|----------|------|
| Zakup: Taryfa dla cen zakupu | Źródło zaimportowanych cen zakupu energii |
| Przesył: Taryfa dla cen przesyłu | Źródło cen przesyłu (transport). Puste = 0 |
| Sprzedaż: Taryfa dla cen sprzedaży | Źródło zaimportowanych cen sprzedaży energii |

Szczegóły wzorów cenowych — w module [Ceny]({{< relref "/konfiguracja/ceny" >}}).

## Bateria

| Parametr | Jednostka | Opis |
|----------|-----------|------|
| Pojemność baterii (brutto) | kWh | Całkowita pojemność baterii |
| Średnie napięcie baterii | V | Używane do przeliczania W z A i A z W. Może być przybliżone |
| Minimalny {{< glossary "SOC" >}} baterii | % | {{< glossary "MinSOC" >}} — żelazna rezerwa. Poniżej tej wartości energia używana tylko w sytuacjach awaryjnych |
| Maksymalna moc ładowania falownika (DC) | kW | Maksymalna moc ładowania po stronie DC |
| Maksymalna moc rozładowania falownika (DC) | kW | Maksymalna moc rozładowania po stronie DC |
| Maksymalna moc BMS ładowania baterii (DC) | kW | Istotne, gdy jest inna niż moc falownika i PV podłączone po stronie DC |
| Maksymalna moc BMS rozładowania baterii (DC) | kW | Istotne, gdy jest inna niż moc falownika i PV podłączone po stronie DC |
| Straty na ładowaniu baterii z sieci | % | Straty na ładowaniu (wliczając sposób liczenia SOC przez BMS) |
| Straty na rozładowaniu baterii do sieci/zużycia | % | Straty na rozładowaniu (wliczając sposób liczenia SOC przez BMS) |

## Victron

{{< badge "victron-only" >}}

| Parametr | Opis |
|----------|------|
| VRM Portal Id | Identyfikator portalu {{< glossary "VRM" >}}. Znajdziesz w: Cerbo → Settings → VRM Online Portal → VRM Portal ID |
| Installation Id | Numer w adresie strony VRM |
| Login/email VRM | Login do portalu VRM |
| Hasło do VRM | Hasło do portalu VRM (jeśli nie używasz 2FA) |
| VRM Token | Token dla uwierzytelniania dwuskładnikowego (2FA) |
| Numer VRM Instance urządzenia VE.Bus System | Normalnie falownik ma numer `276`, ale czasami inny |

## Solarman / DeyeCloud

| Parametr | Dotyczy | Opis |
|----------|---------|------|
| Sposób zalogowania się | — | Email, login lub numer telefonu |
| Email / Login / Numer telefonu | — | Dane logowania do Solarman/DeyeCloud |
| Hasło | — | Hasło do Solarman/DeyeCloud |
| Zapamiętaj dane do logowania | — | Automatyczne ponowne łączenie. Bez tego wymagane ręczne logowanie (email z powiadomieniem) |
| Wybierz SerialNo falownika | — | Po połączeniu wybierz numer seryjny falownika |
| Rodzaj falownika | — | Rodzaj falownika. **Nie wolno się pomylić!** Błędny wybór i wysłanie danych wymaga przywrócenia ustawień fabrycznych falownika |
| Deye: Dodaj produkcję MI/GEN do produkcji PV | {{< badge "deye-only" >}} | Na niektórych wersjach firmware produkcja z wejścia GEN musi być dodana ręcznie |
| Deye: Nie ma CT, więc nie próbuj ustawić ZeroToCT | {{< badge "deye-only" >}} | Przy braku CT program powraca do ZeroToLoad zamiast ZeroToCT po zakończeniu rozładowania |
| Deye: Ustaw czas falownika o północy | {{< badge "deye-only" >}} | Synchronizuje zegar falownika o północy |
| Dane o SOC z HomeAssistant/SolarAssistant | — | Nie pobieraj {{< glossary "SOC" >}} z falownika — zostanie dostarczony przez HA/SA |
| Dane ZSieci/DoSieci pobierane z | — | Nie pobieraj ZSieci/DoSieci z falownika — dane z HomeAssistant lub licznika IoT |
| Dane Zużycia z HomeAssistant/SolarAssistant | — | Nie pobieraj Zużycia z falownika — zostanie dostarczone przez HA/SA |

### Zapasowe połączenie — DeyeCloud

Dotyczy tylko instalacji typu Solarman. Szczegóły na stronie [DeyeCloud]({{< relref "/instalacja/metody-polaczenia/deye-cloud" >}}).

| Parametr | Opis |
|----------|------|
| Jak połączenie zapasowe ma być używane | **Wyłączone** / **Włączone** (przy błędzie Solarman) / **Tylko zapasowe** (zawsze DeyeCloud) |
| Sposób zalogowania / Email / Hasło | Dane logowania do DeyeCloud |
| Zapamiętaj dane do logowania | Automatyczne ponowne logowanie do DeyeCloud |
| Wybierz SerialNo falownika | Po połączeniu wybierz numer seryjny |

## Parametry falownika

{{< badge "deye-only" >}}

| Parametr | Opis |
|----------|------|
| Steruj poprzez V, a nie przez SOC | Falownik używa napięcia (V) zamiast SOC w TimeOfUse |
| Także aktualne SOC obliczaj z V | Obliczaj bieżący SOC na podstawie napięcia. Jeśli odznaczone — SOC pobierany z falownika |

## GbbShunt

{{< badge "deye-only" >}} Dotyczy tylko instalacji Solarman + Deye. Szczegóły na stronie [Solarman]({{< relref "/instalacja/metody-polaczenia/solarman" >}}).

| Parametr | Jednostka | Opis |
|----------|-----------|------|
| Włączony | — | Aktywuje moduł GbbShunt |
| Minimalny SOC baterii / V kiedy SOC → MinSOC | V | Napięcie, przy którym SOC zostanie ustawiony na {{< glossary "MinSOC" >}} |
| Maksymalny SOC baterii / V kiedy SOC → MaxSOC | V | Napięcie, przy którym SOC zostanie ustawiony na {{< glossary "MaxSOC" >}} |
| Straty na ładowaniu + rozładowaniu | % | Procent energii pomijanej w obliczeniach |
| V podczas ładowania baterii | V | Napięcie wysyłane do TimeOfUse zamiast wartości wyliczonej z docelowego SOC |
| V podczas rozładowania baterii | V | Napięcie wysyłane do TimeOfUse zamiast wartości wyliczonej z docelowego SOC |

## Pomoc techniczna

| Parametr | Jednostka | Opis |
|----------|-----------|------|
| Wyślij email po utracie połączenia | godziny | Po ilu godzinach bez połączenia program wyśle powiadomienie. Puste pole = brak powiadomień |
| Wyślij email z błędami w logu | — | Co godzinę wysyła zestawienie błędów z logu |
| Dodatkowe adresy email | — | Dodatkowe adresy do wysyłania powiadomień. Przydatne dla instalatorów, aby klient również otrzymywał emaile |
| Udostępnij instalację pomocy technicznej | — | Daje dostęp pomocy technicznej do Twojej instalacji. Skontaktuj się najpierw na Discordzie |
