---
title: "DongleDirect"
weight: 40
---

# DongleDirect

{{< glossary "DongleDirect" >}} works similarly to GbbConnect2 — it establishes a connection between GbbOptimizer and the inverter without requiring local software. The WiFi dongle is reconfigured to communicate directly with GbbOptimizer's server.

## Setup

1. Note your GbbOptimizer server name from the browser address bar
2. Access the dongle's admin interface using default credentials
3. Navigate to the hidden configuration page at the dongle's IP address
4. **Screenshot all existing settings** for reference
5. Modify **Server A** settings — replace the IP with your GbbOptimizer domain (port 10000, TCP)
6. Apply identical settings to the **Optional Server** section
7. Change the plant type to **DongleDirect** in GbbOptimizer
8. Enter: inverter serial number, dongle serial number, and original domain name
9. Save and wait 2-5 minutes for connection
10. Verify through server logs

## Optional: Data Relay to Solarman

DongleDirect can optionally relay data bidirectionally to Solarman servers, so you don't lose access to the Solarman monitoring portal.

## Dongle Reset

If you need to reset the dongle:
1. Press the reset button for 5-10 seconds
2. Verify LED status changes
3. Reconfigure through the Solarman Smart mobile application
