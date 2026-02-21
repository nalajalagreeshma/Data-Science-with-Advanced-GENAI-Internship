#!/bin/python3

import sys

# Read input safely from stdin
try:
    n = int(sys.stdin.read())
except:
    n = 0  # fallback if no input provided

if n % 2 == 1:  # Odd
    print("Weird")
else:  # Even
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:  # n > 20
        print("Not Weird")