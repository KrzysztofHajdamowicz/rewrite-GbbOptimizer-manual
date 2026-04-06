|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Solarmana / DeyeCloud | GbbConnect2 | DongleDirect | HomeAssistant |
| Data from GbbOptimizer to Inverter | GbbOptimizer -> DeyeCloud -> Solarman -> Dongle -> Inverter | GbbOptimizer -> GbbConnect2 -> Dongle -> Inverter | GbbOptimizer -> Dongle -> Inverter | GbbOptimizer -> HA Automation -> Inverter |
| Data from Inverter to GbbOptimizer | Inverter -> Dongle -> Solarman -> DeyeCloud -> GbbOptimizer | Inverter -> Dongle -> GbbConnect2 -> GbbOptimizer | Inverter -> Dongle -> GbbOptimizer | Inverter -> HA Automation -> GbbOptimizer |
| Data from DeyeCloud/Solarman to inverter | DeyeCloud -> Solarman -> Dongle -> Inverter | DeyeCloud -> Solarman -> Dongle -> Inverter | DeyeCloud -> Solarman -> GbbOptimizer -> Dongle -> Inverter | N/A |
| Data from inverter to DeyeCloud/Solarman | Inverter -> Dongle -> Solarman -> DeyeCloud | Inverter -> Dongle -> Solarman -> DeyeCloud | Inverter -> Dongle -> GbbOptimizer -> Solarman -> DeyeCloud | N/A |
| Dongle disconnection issue | yes | no | yes | no |
| Sofware required to install | non | GbbConnect2 on local network | non | HomeAssistant on local network |
| Data is going to servers under Chinese control | yes | yes (no if you block dongle on firewall) | yes or no (your decision) | no |
| Can change inverter parameters outside home | yes | no (but you can use Solarman/DeyeCloud in paraller) | yes or no (your decision) | yes |
