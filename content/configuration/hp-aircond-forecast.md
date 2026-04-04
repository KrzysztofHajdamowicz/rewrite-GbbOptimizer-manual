---
title: "HP / AirCond Forecast"
weight: 80
---

# Heat Pump & Air Conditioning Forecast

This module handles forecasting for heat pumps (HP) and air conditioning systems, which represent significant variable loads that affect battery optimization.

## Overview

Heat pumps and air conditioning units consume substantial energy that varies with weather conditions. By forecasting these loads, GbbOptimizer can better plan battery charge/discharge cycles.

## Configuration

Configure HP/AC parameters to enable the forecasting engine to account for these loads in the battery optimization plan.

## MQTT Control

Heat pump scheduling can be controlled via MQTT — see [Set HP Parameters]({{< relref "/mqtt-api/data-commands#endpoint-sethp" >}}) for the API reference.
