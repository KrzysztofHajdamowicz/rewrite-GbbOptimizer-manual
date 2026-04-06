---
title: "Prognoza baterii"
weight: 10
---

# Prognoza baterii

Centralny moduł GbbOptimizer. Analizuje {{< glossary "SOC" >}} baterii na najbliższe 24h (lub więcej) w oparciu o ładowanie z PV, ładowanie z sieci, rozładowanie i zużycie przez dom. Zawiera optymalizator, który automatycznie dobiera parametry ładowania i rozładowania.

W tym module możesz:
- Analizować prognozę SOC baterii na najbliższe 24h
- Zobaczyć, kiedy SOC przekracza minimalne lub maksymalne wartości
- Optymalizować plany ładowania i rozładowania
- Podglądać ceny zakupu i sprzedaży oraz zyski

## Kolumny tabeli prognozy

Tabela pokazuje dane na najbliższe 24h. Skróty: **DC** = prąd stały, **AC** = prąd zmienny.

### Bateria

| Kolumna | Opis |
|---------|------|
| Dzień | Dzień |
| Godzina | Godzina w danym dniu |
| Pocz bateria % (kWh) AC/DC | SOC i kWh baterii na początku godziny (w AC i DC) |
| Prognoza PV (kWh AC) | Prognoza produkcji PV w tej godzinie |
| Prognoza PV % (kWh DC) | Ile kWh z PV trafia do baterii (po konwersji na DC), po odjęciu zużycia domu |
| Zużycie +Extra (kWh AC) | Prognoza zużycia domu (wliczając Extra Zużycie) |
| Zużycie +Extra % (kWh DC) | Ile kWh pobrane z baterii na pokrycie zużycia minus PV |
| Ładowanie z sieci (kWh AC) | Ile pobrane z sieci do naładowania baterii |
| Ładowanie z sieci % (kWh DC) | Jak wyżej, po konwersji na DC |
| Rozładowanie | Status Planu Rozładowania na tę godzinę |
| Rozładowanie (kWh AC) | Ile wysłane z baterii do sieci (w AC) |
| Rozładowanie % (kWh DC) | Ile wysłane z baterii do sieci (w DC) |
| Koniec baterii (kWh AC) | kWh w baterii na koniec godziny. **= Pocz AC + PV AC - Zużycie AC + Ładowanie AC - Rozładowanie AC** |
| Koniec baterii % (kWh DC) | SOC i kWh na koniec godziny. **= Pocz DC + PV DC - Zużycie DC + Ładowanie DC - Rozładowanie DC** |
| Poniżej Min | „Tak" = koniec baterii może zejść poniżej {{< glossary "MinSOC" >}} |
| Powyżej Max | „Tak" = koniec baterii może przekroczyć {{< glossary "MaxSOC" >}} |

### Zysk

| Kolumna | Opis |
|---------|------|
| Kwota zysku | **= Kwota zużycia - (Kwota zakupu - Zmiana wartości baterii) + Kwota sprzedaży - Kwota kosztu baterii** |
| Nie zapłacona kwota za energię | **= Kwota sprzedaży - (Kwota zakupu - Zmiana wartości baterii) - Kwota kosztu baterii** |
| Kwota kosztu baterii | „Koszt używania baterii za kWh" × „Ładowanie baterii kWh" — amortyzacja baterii |
| Z sieci (kWh) | Ile pobrane z sieci w tej godzinie |
| Cena zakupu | Cena zakupu energii |
| Kwota zakupu | Z sieci × Cena zakupu |
| Do sieci (kWh) | Ile wysłane do sieci |
| Cena sprzedaży | Cena sprzedaży energii |
| Kwota sprzedaży | Do sieci × Cena sprzedaży |
| Zużycie (kWh) | Zużycie domu |
| Cena zużycia | Cena energii zużytej przez dom |
| Kwota zużycia | Zużycie × Cena zużycia |

### Wartość energii w baterii

