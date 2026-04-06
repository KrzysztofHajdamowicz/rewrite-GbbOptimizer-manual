---
title: "GbbConnect2"
weight: 30
---

# GbbConnect2

{{< glossary "GbbConnect2" >}} to oprogramowanie działające w sieci lokalnej, które łączy falownik bezpośrednio z GbbOptimizer przez {{< glossary "ModbusInMqtt" >}}, omijając serwery chmurowe.

## Wymagania

- Komputer z **Windows** lub kontener **Docker** działający 24/7 w sieci lokalnej
- Falownik hybrydowy **Deye** z loggerem (donglem) WiFi
- Stały adres IP loggera w sieci lokalnej

## Konfiguracja krok po kroku

1. Pobierz i zainstaluj GbbConnect2: [github.com/gbbsoft/GbbConnect2](https://github.com/gbbsoft/GbbConnect2)
2. W GbbOptimizer stwórz nową instalację typu **GbbConnect2** (lub zmień typ istniejącej)
3. Wpisz nazwę instalacji, przejrzyj pozostałe pola i **Zapisz**
4. Naciśnij **Popraw**, a następnie **Wygeneruj nowy Token**
5. Zapamiętaj {{< glossary "PlantId" >}} i {{< glossary "PlantToken" >}}
6. W GbbConnect2: stwórz nowy Plant z nazwą i typem „SolarmanV2"
7. W zakładce **Test and Log** naciśnij **Search for Inverters**, aby znaleźć IP i SerialNumber falownika
8. W zakładce **Plants** wprowadź **IP address** i **SerialNumber** loggera

   > [!WARNING]
   > Logger pod falownikiem **musi mieć stały adres IP** w sieci lokalnej. Ustaw rezerwację DHCP na routerze.

9. W sekcji **GbbOptimizer** wprowadź {{< glossary "PlantId" >}} i {{< glossary "PlantToken" >}}
10. Wprowadź adres serwera MQTT — patrz [Serwery MQTT]({{< relref "/referencje/serwery-mqtt" >}})
11. W zakładce **Parameters** zaznacz „Start server after program starts", aby komunikacja startowała automatycznie
12. Naciśnij **StartServer**

## Wersja Docker

Istnieje wersja **GbbConnect2Console** dla Dockera:

1. Zacznij od wersji **Windows** — przetestuj połączenie i stwórz plik konfiguracyjny
2. Przenieś się na wersję **Docker** z tym samym plikiem konfiguracyjnym

> [!NOTE]
> Program powinien działać **24/7**, aby zbierać dane statystyczne z falownika i wykonywać polecenia z GbbOptimizer.
