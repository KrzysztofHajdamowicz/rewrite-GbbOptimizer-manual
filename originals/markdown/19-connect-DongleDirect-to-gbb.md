DongleDirect działa podobnie jak GbbConnect2:
łączy GbbOptimizer z Inwerterem, ale bez instalacji jakiegokolwiek
oprogramowania w sieci lokalnej. DongleDirect przekierowujesz Dongle do
serwera GbbOptimizer, a ten serwer (jeśli chcesz) kopiuje te dane do
serwerów Solarman w obu kierunkach.

*Uwaga: Od 2026-03-09 może być niemożliwe zrobienie tych zmian w
dongle. Wtedy nalezy dongle zresetować i przywrócić oryginalne
ustawienia*

Jak skonfigurować DongleDirect:
1. Zapamiętaj nazwę swojego serwera GbbOptimizer z adresu przeglądarki internerowej (np. gbboptimizer5.gbbsoft.pl)
2. Zaloguj się do swojego Dongle (musisz znać jego adres IP w lokalnej sieci, nazwa: admin, hasło: admin)
3. Zmień stronę na <ip dongla>/config\_hide.html (ręcznie zmień ją w adres przeglądarce internerowej)
4. Zrobić zdjęcia ekranu ze wszystkimi ustawienia na tej stronie (!)
5. Zmień „Server A Setting”:
- usuń adres IP
- zapamiętaj nazwę domeny z ustawień Server A
- zmień nazwę domeny ServerA na nazwę swojego serwera GbbOptimizer (np: gbboptimizer10.gbbsoft.pl)
- Port: 10000
- Połączenie: TCP
- Save + Restart
6. Zmień „Optional Server Setting” na ten same dane (!) + Save + Restart
7. W GbbOptimizer: Zmień typ instalacji na DongleDirect (albo stwórz nowa instalację)
8. W ustawieniach instalacji wpisz:
- numer seryjny falownika
- numer seryjny dongla (tylko cyfry)
- oryginalną nazwę domeny ServerA (jeśli pozostawisz to pole puste,
GbbOptimizer nie skopiuje danych do Solarman, więc Solarman/DeyeCloud
przestanie działać)
9. Zapisz i odczekaj minimum 2-5 minut (Dongle łączy się z serwerem GbbOptimizer po 2-5 minutach)
10. W logu powinny być widoczne takie wpisy typu:
2025-06-21 11:00:27: **From Dongle**: A501001047F585579AF6A5005E15
2025-06-21 11:00:28: **From Server**: A50A001017F685579AF6A50001AB745668780000008E15

Podziękowania dla wesolyyyy za ideę i jarakera dla pomoc w testach

## Reset dongla

1. Lokalizacja przycisku: Znajdź przycisk resetowania (zazwyczaj mały
otwór z napisem "Reset" lub "Reload") na sztycy (loggerze) wpiętej do
falownika.
2. Reset: Przy włączonym falowniku, przytrzymaj przycisk (np. szpilką) przez około 5 do 10 sekund.
3. Weryfikacja: Diody na loggerze powinny zgasnąć i ponownie się
zaświecić (lub zacząć mrugać w specyficzny sposób), co oznacza restart.
4. Konfiguracja: Otwórz aplikację Solarman Smart na telefonie
5. Łączenie: Wybierz opcję dodawania urządzenia ("Add now" lub "Configure")
6. Sieć domowa: W aplikacji wpisz dane do swojego domowego routera Wifi
