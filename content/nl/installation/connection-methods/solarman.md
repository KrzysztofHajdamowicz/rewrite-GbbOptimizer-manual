---
title: "Solarman"
weight: 10
translationKey: "solarman"
---

# Solarman

Solarman is een cloud-gebaseerde methode om de omvormer met GbbOptimizer te verbinden. De gegevens gaan via de Solarman-servers — er is geen extra software nodig.

## Stap-voor-stap configuratie

1. Voeg een installatie toe: **Nieuwe installatie met een omvormer verbonden met Solarman toevoegen**
2. Vul de velden in de groep „Solarman" in (details in [Installatieparameters]({{< relref "/installation/installation-parameters" >}}))
3. Log in op de Solarman-servers: voer je **e-mail** en **wachtwoord** in (dezelfde als voor de Solarman-app) en klik op **Verbinden**
4. Kies je omvormer in de lijst **SerialNo van de omvormer kiezen**
5. Kies het **Type omvormer**

   > [!WARNING]
   > Kies nooit het verkeerde type omvormer! Een verkeerde keuze en het verzenden van gegevens vereist een fabrieksreset van de omvormer.

6. Klik op **Verbinding met de omvormer testen** — het programma haalt de actuele {{< glossary "SOC" >}} op uit de omvormer. Controleer of de waarde klopt. In de module Log vind je meer informatie uit de omvormer
7. Ga verder met het invullen van de batterijvelden en klik op **Doorgaan met FastSetup**

## Besturen via spanning (V) in plaats van SOC

Als je liever de batterij stuurt via spanning in plaats van {{< glossary "SOC" >}}:

1. Vink **Besturen via V en niet via SOC** aan
2. Klik op **SOC-naar-V-mapping bewerken**
3. Voer ten minste **twee bekende paren** SOC en V in zodat het programma een mapping kan aanmaken. Hoe meer paren — hoe nauwkeuriger de mapping

> [!NOTE]
> De mapping is **proportioneel (lineair)** — het programma interpoleert op basis van de twee dichtstbijzijnde punten.

## GbbShunt

GbbShunt is een module die ontworpen is voor het aansturen van loodzuurbatterijen. Hij vervult twee functies (normaal door de omvormer uitgevoerd):

- **Berekent de {{< glossary "SOC" >}}** op basis van de energie die naar/uit de batterij is gevloeid
- **Beëindigt het laden/ontladen** zodra het aangegeven SOC-niveau is bereikt

### GbbShunt-parameters

Een gedetailleerde beschrijving van de GbbShunt-parameters vind je in [Installatieparameters]({{< relref "/installation/installation-parameters" >}}).

### Hoe berekent GbbShunt de SOC?

1. Op basis van het verschil tussen de begin- en de actuele energie die naar/uit de batterij is gevloeid, wordt het energieverschil berekend
2. Na de actuele energie te delen door de totale batterijcapaciteit verkrijgt men de **Berekende SOC**
3. Wanneer de Berekende SOC < 0 of SOC > 100 is, of wanneer de batterijspanning de in de parameters gedefinieerde niveaus bereikt — volgt een **reset van de gegevens**: het programma bewaart de actuele waarden als beginwaarden
4. Bij de eerste start (of na een onderbreking van > 12 uur) berekent het programma de beginenergie op basis van de uit de omvormer opgehaalde SOC
5. De berekeningen worden **elke minuut** uitgevoerd

### Hoe bestuurt GbbShunt het einde van het laden/ontladen?

1. Bij het verzenden van gegevens naar de omvormer ontvangt GbbShunt informatie over de doel-SOC voor het huidige uur
2. **Laden**: wanneer de Berekende SOC ≥ doel-SOC — volgt een stop. Als de SOC in hetzelfde uur onder doel-SOC - 5% daalt, wordt het laden hervat
3. **Ontladen**: wanneer de Berekende SOC ≤ doel-SOC — volgt een stop. Als de SOC in hetzelfde uur boven doel-SOC + 5% stijgt, wordt het ontladen hervat
4. Beëindiging van het laden/ontladen leidt tot het verzenden van de **Normal**-bewerking naar de omvormer

> [!NOTE]
> Het is aan te raden dat de omvormer **elke minuut** gegevens naar Solarman stuurt (standaard elke 5 minuten). Wijzig deze parameter in de instellingen van de omvormer.

### GbbShunt Monitor

In de GbbOptimizer-interface is een GbbShunt-monitor beschikbaar die de actuele status van de module toont:

- **Berekende SOC** — de actuele SOC zoals berekend door GbbShunt
- **Batterijspanning** — de actuele spanning zoals afgelezen uit de omvormer
- **Energie in de batterij** — de berekende energie (kWh) boven MinSOC
- **Status van laden / ontladen** — of GbbShunt het laden of ontladen heeft gestopt

De monitor is handig om te verifiëren of GbbShunt de SOC correct berekent en reageert op de spanningsdrempels.
