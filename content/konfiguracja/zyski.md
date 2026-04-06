---
title: "Zyski"
weight: 80
---

# Zyski

Moduł zbiera dane z instalacji i oblicza zyski z fotowoltaiki. Importuj dane ręcznie przynajmniej raz dziennie lub zaznacz **Automatycznie importuj dane z Instalacji**.

Dane wyświetlane są wg godzin, dni lub miesięcy:
- Dane godzinowe — przechowywane przez **2 miesiące**
- Dane dzienne — przechowywane przez **2 lata**
- Dane miesięczne — przechowywane **na zawsze**

## Kolumny — Zysk

| Kolumna | Opis |
|---------|------|
| Dzień / Godzina | Dzień i godzina |
| Wartość zysku | **= Wartość Zużycia - Wartość Inwertera - (Wartość Zakupu - Zmiana Wartości baterii) + Wartość Sprzedaży** |
| Zysk / Zużycie | KPI: Wartość zysku / Zużycie kWh |
| Profit / Solar | KPI: Wartość zysku / PV kWh |
| Koszt energii | Wartość Zakupu - Wartość Sprzedaży |
| Z sieci (kWh) | Ile pobrano z sieci |
| Z sieci zbilansowane (kWh) | Pobrano po bilansowaniu godzinowym (dla Polski) |
| Cena Zakupu | Cena zakupu energii |
| Wartość Zakupu | Z sieci [zbilansowane] × Cena Zakupu + Koszt Miesięczny |
| Zakup / Produkcja | KPI: Wartość Zakupu / Wartość Zużycia |
| (Zakup - Sprzedaż) / Produkcja | KPI: ile procent rachunku za energię zapłacisz |
| Do sieci (kWh) | Ile wysłano do sieci |
| Do sieci zbilansowane (kWh) | Wysłano po bilansowaniu godzinowym (dla Polski) |
| Cena Sprzedaży | Cena sprzedaży energii |
| Wartość Sprzedaży | Do sieci [zbilansowane] × Cena Sprzedaży |
| Zużycie (kWh) | Zużycie prądu przez dom |
| Cena Zużycia | Cena energii zużytej przez dom (wliczając falownik) |
| Wartość Zużycia | Zużycie kWh × Cena Zużycia |
| Zużycie Inwertera (kWh) | Zużycie prądu przez falownik |
| Wartość Inwerter | Zużycie Inwertera kWh × Cena Zużycia |
| Autokonsumpcja | KPI: 1 - (Do sieci kWh / PV kWh) — ile energii z PV nie idzie do sieci |
| Samowystarczalność | KPI: PV / Zużycie — ile % energii z PV pokrywa zużycie |
| {{< glossary "RTE" >}} | KPI: Do sieci kWh / (Z sieci kWh + PV kWh - Zużycie kWh) |
| PV (kWh) | Produkcja PV |
| Do baterii (kWh) | Energia wysłana do baterii (przed konwersją na DC) |
| min/max/śred SOC (%) | Minimalny, maksymalny i średni SOC baterii |

## Kolumny — Wartość energii w baterii

| Kolumna | Opis |
|---------|------|
| Pocz. SOC (%) | Początkowy SOC (obliczany z MinSOC i MaxSOC, jeśli instalacja nie podaje) |
| Koń SOC (%) | Końcowy SOC |
| Zmiana Baterii (kWh) | >0 ładowanie, <0 rozładowanie — wyliczone z KońSOC - PoczSOC |
| Ładowanie z sieci (kWh) | Energia użyta do ładowania z sieci (po stronie AC) |
| Ładowanie z PV (kWh) | Energia użyta do ładowania z PV (po stronie AC) |
| Straty na ładowaniu (kWh) | Różnica między DC a AC podczas ładowania |
| Wydajność ładowania (%) | 1 - Straty / (Ładowanie z sieci + z PV) |
| Rozładowanie do sieci (kWh) | Energia z baterii do sieci (AC) |
| Rozładowanie do zużycia (kWh) | Energia z baterii do domu (AC) |
| Straty na rozładowaniu (kWh) | Różnica DC/AC podczas rozładowania |
| Wydajność rozładowania (%) | 1 - Straty / (Rozładowanie do sieci + do zużycia) |
| Pocz / Koń kWh w baterii | Energia w baterii ponad MinSOC |
| Pocz / Koń Wartość (PLN) | Wartość energii w baterii |
| Zmiana Wartości baterii (PLN) | Rozładowanie: kWh × Średnia cena (poprzednia godzina). Ładowanie: kWh × Cena Zakupu |
| Średnia koń cena (PLN) | Koń Wartość / Koń kWh w baterii |
| MinSOC (%) | Zapamiętana wartość „Minimalna SOC baterii %" z parametrów instalacji |

## Kolumny — Extra Zużycie

| Kolumna | Opis |
|---------|------|
| Cena Extra Zużycia (PLN) | Średnia cena kWh: średnia z 0 (PV), Średniej ceny baterii i Ceny Zakupu (w proporcjach użycia) |
| Samochód elektryczny (kWh / PLN) | Energia i wartość ładowania EV |
| Pompa ciepła (kWh / PLN) | Energia i wartość pompy ciepła |
| Inne1 (kWh / PLN) | Energia i wartość „Inne1" |
| Inne2 (kWh / PLN) | Energia i wartość „Inne2" |
