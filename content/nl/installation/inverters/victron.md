---
title: "Victron"
weight: 10
translationKey: "victron"
---

# Victron

{{< badge "victron-only" >}}

De configuratie van een Victron-omvormer met GbbOptimizer vereist een correcte instelling van het {{< glossary "ESS" >}}-systeem en het {{< glossary "VRM" >}}-portaal.

## Checklist

Controleer de volgende instellingen voordat je GbbOptimizer start:

1. **Installeer geen Beta-versies** van de firmware
2. **DESS moet uitgeschakeld zijn**
3. **Schedules** — de optie „Self-consumption above limit" moet worden ingesteld op **PV** (en niet op „PV & Battery"). Zo veroorzaken de schema's 's nachts geen ontlading van de batterij
4. **Battery Life** in {{< glossary "ESS" >}} moet **uitgeschakeld** zijn — kies de modus: `Optimized (without BatteryLife)`
5. **Log interval** (in VRM Online Portal) instellen op **1 min**
6. **VRM-rechten** — de gebruiker moet het recht **Full Control** hebben
7. **Herstart de Cerbo** na het doorvoeren van de wijzigingen

> [!WARNING]
> Onjuiste instellingen van Battery Life of Schedules kunnen onverwachte nachtelijke ontlading van de batterij veroorzaken.

## Victron-parameters in GbbOptimizer

Een gedetailleerde beschrijving van de Victron-parameters (VRM Portal Id, Installation Id, VRM Token enz.) vind je in het onderdeel [Installatieparameters]({{< relref "/installation/installation-parameters" >}}).

## MQTT-topics die door GbbOptimizer worden gewijzigd

GbbOptimizer wijzigt **uitsluitend** de onderstaande topics/properties in het Victron-systeem. De variabele `{i}` staat voor het schema-nummer (0-4).

### Laadschema's (Schedules)

| MQTT-topic | Property | Opmerkingen |
|------------|------------|-------|
| `settings/0/Settings/CGwacs/BatteryLife/Schedule/Charge/{i}/Day` | Schemadag | |
| `settings/0/Settings/CGwacs/BatteryLife/Schedule/Charge/{i}/Soc` | SOC-limiet | |
| `settings/0/Settings/CGwacs/BatteryLife/Schedule/Charge/{i}/Start` | Starttijd | |
| `settings/0/Settings/CGwacs/BatteryLife/Schedule/Charge/{i}/Duration` | Duur | |

### ESS en vermogenssturing

| MQTT-topic | Property | Opmerkingen |
|------------|------------|-------|
| `settings/0/Settings/CGwacs/BatteryLife/MinimumSocLimit` | {{< glossary "ESS" >}} / Minimum SOC | |
| `settings/0/Settings/CGwacs/AcPowerSetPoint` | {{< glossary "ESS" >}} / {{< glossary "GridSetpoint" >}} | |
| `settings/0/Settings/SystemSetup/MaxChargeCurrent` | DVCC / Maximale laadstroom | |
| `vebus/{257 or other}/Ac/ActiveIn/CurrentLimit` | MultiPlus / Ingangsstroomlimiet | |

### Sturing bij negatieve prijzen (Price < 0)

| MQTT-topic | Property | Opmerkingen |
|------------|------------|-------|
| `system/0/Relay/0/State` | Relay 1 | Geactiveerd wanneer prijs < 0 |
| `system/0/Relay/1/State` | Relay 2 | Geactiveerd wanneer prijs < 0 |
| `vebus/{257 or other}/Mode` | Omvormermodus | Geactiveerd wanneer prijs < 0 |
| `settings/0/Settings/CGwacs/OvervoltageFeedIn` | DC-coupled PV — feed in excess | Geactiveerd wanneer prijs < 0 |

> [!NOTE]
> Het VE.Bus instance-nummer (standaard `257`) kan in jouw systeem afwijken. Controleer dit in de installatieparameters onder „VRM Instance-nummer van het VE.Bus System-apparaat".
