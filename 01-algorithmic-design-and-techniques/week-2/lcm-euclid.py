#!/user/bin/python

'''Least Common Multiple
Smallest positive integer that is perfectly divisible by two given numbers.

To get the LCM of two numbers, multiply them and divide the result by their
euclid GCD.
'''

import sys


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def euclid_gcd(a, b):
    a_prime = 0

    if b == 0:
        return a
    else:
        a_prime = a % b

    return euclid_gcd(b, a_prime)


def lcm_fast(a, b):

    return int((a * b) // euclid_gcd(a, b))


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))
