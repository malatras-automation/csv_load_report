# CSV Load Report

A Python tool that reads circuit currents from a CSV file (for example an
Excel export), checks each circuit against the breaker rating and saves
the result to a text report.

## Input file format

Semicolon-separated, with decimal commas (the Excel default in most of
continental Europe, e.g. the Netherlands, Germany and Greece). Exports from
UK or US settings use commas and decimal points and are not supported yet.

```
circuit;current
Kitchen;12,3
Oven;17,8
```

A sample file, `circuits.csv`, is included.

## How it works

- Reads the CSV, skips the header and empty lines, and converts decimal commas.
- Splits the circuits into OK and OVERLOAD against the breaker rating.
- Builds the report once and writes it to `report.txt` and to the screen.
- Shows a clear message if the input file is missing.

## How to run

```
python csv_load_report.py
```

## Example output

```
--- Breaker load check (breaker 16 A) ---
✅ Kitchen: 12.3 A - OK
✅ Lights: 9.5 A - OK
✅ Sockets living room: 16.0 A - OK
❌ Oven: 17.8 A - OVERLOAD
❌ Heat pump: 21.4 A - OVERLOAD
❌ Electrical boiler: 18.7 A - OVERLOAD
------------------------------
✅ OK: 3
❌ OVERLOAD: 3
Report saved to report.txt 
```

## Author

Michalis Malatras, Electrical Engineer, learning Python for industrial automation.
