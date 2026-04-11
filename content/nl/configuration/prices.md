---
title: "Prijzen"
weight: 40
translationKey: "ceny"
---

# Prijzen

De module voor de configuratie van in- en verkoopprijzen van energie. De bronnen van de prijsgegevens worden ingesteld in de [installatieparameters]({{< relref "/installation/installation-parameters" >}}), de overige parameters hier.

## Inkoopprijs

**Formule:**

```
Inkoopprijs = (Geïmporteerde prijs × Multiplier + Transportprijs + Transportkosten) × BTW/100
              + (Maandelijkse kosten / aantal uren in de maand)
```

| Component | Beschrijving |
|----------|------|
| Geïmporteerde prijs | **Vast** → 0. **Afhankelijk van geïmporteerde prijzen en transportkosten** → prijs uit de bron opgegeven in de installatieparameters. **Afhankelijk van verkoopprijzen** → Verkoopprijs |
| Multiplier | „Geïmporteerde inkoopprijzen vermenigvuldigen met" |
| Transportprijs | Prijs uit de bron opgegeven in de installatieparameters (item „Transport: Tarief voor transportprijzen"). 0 indien niet opgegeven |
| Transportkosten | Prijs uit de tabel onder de knop „Transportkosten / vaste inkoopprijzen wijzigen" |
| Maandelijkse kosten | Som van de vaste inkoopkosten — gelijkmatig verdeeld over alle uren in de maand |

## Verkoopprijs

**Formule:**

```
Verkoopprijs = (Geïmporteerde prijs × Multiplier + Extra toeslagen) × BTW/100
               × MultiplierVerkoop2 × DagelijksPercentage
```

| Component | Beschrijving |
|----------|------|
| Geïmporteerde prijs | Als „Er is slechts één, vaste verkoopprijs" is aangevinkt → vaste waarde. Anders → prijs uit de bron opgegeven in de installatieparameters |
| Multiplier | „Geïmporteerde verkoopprijzen vermenigvuldigen met" |
| Extra toeslag | Tabel onder de knop „Extra toeslagen voor verkoopprijzen wijzigen" |
| MultiplierVerkoop2 | Tabel onder de knop „Extra multiplier2 voor verkoopprijzen wijzigen" |
| DagelijksPercentage | 1 + Percentage/100 van zonsopgang tot zonsondergang (indien ingeschakeld) |
