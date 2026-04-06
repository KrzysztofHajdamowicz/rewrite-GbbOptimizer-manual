---
title: "Rozładowanie"
weight: 30
---

# Rozładowanie

Moduł rozładowania kontroluje, kiedy i jak energia z baterii jest wysyłana do sieci lub używana do zasilania domu. Kluczowym parametrem jest {{< glossary "GridSetpoint" >}}.

## GridSetpoint — jak działa

{{< glossary "GridSetpoint" >}} określa, ile energii powinna przepływać przez licznik sieci:

- **Wartość dodatnia** (np. +100 W) — system pobiera energię z sieci. Nadwyżka z PV idzie do baterii.
- **Wartość ujemna** (np. -5000 W) — system eksportuje energię do sieci. Najpierw z PV, potem z baterii.

**Przykład 1:** GridSetpoint = +100 W

| Parametr | Wartość |
|----------|---------|
| PV produkuje | 2000 W |
| Dom zużywa | 500 W |
| Z sieci | +100 W |
| **Do baterii** | **1600 W** |

**Przykład 2:** GridSetpoint = -5000 W

| Parametr | Wartość |
|----------|---------|
| PV produkuje | 2000 W |
| Dom zużywa | 500 W |
| Do sieci | 5000 W |
| **Z baterii** | **3500 W** |

**Przykład 3:** GridSetpoint = -5000 W, dużo PV

| Parametr | Wartość |
|----------|---------|
| PV produkuje | 6000 W |
| Dom zużywa | 500 W |
| Do sieci | 5000 W |
| **Do baterii** | **500 W** |

Aby chronić baterię podczas rozładowania:
- Ustaw {{< glossary "MinSOC" >}} — bateria nie zejdzie poniżej tego poziomu
- Zaznacz „Zablokuj rozładowywanie baterii" — bateria nie zejdzie poniżej aktualnego SOC (ale może być ładowana)

## Pierwszy krok

Aby zacząć rozładowywać:

1. Stwórz jeden **Plan Rozładowania** (o ile nie istnieje)
2. {{< badge "victron-only" >}} Jeśli „Battery Life" jest włączony w ESS — wyłącz go. Ustaw na „Optimized (without BatteryLife)"

## Normalne rozładowanie

Aby ustawić normalne rozładowanie w wybranej godzinie:

1. Zaznacz **Włącz** dla wybranej godziny
2. Wpisz **Max GridSetpoint** — wartość ujemna, ile W maksymalnie powinno iść do sieci
3. *(Opcjonalnie)* Wpisz **MinSOC** — ograniczenie rozładowania do wskazanego poziomu SOC

> [!NOTE]
> Program sprawdza aktualny SOC baterii. Jeżeli MinSOC jest wyższy niż aktualny SOC, program wyśle aktualny SOC. Zapobiega to ładowaniu baterii do MinSOC zamiast rozładowania.

Aby przetestować ustawienia dla bieżącej godziny — naciśnij **Wyślij teraz dane do instalacji**.

## Zadania godzinowe

Aby automatycznie wysyłać dane do instalacji co godzinę:

1. Zaznacz **Uruchom zadanie co godzinę**
2. {{< badge "victron-only" >}} Wpisz aktualny MinSOC (z ESS w Cerbo) w polu **Domyślny MinSOC po rozładowaniu**
3. {{< badge "victron-only" >}} Wpisz aktualny GridSetpoint (z ESS) w polu **Domyślny GridSetpoint po rozładowaniu**
4. Zapisz zmiany

> [!NOTE]
> - Co godzinę program wysyła dane rozładowania tylko dla godzin z zaznaczonym „Włącz"
> - Po ostatniej godzinie rozładowania program przywraca wartości domyślne
> - Opcja „Nie rozładowuj jeżeli Cena Sprzedaży < ostatnia cena zakupu" blokuje rozładowanie, gdy sprzedaż byłaby nieopłacalna

## Rozładowanie warunkowe — gdy cena > minimum

Aby rozładowywać tylko wtedy, gdy cena sprzedaży przekracza próg:

1. Zaznacz **Włącz** dla wybranej godziny
2. Wpisz **Max GridSetpoint** (wartość ujemna)
3. *(Opcjonalnie)* Wpisz **MinSOC**
4. Zaznacz **Tylko jeżeli Cena > MinCenaSprzedaży**
5. Wpisz limit w **MinCenaSprzedaży**

## Blokowanie rozładowania / ładowania baterii

Aby zablokować rozładowanie (lub ładowanie) baterii poniżej bieżącego SOC:

