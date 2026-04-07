---
title: "Solarman"
weight: 10
translationKey: "solarman"
---

# Solarman

Solarman is a cloud-based method for connecting an inverter to GbbOptimizer. Data passes through Solarman servers — no additional software installation required.

## Step-by-step configuration

1. Add an installation: **Add new installation with inverter connected to Solarman**
2. Fill in the fields up to the "Solarman" group (details in [Installation parameters]({{< relref "/installation/installation-parameters" >}}))
3. Log in to the Solarman servers: enter your **email** and **password** (the same as for the Solarman app) and press **Connect**
4. Select your inverter from the list **Select inverter SerialNo**
5. Select the **Inverter type**

   > [!WARNING]
   > Do not mix up the inverter type! An incorrect selection and data transmission requires a factory reset of the inverter.

6. Press **Test connection to inverter** — the program will retrieve the current {{< glossary "SOC" >}} from the inverter. Check that the value is correct. In the Log module you will find more information from the inverter
7. Continue filling in the battery fields and press **Continue in Quick Setup**

## Control via voltage (V) instead of SOC

If you prefer to control the battery by voltage instead of {{< glossary "SOC" >}}:

1. Check **Control via V, not SOC**
2. Press **Edit SOC to V mapping**
3. Enter at least **two known pairs** of SOC and V so the program can create a mapping. The more pairs — the more accurate the mapping

> [!NOTE]
> The mapping is **proportional (linear)** — the program interpolates based on the two nearest points.

## GbbShunt

GbbShunt is a module designed to control lead-acid batteries. It performs two functions (normally carried out by the inverter):

- **Calculates {{< glossary "SOC" >}}** based on energy sent to and drawn from the battery
- **Ends charging/discharging** upon reaching the indicated SOC level

### GbbShunt parameters

A detailed description of GbbShunt parameters can be found in [Installation parameters]({{< relref "/installation/installation-parameters" >}}).

### How does GbbShunt calculate SOC?

1. Based on the difference between the initial and current energy sent/drawn from the battery, it calculates the energy increment
2. By dividing the current energy by the total battery capacity, it obtains the **Calculated SOC**
3. When the Calculated SOC < 0 or SOC > 100, or the battery voltage reaches the levels set in the parameters — a **data reset** occurs: the program remembers the current values as initial values
4. On first startup (or after a break of > 12 hours), the program calculates the initial energy based on the SOC fetched from the inverter
5. Calculations are performed **every minute**

### How does GbbShunt control the end of charging/discharging?

1. When sending data to the inverter, GbbShunt receives information about the target SOC for the current hour
2. **Charging**: when the Calculated SOC ≥ target SOC — a stop occurs. If the SOC drops below the target SOC - 5% within the same hour, charging will resume
3. **Discharging**: when the Calculated SOC ≤ target SOC — a stop occurs. If the SOC rises above the target SOC + 5% within the same hour, discharging will resume
4. Ending charging/discharging sends the **Normal** operation to the inverter

> [!NOTE]
> It is good if the inverter sends data to Solarman **every 1 minute** (default is every 5 minutes). Change this parameter in the inverter settings.

### GbbShunt Monitor

The GbbOptimizer interface includes a GbbShunt monitor that displays the current state of the module:

- **Calculated SOC** — current SOC calculated by GbbShunt
- **Battery voltage** — current voltage read from the inverter
- **Battery energy** — calculated energy (kWh) above MinSOC
- **Charging / discharging state** — whether GbbShunt has stopped charging or discharging

The monitor is useful for verifying that GbbShunt is correctly calculating SOC and responding to voltage thresholds.
