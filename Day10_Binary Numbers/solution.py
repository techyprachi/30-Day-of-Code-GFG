#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    # convert number to binary (without '0b')
    binary = bin(n)[2:]

    # split by '0' to get groups of consecutive '1's
    groups = binary.split('0')

    # find max length of consecutive '1's
    max_consecutive_ones = max(len(group) for group in groups)

    print(max_consecutive_ones)
