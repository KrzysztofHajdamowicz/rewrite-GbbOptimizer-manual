---
title: "GbbConnect2"
weight: 30
translationKey: "gbbconnect2"
---

# GbbConnect2

{{< glossary "GbbConnect2" >}} is software die in het lokale netwerk draait en de omvormer rechtstreeks met GbbOptimizer verbindt via {{< glossary "ModbusInMqtt" >}}, waarbij de cloud-servers worden omzeild.

## Vereisten

- Een computer met **Windows** of een **Docker**-container die 24/7 in het lokale netwerk draait
- Een hybride **Deye**-omvormer met WiFi-logger (dongle)
- Een vast IP-adres voor de logger in het lokale netwerk

## Stap-voor-stap configuratie

1. Download en installeer GbbConnect2: [github.com/gbbsoft/GbbConnect2](https://github.com/gbbsoft/GbbConnect2)
2. Maak in GbbOptimizer een nieuwe installatie van het type **GbbConnect2** (of wijzig het type van een bestaande installatie)
3. Vul de installatienaam in, controleer de overige velden en klik op **Opslaan**
4. Klik op **Bewerken** en vervolgens op **Nieuw token genereren**
5. Noteer het {{< glossary "PlantId" >}} en {{< glossary "PlantToken" >}}
6. In GbbConnect2: maak een nieuwe Plant aan met een naam en type „SolarmanV2"
7. Klik in het tabblad **Test and Log** op **Search for Inverters** om het IP en SerialNumber van de omvormer te vinden
8. Voer in het tabblad **Plants** het **IP address** en **SerialNumber** van de logger in

   > [!WARNING]
   > De logger onder de omvormer **moet een vast IP-adres** hebben in het lokale netwerk. Stel een DHCP-reservering in op de router.

9. Voer in de sectie **GbbOptimizer** het {{< glossary "PlantId" >}} en {{< glossary "PlantToken" >}} in
10. Voer het adres van de MQTT-server in — zie [MQTT-servers]({{< relref "/references/mqtt-servers" >}})
11. Vink in het tabblad **Parameters** „Start server after program starts" aan, zodat de communicatie automatisch start
12. Klik op **StartServer**

## Docker-versie

Er bestaat een **GbbConnect2Console**-versie voor Docker:

1. Begin met de **Windows**-versie — test de verbinding en maak een configuratiebestand aan
2. Stap over naar de **Docker**-versie met hetzelfde configuratiebestand

> [!NOTE]
> Het programma moet **24/7** draaien om statistische gegevens uit de omvormer te verzamelen en commando's van GbbOptimizer uit te voeren.
