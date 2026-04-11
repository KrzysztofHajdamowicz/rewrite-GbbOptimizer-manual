---
title: "GbbConnect2 Addon"
weight: 15
translationKey: "gbbconnect2-addon"
---

# GbbConnect2 — addon Home Assistant

{{< glossary "GbbConnect2" >}} jest dostępny jako **addon Home Assistant**, co pozwala uruchomić go bezpośrednio w HA bez potrzeby osobnego komputera z Windows czy kontenera Docker.

Addon uruchamia aplikację GbbConnect2Console i łączy falownik z GbbOptimizer przez {{< glossary "ModbusInMqtt" >}}.

## Wymagania

- **Home Assistant OS** lub **Home Assistant Supervised** (wymagany Supervisor)
- Aktywne konto w GbbOptimizer z instalacją typu **GbbConnect2**
- Falownik hybrydowy z dataloggerem (WiFi lub Ethernet)
- **Stały adres IP** dataloggera w sieci lokalnej

## Instalacja

### 1. Dodaj repozytorium

Kliknij poniższy przycisk, aby automatycznie dodać repozytorium do Home Assistant:

[![Dodaj repozytorium do Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FKrzysztofHajdamowicz%2Fgbbconnect2-ha-addon)

Lub ręcznie:

1. W Home Assistant przejdź do **Ustawienia** -> **Dodatki** -> **Sklep z dodatkami**
2. Kliknij menu (⋮) w prawym górnym rogu -> **Repozytoria**
3. Dodaj URL repozytorium:
   ```
   https://github.com/KrzysztofHajdamowicz/gbbconnect2-ha-addon
   ```
4. Kliknij **Dodaj**

### 2. Zainstaluj addon

1. W Sklepie z dodatkami wyszukaj **GbbConnect2**
2. Kliknij **Zainstaluj**
3. Poczekaj na zakończenie instalacji

## Konfiguracja

Przed uruchomieniem addonu przygotuj dane z GbbOptimizer — patrz [konfiguracja GbbConnect2]({{< relref "/instalacja/metody-polaczenia/gbbconnect2" >}}) (kroki 2–5).

W zakładce **Konfiguracja** addonu wypełnij pola:

| Pole | Opis |
|------|------|
| `plant_name` | Nazwa instalacji (jak w GbbOptimizer) |
| `plant_driver_no` | Typ drivera: `0` = SolarmanV5 (WiFi), `1` = ModBusTCP (Ethernet) |
| `plant_address_ip` | Adres IP dataloggera w sieci lokalnej |
| `plant_port_no` | Port dataloggera (zwykle `8899`) |
| `plant_serial_number` | Numer seryjny **dataloggera** (nie falownika!) |
| `gbboptimizer_plant_id` | {{< glossary "PlantId" >}} z GbbOptimizer |
| `gbboptimizer_plant_token` | {{< glossary "PlantToken" >}} z GbbOptimizer |
| `gbboptimizer_mqtt_address` | Adres serwera MQTT — patrz [Serwery MQTT]({{< relref "/referencje/serwery-mqtt" >}}) |
| `gbboptimizer_mqtt_port` | Port MQTT (zwykle `8883`) |
| `server_autostart` | Automatyczny start serwera (zalecane: `true`) |

> [!WARNING]
> Datalogger **musi mieć stały adres IP** w sieci lokalnej. Ustaw rezerwację DHCP na routerze.

> [!NOTE]
> Numer seryjny to numer **dataloggera**, nie falownika. Typowe formaty: 17xxxxxxx, 21xxxxxxx, 40xxxxxxx. Możesz go znaleźć za pomocą wersji Windows GbbConnect2 (funkcja **Search for Inverters**).

## Uruchomienie

1. Przejdź do zakładki **Informacje** addonu
2. Kliknij **Uruchom**
3. Sprawdź zakładkę **Logi** — poczekaj na komunikat o nawiązaniu połączenia
4. W GbbOptimizer zweryfikuj, czy dane z falownika są odbierane

> [!NOTE]
> Addon powinien działać **24/7**, aby GbbOptimizer mógł zbierać dane i wysyłać polecenia do falownika.

## Rozwiązywanie problemów

- **Brak połączenia z falownikiem** — sprawdź adres IP, port i numer seryjny dataloggera. Upewnij się, że HA ma dostęp do dataloggera w sieci.
- **Brak połączenia z MQTT** — zweryfikuj {{< glossary "PlantId" >}}, {{< glossary "PlantToken" >}} i adres serwera MQTT. Sprawdź, czy port 8883 nie jest blokowany przez firewall.
- **Błąd autoryzacji** — wygeneruj nowy token w GbbOptimizer i zaktualizuj konfigurację addonu.

Włącz opcje `is_verbose_log`, `is_driver_log` i `is_driver_log2` w konfiguracji, aby uzyskać szczegółowe logi diagnostyczne.
