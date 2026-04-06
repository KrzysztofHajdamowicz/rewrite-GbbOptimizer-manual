---
title: "GBB Shunt"
weight: 20
---

# GBB Shunt

GBB Shunt to modul GbbOptimizer przeznaczony do instalacji z bateriami olowianymi (kwasowymi, zelowymi, AGM).

## Czym jest GBB Shunt?

W instalacjach z bateriami olowianymi standardowy pomiar {{< glossary "SOC" >}} przez falownik moze byc niedokladny. GBB Shunt pozwala na dokladniejsze sledzenie stanu naladowania baterii na podstawie pomiaru pradu przez bocznik (shunt).

## Kluczowe funkcje

- **Dokladny pomiar SOC** — na podstawie pomiaru pradu (kulomierz), a nie napiecia
- **Kompensacja temperatury** — uwzglednia wplyw temperatury na pojemnosc baterii olowianej
- **Ochrona baterii** — zapobiega glebokim rozladowaniom, ktore skracaja zywotnosc baterii olowianych

## Kiedy uzywac?

GBB Shunt jest zalecany, jesli:

- Uzywasz baterii olowianych (nie litowych)
- Falownik nie ma dokladnego pomiaru SOC dla baterii olowianych
- Chcesz wydluzyc zywotnosc baterii przez precyzyjne sterowanie cyklami

> [!NOTE]
> Baterie litowe (LiFePO4, Li-ion) z BMS maja wbudowany dokladny pomiar SOC i nie wymagaja modulu GBB Shunt.

## Konfiguracja

Modul GBB Shunt konfiguruje sie w ustawieniach instalacji w sekcji zaawansowanej. Wymaga podania:

- Pojemnosci baterii (Ah)
- Napiecia nominalnego
- Parametrow bocznika (shunt)