1. Zaznacz **Włącz** dla wybranej godziny
2. {{< badge "victron-only" >}} Wpisz **Max GridSetpoint**
3. Zaznacz **Zablokuj rozładowanie baterii** (lub **Zablokuj ładowanie baterii**)

> [!NOTE]
> {{< badge "victron-only" >}} Program ustawia MinSOC w ESS na bieżącą wartość SOC, co blokuje rozładowanie ale pozwala na ładowanie. Po tej godzinie MinSOC wraca do wartości domyślnej.

> [!WARNING]
> {{< badge "victron-only" >}} Jeśli ustawisz „Zablokuj rozładowanie baterii" z GridSetpoint = duża wartość ujemna (np. minus całkowita moc PV), cała energia z PV pójdzie do sieci i bateria nie będzie ładowana. Można to wykorzystać do **opóźnienia ładowania baterii**.

## Dynamiczne rozładowanie (Dynamic Discharge — DD)

{{< glossary "Dynamic Discharge" >}} automatycznie szuka godzin z najwyższą ceną sprzedaży i w tych godzinach ustawia rozładowanie.

> [!WARNING]
> Nie używaj tej funkcji z **optymalizatorem opartym o ceny**!

Aby skonfigurować DD:

1. Dodaj przynajmniej jeden okres rozładowania
2. Wpisz **od której godziny** i **ile godzin** program ma przeszukiwać
   - 24 godziny → godzina początkowa nieistotna, program sprawdza 24h od bieżącej godziny
   - Mniej niż 24h → program sprawdza od wskazanej godziny. Jeśli okres minął — sprawdza następny dzień
3. Wpisz **ile godzin** chcesz rozładowywać
4. Dla wszystkich godzin w okresie — wpisz **Max GridSetpoint**
5. Aby automatyzować: zaznacz **Uruchom zadanie co godzinę** i **Automatycznie optymalizuj DD i DDBD**

Aby przetestować — naciśnij **Optymalizuj dynamiczne rozładowanie teraz**.

Program zaznacza godziny z maksymalną ceną sprzedaży i blokuje pozostałe. Pomija godziny bez wpisanego GridSetpoint oraz godziny, w których obowiązuje ładowanie.

> [!NOTE]
> Jeśli zdefiniujesz dwa okresy DD dla tego samego czasu — pierwszy znajduje godziny z najwyższymi cenami, drugi szuka kolejnych najwyższych (z wykluczeniem już znalezionych).

## Dynamiczny MinSOC przez Optymalizator

Aby optymalizator z {{< relref "/konfiguracja/prognoza-baterii" >}} dynamicznie zmieniał MinSOC:

1. Zaznacz **Włącz** (lub użyj DD/DDBD do włączania)
2. Wpisz **Max GridSetpoint**
3. Zaznacz **MinSOC optymalizuj przez Prognozę Baterii**
4. *(Opcjonalnie)* Wpisz **MinimalSOC** — dolny limit rozładowania przez optymalizator
5. *(Opcjonalnie)* Zaznacz **Tylko jeżeli Cena > MinCena** i wpisz **MinCena**

**Przykład:** Program rozładowuje baterię o 21:00 (najwyższa cena sprzedaży), aby do 16:00 zrobić miejsce na energię z PV. SOC nigdy nie spada poniżej MinSOC.

## Dynamiczne blokowanie rozładowania (DDBD)

**DDBD** (Dynamically Disable Battery Discharge) wymusza wysyłanie produkcji PV do sieci aż do momentu, gdy cena jest najniższa — wtedy lepiej ładować baterię z PV niż sprzedawać.

> [!WARNING]
> Nie używaj tej funkcji z **optymalizatorem opartym o ceny**!

Aby skonfigurować DDBD:

1. Dodaj przynajmniej jeden okres
2. Wpisz **od jakiej godziny** i **ile godzin** program ma szukać minimalnej ceny zakupu
3. Wpisz **ile godzin** chcesz ładować baterię
4. Dla wszystkich godzin w okresie — wpisz **Max GridSetpoint** (duża wartość ujemna)
5. Aby automatyzować: zaznacz **Uruchom zadanie co godzinę** i **Automatycznie optymalizuj DD i DDBD**

Aby przetestować — naciśnij **Optymalizuj blokowanie baterii teraz**.

### Wyłącz DDBD jeśli bateria nie będzie naładowana

Program może sprawdzić, czy po upływie czasu DDBD bateria zostanie naładowana do wymaganego poziomu. Jeśli nie — wyłącza DDBD jednorazowo.

