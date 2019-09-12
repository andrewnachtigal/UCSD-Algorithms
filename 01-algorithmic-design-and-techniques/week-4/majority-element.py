#!/user/bin/python

'''Majority Element
Decision rule that selects the alternative which has a majority of votes.
Check whether an element appears more than n/2 times.

'''

import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    for i in range(0, n):
        currentElem = a[i]
        count = 0
        for j in range(0, n):
            if a[j] == currentElem:
                count = count + 1
        if count > n/2:
            return a[i]
    # return('no majority element')

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
