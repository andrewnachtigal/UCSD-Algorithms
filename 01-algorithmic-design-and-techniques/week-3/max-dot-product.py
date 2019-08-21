#!/user/bin/python

'''Maximizing Advertisement Revenue: Dot Product/Sum of Products
Given two sequences, profit per click of ith ad and average number of clicks
per day of the i-th slot, partition inot n pairs such that the sum of products
is maximized.


'''

import sys

def max_dot_product(a, b):
    result = 0

    for i in range(len(a)):
        max_a = get_max(a)
        max_b = get_max(b)
        result += a[max_a] * b[max_b]
        a.remove(a[max_a])
        b.remove(b[max_b])
    return result

def get_max(arr):
    max = arr[0]
    index = 0
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]
            index = i
    return index

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
