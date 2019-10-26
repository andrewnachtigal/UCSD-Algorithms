#!/user/bin/python

'''Money Change with Dynamic Programming

Apply dynamic programming for solving the money change problem for
denominations 1, 3, and 4.

'''

# Uses python3
import sys

def get_change(m):
    #write your code here
    return m // 4

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
