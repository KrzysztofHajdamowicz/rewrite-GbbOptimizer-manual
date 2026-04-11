---
title: "GBB Shunt"
weight: 20
translationKey: "gbb-shunt"
---

# GBB Shunt

GBB Shunt is een GbbOptimizer-module voor installaties met loodaccu's (zuur, gel, AGM).

## Wat is GBB Shunt?

In installaties met loodaccu's kan de standaard {{< glossary "SOC" >}}-meting door de omvormer onnauwkeurig zijn. Met GBB Shunt kun je de laadtoestand nauwkeuriger volgen op basis van de stroommeting via een shunt.

## Belangrijkste functies

- **Nauwkeurige SOC-meting** — op basis van stroommeting (coulombmeter), niet van spanning
- **Temperatuurcompensatie** — houdt rekening met de invloed van temperatuur op de capaciteit van loodaccu's
- **Batterijbescherming** — voorkomt diepe ontladingen die de levensduur van loodaccu's verkorten

## Wanneer gebruiken?

GBB Shunt wordt aanbevolen als:

- Je loodaccu's gebruikt (geen lithium)
- De omvormer geen nauwkeurige SOC-meting voor loodaccu's heeft
- Je de levensduur van de batterij wilt verlengen door nauwkeurige cyclusbesturing

> [!NOTE]
> Lithiumbatterijen (LiFePO4, Li-ion) met BMS hebben een ingebouwde nauwkeurige SOC-meting en hebben de GBB Shunt-module niet nodig.

## Configuratie

De GBB Shunt-module wordt geconfigureerd in de installatie-instellingen in de geavanceerde sectie. Je moet opgeven:

- Batterijcapaciteit (Ah)
- Nominale spanning
- Shunt-parameters
