#!/user/bin/python

'''Maximizing Advertisement Revenue (Maximize Dot Product)
Given two sequences, profit per click of ith ad and average number of clicks
per day of the i-th slot, partition inot n pairs such that the sum of products
is maximized.


'''

import sys

def max_dot_product(a, b):
    # code here
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
