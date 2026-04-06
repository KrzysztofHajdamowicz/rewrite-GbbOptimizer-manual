---
title: "Profile zużycia"
weight: 50
translationKey: "profile-zuzycia"
---

# Profile zużycia

Moduł prognozowania zużycia energii przez dom. Zużycie jest podzielone na godziny i dni tygodnia.

## Ręczne wprowadzanie

Wpisz kWh dla każdej godziny i dnia tygodnia bezpośrednio w tabeli.

## Import danych z instalacji

Ustaw okres importu i naciśnij **Importuj z Instalacji**. Program oblicza średnie zużycie dla każdej godziny i dnia tygodnia na podstawie danych z falownika.

### Automatyczny import

Zaznacz **Automatycznie importuj dane w nocy** — program co noc importuje dane z ostatnich 28 dni.

## Import ręczny z Excela

1. W Excelu przygotuj dane: godziny w wierszach, dni tygodnia w kolumnach
2. Skopiuj dane (Ctrl+C)
3. Wklej w polu „Twój profil"
4. Wybierz separator kolumn i separator dziesiętny
5. Naciśnij **Importuj**

> [!NOTE]
> - Pusta komórka = program nie zmienia danych w tym miejscu
> - Możesz wkleić mniej niż 24 wiersze lub 7 kolumn — brakujące godziny/dni nie będą zmienione
> - Nadmiarowe kolumny i wiersze są pomijane

## Wiele profili

Możesz zdefiniować wiele profili zużycia. Wybrany profil jest używany w [Prognozie baterii]({{< relref "/konfiguracja/prognoza-baterii" >}}) do wyświetlania danych, wykresów i optymalizacji.

## Ograniczenie okresu importu

W edycji profilu możesz ustawić:
- **Od miesiąca / Od dnia** — ogranicza dzień rozpoczęcia importu danych
- **Do miesiąca / Do dnia** — ogranicza dzień zakończenia importu

Przydatne np. dla **profilu wakacyjnego**, gdzie import powinien wykorzystywać dane tylko z okresu wakacji.

Jeśli „Od dnia" jest puste — program użyje pierwszego dnia miesiąca. Jeśli „Do dnia" jest puste — użyje ostatniego dnia.

## Automatyczna zmiana profilu

Aby automatycznie przełączać profile:

1. Zdefiniuj co najmniej dwa profile z wypełnionym polem „Od miesiąca" (i opcjonalnie „Od dnia"), pustym „Do miesiąca"
2. Zaznacz **Automatycznie zmieniaj profil na podstawie pól „Od miesiąca/Dnia"**

> [!NOTE]
> To również ogranicza okres importu danych z instalacji!

## Automatyczny profil wakacyjny

Zdefiniuj profil z wypełnionymi polami **zarówno** „Od miesiąca/dnia" jak i „Do miesiąca/dnia". Program:
- Włączy profil wakacyjny w dniu rozpoczęcia
- Powróci do normalnego profilu dzień po zakończeniu
