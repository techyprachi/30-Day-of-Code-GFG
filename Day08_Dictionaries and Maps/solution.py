#!/bin/python3

import sys

# Read number of entries
n = int(input())
phone_book = {}

# Build the phone book
for _ in range(n):
    name, number = input().split()
    phone_book[name] = number

# Process queries until EOF
for line in sys.stdin:
    query = line.strip()
    if query in phone_book:
        print(f"{query}={phone_book[query]}")
    else:
        print("Not found")
