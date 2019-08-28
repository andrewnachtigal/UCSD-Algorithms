#!/user/bin/python

'''Binary Search
Implement binary search algorithm allowing very efficient search, provided the
list is sorted.

'''

import sys
import math

def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here
    if a[0] < x:
        return -1

    mid = math.floor(a[0] + (a[n] - a[0])/2)

    if x = a[mid]:
        return mid
    else:


    for i in range(len(a)):
        if a[i] <= x:


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(linear_search(a, x), end = ' ')
