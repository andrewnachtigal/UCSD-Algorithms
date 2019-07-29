#!/user/bin/python

'''Fibonacci Number Modulo m

    Compute the nth Fibonacci number modulo m.
        Input: Integers 0 <= n <= 10^18 and 2 <= m <= 10^5
        Output: nth Fibonacci number modulo m, F(n) mod m.

        To compute F(n) mod m, calculate the remainder of n mod length...

        ...

        A Pisano period is the period of an integer sequence which is
        obtained by reducing each term of a primary sequence modulo some integer
        m ≥ 1.

        The Pisano period is defined as the length of the period of the sequence obtained
        by reading the Fibonacci sequence modulo m



'''

import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_fast(n, m):
    '''Calculate length of Pisano Period given m:



    '''

    return current % m


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
