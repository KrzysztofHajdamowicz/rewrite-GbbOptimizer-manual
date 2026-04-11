---
title: "DongleDirect"
weight: 40
translationKey: "dongle-direct"
---

# DongleDirect

{{< glossary "DongleDirect" >}} werkt vergelijkbaar met {{< glossary "GbbConnect2" >}} — het verbindt de omvormer met GbbOptimizer, maar **zonder extra software** in het lokale netwerk. De dongle (WiFi-logger) wordt rechtstreeks doorverwezen naar de GbbOptimizer-server.

> [!WARNING]
> Sinds 09-03-2026 is het wijzigen van dongle-instellingen op sommige modellen mogelijk niet meer mogelijk. In dat geval is een reset van de dongle en het herstellen van de oorspronkelijke instellingen vereist.

## Stap-voor-stap configuratie

1. Onthoud de naam van de GbbOptimizer-server uit het browseradres (bijv. `gbboptimizer5.gbbsoft.pl`)
2. Log in op de dongle — je moet het IP-adres ervan in het lokale netwerk kennen (login: `admin`, wachtwoord: `admin`)
3. Ga naar de pagina `http://<ip_van_de_dongle>/config_hide.html` (wijzig het adres handmatig in de browser)
4. **Maak screenshots** van alle huidige instellingen (voor het geval je ze moet herstellen!)
5. Wijzig **Server A Setting**:
   - Verwijder het IP-adres
   - Onthoud de oorspronkelijke domeinnaam van Server A
   - Wijzig het domein naar de naam van de GbbOptimizer-server (bijv. `gbboptimizer10.gbbsoft.pl`)
   - Poort: `10000`
   - Verbinding: `TCP`
   - **Save + Restart**
6. Wijzig **Optional Server Setting** naar dezelfde gegevens — **Save + Restart**
7. Wijzig in GbbOptimizer het type installatie naar **DongleDirect** (of maak een nieuwe aan)
8. Voer in de instellingen van de installatie in:
   - **Serienummer van de omvormer**
   - **Serienummer van de dongle** (alleen cijfers)
   - **De oorspronkelijke domeinnaam van Server A** — als dit veld leeg is, kopieert GbbOptimizer de gegevens niet naar Solarman en stopt Solarman/DeyeCloud met werken
9. Sla op en wacht **2-5 minuten** (de dongle verbindt na enkele minuten met de GbbOptimizer-server)
10. In het logboek zouden regels zoals deze moeten verschijnen:
    ```
    2025-06-21 11:00:27: From Dongle: A501001047F585579AF6A5005E15
    2025-06-21 11:00:28: From Server: A50A001017F685579AF6A50001AB745668780000008E15
    ```

## Dongle resetten

Als de oorspronkelijke dongle-instellingen hersteld moeten worden:

1. Zoek de reset-knop (een klein gaatje met de tekst „Reset" of „Reload") op de logger die in de omvormer is gestoken
2. Houd bij **ingeschakelde omvormer** de knop (bijv. met een paperclip) **5-10 seconden** ingedrukt
3. De leds op de logger zouden moeten doven en opnieuw gaan branden (of knipperen), wat op een herstart wijst
4. Open de **Solarman Smart**-app op je telefoon
5. Kies de optie **apparaat toevoegen** („Add now" of „Configure")
6. Voer de gegevens van je thuis-WiFi-router in

> [!NOTE]
> Als je de oorspronkelijke domeinnaam van Server A in de installatie-instellingen van GbbOptimizer invoert, worden de gegevens in beide richtingen naar Solarman gekopieerd — je behoudt dan de volledige functionaliteit van het Solarman/DeyeCloud-portaal.
