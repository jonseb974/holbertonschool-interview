#!/usr/bin/python3
"""
0-log_parsing
"""


import sys
from collections import defaultdict


def parse_line(line):
    """
    Define a function to parse the input line
    and return the IP address,
    status code, and file size
    """
    parts = line.split()
    if len(parts) != 7:
        return None
    ip_address, _, _, timestamp, _, status_code, file_size = parts
    try:
        status_code = int(status_code)
        file_size = int(file_size)
    except ValueError:
        return None
    return ip_address, status_code, file_size

# Initialize variables to keep track of the total file size and
# the number of lines by status code


total_size = 0
lines_by_status = defaultdict(int)
num_lines = 0


# Define a function to print the statistics
def print_statistics():
    print(f"Total file size: {total_size}")
    for status_code in sorted(lines_by_status.keys()):
        print(f"{status_code}: {lines_by_status[status_code]}")


# Loop over stdin, reading one line at a time
try:
    for line in sys.stdin:
        # Parse the input line
        parsed = parse_line(line.strip())
        if parsed is None:
            continue
        ip_address, status_code, file_size = parsed

        # Update the total file size and the number of lines by status code
        total_size += file_size
        lines_by_status[status_code] += 1
        num_lines += 1

        # Print statistics every 10 lines
        if num_lines % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # If the user interrupts the script, print the final statistics
    print_statistics()
