#!/usr/bin/python3
""""
0-log_parsing
"""


import sys


def extract_status_code(line):
    """
    Define a function to extract the status code from a log line
    """
    fields = line.split()
    if len(fields) < 8:
        return None
    try:
        status_code = int(fields[7])
        return status_code
    except ValueError:
        return None

# Initialize variables to hold the statistics


total_size = 0
status_counts = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
    }
line_count = 0

# Read lines from standard input
for line in sys.stdin:
    line_count += 1

    # Extract the file size from the log line
    fields = line.split()
    if len(fields) < 8:
        continue
    try:
        file_size = int(fields[8])
    except ValueError:
        continue

    # Extract the status code from the log line and update the status count
    status_code = extract_status_code(line)
    if status_code is not None and status_code in status_counts:
        status_counts[status_code] += 1

    # Update the total file size
    total_size += file_size

    # If we've reached the end of a block of 10 lines,
    # or if we've received a keyboard interrupt, print the statistics
    if line_count % 10 == 0:
        print("File size:", total_size)
        for status_code in sorted(status_counts.keys()):
            count = status_counts[status_code]
            if count > 0:
                print("{}: {}".format(status_code, count))
        print()
        sys.stdout.flush()

print("File size:", total_size)
for status_code in sorted(status_counts.keys()):
    count = status_counts[status_code]
    if count > 0:
        print("{}: {}".format(status_code, count))
sys.stdout.flush()
