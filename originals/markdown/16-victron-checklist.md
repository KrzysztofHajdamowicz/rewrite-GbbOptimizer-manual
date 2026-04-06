Lista kontrolna dla Instalacji Victron:

- Nie instaluj wersji Beta oprogramowania sprzętowego
- DESS musi być wyłaczony
- Schedulers: Zakładamy, że 'Self-consumption above limit' jest
  ustawione na 'PV' (a nie 'PV & Battery'), powieważ chcemy, aby
  Schedules nie powodowały rozładowanie baterii w nocy.
- 'Battery Life' w ESS powinno być wyłaczone, tzn: Select Mode='Optimized (without BatteryLife)'.
- 'Log interval' (w VRM online portal) powinien być ustawiony na: 1 min.
- VRM: Uzytkownik musi mieć włączone prawo 'Full Control'
- Zrestartuj Cerbo
