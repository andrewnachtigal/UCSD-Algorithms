#!/user/bin/python

'''primitive calculator
Given a primitive calculator that can perform three operations:
current number x:
    x * 2
    x * 3
    x + 1

Given a positive integer n, find the minimum number of operations to obtain
the number n, starting from the number 1.

Going from 1 to n is the same as going from n to 1, where instead of multiplying
and adding numbers, we divide and subtract:
    n / 3
    n / 2
    n - 1

'''

# Uses python3
import sys

def optimal_sequence(n):
    #numOperations = 0
    sequence = []
    while n >= 1:
        #numOperations += 1
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    #return numOperations
    return reversed(sequence)

def sequence_dp(n):
    temp = [0]*(n+1)
    for i in range(1, len(temp)):
        temp[i] = temp[i - 1] + 1
        if i % 3 == 0:
            temp[i] = min(temp[i], temp[i // 3] + 1)
        elif i % 2 == 0:
            temp[i] = min(temp[i], temp[i // 2] + 1)

    sequence = [1] * temp[-1]
    for i in range(1, temp[-1]):
        sequence[-i] = n
        if temp[n-1] == temp[n] -1:
            n -= 1
        elif n % 3 == 0 and (temp[n // 3] == temp[n] - 1):
            n //= 3
        else:  #n % 2 == 0 and (temp[n // 2] == temp[target] -1):
            n //= 2
    return sequence



input = sys.stdin.read()
n = int(input)
sequence = list(sequence_dp(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
