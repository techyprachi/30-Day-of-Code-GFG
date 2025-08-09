#!/bin/python3

import sys

S = input().strip()   # Yeh strip hidden cases ke liye zaroori hai

try:
    print(int(S))
except ValueError:
    print("Bad String")
