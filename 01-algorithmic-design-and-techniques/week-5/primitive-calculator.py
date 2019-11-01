#!/user/bin/python

'''primitive calculator
given a primitive calculator that can perform three operations:
current number x
    x * 2
    x * 3
    x + 1

Given a positive integer n, find the minimum number of operations to obtain
the number n starting from the number 1.


'''

# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
