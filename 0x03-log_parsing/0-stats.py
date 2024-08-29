#!/usr/bin/python3
"""The sys module to read from stdin.
   The signal module handle keyboard interruptions."""
import signal
import sys


def display_status(total_size, status_codes):
    """This function will be responsible for printing the total file size
    and the count of each status code."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if code > 0:
            print(f"{code}: {status_codes[code]}")


total_size = 0
i = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0}


"""Loop through each line in stdin,  and update the metrics"""
for line in sys.stdin:
    i += 1
    temp = line.split()
    if len(temp) < 7:
        continue

    try:
        code = int(temp[-2])
        file_size = int(temp[-1])
        total_size += file_size
        if code in status_codes:
            status_codes[code] += 1

    except (ValueError, IndexError):
        continue

    if i % 10 == 0:
        """ After the loop ends, if there are any lines left,
      print the statistics one last time.python"""
        display_status(total_size, status_codes)


def Interrupt_signal(sig, frame):
    """This function will handle CTRL + C (keyboard interruption)
    to print statistics before the program exits."""
    display_status(total_size, code)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
