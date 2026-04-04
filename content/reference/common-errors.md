---
title: "Common Errors"
weight: 20
---

# Most Common Errors

Error messages received by email from GbbOptimizer, organized by subsystem.

## Solarman Connection

| Error | Cause |
|-------|-------|
| Timeout | Unable to communicate with inverter via Solarman. Check local network connectivity or verify the inverter is transmitting data to Solarman. |

## DeyeCloud

| Error | Cause |
|-------|-------|
| Timeout | Connection timeout to DeyeCloud service |
| Device offline | Inverter not communicating with DeyeCloud — check local network |
| Insufficient permissions | Account lacks required access — often related to installer-restricted accounts |

## GbbConnect2 (Local Dongle)

| Error | Cause |
|-------|-------|
| Timeout | Cannot reach the local GbbConnect2 instance — verify it is running |
| Dongle offline | Physical Deye dongle lost network connectivity |

## Victron

| Error | Cause |
|-------|-------|
| MQTT connection failed | Cannot communicate with Cerbo via Victron's servers — check VRM credentials and Cerbo connectivity |

## External API Failures

| Service | Common Issues |
|---------|--------------|
| Solcast | Rate limiting (exceeded free API quota) |
| ENTSO-E | API service temporarily unavailable |
| Tibber | Authentication or API connectivity issues |
| Amber | API connectivity issues |
| Pstryk | Cache service issues |
| Hinen | Service connectivity issues |
