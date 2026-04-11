---
title: "ModbusInMqtt"
weight: 50
translationKey: "modbus-in-mqtt"
---

# ModbusInMqtt-protocol

Protocol voor communicatie tussen GbbOptimizer en {{< glossary "GbbConnect2" >}} — het overbrengen van Modbus-commando's via MQTT.

## GbbOptimizer → GbbConnect2

{{< mqtt-topic topic="{PlantId}/ModbusInMqtt/toDevice" direction="publish" description="Modbus-commando's verstuurd naar GbbConnect2" >}}

| Veld | | Type | Vereist | Beschrijving |
|------|--|-----|---------|------|
| `OrderId` | | string | nee | Tekst die naar het antwoord wordt gekopieerd |
| `Lines` | | array | ja | |
| | `LineNo` | int | ja | Regelnummer |
| | `Tag` | string | nee | Willekeurige tekst die naar het antwoord wordt gekopieerd |
| | `Timestamp` | int | nee | Unix-tijd UTC (seconden) |
| | `Modbus` | string | ja | Modbus-commando om naar de omvormer te sturen |
| `LogLevel` | | string | nee | Wijzig logniveau: `OnlyErrors`, `Min`, `Max` |
| `SendLastLog` | | int | nee | 1 = logs bij het antwoord voegen (incrementeel) |

**Voorbeeld:**
```json
{
  "Lines": [
    {"LineNo": 0, "Timestamp": 1746136816, "Modbus": "010300D6000225F3"},
    {"LineNo": 1, "Timestamp": 1746136816, "Modbus": "0103020800024471"}
  ],
  "OrderId": "f0PGI3obQIZTs8w="
}
```

## GbbConnect2 → GbbOptimizer

{{< mqtt-topic topic="{PlantId}/ModbusInMqtt/fromDevice" direction="subscribe" description="Modbus-antwoorden uit GbbConnect2" >}}

| Veld | | Type | Vereist | Beschrijving |
|------|--|-----|---------|------|
| `OrderId` | | string | nee | Gekopieerd uit de request |
| `Error` | | string | ja | `"OK"` of foutbeschrijving (niet gekoppeld aan een specifieke regel) |
| `Lines` | | array | ja | |
| | `LineNo` | int | ja | Regelnummer |
| | `Tag` | string | nee | Gekopieerd uit de request |
| | `Timestamp` | int | nee | Unix-tijd UTC |
| | `Modbus` | string | ja | Modbus-antwoord uit de omvormer (leeg na de eerste fout) |
| | `Error` | string | nee | Leeg = OK. Ingevuld = fout tijdens communicatie met de omvormer |
| `GbbVersion` | | string | nee | Versie van GbbConnect |
| `GbbEnvironment` | | string | nee | Omgeving: Windows, Console, Library |
| `LastLog` | | string | nee | Logs sinds de vorige verzending (indien `SendLastLog=1`) |
