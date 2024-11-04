#!/usr/bin/python3
"""
log parsing
"""


import sys
import signal


# Initialize counters and data structures
total_file_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
valid_status_codes = set(status_code_counts.keys())
line_count = 0


def print_statistics():
    """Print the accumulated statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def handle_interrupt(signal, frame):
    """Handle keyboard interruption (CTRL + C) and print statistics."""
    print_statistics()
    sys.exit(0)

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_interrupt)


try:
    for line in sys.stdin:
        line_count += 1
        try:
            parts = line.split()
            # Validate and extract components of the line
            if len(parts) < 7:
                continue
            ip_address = parts[0]
            date = parts[3] + " " + parts[4]
            method = parts[5].strip("\"")
            resource = parts[6]
            protocol = parts[7].strip("\"")
            status_code = parts[8]
            file_size = int(parts[9])

            # Validate the request format
            if method != "GET" or resource != "/projects/260" or protocol != "HTTP/1.1":
                continue

            # Update total file size
            total_file_size += file_size

            # Update status code count if valid
            if status_code in valid_status_codes:
                status_code_counts[status_code] += 1

        except (IndexError, ValueError):
            # Skip lines that don't match the expected format
            continue

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Handl keyboard interruption (CTRL + C) and print statistics
    print_statistics()
    sys.exit(0)
