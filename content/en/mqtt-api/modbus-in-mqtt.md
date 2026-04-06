---
title: "ModbusInMqtt"
weight: 50
translationKey: "modbus-in-mqtt"
---

# ModbusInMqtt Protocol

Communication protocol between GbbOptimizer and {{< glossary "GbbConnect2" >}} — transferring Modbus commands over MQTT.

## GbbOptimizer → GbbConnect2

{{< mqtt-topic topic="{PlantId}/ModbusInMqtt/toDevice" direction="publish" description="Modbus commands sent to GbbConnect2" >}}

| Field | | Type | Required | Description |
|-------|--|------|----------|-------------|
| `OrderId` | | string | no | Text copied to the response |
| `Lines` | | array | yes | |
| | `LineNo` | int | yes | Line number |
| | `Tag` | string | no | Arbitrary text copied to the response |
| | `Timestamp` | int | no | Unix UTC time (seconds) |
| | `Modbus` | string | yes | Modbus command to be sent to the inverter |
| `LogLevel` | | string | no | Change log level: `OnlyErrors`, `Min`, `Max` |
| `SendLastLog` | | int | no | 1 = attach logs to response (incrementally) |

**Example:**
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

{{< mqtt-topic topic="{PlantId}/ModbusInMqtt/fromDevice" direction="subscribe" description="Modbus responses from GbbConnect2" >}}

| Field | | Type | Required | Description |
|-------|--|------|----------|-------------|
| `OrderId` | | string | no | Copied from the request |
| `Error` | | string | yes | `"OK"` or error description (not related to a specific line) |
| `Lines` | | array | yes | |
| | `LineNo` | int | yes | Line number |
| | `Tag` | string | no | Copied from the request |
| | `Timestamp` | int | no | Unix UTC time |
| | `Modbus` | string | yes | Modbus response from the inverter (empty after the first error) |
| | `Error` | string | no | Empty = OK. Filled = error during communication with inverter |
| `GbbVersion` | | string | no | GbbConnect version |
| `GbbEnvironment` | | string | no | Environment: Windows, Console, Library |
| `LastLog` | | string | no | Logs since last send (if `SendLastLog=1`) |
