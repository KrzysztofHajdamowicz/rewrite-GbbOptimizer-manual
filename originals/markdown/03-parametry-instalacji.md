|  |  |  |  |
| --- | --- | --- | --- |
|  | Parametr |  | opis |
| Typ |  |  |  |
|  | Typ |  | Typ połaczenia z inwerterem |
|  | Przedziałów czasu dziennie |  | Ilość przedziałów czasu dziennie. W Polsce obowiązuje obecnie 60 przedziałów czasu dla klientów indywidualnych. |
| Instalacja |  |  |  |
|  | Nazwa |  | Nazwa instalacji. Musi być unikalna w ramach konta. |
|  | Strefa czasowa |  | Strefa czasowa instalacji |
|  | Maksymalna moc pobierania z sieci | kW | Parametr przyłącza |
|  | Maksymalna moc wysyłania do sieci | kW | Parametr przyłącza |
|  | Jaki % PV jest podłączone po stronie DC (prąd stały) inwertera? | % | 0% - wszystkie PV są podłaczone do AC (prąd zmienny)  100% - wszystkie PV są podłączone do DC (prąd stały) |
|  | Szerokość/Długość geograficzna |  | Położenie geograficzne instalacji  Może być używane w modułach: Metei i prognozy PV |
| Bateria w instalacji |  |  |  |
|  | Pojemność kWh baterii (brutto) | kWh | Pojemność baterii |
|  | Średnie napięcie baterii (V) | V | Używane do liczenia W z A oraz A z W. Może być przybliżone i zaokrąglone |
|  | Minimalny SOC baterii (%) | % | Minimalny SOC baterii.  Poniżej jest prąd używany tylko w wyjątkowych sytuacjach, np: brak pradu. Żelazna rezerwa. |
|  | Maksymalna moc ładowania inwertera (kW) DC | kW | Maksymalna moc ładowania inwertera |
|  | Maksymalna moc rozładowania inwertera (kW) DC | kW | Maksymalna moc rozładowywania inwertera |
|  | Maksymalna moc BMS ładowania baterii (kW) DC | kW | Maksymalna moc ładowania baterii.  Istotne jeżeli jest inna niż moc inwertera i gdy PV jest podłączone po stronie DC. |
|  | Maksymalna moc BMS rozładowania baterii (kW) DC | kW | Maksymalna moc rozłładowywania baterii.  Istotne jeżeli jest inna niż moc inwertera i gdy PV jest podłączone po stronie DC. |
|  | Straty na ładowaniu baterii z sieci (%) | % | Straty na ładowaniu  (wliczając sposób liczenia SOC przez BMS) |
|  | Straty na rozładowaniu z baterii do sieci/Zużycia (%) | % | Straty na rozładowywaniu  (wliczając sposób liczenia SOC przez BSM) |
| Victron |  |  |  |
|  | VRM Portal Id |  | 'VRM Portal Id' można znaleźć w: Cerbo -> setting -> VRM online portal -> VRM portal ID |
|  | Installation Id |  | 'Installation Id' to numer w adresie strony VRM |
|  | Login/email VRM |  | Login do portalu VRM |
|  | Hasło do VRM |  | Hasło do portalu VRM, jeżeli nie uzywasz 2FA |
|  | VRM Token |  | Token dla 2FA |
|  | Numer 'VRM Instance' urządzenia 'VE.Bus System' |  | Normalnie inwerter ma numer 276. Ale czasami inny. |
| Solarman / DeyeCloud |  |  |  |
|  | Sposób zalogowania się |  | Czy logujesz się emailem, loginem czy numerem telefonu |
|  | Email, Login lub Prefix i numer telefonu |  | Login do Solarman/DeyeCloud |
|  | Hasło |  | Hasło do Solarman |
|  | Zapamiętaj dane do logowania, aby automatycznie ponownie się łączyć. |  | Zapamiętaj Login i hasło aby sie automatycznie ponownie łaczyć od czasu do czasu.  W przeciwnym wypadku będziesz musiał się łaczyć ręcznie (dostaniesz email na ten temat) |
|  | Wybierz SerialNo inwertera |  | Po połączeniu sie SerialNo musi być wybrany, |
|  | Rodzaj inwertera (nie wolno się pomylić!) |  | Rodzaj inwertera. Jeżeli sie pomylisz i wyślesz dane do inwertera, to będziesz musiał przywrócić ustawienia fabryczne w inwerterze! |
|  | Deye: Dodaj produkcje MI/GEN do produkcji PV | Tylko Deye | Normalnie produkcja z wejścia GEN jest dodawana do produkcji PV, ale na niektórych wersjach musisz zaznaczyć tą opcje |
|  | Deye: Nie ma CT, więc nie próbuj ustawić ZeroToCT | Tylko Deye | Przed rozładowaniem program zapamiętuje aktualny tryb, aby powrócić do niego po zakończeniu rozładowania. Jeśli przed rozładowaniem aktualny tryb to „Selling First”, program nie wie, do którego trybu powinien powrócić. W związku z tym powraca do ZeroToCT. Po zaznaczeniu tej opcji program powróci do ZeroToLoad. |
|  | Deye: Ustaw czas inwertera o północy | Tylko Deye | Ustaw czas na inwerterze o północy. |
|  | Dane o SOC są wysyłane z HomeAssistant/SolarAssistant a nie pobierane z invertera: |  | Nie pobieraj SOC z inwertera ale SOC zostanie wyeksportowane przez HomeAssistant |
|  | Dane ZSieci i DoSieci są pobierane z |  | Nie pobieraj ZSieci/DoSieci z inwertera ale ZSieci/DoSieci zostanie wykeportowane przez HomeAssistant lub zaimportowane z licznika IoT |
|  | Dane Zużycia są wysyłane z HomeAssistant/SolarAssistant a nie pobierane z invertera |  | Nie pobieraj Zużycia z inwertera, ale Zużycie zostanie wyeksportowane przez HomeAssistant |
| Zapasowe połączenie - DeyeCloud |  | tylko Solarman |  |
|  | Jak połączenie zapasowe ma być używane |  | Wyłączone - nie używaj DeyeCloud jako połączenie zapasowe  Włączone - uzywaj DeyeCloud jeżeli Solarman zgłosi błąd  Tylko zapasowe - nie używaj Solarman, ale zawsze DeyeCloud |
|  | Sposób zalogowania/Email/Hasło |  | Login i hasło do DeyeCloud |
|  | Zapamiętaj dane do logowania, aby automatycznie ponownie się łączyć |  | Zapamiętaj login i hasło aby automatycznie logować do DeyeCloud od czasu do czasu. W przeciwnym razie będziesz musiał się logować ręcznie. |
|  | Wybierz SerialNo inwertera |  | Po połączeniu wybierz SerialNo inwertera |
| Parametry inwertera |  | Tylko Deye |  |
|  | Steruj poprzez V a nie przez SOC |  | Inwerter używa V a nie SOC w TimeOfUse |
|  | Także aktualne SOC obliczaj z V |  | Jeżeli zaznaczone, to licz SOC z V. Jeżeli nie, to pobieraj SOC z inwertera |
| GbbShunt |  | Tylko Solarman+Deye |  |
|  | Włączony |  | Włacz GbbShunt |
|  | Minimalny SOC baterii / V kiedy SOC zostanie ustawiony na Minimalny SOC |  | Gdy V dojdzie do 'Minimalny SOC baterii', to SOC zostanie ustawiony na 'Minimalny SOC baterii' |
|  | Maksymalny SOC baterii / V kiedy SOC zostanie ustawiony na Minimalny SOC |  | Gdy V dojdzie do 'Maksymalny SOC baterii', to SOC zostanie ustawiony na 'Maksymalny SOC baterii' |
|  | Straty na ładowaniu+rozładowaniu (%) | % | Straty na procesie ładowania plus rozładowania. |
|  | V podczas ładowania baterii | V | V wysyłane do TimeOfUse podczas ładowania |
|  | V podczas rozładowania baterii | V | V wysyłane do TimeOfUse podczas rozładowania |
| Pomoc Techniczna |  |  |  |
|  | Wyślij email do mnie, jeżeli nie można nawiązać połączenia z Instalacją przez x godzin | hours | Po ilu godzinach program ma wysłać Ci emaila, że nie ma połączenia z instalacją. Wyczyść pole, jeżeli nie chcesz otrzymywać takich emaili. |
|  | Wyślij e-mail do mnie z błędami w logu (sprawdzane co godzinę) |  | Wysyłaj co godzinę emaila z błędami które wystąpiły. |
|  | Dodatkowe emaile do wysyłania e-maila (błędy w logu, raport miesięczny) |  | Dodatkowe adresy do wysyłania emaili. Dobre dla instalatorów aby wysyłać emaile także do Klienta (lub vice versa) |
|  | Utępnij Instalację pomocy technicznej |  | Daj dostęp Pomocy Technicznej do twojej instalacji. Pomoc Techniczna może np: sprawdzić twoja instalacje, ale najpierw skontaktuj sie z nią na Discordzie. |
