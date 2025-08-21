#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())
    names = []

    for _ in range(N):
        firstName, emailID = input().rstrip().split()
        if emailID.endswith('@gmail.com'): 
            names.append(firstName)

    names.sort()
    print('\n'.join(names))
