---
title: "Tuya"
weight: 30
translationKey: "tuya"
---

# Integratie met Tuya

GbbOptimizer kan Tuya-apparaten (bijv. slimme stopcontacten) aansturen via de Tuya Cloud API. Dit vereist het aanmaken van een ontwikkelaarsproject op het Tuya-platform en het verkrijgen van API-sleutels.

## Access ID en Access Secret verkrijgen

### 1. Maak een ontwikkelaarsaccount aan

Registreer op [platform.tuya.com](https://platform.tuya.com/).

### 2. Maak een Cloud Project aan

1. Ga naar **Cloud** -> **Development**
2. Klik op **Create Cloud Project** (rechtsboven)
3. Vul het formulier in:
   - Projectnaam — naar keuze
   - Industry — kies de juiste sector
   - Development Method — **Smart Home**
   - Data Center — kies degene die het dichtst bij jouw locatie ligt
4. Klik in het volgende scherm op **Authorize**

### 3. Koppel de mobiele app

1. Ga naar **Devices** -> **Link App Account**
2. Klik op **Add App Account**
3. Er verschijnt een QR-code
4. In de mobiele Tuya/Smart Life-app: **Me** (onderste menu) -> scan-icoon (rechtsboven)
5. Scan de QR-code

Na koppeling verschijnt in het tabblad **All Devices** een lijst met jouw apparaten.

### 4. Kopieer de API-sleutels

In het tabblad **Overview** vind je:

- **Access ID / Client ID**
- **Access Secret / Client Secret**

Voer deze gegevens in de GbbOptimizer-configuratie in onder IoT -> Tuya.

## De proefperiode verlengen

Tuya API-sleutels hebben een beperkte proefperiode. Om deze te verlengen:

1. Log in op [platform.tuya.com](https://platform.tuya.com/)
2. Ga naar **Cloud** -> **Cloud Services**
3. Selecteer **IoT Core** en klik op **View Details**
4. Klik op **Extend Trial Period** en volg de instructies

> [!WARNING]
> Als de proefperiode verloopt, verliest GbbOptimizer de mogelijkheid om Tuya-apparaten aan te sturen. Denk eraan de proefperiode regelmatig te verlengen.
