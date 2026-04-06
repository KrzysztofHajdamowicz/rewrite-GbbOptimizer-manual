---
title: "ModbusInMqtt"
weight: 50
---

# Protokół ModbusInMqtt

Protokół komunikacji między GbbOptimizer a {{< glossary "GbbConnect2" >}} — transfer komend Modbus przez MQTT.

## GbbOptimizer → GbbConnect2

{{< mqtt-topic topic="{PlantId}/ModbusInMqtt/toDevice" direction="publish" description="Komendy Modbus wysyłane do GbbConnect2" >}}

| Pole | | Typ | Wymagane | Opis |
|------|--|-----|---------|------|
| `OrderId` | | string | nie | Tekst skopiowany do odpowiedzi |
| `Lines` | | tablica | tak | |
| | `LineNo` | int | tak | Numer linii |
| | `Tag` | string | nie | Dowolny tekst skopiowany do odpowiedzi |
| | `Timestamp` | int | nie | Czas Unix UTC (sekundy) |
| | `Modbus` | string | tak | Komenda Modbus do przesłania do falownika |
| `LogLevel` | | string | nie | Zmień poziom logów: `OnlyErrors`, `Min`, `Max` |
| `SendLastLog` | | int | nie | 1 = dołącz logi do odpowiedzi (przyrostowo) |

**Przykład:**
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

{{< mqtt-topic topic="{PlantId}/ModbusInMqtt/fromDevice" direction="subscribe" description="Odpowiedzi Modbus z GbbConnect2" >}}

| Pole | | Typ | Wymagane | Opis |
|------|--|-----|---------|------|
| `OrderId` | | string | nie | Skopiowany z zapytania |
| `Error` | | string | tak | `"OK"` lub opis błędu (niezwiązany z konkretną linią) |
| `Lines` | | tablica | tak | |
| | `LineNo` | int | tak | Numer linii |
| | `Tag` | string | nie | Skopiowany z zapytania |
| | `Timestamp` | int | nie | Czas Unix UTC |
| | `Modbus` | string | tak | Odpowiedź Modbus z falownika (puste po pierwszym błędzie) |
| | `Error` | string | nie | Puste = OK. Wypełnione = błąd podczas komunikacji z falownikiem |
| `GbbVersion` | | string | nie | Wersja GbbConnect |
| `GbbEnvironment` | | string | nie | Środowisko: Windows, Console, Library |
| `LastLog` | | string | nie | Logi od poprzedniego wysłania (jeśli `SendLastLog=1`) |
