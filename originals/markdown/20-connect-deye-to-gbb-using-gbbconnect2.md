## Podłączenie GbbConnect2 z inwerterami hybrydowymi Deye

Jeżeli chcesz podłączyć inwerter hybrydowy Deye bezpośrednio do GbbOptimizer2

1. Pobierz i zainstaluj GbbConnect: <https://github.com/gbbsoft/GbbConnect2>
2. W GbbOptimizer: Stwórz nową Instalację typu "instalację z GbbConnect2" albo zmień typ instniejacej instalacji na "GbbConnect2"
3. Wpisz nazwę Instalacji (przejrzyj pozostałe pola) i Zapisz.
4. Naciśnij ponownie przycisk "Popraw".
5. Nacisnij przycisk "Wygeneruj nowy Token", zapamiętaj "Plant Id" i "Plant Token"
6. W GbbConnect2: stwórz nowy Plant wprowadzające jego nazwę i "SolarmanV2".
7. W zakładce "Test and Log" możesz nacisnąć "Search for Invertes" aby znaleźć IP i SerialNumber inwertera (tylko w sieci lokalnej)
8. Uwaga: Logger pod inwerterem powinien mieć stały adres IP!
9. W zakładce "Plants" wprowadź: IPaddress i SerialNumber twojego Loggera.
10. W sekcji "GbbOptimizer" wprowadź PlantId i PlantToken.
11. Wprowadż adres serwera mqtt, odpowiedni adres znajdziesz tutaj: [patrz tutaj](https://gbboptimizer10.gbbsoft.pl/Manual?PageNo=14)
12. W zakładce Parameters możesz zaznaczyć "Start server after program
    starts", aby komunikacja z inwerterem startowała zaraz po uruchomieniu
    programu
13. Naciśnij StartServer

Uwag:

- Program powinien działać 24h 7 dniw tygodniu, aby zbierać dane
  statystyczne z inwertera i wykonywac polecenia przysłane z GbbOptimizer.
- Istnieje wersja GbbConnect2Console dla Dockera. Zacznij uzywać
  GbbConnect2 na Windowsach aby przetestować połączenie i stworzyć plik
  konfiguracyjny. Potem możesz przenieść się na wersję na Docker i
  skopiować ten sam plik konfiguracyjny.
