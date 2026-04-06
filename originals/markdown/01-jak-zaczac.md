# Witamy w programie GbbOptimizer (vel. GbbVictronWeb).

## Alternatywny Manual stworzony przez 0xDEADBEEF1137:

<https://krzysztofhajdamowicz.github.io/rewrite-GbbOptimizer-manual/>

## Aby zacząć używac program powinieneś:

- Stworzyć 'Instalację': Instalacja to jeden system Victron (Cerbo GX lub inny moduł GX) lub jeden inwerter Deye.

- Naciśnij 'Dodaj nową instalację z Victron System', jezeli masz system Victron (z lub bez HomeAssistant)
- Naciśnij 'Dodaj nowa instalację z inwerterem Deye podłączonym do
  DeyeCloud', jeżeli masz inwerter hybrydowy Deye połączony do DeyeCloud
- Naciśnij 'Dodaj nowa instalację z Solarman', jeżeli masz inwerter
  hybrydowy Deye połączony z programem Solarman (i nie chcesz
  wykorzystywac HomeAssistant)
- Naciśnij 'Dodaj nowa instalację z Solarman', jeżeli masz inny
  inwerter hybrydowy połączony z programem Solarman i wiesz jak ustawiać
  rejestry w nim dla różnych trybów z programu.
- Naciśnij 'Dodaj nową instalację z Home Assistant', jeżeli masz
  inwerter hybrydowy Deye połączony z HomeAssistant (z lub bez
  SolarAssistant) LUB inny inwerter hybrydowy podłączony bezpośrednio do
  HomeAssistant.
- Itd
- Jeżeli masz inwerter SofarSolar: (1) naciśnij 'Instalacja z
  DongleDirect (Deye, SofarSolar)' (2) na końcu przejdź także tą
  procedurę: [DongleDirect konfiguracja](https://gbboptimizer10.gbbsoft.pl/Manual?Filters.PageNo=36)
- Jeżeli masz inwertery Deye w układzie Master-Slave, to (1) naciśnij
  'Instalacja z Solarman' (2) dodaj Master jako głównym inwerter i
  Slave-y jako dodatkowe (w parametrach instalacji)

- Wypełnij wszystkie pola (przynajmniej te z gwiazdką \*) i
kontynuj w Szybkiej Konfiguracji. Po wypełnieniu wszystkich pól naciśnij
'Zapisz zmiany'
- w module 'Ceny': powinieneś zaimportować taryfę lub ręcznie skonfigurować ceny zakupu i sprzedazy.
- w module 'Profil Zużycia': wprowadź ręcznie zużycie twojego domu lub zaimportuj z Instalacji

Po tym wszystkich:

- Instalacja jest w 'trybie testowym'. Aby rozpocząć wysyłanie
  ustawień do Istalacji powinieneś wyłączyć 'tryb testowy' w module
  'Prognoza Baterii'
- Wybrany jest "Optymalizator oparty o ceny"
- Najlepiej poczekać tydzień, aby profil zuzycia się zaktualizował a w prognozie PV policzył się współczynnik korygujący.
- Dopiero po tygodniu wyłączyc 'tryb testowy'

Najważniejsze rzeczy do sprawdzenia:

- czy ceny są prawidłowe. Pamiętaj wprowadzić koszty transportu dla cen zakupu.
- czy Prognoza PV jest prawidłowa. Jeżeli nie, spróbuj inne źródło prognozy PV.
- czy Profil Zużycia jest prawidłowy. Jezeli nie chcesz wprowadzać ręczcnie Profilu Zużycia poczekaj tydzień aby zebrać dane.

## Filmy:

- Dodawanie systemu Victron do GbbOptimizer: <https://youtu.be/5q6gORx1KUY>
- Dodawanie inwertera Deye przez Solarmana: <https://youtu.be/y8fhh1UecqQ>
- Konfigurowanie cen zakupu i sprzedaży: <https://youtu.be/m27uQfO60pc>

## Najlepsze praktyki

- Cierpliwości. Program uczy cierpliwości.
- zmień źródło prognozy PV z 'foracast.solar' na 'solcast.com' (ale
  najpierw tam załóż darmowe konto 'Home', jedno konto na każde dwie
  Płaszczyzny PV)
- czym mniej dodatkowych opcji zaznaczonych w parametrach optymalizatora, tym wieksze zyski
- ustaw MaxSOC=90% aby mieć bufor na nietrafioną prognozę pogody.
  Oraz ustaw 'Lista dni w miesiącu (oddzielona przecinkiem) kiedy
  'Maksymalna SOC baterii' ma być zmieniony na 100% (na około 2h)' na (na
  przykład): 1, 15, aby jednak czasami dochodzić do 100% dla dobra
  baterii.
- Jezeli w HomeAssistant jest importowanie danych z inwertera,
  ustawić "update\_interval" na co najmniej 20sek. Inaczej Solarman gryzie
  się z HomeAssistant. ( [Discord](https://discord.com/channels/1119519533498126380/1294610337936441357/1353688730698780764) ). Albo przejść z Solarman na GbbConnect2.

## Jeżeli chcesz tylko optymalizować ładowanie EV (bez fotowoltaiki)

1. Dodaj inatalację "z HomeAssistant"
2. Wypełnij pola
- Nazwa
- Moc przyłacza - pobieranie
- Moc przyłacza - wysyłanie <- wpisz 0
- pojemność KWh baterii <- wpisz 0
3. Przycisk "Zapisz i kontynuj w Szybkiej Konfiguracji", na tej stronie zrób tylko takie zmiany
- odznacz 'Dodaj pierwsza PłaszczyznęPV'
- zaznacz 'EV: Automatycznie importuj dane z ładowarek EV co godzinę'
4. Przycisk "Zapisz" i zostaniesz przeniesiony do menu Ceny
- w pozycji 'albo Wybierz taryfę dystrybutora i sprzedawcy energii' wybierz taryfę dystrybucji i taryfę dostawcy energii
- naciśnij "Importuj wybrane taryfy"
5. Przejdź do menu 'EV/Extra Zuzycie'
- w sekcji "Ładowanie EV" dodaj swoja ładowarkę
- w sekcji 'AutoŁadowanie EV' dodaj jak chcesz ładować samochód (np: w
sekcji "Warunki" wybierz "Cena" 3 "najniższa Cena Zakupu")