| Kolumna | Opis |
|---------|------|
| Ładowanie baterii (kWh) | >0 ładowanie, <0 rozładowanie — ile energii poszło do/z baterii |
| Ładowanie z sieci (kWh) | Ile energii wysłanej do baterii pochodzi z sieci |
| Rozładowanie (kWh) | Ile energii pobrane z baterii |
| Pocz. kWh w baterii | Energia w baterii na początku godziny (ponad MinSOC%) |
| Wartość pocz. (PLN) | Wartość energii w baterii na początku godziny |
| Końcowe kWh w baterii | Energia w baterii na końcu godziny (ponad MinSOC%) |
| Wartość końcowa (PLN) | Wartość energii w baterii na końcu godziny |
| Zmiana wartości (PLN) | **= Wartość końcowa - Wartość początkowa.** Rozładowanie: Rozładowanie kWh × Średnia cena z poprzedniej godziny. Ładowanie: Ładowanie z sieci kWh × Cena zakupu |
| Średnia końcowa cena (PLN) | Wartość końcowa / Końcowe kWh w baterii |

## Optymalizator

Po kliknięciu **Uruchom Optymalizator teraz** program może zmienić:
- SOCLimit w module [Ładowanie]({{< relref "/konfiguracja/ladowanie" >}}) (i nawet zablokować ładowanie)
- MinSOC w Planie [Rozładowania]({{< relref "/konfiguracja/rozladowanie" >}})
- Wyłączyć DDBD (Dynamiczne Blokowanie Rozładowania Baterii)

### Optymalizator 1: Oparty o SOC

**„Ładowanie/Rozładowywanie jest optymalizowane na podstawie SOC (z dodatkowymi optymalizatorami)"**

Ten optymalizator próbuje:
- Dojść do 100% (lub {{< glossary "MaxSOC" >}}) w jakimś momencie (ale nie za długo)
- Utrzymać baterię powyżej {{< glossary "MinSOC" >}} — co jest ważniejsze
- Wykorzystuje ustawione momenty ładowania i rozładowania (trzeba je wcześniej ręcznie ustawić)

> [!NOTE]
> - Może być łączony z {{< glossary "Dynamic Discharge" >}} i Dynamic Charge
> - Może ładować baterię w nocy (tania taryfa) tak, aby zostało miejsce na PV w ciągu dnia
> - Może rozładowywać baterię przy wysokich cenach tak, aby PV naładowało ją do MaxSOC
> - Jeśli cena zakupu < 0, ładowanie w tych godzinach jest ustawiane na MaxSOC

### Optymalizator 2: Oparty o ceny {{< badge "recommended" >}}

**„Ładowanie/Rozładowywanie jest optymalizowane na podstawie cen zakupu i sprzedaży (aby zwiększyć Zysk)"**

Próbuje maksymalizować sumę w kolumnie „Kwota zysku" — znajduje najlepszą kombinację ładowania/rozładowania w każdej godzinie.

> [!WARNING]
> Po optymalizacji nowe ustawienia **nie są automatycznie wysyłane** do instalacji. Sprawdź wyniki, a potem naciśnij **Wyślij nowe SOCLimit z Ładowania do Instalacji**.

> [!NOTE]
> - Powinien być uruchamiany co godzinę
> - Wymaga, aby import w module [Zyski]({{< relref "/konfiguracja/zyski" >}}) był uruchamiany co godzinę
> - Ładowanie, gdy energia nigdy nie jest zużywana (bo prognoza działa na 24h), jest „darmowe" — na końcu okresu często pojawia się nadmiarowe ładowanie. Poczekaj kilka godzin na lepszą prognozę
> - Każda włączona dodatkowa opcja obniża zyski!

## Parametry optymalizatora opartego o ceny

### SOC

