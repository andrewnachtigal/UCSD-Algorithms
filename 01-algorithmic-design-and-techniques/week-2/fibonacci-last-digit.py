#!/usr/bin/python

'''Last Digit of a Large Fibonacci Number
Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number 𝐹𝑛
(that is, 𝐹𝑛 mod 10).
Input: an integer n
s.t. 0 <= n <= 10^7
Output: last digit of 𝐹𝑛

FibonacciLastDigit(n):
    F[0] = 0
    F[1] = 1
    for i from 2 to n:
        F[i] = F[i -1] + F[i -2]
    print(F[n] mod 10)

'''

import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_fast(n):
    fib = []
    fib.append(0)
    fib.append(1)

    for i in range(2, n + 1):
        fib.append((fib[i - 1] + fib[i - 2]) % 10)

    return fib[n]


if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit_fast(n))
    # print(get_fibonacci_last_digit_naive(n))
