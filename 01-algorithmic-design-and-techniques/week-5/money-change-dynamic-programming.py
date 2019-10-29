#!/user/bin/python

'''Money Change with Dynamic Programming

Apply dynamic programming for solving the money change problem for
denominations 1, 3, and 4, i.e., the minimum number of 1, 3, and 4 coins that
changes money.

'''

# Uses python3
import sys

# INEFFICIENT ALGORITHM:
def get_change_ineff(m):
    # base case
    denom = [1,3,4]
    min = m
    if m % 4 == 0:
        return m // 4
    else:
        for i in [c for c in denom if c <= m]:
            numCoins = 1 + get_change(m-i)
            if numCoins < min:
                min = numCoins
    return min

def get_change(m):
    

    return m //4

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
