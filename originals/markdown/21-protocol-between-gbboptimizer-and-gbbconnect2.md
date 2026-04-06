# 1. Protocol between GbbConnect2 and GbbOptimizer (ModbusInMqtt)

Protocol uses mqtt server to transfer messages.

## Message from GbbOptimizer to GbbConnect2

Topic with data send to GbbConnect2: {plantId}/ModbusInMqtt/toDevice

Payload:

|  |  |  |  |
| --- | --- | --- | --- |
| Key |  | type | remarks |
| OrderId |  | string(255), optional | Any text copied from request to answer |
| Lines |  | table of objects |  |
|  | LineNo | int, required | Number of line |
|  | Tag | string(255), optional | Any string copied from requst to answer |
|  | Timestamp | int, optional | Current time in Unix seconds UTC |
|  | Modbus | string, required | Modbus command to transfer to inverter |
| LogLevel |  | string.optional | Change log level to: OnlyErrors, Min, Max |
| SendLastLog |  | int, optional | 1-in answer send increametally log (new lines from previous sending) |

example:

{"Lines":
 [{"LineNo":0,"Timestamp":1746136816,"Modbus":"010300D6000225F3"},

{"LineNo":1,"Timestamp":1746136816,"Modbus":"0103020800024471"},

{"LineNo":2,"Timestamp":1746136816,"Modbus":"0103020E0001E471"},

{"LineNo":3,"Timestamp":1746136816,"Modbus":"010302110001D5B7"},
 {"LineNo":4,"Timestamp":1746136816,"Modbus":"01030218000105B5"}
],"OrderId":"f0PGI3obQIZTs8w="}

## Message from GbbConnec2 to GbbOptimizer

Topic with data send to GbbOptimizer: {plantId}/ModbusInMqtt/fromDevice

Payload:

|  |  |  |  |
| --- | --- | --- | --- |
| Key |  | type | remarks |
| OrderId |  | string(255), optional | Any text copied from request to answer |
| Error |  | string, required | OK or error message (error not connected with line) |
| Lines |  | table of objects |  |
|  | LineNo | int, required | Number of line |
|  | Tag | string(255), optional | Any string copied from requst to answer |
|  | Timestamp | int, optional | Current time in Unix seconds UTC (can be coppied from request message) |
|  | Modbus | string, required | Modbus command received from inverter. After first line with Error this field is absent (or empty) |
|  | Error | string | not present (or empty) = OK, no error, in Modbus there is answer from inverter  else: error during sending message to inverter connected with this line, also error from answer Modbus string.  After first line program doesn't sent next lines to inverter  (field Modbus are missing or empty) |
| GbbVersion |  | string, optional | GbbConnect version |
| GbbEnvironment |  | string, optional | GbbConnect enviroment: Windows, Console, Library, etc |
| LastLog |  | string | If SendLastLog=1 then new lines from log from previous sending |

example:

{"Lines":
[{"LineNo":0,"Timestamp":1746136816,"Modbus":"010304000F14338525"},
{"LineNo":1,"Timestamp":1746136816,"Modbus":"01030401020176DA79"},
{"LineNo":2,"Timestamp":1746136816,"Modbus":"0103020115781B"},
{"LineNo":3,"Timestamp":1746136816,"Modbus":"010302018E39B0"},
{"LineNo":4,"Timestamp":1746136816,"Modbus":"0103020000B844"}
],"OrderId":"f0PGI3obQIZTs8w="}
