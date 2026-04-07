---
title: "DeyeCloud"
weight: 20
translationKey: "deye-cloud"
---

# DeyeCloud

{{< badge "deye-only" >}}

DeyeCloud is a backup connection method available for **Solarman**-type installations. It can be used as a fallback in case of Solarman issues, or as the sole connection.

## Operating modes

| Mode | Description |
|------|-------------|
| **Disabled** | DeyeCloud is not used |
| **Enabled** | DeyeCloud activates automatically when Solarman reports an error |
| **Backup only** | Do not use Solarman — always use DeyeCloud |

## Configuration

1. In the **Backup connection — DeyeCloud** section of the installation parameters, select the operating mode
2. Enter the **login credentials** for DeyeCloud (may differ from Solarman)
3. Check **Remember login credentials** — without this, manual re-login is required
4. After connecting, select the **inverter SerialNo**

A detailed description of the parameters can be found in [Installation parameters]({{< relref "/installation/installation-parameters" >}}).

> [!NOTE]
> DeyeCloud and Solarman are two independent portals with separate login credentials. Make sure you have an account in both services if you want to use the backup connection.
