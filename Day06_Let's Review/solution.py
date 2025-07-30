#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        even_chars = s[::2]
        odd_chars = s[1::2]
        print(f"{even_chars} {odd_chars}")
