# AI-Assisted Solutions Package

This document contains the source code for the solutions generated using GitHub Copilot for the benchmark tasks.

## Directory Structure
- /with_ai/task1_log_parser.py
- /with_ai/task2_UserCard.tsx
- /with_ai/task3_sales_analysis.sql
- /with_ai/notes.md

---

### File: /with_ai/task1_log_parser.py

```python
import re
import csv
from collections import Counter
import os

def parse_server_logs(input_file='server.log', output_file='error_summary.csv'):
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    error_pattern = re.compile(r'\[ERROR\]\s+(.*)')
    error_messages = []

    try:
        with open(input_file, 'r') as f:
            for line in f:
                if '[ERROR]' in line:
                    match = error_pattern.search(line)
                    if match:
                        error_messages.append(match.group(1).strip())
        
        # Count frequencies
        counter = Counter(error_messages)

        # Write to CSV
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Error Message', 'Count'])
            for error, count in counter.most_common():
                writer.writerow([error, count])
        
        # Print most frequent error
        if counter:
            most_common = counter.most_common(1)[0]
            print(f"Top Error: {most_common[0]} (Count: {most_common[1]})")
        else:
            print("No errors found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parse_server_logs()
