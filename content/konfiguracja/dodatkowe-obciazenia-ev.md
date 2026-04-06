---
title: "Extra Zużycie / EV"
weight: 60
---

# Extra Zużycie / EV

Extra Zużycie to część zużycia energii, która **nie wchodzi do średniej domu** — np. ładowanie samochodu elektrycznego czy pompa ciepła. Celem jest wydzielenie nieprzewidywalnej, zmiennej części ze standardowego zużycia.

**Przepływ danych:**
- Liczniki IoT → Extra Zużycie → [Zyski]({{< relref "/konfiguracja/zyski" >}}) → [Prognoza baterii]({{< relref "/konfiguracja/prognoza-baterii" >}})
- Ładowarki EV → Extra Zużycie → Zyski → Prognoza baterii

## AutoKonwerter

AutoKonwerter wykrywa piki w zużyciu i automatycznie zamienia je na ładowanie samochodu (lub inny typ Extra Zużycia).

| Parametr | Opis |
|----------|------|
| Limit Zużycia, powyżej którego włącza się AutoKonwerter (kWh/h) | AutoKonwerter aktywuje się dopiero po przekroczeniu tego progu |
| Zużycie nigdy nie zamieniane na Extra Zużycie | Ta energia zawsze pozostaje jako Zużycie |
| Maksymalne Extra Zużycie (kWh/h) | Maksymalna konwertowana energia (np. moc ładowarki EV). Reszta = Zużycie |
| Typ Extra Zużycia | Typ, do którego kierowana jest przekonwertowana energia |

AutoKonwerter jest uruchamiany podczas importu w module [Zyski]({{< relref "/konfiguracja/zyski" >}}).

## AutoDodawaj

Mechanizm stałego wypełniania Extra Zużycia — dla urządzeń uruchamianych wg schematu, które nie mają własnego licznika.

| Parametr | Opis |
|----------|------|
| Zablokowany | Wiersz nie jest brany pod uwagę |
| Typ Extra Zużycia | Typ Extra Zużycia wypełniany wg tego wiersza |
| Extra Zużycie (kWh/h) | Energia pobierana na godzinę |
| OdDnia, DoDnia | Okres obowiązywania (OdDnia musi być wypełnione) |
| OdGodziny, DoGodziny | Przedział godzinowy w ciągu dnia |
| Pon, ..., N | Dni tygodnia |
| Powtarzaj co X tygodni | Co ile tygodni wiersz obowiązuje (licząc od OdDnia) |

> [!NOTE]
> Zaznacz **Automatycznie importuj dane z ładowarek EV i AutoDodawaj ExtraLoads co godzinę**, aby AutoDodawaj działał automatycznie.
