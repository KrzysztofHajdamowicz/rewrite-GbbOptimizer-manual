---
title: "Tuya"
weight: 30
---

# Integracja z Tuya

GbbOptimizer moze sterowac urzadzeniami Tuya (np. gniazdkami smart) przez Tuya Cloud API. Wymaga to utworzenia projektu deweloperskiego na platformie Tuya i uzyskania kluczy API.

## Uzyskanie Access ID i Access Secret

### 1. Utworz konto deweloperskie

Zarejestruj sie na [platform.tuya.com](https://platform.tuya.com/).

### 2. Utworz projekt Cloud

1. Przejdz do **Cloud** -> **Development**
2. Kliknij **Create Cloud Project** (prawy gorny rog)
3. Wypelnij formularz:
   - Nazwa projektu — dowolna
   - Industry — wybierz odpowiednia branze
   - Development Method — **Smart Home**
   - Data Center — wybierz najblizszy Twojej lokalizacji
4. Na nastepnym ekranie kliknij **Authorize**

### 3. Polacz aplikacje mobilna

1. Przejdz do **Devices** -> **Link App Account**
2. Kliknij **Add App Account**
3. Wyswietli sie kod QR
4. W aplikacji mobilnej Tuya/Smart Life: **Me** (dolne menu) -> ikona skanowania (prawy gorny rog)
5. Zeskanuj kod QR

Po polaczeniu w zakladce **All Devices** pojawi sie lista Twoich urzadzen.

### 4. Skopiuj klucze API

W zakladce **Overview** znajdziesz:

- **Access ID / Client ID**
- **Access Secret / Client Secret**

Wpisz te dane w konfiguracji GbbOptimizer w sekcji IoT -> Tuya.

## Przedluzenie okresu probnego

Klucze API Tuya maja ograniczony okres probny. Aby go przedluzyc:

1. Zaloguj sie na [platform.tuya.com](https://platform.tuya.com/)
2. Przejdz do **Cloud** -> **Cloud Services**
3. Wybierz **IoT Core** i kliknij **View Details**
4. Kliknij **Extend Trial Period** i postepuj zgodnie z instrukcjami

> [!WARNING]
> Jesli okres probny wygasnie, GbbOptimizer straci mozliwosc sterowania urzadzeniami Tuya. Pamietaj o regularnym przedluzaniu.
