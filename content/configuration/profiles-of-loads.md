---
title: "Profiles of Loads"
weight: 60
---

# Profiles of Loads

Load profiles tell the optimizer how much energy your household typically consumes at each hour of each weekday. Accurate profiles improve optimization results.

## Manual Entry

Enter kWh values for each hour (0-23) and weekday (Mon-Sun) in the grid.

## Import from Plant

1. Set the import period (date range)
2. Press **"Import from Plant"**
3. The program calculates average loads for every hour and weekday from the imported data

### Automatic Nightly Import

Enable automatic data retrieval from VRM (last 28 days) by checking the appropriate option.

## Import from Excel

Copy-paste data from Excel with:
- Hours in rows (up to 24)
- Weekdays in columns (up to 7)

Rules:
- Empty cells remain unchanged
- Supports partial data (fewer than 24 rows or 7 columns)
- Extra rows/columns beyond standard dimensions are ignored

## Multiple Profiles

You can define multiple load profiles for different scenarios (e.g., summer vs. winter, holiday periods).

### Period Configuration

| Field | Description |
|-------|-------------|
| From Month/Day | When this profile becomes active |
| Profile name | Descriptive label |

The system supports automatic profile switching based on defined date ranges. Temporary holiday periods revert automatically when the period ends.
