---
title: "Tuya"
weight: 30
translationKey: "tuya"
---

# Integration with Tuya

GbbOptimizer can control Tuya devices (e.g. smart sockets) via the Tuya Cloud API. This requires creating a developer project on the Tuya platform and obtaining API keys.

## Obtaining Access ID and Access Secret

### 1. Create a developer account

Register at [platform.tuya.com](https://platform.tuya.com/).

### 2. Create a Cloud Project

1. Go to **Cloud** -> **Development**
2. Click **Create Cloud Project** (top right corner)
3. Fill in the form:
   - Project name — any name
   - Industry — select the appropriate industry
   - Development Method — **Smart Home**
   - Data Center — select the one closest to your location
4. On the next screen click **Authorize**

### 3. Connect the mobile app

1. Go to **Devices** -> **Link App Account**
2. Click **Add App Account**
3. A QR code will appear
4. In the Tuya/Smart Life mobile app: **Me** (bottom menu) -> scan icon (top right corner)
5. Scan the QR code

After connecting, a list of your devices will appear in the **All Devices** tab.

### 4. Copy API keys

In the **Overview** tab you will find:

- **Access ID / Client ID**
- **Access Secret / Client Secret**

Enter these in the GbbOptimizer configuration under IoT -> Tuya.

## Extending the Trial Period

Tuya API keys have a limited trial period. To extend it:

1. Log in to [platform.tuya.com](https://platform.tuya.com/)
2. Go to **Cloud** -> **Cloud Services**
3. Select **IoT Core** and click **View Details**
4. Click **Extend Trial Period** and follow the instructions

> [!WARNING]
> If the trial period expires, GbbOptimizer will lose the ability to control Tuya devices. Remember to extend it regularly.
