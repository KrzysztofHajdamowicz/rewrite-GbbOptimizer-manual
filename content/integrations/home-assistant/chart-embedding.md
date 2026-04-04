---
title: "Chart Embedding"
weight: 40
---

# Embedding Charts in Home Assistant

Display GbbOptimizer Battery Forecast charts directly in your Home Assistant dashboard.

## URL Format

```
https://<address>/Forecast/IndexChart?PlantId=<PlantId>&PlantToken=<PlantToken>&NoMenu=1
```

## URL Encoding

Special characters in the PlantToken must be URL-encoded:

| Character | Encoding |
|-----------|----------|
| `+` | `%2b` |
| `/` | `%2f` |

## Dark Mode

Append `&DarkMode=1` to the URL for dark theme support:

```
https://<address>/Forecast/IndexChart?PlantId=<PlantId>&PlantToken=<PlantToken>&NoMenu=1&DarkMode=1
```