Parametry:
- **Ilość godzin ładowania** — przez ile godzin bateria powinna być ładowana
- **Tylko jeżeli SOC wzrośnie nie mniej niż X %** — wymagany wzrost SOC w godzinach ładowania

> [!NOTE]
> Jeśli pole „tylko jeśli SOC wzrośnie..." jest puste, optymalizator nie sprawdza, czy bateria zostanie naładowana do wymaganego poziomu.

## Automatyczne włączanie rozładowania (dzień/noc)

Program może automatycznie włączać rozładowanie tylko w dzień lub tylko w nocy, na podstawie godzin wschodu i zachodu słońca.

> [!NOTE]
> Wymaga ustawienia szerokości i długości geograficznej w [parametrach instalacji]({{< relref "/instalacja/parametry-instalacji" >}}).

## Parametry rozładowania

| Parametr | Falownik | Opis |
|----------|----------|------|
| Automatycznie włącz Rozładowanie | Wszyscy | Włącz rozładowanie (kolumna „Włącz") tylko w dzień lub w nocy, wyłącz w pozostałych godzinach |
| Domyślny MinSOC po rozładowaniu (%) | {{< badge "victron-only" >}} | MinSOC ustawiany w falowniku po zakończeniu rozładowania |
| Domyślny GridSetpoint po rozładowaniu (W) | {{< badge "victron-only" >}} | GridSetpoint ustawiany w falowniku po zakończeniu rozładowania |
| Rozciągnij rozładowanie do pełnej godziny | Wszyscy | Ustaw GridSetpoint/MaxSellPower tak, aby rozładowanie trwało całą godzinę |
| Zawsze wysyłaj stały MinSOC | Wszyscy | Wysyłaj stałą wartość MinSOC zamiast wartości z Planu Rozładowania. Idea: prędkość rozładowania kontrolowana tylko przez GridSetpoint, mniejsze ryzyko ładowania z sieci po osiągnięciu TargetSOC |
| Specjalne liczenie GridSetpoint gdy SOC = TargetSOC | Wszyscy | Podczas utrzymywania stałego SOC — ustaw mały GridSetpoint zamiast maksymalnego |
| Powiększ GridSetpoint o prognozowane Zużycie | Wszyscy | Dla systemów z domem po stronie sieci falownika |
| Wyłącz Peak-Shaving podczas rozładowania | {{< badge "deye-only" >}} | W niektórych firmware peak-shaving blokuje rozładowanie — program może go wyłączyć |
| Ustaw MaxCharge=0 podczas rozładowania | {{< badge "deye-only" >}} | Blokuj ładowanie (nawet przypadkowe) podczas godziny rozładowania |
| Jeżeli nie ma co robić | {{< badge "victron-only" >}} {{< badge "deye-only" >}} | Gdy: brak PV, brak ładowania, brak rozładowania, MinSOC < SOC < MaxSOC, brak ładowania EV → odłącz falownik od sieci (lub Deye: ustaw „NoBatt"). Idea: zmniejszenie zużycia prądu przez falownik |

## Cena sprzedaży ≤ 0

Specjalne operacje, gdy cena sprzedaży jest ujemna lub równa 0:

### Victron

| Opcja | Opis |
|-------|------|
| Odłącz od sieci | Falownik wchodzi w tryb „Inverter only" |
| Wyłącz „DC-coupled PV — feed in excess" | Wyłącza opcję dla PV podłączonego po stronie DC |
| Ustaw GridSetpoint jeżeli Cena ≤ 0 | Np. 0 — ogranicza wysyłanie prądu do sieci |
| Włącz Relay 1/2 | Wyłączenie PV za pomocą wyjścia Relay1/Relay2 Cerbo |
| Załóż, że nie ma PV | Program zakłada, że PV nie działa w godzinach z ceną ≤ 0 |

### Solarman (Deye)

| Opcja | Opis |
|-------|------|
| Odłącz od sieci | Zmienia dozwolone minimalne napięcie na 270 V — Deye odłącza się od sieci |
| Wyłącz SolarSell i MI export to Grid cutoff | Wyłącza SolarSell i mikroinwertery podczas godzin z ceną < 0 |
| Załóż, że nie ma PV | Jak wyżej |

### DeyeCloud

| Opcja | Opis |
|-------|------|
| Wyłącz SolarSell | Wyłącza SolarSell podczas godzin z ceną < 0 |
| Załóż, że nie ma PV | Jak wyżej |

### HomeAssistant / GbbConnect

| Opcja | Opis |
|-------|------|
| Załóż, że nie ma PV | Program zakłada, że PV nie działa w godzinach z ceną ≤ 0 |