| Parametr | Opis |
|----------|------|
| Wolę mieć więcej w baterii niż mniej | Strategia dla sytuacji, gdy różne ładowania dają ten sam zysk: **Poziom 0** — wolę nie ładować. **Poziom 1** — wolę ładować więcej. **Poziom 2** — wolę ładować więcej + wolę ładować niż nie ładować (dla taryfy G12w) |
| Maksymalny SOC baterii (%) | Optymalizator próbuje nie przekraczać tej wartości |
| Minimalny SOC baterii (%) | Optymalizator próbuje nie schodzić poniżej tej wartości |
| Zwiększ Min/Max SOC o X jeżeli Prognoza PV < Y | Zwiększ rezerwę w bateriach, gdy prognoza PV jest niska |
| Wymuszaj codziennie MaxSOC (100%) — UPS | Raz dziennie przez 2–3h bateria jest ładowana do 100% |
| ... tylko podczas optymalizacji od północy do wschodu słońca | Wymuszanie obliczane tylko w nocy — jeśli prognoza pogody spadnie, program nie próbuje na siłę dobić do 100% w ciągu dnia |
| ... zamień zachód słońca na stałą godzinę | Np. godzina końca taniej taryfy zamiast zachodu słońca |

### Balansowanie baterii

| Parametr | Opis |
|----------|------|
| Minimalny SOC aby uznać za balansowanie | SOC, od którego program uznaje, że trwa balansowanie. Jeśli SOC spada nieznacznie — wpisz niższą wartość |
| Musi trwać co najmniej (godzin) | Czas trwania balansowania |
| Lista dni w miesiącu do 3h×100% | Wymuszaj balansowanie w te dni miesiąca (oddzielone przecinkiem) |
| Ile dni wstecz sprawdzać 3h×100% | Blokada zbyt częstego balansowania |
| Po ilu dniach ponownie trzymać 3h×100% | Alternatywne wymuszanie: co X dni od poprzedniego |
| Ręcznie wymuś 3h×100% dzisiaj | Jednorazowe wymuszenie, wyłącza się po balansowaniu |
| 3h×100% jeżeli cena < ... przez co najmniej ... godzin | Wymuszaj balansowanie przy niskiej cenie zakupu |

### Ładowanie i rozładowanie

| Parametr | Opis |
|----------|------|
| Ładowanie baterii z sieci | Pozwala wyłączyć ładowanie z sieci |
| Rozładowywanie baterii do sieci | Pozwala wyłączyć rozładowanie (lub zostawić ustawienia z Planu Rozładowania) |
| Min różnica cen dla rozładowania do sieci | Minimalna różnica między ceną energii w baterii a ceną sprzedaży. Wartość 0 = program nie rozładowuje ze stratą |
| Nie rozładowuj gdy cena sprzedaży < X | Blokuje rozładowanie przy niskiej cenie sprzedaży |
| Nie rozładowuj gdy cena zakupu < X | Blokuje rozładowanie — idea: w taniej taryfie bierz z sieci, baterię ładuj z PV, rozładowuj przy drogiej taryfie |
| Nie ładuj z sieci gdy cena zakupu > X | Blokuje ładowanie przy zbyt wysokiej cenie |

### Import / eksport z sieci

| Parametr | Opis |
|----------|------|
| Próbuj nie importować z sieci | Optymalizator unika pobierania z sieci (ale może się zdarzyć). Aby całkowicie zablokować — zaznacz „Zablokowany" w module [Ładowanie]({{< relref "/konfiguracja/ladowanie" >}}) |
| Próbuj nie eksportować do sieci | Optymalizator unika eksportu (z PV i baterii) |
| Nie sprzedawaj więcej niż nie-skorygowana prognoza PV z 24h | *(Opcja dla PL)* Blokuje sprzedaż więcej z baterii niż wyprodukowano z PV. Koszt obliczeniowy: O(n) |
| Próbuj nie eksportować gdy cena sprzedaży < 0 | Unikaj eksportu przy ujemnych cenach |

### Inne parametry

