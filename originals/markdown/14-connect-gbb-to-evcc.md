## Connecting evcc.io to GbbOptimizer

To connect evcc.io to GbbOptimizer your mqtt server should be used (mosquitto or HomeAssistant mqtt)

- In Mosquitto broker activate Customize and setup folder to: mosquitto
- Ceate file mosquitto/GbbOptimizer.conf:
  connection GbbOptimizer\_<plantID>
  remote\_username <plantID>
  remote\_password <plantToken>
  address <mqtt address [see here](https://gbboptimizer10.gbbsoft.pl/Manual?PageNo=14) >:8883
  bridge\_capath /etc/ssl/certs
  **topic # both 2 evcc/loadpoints/ <plantID>/evcc/site/loadpoints/**

Evcc should send data using topic: <plantid>/evcc/site/statistic/total/chargedKWh

GbbOptimizer send following topics:

- <plantid>/evcc/loadpoints/{chargerId}/mode
  - payload: *off* or *now*
- <plantid>/evcc/loadpoints/{chargerId}/maxCurrent
- <plantid>/evcc/loadpoints/{chargerId}/connected
