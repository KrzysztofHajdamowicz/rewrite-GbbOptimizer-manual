Inverter should collect following information:

"soc%" (or "V" if 'Use Voltage (V) instead of SOC (Deye)' checked)

"loads\_total\_kWh"

"fromgrid\_total\_kWh"

"togrid\_total\_kWh"

"pv\_total\_kWh"

Following information are optional:

"ev\_charge\_total\_kWh"

"hp\_total\_kWh"

"other1\_total\_kWh"

"other2\_total\_kWh"

Inverter must does following modes:

|  |  |
| --- | --- |
| Charge | start charge up to SOC% from PV and grid with given speed in W. When SOC level is riched: stop charge from grid, don't discharge battery below SOC, can charge from PV |
| Discharge | start discharge from battery and PV to grid up to given SOC% with given speed in W (speed to grid) |
| DisableCharge | stop charge battery, send PV to loads and grid |
| Normal | return to normal operation (PV to loads than to battery than to grid, Loads from PV than from battery than from grid) |
