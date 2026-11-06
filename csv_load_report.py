"""
CSV load report: reads circuit currents from a CSV file (exported from Excel),
compares them against the breaker rating and saves a report to a text file.
"""

# Constants
BREAKER = 16           #A
INPUT_FILE = "circuits.csv"
REPORT_FILE = "report.txt"

def read_circuits(filename):
    """ Read (name, current) pairs from a semicolon csv with decimal commas."""
    circuits = []
    with open(filename, encoding="utf-8")  as file:
        file.readline()     # skip the header
        for line in file:
            line = line.strip()
            if line == "":
                continue            # skip empty lines
            name, current = line.split(";")  
            current = float(current.replace(",", "." )) 
            circuits.append((name, current))
    return circuits

def built_report(circuits, breaker):
    """ Return the report as a list of text lines."""
    ok_lines = []
    over_lines = []
    for name, current in circuits:
        if current <= breaker:
            ok_lines.append(f"✅ {name}: {current} A - OK")
        else: 
            over_lines.append(f"❌ {name}: {current} A - OVERLOAD")

    lines = [f"--- Breaker load check (breaker {breaker} A) ---"]
    lines = lines + ok_lines + over_lines
    lines.append("-" * 30)
    lines.append(f"✅ OK: {len(ok_lines)}")
    lines.append(f"❌ OVERLOAD: {len(over_lines)}")
    return lines

# Main program
try:
    circuits = read_circuits(INPUT_FILE)
except FileNotFoundError:
    print(f"File '{INPUT_FILE}' not found. Check the name and the folder.")
    quit()

report_lines = built_report(circuits, BREAKER)

with open(REPORT_FILE, "w", encoding="utf-8") as report:
    for line in report_lines:
        report.write(line + "\n")

for line in report_lines:
    print(line)

print(f"Report saved to {REPORT_FILE}")
