---
title: "GbbConnect2 Addon"
weight: 15
translationKey: "gbbconnect2-addon"
---

# GbbConnect2 — Home Assistant Addon

{{< glossary "GbbConnect2" >}} is beschikbaar als **Home Assistant addon**, waarmee u het direct in HA kunt draaien zonder een aparte Windows-pc of Docker-container.

De addon draait de GbbConnect2Console-applicatie en verbindt de omvormer met GbbOptimizer via {{< glossary "ModbusInMqtt" >}}.

## Vereisten

- **Home Assistant OS** of **Home Assistant Supervised** (Supervisor vereist)
- Een actief GbbOptimizer-account met een installatie van het type **GbbConnect2**
- Een hybride omvormer met een datalogger (WiFi of Ethernet)
- Een **vast IP-adres** voor de datalogger in het lokale netwerk

## Installatie

### 1. Voeg de repository toe

Klik op de onderstaande knop om de repository automatisch toe te voegen aan Home Assistant:

[![Voeg repository toe aan Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FKrzysztofHajdamowicz%2Fgbbconnect2-ha-addon)

Of handmatig:

1. Ga in Home Assistant naar **Instellingen** -> **Add-ons** -> **Add-on Store**
2. Klik op het menu (⋮) in de rechterbovenhoek -> **Repositories**
3. Voeg de repository-URL toe:
   ```
   https://github.com/KrzysztofHajdamowicz/gbbconnect2-ha-addon
   ```
4. Klik op **Toevoegen**

### 2. Installeer de addon

1. Zoek in de Add-on Store naar **GbbConnect2**
2. Klik op **Installeren**
3. Wacht tot de installatie is voltooid

## Configuratie

Bereid vóór het starten van de addon de gegevens uit GbbOptimizer voor — zie [GbbConnect2-configuratie]({{< relref "/installation/connection-methods/gbbconnect2" >}}) (stappen 2–5).

Vul op het tabblad **Configuratie** van de addon de velden in:

| Veld | Beschrijving |
|------|--------------|
| `plant_name` | Installatienaam (zoals in GbbOptimizer) |
| `plant_driver_no` | Drivertype: `0` = SolarmanV5 (WiFi), `1` = ModBusTCP (Ethernet) |
| `plant_address_ip` | IP-adres van de datalogger in het lokale netwerk |
| `plant_port_no` | Poort van de datalogger (meestal `8899`) |
| `plant_serial_number` | Serienummer van de **datalogger** (niet de omvormer!) |
| `gbboptimizer_plant_id` | {{< glossary "PlantId" >}} uit GbbOptimizer |
| `gbboptimizer_plant_token` | {{< glossary "PlantToken" >}} uit GbbOptimizer |
| `gbboptimizer_mqtt_address` | MQTT-serveradres — zie [MQTT-servers]({{< relref "/references/mqtt-servers" >}}) |
| `gbboptimizer_mqtt_port` | MQTT-poort (meestal `8883`) |
| `server_autostart` | Automatische serverstart (aanbevolen: `true`) |

> [!WARNING]
> De datalogger **moet een vast IP-adres** hebben in het lokale netwerk. Stel een DHCP-reservering in op uw router.

> [!NOTE]
> Het serienummer is het serienummer van de **datalogger**, niet van de omvormer. Veelvoorkomende formaten: 17xxxxxxx, 21xxxxxxx, 40xxxxxxx. U kunt het vinden met de Windows-versie van GbbConnect2 (functie **Search for Inverters**).

## Opstarten

1. Ga naar het tabblad **Informatie** van de addon
2. Klik op **Starten**
3. Controleer het tabblad **Logboek** — wacht op een bericht dat de verbinding tot stand is gebracht
4. Controleer in GbbOptimizer of gegevens van de omvormer worden ontvangen

> [!NOTE]
> De addon moet **24/7** draaien zodat GbbOptimizer gegevens kan verzamelen en commando's naar de omvormer kan sturen.

## Probleemoplossing

- **Kan geen verbinding maken met de omvormer** — controleer het IP-adres, de poort en het serienummer van de datalogger. Zorg ervoor dat HA de datalogger in het netwerk kan bereiken.
- **Kan geen verbinding maken met MQTT** — controleer het {{< glossary "PlantId" >}}, {{< glossary "PlantToken" >}} en het MQTT-serveradres. Controleer of poort 8883 niet wordt geblokkeerd door een firewall.
- **Authenticatiefout** — genereer een nieuw token in GbbOptimizer en werk de addon-configuratie bij.

Schakel `is_verbose_log`, `is_driver_log` en `is_driver_log2` in de configuratie in voor gedetailleerde diagnostische logboeken.
