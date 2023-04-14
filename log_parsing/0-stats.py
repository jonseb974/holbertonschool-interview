#!/usr/bin/python3
import random
import sys

# Define the possible status codes
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

# Initialize the counters
total_size = 0
line_counts = {code: 0 for code in status_codes}

try:
    # Read from standard input line by line
    for i, line in enumerate(sys.stdin):
        # Skip lines that don't match the expected format
        try:
            ip, _, date, request, status_code_str, file_size_str, _ = line.split()
            status_code = int(status_code_str)
            file_size = int(file_size_str)
        except ValueError:
            continue
        
        # Update the counters
        total_size += file_size
        line_counts[status_code] += 1
        
        # Print the statistics every 10 lines
        if (i + 1) % 10 == 0:
            print(f'Total file size: {total_size}')
            for code in sorted(line_counts.keys()):
                if line_counts[code] > 0:
                    print(f'{code}: {line_counts[code]}')
        
except KeyboardInterrupt:
    # Handle keyboard interruption
    print(f'Total file size: {total_size}')
    for code in sorted(line_counts.keys()):
        if line_counts[code] > 0:
            print(f'{code}: {line_counts[code]}')
