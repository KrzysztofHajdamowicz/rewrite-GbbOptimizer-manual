---
title: "Tuya"
weight: 30
---

# Integracja z Tuya

GbbOptimizer może sterować urządzeniami Tuya (np. gniazdkami smart) przez Tuya Cloud API. Wymaga to utworzenia projektu deweloperskiego na platformie Tuya i uzyskania kluczy API.

## Uzyskanie Access ID i Access Secret

### 1. Utwórz konto deweloperskie

Zarejestruj się na [platform.tuya.com](https://platform.tuya.com/).

### 2. Utwórz projekt Cloud

1. Przejdź do **Cloud** -> **Development**
2. Kliknij **Create Cloud Project** (prawy górny róg)
3. Wypełnij formularz:
   - Nazwa projektu — dowolna
   - Industry — wybierz odpowiednią branżę
   - Development Method — **Smart Home**
   - Data Center — wybierz najbliższy Twojej lokalizacji
4. Na następnym ekranie kliknij **Authorize**

### 3. Połącz aplikację mobilną

1. Przejdź do **Devices** -> **Link App Account**
2. Kliknij **Add App Account**
3. Wyświetli się kod QR
4. W aplikacji mobilnej Tuya/Smart Life: **Me** (dolne menu) -> ikona skanowania (prawy górny róg)
5. Zeskanuj kod QR

Po połączeniu w zakładce **All Devices** pojawi się lista Twoich urządzeń.

### 4. Skopiuj klucze API

W zakładce **Overview** znajdziesz:

- **Access ID / Client ID**
- **Access Secret / Client Secret**

Wpisz te dane w konfiguracji GbbOptimizer w sekcji IoT -> Tuya.

## Przedłużenie okresu próbnego

Klucze API Tuya mają ograniczony okres próbny. Aby go przedłużyć:

1. Zaloguj się na [platform.tuya.com](https://platform.tuya.com/)
2. Przejdź do **Cloud** -> **Cloud Services**
3. Wybierz **IoT Core** i kliknij **View Details**
4. Kliknij **Extend Trial Period** i postępuj zgodnie z instrukcjami

> [!WARNING]
> Jeśli okres próbny wygaśnie, GbbOptimizer straci możliwość sterowania urządzeniami Tuya. Pamiętaj o regularnym przedłużaniu.
