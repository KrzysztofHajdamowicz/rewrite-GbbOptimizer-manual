---
title: "Pompa ciepła / Klimatyzacja"
weight: 70
---

# Prognoza pompy ciepła / klimatyzacji

Moduł prognozowania zużycia pompy ciepła (PC) lub klimatyzacji na podstawie temperatury zewnętrznej.

## Dlaczego osobny moduł?

Pompy ciepła i klimatyzacja (podobnie jak ładowarki EV) nie działają zgodnie z rytmem dnia — zależą od temperatury. Dlatego lepiej je **wykluczyć ze średniej** w module [Profile zużycia]({{< relref "/konfiguracja/profile-zuzycia" >}}) i umieścić w [Extra Zużycie]({{< relref "/konfiguracja/dodatkowe-obciazenia-ev" >}}).

## Konfiguracja krok po kroku

1. Wpisz **szerokość i długość geograficzną** w [parametrach instalacji]({{< relref "/instalacja/parametry-instalacji" >}})
2. Zaimportuj prognozę pogody
3. Naciśnij **Parametry PC** i wpisz zużycie kWh pompy/klimatyzacji na każdą godzinę (minimum 2 wartości dla różnych temperatur)
4. Naciśnij **Policz prognozę PC** i sprawdź wyniki
5. Naciśnij **Eksportuj prognozę PC do modułu Extra Zużycie** (menu: Profile Zużycia → Extra Zużycia → Filtr: „Typ" = „Pompa Ciepła")
6. Włącz zadania godzinowe: **Importuj prognozę pogody**, **Oblicz prognozę PC**, **Eksportuj prognozę PC do modułu Extra Zużycie**

## Parametry PC — tabela temperatury vs. zużycie

Dla każdej godziny podaj, ile kWh zużywa PC/klimatyzacja przy danej temperaturze zewnętrznej.

Wskazówki:
- Możesz wypełnić tylko pierwszą kolumnę — **Narzędzie kopiowania** na dole pozwala kopiować dane między kolumnami
- Nie trzeba wypełniać wszystkich temperatur (od -20°C do +40°C). Wystarczą **minimum 2 wartości** — program automatycznie interpoluje resztę proporcjonalnie
- Im więcej danych, tym dokładniejsza prognoza
- Dane można uzupełniać w ciągu roku, w miarę zbierania obserwacji

> [!NOTE]
> Przykład: Wpisz zużycie tylko dla godzin i temperatur, które znasz — np. 10°C, 0°C i -5°C.
