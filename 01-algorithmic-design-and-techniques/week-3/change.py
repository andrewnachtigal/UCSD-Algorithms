#!/user/bin/python

'''Changing Money
Find the minimum number of coins needed to change the input value into coins
with denominations 1, 5, 10.

input integer m

'''

import sys

def get_change(m):
    #write your code here
    remainder = 0
    pennies = 0
    nickles = 0
    dimes = 0

    dimes = m // 10
    remainder = m % 10
    nickles = remainder // 5
    remainder = remainder % 5
    pennies = remainder
    m = int(dimes) + int(nickles) + int(pennies)

    return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
