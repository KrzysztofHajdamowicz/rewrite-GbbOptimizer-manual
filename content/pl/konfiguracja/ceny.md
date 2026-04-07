---
title: "Ceny"
weight: 40
translationKey: "ceny"
---

# Ceny

Moduł konfiguracji cen zakupu i sprzedaży energii. Źródła danych cen ustawia się w [parametrach instalacji]({{< relref "/instalacja/parametry-instalacji" >}}), pozostałe parametry — tutaj.

## Cena zakupu

**Wzór:**

```
Cena Zakupu = (Cena zaimportowana × Mnożnik + Cena przesyłu + Koszt Transportu) × VAT/100
              + (Koszty miesięczne / ilość godzin w miesiącu)
```

| Składnik | Opis |
|----------|------|
| Cena zaimportowana | **Stałe** → 0. **Zależna od zaimportowanych cen i kosztów transportu** → cena ze źródła wskazanego w parametrach instalacji. **Zależna od cen sprzedaży** → Cena Sprzedaży |
| Mnożnik | „Zaimportowane Ceny Zakupu pomnóż przez" |
| Cena przesyłu | Cena ze źródła wskazanego w parametrach instalacji (pozycja „Przesył: Taryfa dla cen przesyłu"). 0 jeśli nie wskazano |
| Koszt Transportu | Cena z tablicy pod przyciskiem „Zmień Koszty Transportu / stałe Ceny Zakupu" |
| Koszty miesięczne | Suma stałych kosztów zakupu — rozbita równo na wszystkie godziny w miesiącu |

## Cena sprzedaży

**Wzór:**

```
Cena Sprzedaży = (Cena zaimportowana × Mnożnik + Dodatkowe opłaty) × VAT/100
                 × MnożnikSprzed2 × DziennyProcent
```

| Składnik | Opis |
|----------|------|
| Cena zaimportowana | Jeśli zaznaczono „Jest tylko jedna, stała Cena Sprzedaży" → stała wartość. W przeciwnym razie → cena ze źródła wskazanego w parametrach instalacji |
| Mnożnik | „Zaimportowane Ceny Sprzedaży pomnóż przez" |
| Dodatkowa opłata | Tablica pod przyciskiem „Zmień dodatkowe opłaty dla Cen Sprzedaży" |
| MnożnikSprzed2 | Tablica pod przyciskiem „Zmień dodatkowy mnożnik2 dla Cen Sprzedaży" |
| DziennyProcent | 1 + Procent/100 od wschodu do zachodu słońca (jeśli włączony) |
