## Najczęstsze błędy otrzymane w emailach z programu

|  |  |  |
| --- | --- | --- |
| Message | Podsystem | Opis |
| SolarmanError: Solarman timeout! | Solarman | Solarman nie może wysłać danych do twojego inwertera (problem lokalnej sieci?) |
| Solarman error: 2101040-device not found | Solarman | Twój inwerter nie wysyła danych do Solarmana (problem lokalnej sieci?) |
| HttpRequestException: An error occurred while sending the request.  Response status code does not indicate success: 503 (Service Unavailable)  Response status code does not indicate success: 500 (Internal Server Error)  Response status code does not indicate success: 504 (Gateway Time-out). | Solarman | API Solarman nie działa poprawnie |
| DeyeCloud error: timeout | DeyeCloud | DeyeCloud nie może wysłać danych do twojego inwertera (problem lokalnej sieci?) |
| DeyeCloud error: 2104006-device offline | DeyeCloud | Twój inwerter nie wysyła danych do DeyeCloud (problem lokalnej sieci?) |
| DeyeCloud error: 2101042-auth no operation permission | DeyeCloud | Za mało praw dla konta w DeyeCloud (np: nadanych przez instalatora) |
| Mqtt to GbbConnect2: timeout! | GbbConnect2 | GbbOptimizer nie może się połączyć z lokalnym GbbConnect2 |
| GbbConnect2Error: Connection timed out 192.168.x.xx:8899 | GbbConnect2 | Lokalny GbbConnect2 nie może się połączyć z donglem Deye (dongl nie jest w sieci) |
| Victron Mqtt: timeout! (15 sec)  Error during checking whether Schedules reached Cerbo successfully | Victron | GbbOptimizer nie moża się połączyc z Cerbo przy użyciu serwerów mqtt Victrona (problem lokalnej sieci?) |
| Solcase.com: Too many requests | Solcast.com | Limit 10 wywołań do solcast.com został osiągnięty. Poczekaj do północy. |
| Get Prices: The SSL connection could not be established  Get Prices: Próba połączenia nie powiodła się, ponieważ połączona strona nie odpowiedziała | Ceny z ENTSOE | API ENTSOE z cenami nie działa |
| Get Prices: HTTP 'POST https://api.tibber.com/v1-beta/gql' call failed with status 'Gateway timeout'  Get Prices: Response status code does not indicate success: 502 (Bad Gateway). | Ceny z Tibber | API Tiber z cenami nie działa |
| Get Prices: Response status code does not indicate success: 502 (Bad Gateway) | Cenyz AU Amber | API Amber z cenami nie działa |
| ERROR from Cache: Response status code does not indicate success: 500 (Internal Server Error). | Pstryk | Błąd po stronie API Pstryka |
| B0220-System function downgrade | Hinen | API Hinen jest aktualizowane |
