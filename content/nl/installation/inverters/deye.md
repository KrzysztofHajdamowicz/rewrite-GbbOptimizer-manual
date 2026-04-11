---
title: "Deye"
weight: 20
translationKey: "deye"
---

# Deye

{{< badge "deye-only" >}}

Deye-hybride omvormers kunnen op meerdere manieren met GbbOptimizer worden verbonden. Op deze pagina vind je een checklist met de instellingen van de omvormer en een vergelijking van de verbindingsmethoden.

## Checklist

Controleer op de Deye-omvormer voordat je GbbOptimizer start:

1. **Werkingsmodus** — `Zero export to CT` of `Zero export to Loads` (niet „Selling First"!)

   > [!WARNING]
   > Controleer de werkingsmodus niet tijdens een actieve ontlading — GbbOptimizer wijzigt de modus tijdelijk.

2. **TimeOfUse** — moet **ingeschakeld** zijn
3. **TimeOfUse** — ingesteld op **%** (en niet V), tenzij er een SOC-naar-V-mapping is gedefinieerd
4. **System Work Mode** (Schema) — ingeschakeld voor **alle 7 dagen** van de week
5. **Energy pattern** — `Load First`
6. **SolarSell / Verkoop energie** — **aangevinkt**
7. **Grid Charge (Netopladen)** — `Enable`
8. **Grid Start, Battery Restart** — waarden **lager dan** {{< glossary "MinSOC" >}}
9. **Interval voor het verzenden van gegevens** — elke **1 min** (standaard elke 5 min — moet worden aangepast)
10. **Copilot** — moet **uitgeschakeld** zijn

## Verbindingsmethoden — vergelijking

Een Deye-omvormer kan op vier manieren met GbbOptimizer worden verbonden:

|  | [Solarman]({{< relref "/installation/connection-methods/solarman" >}}) / [DeyeCloud]({{< relref "/installation/connection-methods/deye-cloud" >}}) | [GbbConnect2]({{< relref "/installation/connection-methods/gbbconnect2" >}}) | [DongleDirect]({{< relref "/installation/connection-methods/dongle-direct" >}}) | HomeAssistant / {{< glossary "SolarAssistant" >}} |
|--|--|--|--|--|
| **Gegevens van GbbOptimizer naar omvormer** | GbbOptimizer → DeyeCloud → Solarman → Dongle → Omvormer | GbbOptimizer → GbbConnect2 → Dongle → Omvormer | GbbOptimizer → Dongle → Omvormer | GbbOptimizer → HA Automation → Omvormer |
| **Gegevens van omvormer naar GbbOptimizer** | Omvormer → Dongle → Solarman → DeyeCloud → GbbOptimizer | Omvormer → Dongle → GbbConnect2 → GbbOptimizer | Omvormer → Dongle → GbbOptimizer | Omvormer → HA Automation → GbbOptimizer |
| **Gegevens van DeyeCloud/Solarman naar omvormer** | DeyeCloud → Solarman → Dongle → Omvormer | DeyeCloud → Solarman → Dongle → Omvormer | DeyeCloud → Solarman → GbbOptimizer → Dongle → Omvormer | N/B |
| **Gegevens van omvormer naar DeyeCloud/Solarman** | Omvormer → Dongle → Solarman → DeyeCloud | Omvormer → Dongle → Solarman → DeyeCloud | Omvormer → Dongle → GbbOptimizer → Solarman → DeyeCloud | N/B |
| **Probleem met het loskoppelen van de dongle** | Ja | Nee | Ja | Nee |
| **Benodigde software** | Geen | GbbConnect2 in het lokale netwerk | Geen | HomeAssistant in het lokale netwerk |
| **Data gaat via Chinese servers** | Ja | Ja (nee, als je de dongle blokkeert op de firewall) | Jouw keuze | Nee |
| **Parameters wijzigen buiten huis** | Ja | Nee (maar je kunt Solarman/DeyeCloud parallel gebruiken) | Jouw keuze | Ja |

> [!NOTE]
> Gedetailleerde configuratie-instructies voor elke methode vind je in de sectie [Verbindingsmethoden]({{< relref "/installation/connection-methods" >}}).
