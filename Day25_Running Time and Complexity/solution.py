# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # check from 5 to sqrt(n), skipping even numbers
    limit = int(math.sqrt(n)) + 1
    for i in range(5, limit, 6):  # check i and i+2
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

t = int(input())  # number of test cases
for _ in range(t):
    n = int(input())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")
