#!/usr/bin/python

'''
Sum of Two Digits Problem
Compute the sum of two single digit numbers.
    Input: Two single digit numbers.
    Input Format: Integers a and b on the same line, separated by a space.

    Output: The sum of these numbers.
    Output Format: The sum of a and b.

    Constraints: 0 <= a, b <= 9

    SUMOFTWODIGITS(a,b):
    return a + b

'''

import sys

input = sys.stdin.read()
tokens = input.split()
a = int(tokens[0])
b = int(tokens[1])
print(a + b)
