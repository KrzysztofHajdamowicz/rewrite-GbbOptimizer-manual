## Wstęp

- źródła danych cen ustawia się w menu Instalacje -> przycisk Popraw
- resztę informacji ustawia się w menu Ceny

## Cena zakupu

Wzór: **Cena Zakupu := (Cena zaimportowana\*Mnożnik + Cena
przesyłu + Koszt Transport) \* VAT\_Podatek/100 + (KosztyMiesięczne/ilośc
godzin w miesiącu)**

gdzie:

- Cena zaimportowana
= 0 gdy "Ceny zakupu" wybrano "stałe"
= cena pobrana ze źródła wskazanego w parametrach Instalacji w
pozycji "Zakup: Taryfa dla cen zakupu", gdy w "Ceny Zakupu" wybrano
"zalezna od Zaimportowanych Cen i Kosztów Transportu"
= Cena Sprzedaży, gdy w "Ceny zakupu" wybrano "zależne od Cen Sprzedazy i Kosztów transportu"

- Mnożnik:
= 'Zaimportowane Ceny Zakupu pomnóż przez'

- Cena przesyłu
= cena pobrana ze źródła wskazane w parametrach Instalacji w pozycji "Przesył: Taryfa dla cen przesyłu"
= 0, jezeli nic nie wskazano.

- Koszt Transportu
= cena z tablicy pod przyciskiem "Zmień Koszty Transportu/stałe Ceny Zakupu"

- KosztyMiesieczne
= suma wszystkich stałych kosztów dotyczących zakupu (będzie rozbita po równo na wszystkie godziny w miesiącu)

## Cena sprzedaży

Wzór: **Cena Sprzedaży := (Cena zaimportowana\*Multipler +
Dodatkowe opłaty) \* VAT\_Podatek\_Wspołczynnik/100 \* MnożnikSprzed2 \*
DziennyProcent**

gdzie:

- Cena zaimportowana
= Stala Cena Sprzedazy, jeżeli zaznaczono "Jest tylko jedna, stała Cena Sprzedaży"
= cena pobrana ze źródła wskazanego w parametrach Instalacji w pozycji "Sprzedaż: Taryfa dla cen sprzedaży"

- Multipler:
= 'Zaimportowane Ceny Sprzedaży pomnóż przez'

- Dodatkowa opłata
= cena z tablicy pod przyciskiem "Zmień dodatkowe opłaty dla Cen Sprzedaży"

- MnożnikSprzed2
= cena z tablicy pod przyciskiem "Zmień dodatkowy mnożnik2 dla Cen Sprzedaży"

- DziennyProcent
= 1+Procent/100 od wschodu do zachodu słońca (jeżeli właczony)
