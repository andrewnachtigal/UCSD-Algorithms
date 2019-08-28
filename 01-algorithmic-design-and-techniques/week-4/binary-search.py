#!/user/bin/python

'''Binary Search
Implement binary search algorithm allowing very efficient search, provided the
list is sorted.

'''

import sys
import math

def binary_search(a, x):
    low, high = 0, len(a)-1

    if high < low:
        return -1

    while low <= high:
        mid = math.floor(low + (high - low)/2)
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid + 1
        elif a[mid] > x:
            high = mid - 1
        else:
            return -1



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
        print(binary_search(a, x), end = ' ')
        #print(linear_search(a, x), end = ' ')
