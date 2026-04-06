---
title: "DongleDirect"
weight: 40
---

# DongleDirect

{{< glossary "DongleDirect" >}} działa podobnie jak {{< glossary "GbbConnect2" >}} — łączy falownik z GbbOptimizer, ale **bez instalacji dodatkowego oprogramowania** w sieci lokalnej. Dongle (logger WiFi) jest przekierowywany bezpośrednio na serwer GbbOptimizer.

> [!WARNING]
> Od 2026-03-09 zmiana ustawień Dongle może być niemożliwa na niektórych modelach. W takim przypadku konieczny jest reset Dongle i przywrócenie oryginalnych ustawień.

## Konfiguracja krok po kroku

1. Zapamiętaj nazwę serwera GbbOptimizer z adresu przeglądarki (np. `gbboptimizer5.gbbsoft.pl`)
2. Zaloguj się do Dongle — musisz znać jego adres IP w sieci lokalnej (login: `admin`, hasło: `admin`)
3. Przejdź na stronę `http://<ip_dongla>/config_hide.html` (zmień ręcznie adres w przeglądarce)
4. **Zrób zdjęcia ekranu** ze wszystkimi aktualnymi ustawieniami (na wypadek potrzeby przywrócenia!)
5. Zmień **Server A Setting**:
   - Usuń adres IP
   - Zapamiętaj oryginalną nazwę domeny Server A
   - Zmień domenę na nazwę serwera GbbOptimizer (np. `gbboptimizer10.gbbsoft.pl`)
   - Port: `10000`
   - Połączenie: `TCP`
   - **Save + Restart**
6. Zmień **Optional Server Setting** na te same dane — **Save + Restart**
7. W GbbOptimizer zmień typ instalacji na **DongleDirect** (lub stwórz nową)
8. W ustawieniach instalacji wpisz:
   - **Numer seryjny falownika**
   - **Numer seryjny Dongle** (tylko cyfry)
   - **Oryginalną nazwę domeny Server A** — jeśli pole będzie puste, GbbOptimizer nie skopiuje danych do Solarman i Solarman/DeyeCloud przestanie działać
9. Zapisz i odczekaj **2-5 minut** (Dongle łączy się z serwerem GbbOptimizer po kilku minutach)
10. W logu powinny pojawić się wpisy typu:
    ```
    2025-06-21 11:00:27: From Dongle: A501001047F585579AF6A5005E15
    2025-06-21 11:00:28: From Server: A50A001017F685579AF6A50001AB745668780000008E15
    ```

## Reset Dongle

Jeśli trzeba przywrócić oryginalne ustawienia Dongle:

1. Znajdź przycisk resetowania (mały otwór z napisem „Reset" lub „Reload") na loggerze wpiętym do falownika
2. Przy **włączonym falowniku** przytrzymaj przycisk (np. szpilką) przez **5-10 sekund**
3. Diody na loggerze powinny zgasnąć i ponownie się zaświecić (lub mrugać), co oznacza restart
4. Otwórz aplikację **Solarman Smart** na telefonie
5. Wybierz opcję **dodawania urządzenia** („Add now" lub „Configure")
6. Wpisz dane do domowego routera WiFi

> [!NOTE]
> Jeśli wpiszesz oryginalną nazwę domeny Server A w ustawieniach instalacji GbbOptimizer, dane będą kopiowane do Solarman w obu kierunkach — zachowasz pełną funkcjonalność portalu Solarman/DeyeCloud.
