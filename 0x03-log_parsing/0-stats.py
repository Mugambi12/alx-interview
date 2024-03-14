#!/usr/bin/python3
import sys
import signal

# Function to parse each line and extract relevant information
def parse_line(line):
    parts = line.split()
    if len(parts) != 10 or parts[8] != '"GET' or parts[9] != '/projects/260':
        return None, None, None, None
    ip_address = parts[0]
    status_code = int(parts[7])
    file_size = int(parts[8])
    return ip_address, status_code, file_size

# Function to print statistics
def print_statistics(total_size, status_counts):
    print(f"File size: {total_size}")
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{code}: {count}")

def main():
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    lines_read = 0

    try:
        for line in sys.stdin:
            # Parse each line
            ip, code, size = parse_line(line.strip())
            if ip is None:
                continue

            # Update total file size
            total_size += size

            # Update status code count
            if code in status_counts:
                status_counts[code] += 1

            lines_read += 1

            # Print statistics every 10 lines
            if lines_read % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle CTRL + C interruption
        print_statistics(total_size, status_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
