import sys
import signal


def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


def print_statistics():
    print("Total file size: File size:", total_file_size)
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print(f"{status_code}: {status_codes[status_code]}")


def process_line(line):
    parts = line.strip().split()
    if len(parts) != 10:
        return

    ip_address, date, method, url, http_version, status_code_str,
    file_size_str = parts

    try:
        status_code = int(status_code_str)
        file_size = int(file_size_str)

        if status_code in status_codes:
            status_codes[status_code] += 1
        total_file_size[0] += file_size

    except ValueError:
        pass


status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_file_size = [0]

# Set up the signal handler to catch CTRL + C
signal.signal(signal.SIGINT, signal_handler)

line_count = 0
try:
    for line in sys.stdin:
        process_line(line)
        line_count += 1
        if line_count % 10 == 0:
            print_statistics()
except KeyboardInterrupt:
    pass

print_statistics()
