---
title: "GBB Shunt"
weight: 20
---

# GBB Shunt

GBB Shunt to moduł GbbOptimizer przeznaczony do instalacji z bateriami ołowiowymi (kwasowymi, żelowymi, AGM).

## Czym jest GBB Shunt?

W instalacjach z bateriami ołowiowymi standardowy pomiar {{< glossary "SOC" >}} przez falownik może być niedokładny. GBB Shunt pozwala na dokładniejsze śledzenie stanu naładowania baterii na podstawie pomiaru prądu przez bocznik (shunt).

## Kluczowe funkcje

- **Dokładny pomiar SOC** — na podstawie pomiaru prądu (kulomierz), a nie napięcia
- **Kompensacja temperatury** — uwzględnia wpływ temperatury na pojemność baterii ołowiowej
- **Ochrona baterii** — zapobiega głębokim rozładowaniom, które skracają żywotność baterii ołowiowych

## Kiedy używać?

GBB Shunt jest zalecany, jeśli:

- Używasz baterii ołowiowych (nie litowych)
- Falownik nie ma dokładnego pomiaru SOC dla baterii ołowiowych
- Chcesz wydłużyć żywotność baterii przez precyzyjne sterowanie cyklami

> [!NOTE]
> Baterie litowe (LiFePO4, Li-ion) z BMS mają wbudowany dokładny pomiar SOC i nie wymagają modułu GBB Shunt.

## Konfiguracja

Moduł GBB Shunt konfiguruje się w ustawieniach instalacji w sekcji zaawansowanej. Wymaga podania:

- Pojemności baterii (Ah)
- Napięcia nominalnego
- Parametrów bocznika (shunt)
