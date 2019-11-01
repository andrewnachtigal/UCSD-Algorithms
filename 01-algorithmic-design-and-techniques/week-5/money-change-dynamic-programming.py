#!/user/bin/python

'''Money Change with Dynamic Programming

Apply dynamic programming for solving the money change problem for
denominations 1, 3, and 4, i.e., the minimum number of 1, 3, and 4 coins that
changes money.

Base Case: make change for the same amount as the value of one coin - one coin.

Inductive Step: if the amount does not match a coin value, we want the minimum
of a penny plus the number of coins needed to make change for the money amount
minus a penny:
    min(1 + numCoins(money - 1))

or 3 plus... or 4 plus...
    1 + numCoins(money - 3)
    1 + numCoins(money - 4)

'''

# Uses python3
import sys

#ineficcient approach
def get_change_ineff(m):
    coinValues = [1,3,4] #coin denomimations
    minCoins = m #minimum number of coins to change money m
    if m in coinValues:
        return 1
    else:
        #filter the list of coins to those less than the current value of
        #change using a list comprehension.
        for i in [coin for coin in coinValues if coin <= m]:
            #reduce the total amount of change needed to make by the value
            #of the coin selected
            numCoins = 1 + get_change_ineff(m-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

#recursively cointing coins with table lookup (i.e., memoization/caching)
def get_change_table(m):
    minCoins = m
    coinValues = [1,3,4]
    results = m*[0]
    if m in coinValues:
        results[m-1] = 1
        return 1
    elif results[m-1] > 0:
        return results[m-1]
    else:
        for i in [coin for coin in coinValues if coin <= m]:
            numCoins = 1 + get_change_table(m-i)
            if numCoins < minCoins:
                minCoins = numCoins
                results[m-1] = minCoins
    return minCoins


#dynamic programming - bottom up
def get_change_dp(m):
    coinValues = [1,3,4]
    minCoins = (m)*[0] #list of the min number coins needed to make each value
    for cents in range(m+1):
        coinCount = cents
        #evaluate all possible coins to make change for cents and store results
        for j in [coin for coin in coinValues if coin <= cents]:
            if 1 + minCoins[cents-j] < coinCount:
                coinCount = 1 + minCoins[cents-j]
        minCoins[cents-1] = coinCount
    return minCoins[m-1]


def get_change(m):
    coinValues = [1,3,4]
    minCoins = []
    minCoins.append(0)
    for i in range(1, m+1):
        minCoins.append(9999)
        for j in coinValues:
            if i >= j:
                numCoins = minCoins[i - j] + 1
                if numCoins < minCoins[i]:
                    minCoins[i] = numCoins
    return minCoins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
