# Baseline Solutions Package

This document contains the source code for the manual solutions (without AI) for the benchmark tasks.

## Directory Structure
- /baseline/task1_log_parser.py
- /baseline/task2_UserCard.tsx
- /baseline/task3_sales_analysis.sql
- /baseline/notes.md

---

### File: /baseline/task1_log_parser.py

```python
import re
import csv
from collections import Counter
import sys
import os

def parse_logs(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Warning: Input file '{input_file}' not found.")
        return

    error_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*\[ERROR\] (.*)')
    errors = []

    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()
            if not lines:
                print("Warning: Log file is empty.")
                return

            for line in lines:
                match = error_pattern.search(line)
                if match:
                    # extracting timestamp (group 1) and message (group 2)
                    # For this task, we only count messages
                    errors.append(match.group(2))
        
        # Count frequencies
        error_counts = Counter(errors)
        
        # Write to CSV
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Error Message', 'Count'])
            for error, count in error_counts.most_common():
                writer.writerow([error, count])
        
        # Console output for most frequent
        if error_counts:
            most_common = error_counts.most_common(1)[0]
            print(f"Most frequent error: '{most_common[0]}' (Count: {most_common[1]})")
        else:
            print("No errors found.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    # Ensure a dummy server.log exists before running or handle the warning
    parse_logs('server.log', 'error_summary.csv')
