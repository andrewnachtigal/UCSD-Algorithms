#!/user/bin/python

'''Knapsack - Maximum amount of Gold (knapsack with single selection)
Given a set of gold bars take as much gold as possible in knapsack. One copy of
each bar and each bar can be taken or not.

Given n gold bars, find the maximum weight of gold that fits into a
bag of capacity W.

# knapsack with repetitions
Knapsack(W):
value(0) = 0
for w from 1 to W:
    value(w) = 0
    for i from 1 to n:
        if wi <= w:
            val = value(w - wi) + vi
            if val > value(w):
                value(w) = val
return value(W)

runtime: O(nW)


# knapsack with memoization
Knapsack(W):
if w is in hash table:
    return value(w)
value(w) = 0
for i from 1 to n:
    if wi <= w:
        val = Knapsack(w-wi) + vi
        if val > value(w):
            value(w) = val
insert value(w) into hash table with key w
return value(w)

runtime: O(nW)

'''

import sys

def optimal_weight(W, w):
    n = len(w)
    # table
    K = [[0 for x in range(W + 1)] for z in range(n + 1)]

    # recurrence
    # i total number of items
    # x weight of knapsack
    for i in range(1, n + 1):
        for x in range(1, W + 1):
            if i == 0 or x == 0:
                K[i][x] = 0

            K[i][x] = K[i - 1][x]
            if w[i - 1] <= x:
                value = K[i - 1][x - w[i - 1]] + w[i -1]
                if value > K[i][x]:
                    K[i][x] = value
    return K[n][W]

'''
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result
'''

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
