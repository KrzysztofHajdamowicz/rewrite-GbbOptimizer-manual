---
title: "Extra verbruik / EV"
weight: 60
translationKey: "dodatkowe-obciazenia-ev"
---

# Extra verbruik / EV

Extra verbruik is het deel van het energieverbruik dat **niet wordt meegenomen in het huisgemiddelde** — bijvoorbeeld het opladen van een elektrische auto of een warmtepomp. Het doel is om het onvoorspelbare, variabele deel uit het standaardverbruik te halen.

**Gegevensstroom:**
- IoT-meters → Extra verbruik → [Winsten]({{< relref "/configuration/profits" >}}) → [Batterijprognose]({{< relref "/configuration/battery-forecast" >}})
- EV-laders → Extra verbruik → Winsten → Batterijprognose

## AutoConverter

AutoConverter detecteert pieken in het verbruik en zet deze automatisch om in het laden van een auto (of een ander type Extra verbruik).

| Parameter | Beschrijving |
|----------|------|
| Verbruikslimiet waarboven AutoConverter wordt ingeschakeld (kWh/u) | AutoConverter wordt pas na overschrijding van deze drempel geactiveerd |
| Verbruik dat nooit in Extra verbruik wordt omgezet | Deze energie blijft altijd Verbruik |
| Maximaal Extra verbruik (kWh/u) | Maximale geconverteerde energie (bijv. het vermogen van een EV-lader). De rest = Verbruik |
| Type Extra verbruik | Type waarnaar de geconverteerde energie wordt doorverwezen |

AutoConverter wordt uitgevoerd tijdens de import in de module [Winsten]({{< relref "/configuration/profits" >}}).

## AutoAdd

Mechanisme voor constante invulling van Extra verbruik — voor apparaten die volgens een schema draaien en geen eigen meter hebben.

| Parameter | Beschrijving |
|----------|------|
| Geblokkeerd | De regel wordt niet meegenomen |
| Type Extra verbruik | Type Extra verbruik dat volgens deze regel wordt ingevuld |
| Extra verbruik (kWh/u) | Energie per uur |
| VanafDag, TotDag | Geldigheidsperiode (VanafDag moet worden ingevuld) |
| VanafUur, TotUur | Uurbereik binnen de dag |
| Ma, ..., Z | Weekdagen |
| Herhaal elke X weken | Om de hoeveel weken de regel van kracht is (gerekend vanaf VanafDag) |

> [!NOTE]
> Vink **Gegevens van EV-laders automatisch importeren en ExtraLoads elk uur automatisch toevoegen** aan zodat AutoAdd automatisch werkt.
