---
title: "ModbusInMqtt"
weight: 50
---

# ModbusInMqtt Protocol

The {{< glossary "ModbusInMqtt" >}} protocol is used for communication between {{< glossary "GbbConnect2" >}} and GbbOptimizer. {{< glossary "Modbus" >}} commands are wrapped in MQTT messages for cloud-based inverter control.

## Topics

{{< mqtt-topic topic="{PlantId}/ModbusInMqtt/toDevice" direction="publish" description="Commands from GbbOptimizer to GbbConnect2" >}}

{{< mqtt-topic topic="{PlantId}/ModbusInMqtt/fromDevice" direction="subscribe" description="Responses from GbbConnect2 to GbbOptimizer" >}}

---

## Request Format

{{< mqtt-endpoint name="ModbusInMqtt Request" topic="{PlantId}/ModbusInMqtt/toDevice" direction="publish" description="Send Modbus commands to the inverter via GbbConnect2" >}}

### Payload

```json
{
  "OrderId": "abc123",
  "Lines": [
    {
      "LineNo": 1,
      "Tag": "read_soc",
      "Timestamp": 1713600000,
      "Modbus": "01 03 00 60 00 01"
    }
  ],
  "LogLevel": "Min",
  "SendLastLog": true
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `OrderId` | string | no | Identifier echoed in the response |
| `Lines` | array | yes | Array of Modbus command objects |
| `Lines[].LineNo` | number | yes | Sequential line number |
| `Lines[].Tag` | string | no | Optional descriptive tag |
| `Lines[].Timestamp` | number | no | Unix timestamp (seconds) |
| `Lines[].Modbus` | string | yes | Modbus command in hex |
| `LogLevel` | string | no | `"OnlyErrors"`, `"Min"`, or `"Max"` |
| `SendLastLog` | boolean | no | Request incremental log lines |

{{< /mqtt-endpoint >}}

## Response Format

{{< mqtt-endpoint name="ModbusInMqtt Response" topic="{PlantId}/ModbusInMqtt/fromDevice" direction="subscribe" description="Responses from GbbConnect2 with Modbus data" >}}

### Payload

```json
{
  "OrderId": "abc123",
  "Error": "OK",
  "Lines": [
    {
      "LineNo": 1,
      "Tag": "read_soc",
      "Modbus": "01 03 02 00 4B"
    }
  ],
  "GbbVersion": "2.1.0",
  "GbbEnvironment": "Docker",
  "LastLog": "..."
}
```

| Field | Type | Description |
|-------|------|-------------|
| `OrderId` | string | Echoed from request |
| `Error` | string | `"OK"` or error message |
| `Lines` | array | Modbus responses from inverter |
| `Lines[].LineNo` | number | Matching line number from request |
| `Lines[].Modbus` | string | Modbus response data in hex |
| `GbbVersion` | string | GbbConnect2 version (optional) |
| `GbbEnvironment` | string | Runtime environment (optional) |
| `LastLog` | string | Incremental log output (if requested) |

### Error Handling

Lines are processed sequentially. If an error occurs, transmission stops at the first failed line.

{{< /mqtt-endpoint >}}
