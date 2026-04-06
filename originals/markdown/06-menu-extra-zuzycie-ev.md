## Extra Zużycie/EV

Extra Zużycie to taka część Zuzycia, które nie wchodzi do średniej domu. Np: ładowanie samochodu elektrycznego czy pompa ciepła.
Chodzi o to, aby wydzielić ze standardowego, przewidywalnego Zużycia część nieprzewidywalną, mocno zmienną.

Przepływ danych:

a) Liczniki IoT -> Extra Zużycie -> Zyski -> Prognoza baterii (lewa część głównego wykresu)
b) Ładowarki EV -> Extra Zuzycie -> Zyski -> Prognoza baterii (lewa częśc głównego wykresu)

## AutoKonwerter

AutoKonwerter wykrywa piki w Zużyciu i zamienia je na ładowanie samochodu (lub inny rodzaj ExtraZużycia).

|  |  |
| --- | --- |
| Parametr | Opis |
| Limit Zużycia, powyżej którego włącza się AutoKonwerter (kWh na godzinę) | AutoKonwerter włącza się tylko, jak Zużycie przekroczy tą kwotę |
| Zużycie nigdy nie zamieniane na Extra Zużycie | Ta energia zawsze zostaje jako Zużycie |
| Maksymalne Extra Zużycie (kWh na godzinę), reszta jest uważana za normalne Zużycie | Maksymalna energia, która jest konwertowana na ExtraZużycie (np: moc ładowatki EV). Pozostała energia zostaje jako Zużycie |
| Typ Extra Zużycia | Typ ExtraZużycia, do którego kierowana jest przekonwertowana energia |

AutoKonwerter jest uruchamiany podczas importu w menu Zyski

## AutoDodawaj

Mechanizm stałego wypełniania ExtraZużycia, np: związany z
urządzeniami, które są uruchamiane wg pewnego schematu, a nie maja
swojego licznika zużycia, który moznaby pobrać do programu.

|  |  |
| --- | --- |
| Parametr | Opis |
| Zablokowany | Jeżeli zaznaczone, to dany wiersz nie jest brany pod uwagę (tak jakby go nie było) |
| Typ Extra Zużycia | Typ ExtraZużycia, który jest wypełniany wg tego wiersza |
| Extra Zużycie (kWh/godzinę) | Energia pobierana na godzinę |
| OdDnia, DoDnia | Okres w jakim wiersz obowiązuje, OdDnia musi być wypełnione |
| OdGodziny, DoGodziny | Przedział czasowy w ciągu dnia, kiedy wiersz obowiązuje |
| Pon,...,N | Dni tygodnia, kiedy wiersz obowiązuje |
| Powtarzaj co X tygodnia | Co ile tygodni wiersz obowiązuje, licząc od daty OdDnia |

'Automatycznie importuj dane z ładowarek EV i AutoDodawaj ExtraLoads
co godzinę' powinien być zaznaczony, aby automatycznie uruchamiać
AutoAdd