| Parametr | Opis |
|----------|------|
| Zablokuj wejście powyżej MaxSOC | Wymusza rozładowanie do MaxSOC |
| Zablokuj zejście poniżej MinSOC | Wymusza ładowanie do MinSOC |
| Nie ładuj z sieci gdy EV będzie ładowany | W czasie ładowania EV — brak ładowania baterii z sieci |
| Nie rozładowuj gdy EV będzie ładowany | W czasie ładowania EV — brak rozładowania baterii |
| Co 5 min testuj ładowanie EV | Auto-wykrywanie ładowania EV i wyłączanie ładowania/rozładowania baterii. Nie trzeba wpisywać z wyprzedzeniem |
| Próbuj prognozować > 24h | Optymalizator bierze pod uwagę więcej godzin (do końca znanych cen). Może się wyłączyć, jeśli trwa za długo |
| Nie cofaj się do prognozy „nic nie rób" | Wyłącza sprawdzanie, czy wymyślona prognoza nie jest gorsza od „nic nie rób" |
| Licz koszt energii w momencie ładowania | Normalnie koszt jest rozliczany w momencie zużycia. Ta opcja rozlicza w momencie zakupu |
| Min/Max SOC na końcu prognozy | Wymuszenie poziomu SOC na koniec prognozy |
| Koszt używania baterii za kWh | = Koszt zakupu baterii / (ilość cykli × pojemność kWh). Zalecamy zostawić puste |

## Harmonogram uruchamiania

| Przedziały czasowe | Optymalizator | Eksport do falownika |
|-------------------|---------------|----------------------|
| 24 (60 min) | po x:00 | po x:00 (powtórzenie przy błędzie) |
| 48 (30 min) | po x:00 i x:30 | po x:00 i x:30 (powtórzenie przy błędzie) |
| 96 (15 min) | po x:00 i x:30 | po x:00, x:15, x:30, x:45 |

## Testowanie scenariuszy

Aby testować różne scenariusze:
- Stwórz więcej niż jeden [Profil Zużycia]({{< relref "/konfiguracja/profile-zuzycia" >}})
- Stwórz więcej niż jeden Plan Rozładowania
- Tymczasowo wyłącz prognozę PV (najgorszy scenariusz)
- W module Ładowanie ustaw „Nowy początek", „Nowy Czas Trwania" i „Nowy SOCLimit" bez wysyłania do instalacji

W sekcji **Filtry** wybierz aktualny Profil Zużycia, Plan Rozładowania i opcjonalnie wyłącz prognozę PV.

## Zadania godzinowe

Gdy ręczna optymalizacja działa poprawnie — ustaw godziny automatycznego uruchamiania.

Najlepsza godzina (dla optymalizatora SOC): początkowe godziny aktywnych ładowań. Jeśli używasz Planu Rozładowania — najlepiej co godzinę.

Aby uruchomić:
1. Zaznacz **Automatycznie naciskaj: „Pobierz wszystkie dane" i „Uruchom Optymalizator"**
2. Zaznacz **... i „Wyślij nowe SOCLimit do Instalacji"**
3. Dodaj jedną lub więcej godzin

### Dodatkowe opcje

| Opcja | Opis |
|-------|------|
| Uruchom także w połowie godziny | Dla 24 przedziałów (60 min): dodatkowe uruchomienie o x:30. Nie rekomendowane |
| Wysyłaj dane do falownika wcześniej | Najpierw wyślij ustawienia (obliczone godzinę wcześniej), potem uruchom optymalizator, potem wyślij nowe ustawienia. Przydatne, gdy optymalizator trwa 4–5 min. Dla 96 przedziałów: zawsze włączone |
| Pobierz Prognozę PV tylko podczas Zadań Godzinowych | Prognoza PV importowana tylko przy zadaniach godzinowych (nie przy „Pobierz wszystkie dane"). Pozwala zobaczyć ostatnią prognozę użytą w optymalizacji |
