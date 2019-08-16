#!/user/bin/python

'''Maximum Value of Loot (Fractional Knapsack)
Find most valuable combination of items given constraints of capacity,
weight, and value.

pseudo:

KnapsackFast(W, w1, v1, ..., wn, vn)
    amounts = [0,0,...,0]
    totalValue = 0
    for i from 1 to n:
        if W = 0:
            return (totalValue, amounts)
        a = min(wi, W)
        totalValue = totalValue + a * vi/wi
        wi = wi - a
        amounts[i] = amounts[i] + a
        W = W - a
    return (totalValue, amount)


'''

import sys

def get_optimal_value(capacity, weights, values):
    totalValue = 0.
    # write your code here
    if capacity == 0:
        return 0
    for i in range(n):
        max_index = select_max_index(values, weights)
        if max_index >= 0:
            avail_weights = min(capacity, weights[max_index])
            value = value + avail_weights * values[max_index]/weights[max_index]
            weights[max_index] = weights[max_index] - avail_weights
            capacity = capacity - avail_weights
    return value

def select_max_index(values, weights):
    index = -1
    max = 0
    for i in range(n):
        if weights[i] > 0 and (values[i] / weights[i]) > max:
            max = values[i]/weights[i]
            index = i
    return index



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
