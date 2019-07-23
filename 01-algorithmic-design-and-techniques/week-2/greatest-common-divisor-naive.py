#!/user/bin/python

'''Naive Greatest Common Divisor
Check all candidate divisors:

Function NaiveGCD(a, b):
    best = 0
    for d from 1 to a + b:
        if d|a and d|b:
            best = d
    return best

Function EuclidGCD(a, b):
    a_prime = 0

    if b == 0:
        return a
    else:
        a_prime = a mod b  # remainder of a|b

    return Euclid(b, a_prime)

'''

import sys


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def euclid_gcd(a, b):
    a_prime = 0

    if b == 0:
        return a
    else:
        a_prime = a % b

    return euclid_gcd(b, a_prime)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
