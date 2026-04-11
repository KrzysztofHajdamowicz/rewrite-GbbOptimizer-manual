---
title: "Veelvoorkomende fouten"
weight: 60
translationKey: "najczestsze-bledy"
---

# Veelvoorkomende fouten

Lijst van de meest voorkomende foutmeldingen in GbbOptimizer, hun bronnen en mogelijke oplossingen.

## Solarman

| Melding | Beschrijving |
|-----------|------|
| `SolarmanError: Solarman timeout!` | Solarman kan geen gegevens naar de omvormer sturen. Controleer het lokale netwerk. |
| `Solarman error: 2101040-device not found` | De omvormer stuurt geen gegevens naar Solarman. Controleer de netwerkverbinding van de omvormer. |
| `Response status code: 503 / 500 / 504` | De Solarman-API werkt niet correct. Probleem aan de kant van Solarman — wacht even en probeer het opnieuw. |

## DeyeCloud

| Melding | Beschrijving |
|-----------|------|
| `DeyeCloud error: timeout` | DeyeCloud kan geen gegevens naar de omvormer sturen. Controleer het lokale netwerk. |
| `DeyeCloud error: 2104006-device offline` | De omvormer stuurt geen gegevens naar DeyeCloud. Controleer de netwerkverbinding van de omvormer. |
| `DeyeCloud error: 2101042-auth no operation permission` | Te weinig rechten voor het DeyeCloud-account (bijv. een door de installateur aangemaakt account). Neem contact op met de installateur om volledige rechten te krijgen. |

## GbbConnect2

| Melding | Beschrijving |
|-----------|------|
| `Mqtt to GbbConnect2: timeout!` | GbbOptimizer kan geen verbinding maken met de lokale {{< glossary "GbbConnect2" >}}. Controleer of GbbConnect2 draait. |
| `GbbConnect2Error: Connection timed out 192.168.x.xx:8899` | {{< glossary "GbbConnect2" >}} kan geen verbinding maken met de Deye-dongle. Controleer of de dongle in het netwerk zit. |

## Victron

| Melding | Beschrijving |
|-----------|------|
| `Victron Mqtt: timeout! (15 sec)` | GbbOptimizer kan geen verbinding maken met de Cerbo via de MQTT-servers van Victron. Controleer het lokale netwerk en externe toegang in {{< glossary "VRM" >}}. |
| `Error during checking whether Schedules reached Cerbo successfully` | ESS-schema's zijn niet bij de Cerbo aangekomen. Controleer de internetverbinding van de Cerbo. |

## Energieprijzen

| Melding | Bron | Beschrijving |
|-----------|--------|------|
| `Get Prices: The SSL connection could not be established` | ENTSO-E | De ENTSO-E-prijzen-API werkt niet. Probleem aan de kant van de provider. |
| `Get Prices: Proba polaczenia nie powiodla sie` | ENTSO-E | ENTSO-E-API niet beschikbaar. |
| `Get Prices: HTTP POST ... Gateway timeout / 502 Bad Gateway` | Tibber | De Tibber-prijzen-API werkt niet. |
| `Get Prices: Response status code: 502 (Bad Gateway)` | AU Amber | De Amber-prijzen-API werkt niet. |

## Overig

| Melding | Bron | Beschrijving |
|-----------|--------|------|
| `Solcast.com: Too many requests` | Solcast | Dagelijkse limiet van 10 verzoeken naar Solcast.com bereikt. Wacht tot middernacht. |
| `ERROR from Cache: Response status code: 500` | Pstryk | Fout aan de kant van de Pstryk-API. |
| `B0220-System function downgrade` | Hinen | De Hinen-API wordt bijgewerkt. Wacht tot de update is voltooid. |

> [!NOTE]
> Foutmeldingen worden per e-mail vanuit het programma verzonden. De meeste „timeout"- en „device offline"-fouten hangen samen met problemen in het lokale netwerk — controleer de verbinding tussen de omvormer en de router.
