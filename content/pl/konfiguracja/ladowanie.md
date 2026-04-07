---
title: "Ładowanie"
weight: 20
translationKey: "ladowanie"
---

# Ładowanie

Moduł ładowania zarządza harmonogramami ładowania baterii z sieci. W systemie Victron odpowiada za Schedules w module ESS.

> [!NOTE]
> {{< badge "victron-only" >}} Zakładamy, że „Self-consumption above limit" jest ustawiony na **PV** (a nie „PV & Battery"), ponieważ chcemy, aby harmonogram zatrzymywał rozładowywanie baterii w nocy.

## Pobierz tablicę z instalacji

{{< badge "victron-only" >}} Program łączy się z instalacją i pobiera 5 harmonogramów (Schedulerów).

## Zmiany ładowania

Możesz modyfikować parametry ładowania:
- **Zablokować / odblokować** wiersz ładowania
- Zmienić **godzinę rozpoczęcia** i **czas trwania** — kolumny „Nowy początek" i „Nowy czas trwania"
- Zmienić **limit SOC** — kolumna „Nowy SOCLimit"

Po zmianie:
- **Zapisz** — zmiany zapisane w programie, ale nie wysłane do instalacji. Pozwala testować scenariusze w [Prognozie baterii]({{< relref "/konfiguracja/prognoza-baterii" >}})
- **Wyślij do Instalacji** — zmiany zapisane i wysłane do falownika

Przycisk **Wyczyść wszystkie nowe wartości** resetuje kolumny „Nowy początek", „Nowy czas trwania" i „Nowy SOCLimit".

## Parametry ładowania

| Parametr | Falownik | Opis |
|----------|----------|------|
| Rozciągnij ładowanie do pełnej godziny | Wszyscy | Zmniejsza moc ładowania, aby trwało całą godzinę. Używaj razem z następną opcją! |
| Specjalne liczenie szybkości gdy SOC = TargetSOC | Wszyscy | Jeśli SOC ≤ TargetSOC, oblicz moc ładowania wg wzoru: PV - Zużycie |
| Zmień tryb na „Zero Export To CT" podczas ładowania z sieci | {{< badge "deye-only" >}} | Zapobiega przeciążeniu zabezpieczenia sieci, gdy jednocześnie ładują się baterie i pracują duże odbiorniki. Współgra z grid peak-shaving |
| Ustaw MaxDischarge=0 podczas ładowania | {{< badge "deye-only" >}} | Blokuje rozładowanie baterii podczas ładowania. Używać tylko gdy do Load/Backup nic nie jest podłączone |
| Ustaw MaxDischarge=0 podczas normalnej pracy gdy CenaZakupu < CenaWBateriach | {{< badge "deye-only" >}} | Blokuje rozładowanie baterii podczas normalnej pracy. Używać tylko gdy do Load/Backup nic nie jest podłączone |
| Nie zmieniaj PeakShaving W podczas ładowania | {{< badge "deye-only" >}} | Pozostawia wartość PeakShaving bez zmian podczas ładowania |

## Ustawienia dla Optymalizatora

Ładowanie jest optymalizowane przez [Prognozę Baterii]({{< relref "/konfiguracja/prognoza-baterii" >}}), jeśli:
- Nie jest zablokowane
- Nie zaznaczono „Nie optymalizuj SOCLimit przez Prognozę Baterii"

Opcje:
- **Minimalny SOCLimit (%)** i **Maksymalny SOCLimit (%)** — ograniczenie zakresu „Nowy SOCLimit" (tylko optymalizator SOC)
- **Może być zablokowany przez Prognozę Baterii** — optymalizator może zablokować ładowanie, aby zrobić miejsce na PV

> [!NOTE]
> Ustawienie SOCLimit = 5% blokuje rozładowywanie baterii.

## Dynamic Charge — dynamiczna zmiana godziny ładowania

Dynamic Charge automatycznie szuka godzin z **najniższą ceną zakupu** i przesuwa tam ładowanie.

> [!WARNING]
> Nie używaj tej opcji z **optymalizatorem opartym o ceny**!

Konfiguracja:

1. Dodaj przynajmniej jeden harmonogram
2. Wybierz, które Ładowanie chcesz zmienić
3. Wpisz **od jakiej godziny** i **ile godzin** program ma przeszukiwać
   - 24 godziny → godzina początkowa nieistotna, program sprawdza 24h od bieżącej godziny
   - Mniej niż 24h → program sprawdza podane godziny. Jeśli okres minął — sprawdza następny dzień
4. Wpisz **ile godzin** chcesz ładować
5. Zapisz

Aby automatyzować — ustaw **Zadanie godzinowe** (patrz niżej).

Aby przetestować — naciśnij **Optymalizuj Ładowanie teraz**.

Program przesuwa godzinę rozpoczęcia do cen minimalnych. Jeśli dwa ładowania mają pokrywające się okresy — program szuka różnych godzin z cenami minimalnymi dla każdego.

## Dynamic Charge: Blokowanie ładowania przy niskiej cenie

Blokuje rozładowanie baterii, gdy cena jest zbyt niska w porównaniu z ceną ostatniego ładowania.

> [!WARNING]
> Nie używaj tej opcji z **optymalizatorem opartym o ceny**!

Konfiguracja:

1. Dodaj przynajmniej jeden wiersz
2. Wybierz Ładowanie do zmiany (nie powinno być używane w innych modułach)
3. Wpisz **od jakiej godziny** i **ile godzin** program ma szukać ceny niższej od ceny ostatniego ładowania
   - 24 godziny → godzina początkowa nieistotna
   - Mniej niż 24h → sprawdza podane godziny, jeśli minęły — następny dzień
4. Wpisz **ile %** doliczyć do ceny ostatniego ładowania (np. 10%)
5. Zapisz

**Jak to działa** (przykład: od godziny 0, sprawdzanie 6h):
1. Szuka **ceny ostatniego ładowania**: od godziny przed końcem okresu, wstecz. Pobiera ostatnie ładowanie w okresie lub pierwsze ładowanie przed okresem
2. Sprawdza godziny, w których cena zakupu < cena ostatniego ładowania + „Dodaj procent". Szuka od początku okresu (lub od końca ładowania)

> [!NOTE]
> Jedno Ładowanie może być używane w wielu blokadach, jeśli okresy godzinowe nie nakładają się.

> [!WARNING]
> Jeśli masz Ładowanie, które zmienia się dynamicznie (np. od 0 do 6), skonfiguruj harmonogram blokowania z **tego samego okresu** (od 0 do 6) **lub dłuższego** (np. od 0 do 9).

## Zadanie godzinowe

Aby automatycznie optymalizować ładowania i wysyłać dane do instalacji co godzinę:

Zaznacz **Automatycznie optymalizuj Ładowania co godzinę i wysyłaj informacje do Instalacji**.

## Ostrzeżenia meteorologiczne

Moduł automatycznie ładuje baterie do 100% (lub innej wartości), gdy nadchodzą ważne ostrzeżenia meteorologiczne.

Konfiguracja:
1. Dodaj kraj (np. Polska z MeteoAlarm lub IMGW)
2. Dodaj rodzaje ostrzeżeń, które Cię interesują
3. Dla każdego rodzaju wskaż **od jakiego poziomu** (ten i wyższe) i **jaki SOC** wymusić

Gdy pojawi się ostrzeżenie danego rodzaju i poziomu — optymalizator oparty o ceny wymusi wskazany poziom SOC w czasie trwania ostrzeżenia, nawet kosztem ładowania z sieci.
