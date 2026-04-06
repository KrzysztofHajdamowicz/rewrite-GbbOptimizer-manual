---
title: "DongleDirect"
weight: 40
translationKey: "dongle-direct"
---

# DongleDirect

{{< glossary "DongleDirect" >}} works similarly to {{< glossary "GbbConnect2" >}} — it connects the inverter to GbbOptimizer, but **without installing additional software** on the local network. The dongle (WiFi logger) is redirected directly to the GbbOptimizer server.

> [!WARNING]
> From 2026-03-09 changing Dongle settings may not be possible on some models. In that case, a Dongle reset and restoration of original settings is required.

## Step-by-step configuration

1. Note the GbbOptimizer server name from the browser address (e.g. `gbboptimizer5.gbbsoft.pl`)
2. Log in to the Dongle — you must know its IP address on the local network (login: `admin`, password: `admin`)
3. Go to the page `http://<dongle_ip>/config_hide.html` (manually change the address in the browser)
4. **Take screenshots** of all current settings (in case you need to restore them!)
5. Change the **Server A Setting**:
   - Remove the IP address
   - Note the original Server A domain name
   - Change the domain to the GbbOptimizer server name (e.g. `gbboptimizer10.gbbsoft.pl`)
   - Port: `10000`
   - Connection: `TCP`
   - **Save + Restart**
6. Change the **Optional Server Setting** to the same data — **Save + Restart**
7. In GbbOptimizer, change the installation type to **DongleDirect** (or create a new one)
8. In the installation settings, enter:
   - **Inverter serial number**
   - **Dongle serial number** (digits only)
   - **Original Server A domain name** — if this field is empty, GbbOptimizer will not copy data to Solarman and Solarman/DeyeCloud will stop working
9. Save and wait **2-5 minutes** (the Dongle connects to the GbbOptimizer server after a few minutes)
10. The log should show entries such as:
    ```
    2025-06-21 11:00:27: From Dongle: A501001047F585579AF6A5005E15
    2025-06-21 11:00:28: From Server: A50A001017F685579AF6A50001AB745668780000008E15
    ```

## Dongle reset

If original Dongle settings need to be restored:

1. Find the reset button (small hole labeled "Reset" or "Reload") on the logger plugged into the inverter
2. With the **inverter powered on**, hold the button (e.g. with a pin) for **5-10 seconds**
3. The LEDs on the logger should go out and turn back on (or blink), indicating a restart
4. Open the **Solarman Smart** app on your phone
5. Select the **add device** option ("Add now" or "Configure")
6. Enter your home router WiFi credentials

> [!NOTE]
> If you enter the original Server A domain name in the GbbOptimizer installation settings, data will be copied to Solarman in both directions — you will retain full Solarman/DeyeCloud portal functionality.
