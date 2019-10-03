#!/user/bin/python

'''Majority Element (Quadratic Time)
Majority Rule is a decision rule that selects the alternative which has a
majority of votes.

Check whether an element appears more than n/2 times. If so, output 1. Otherwise
output -1.

Recursive Solution:
divide-and-conquer in O(nlogn). split a sequence into halves and make two
recursive calls, then combine the results.

'''

import sys

def get_majority_element_sort(a, left, right):

    # base case
    if left == right: # empty array
        return -1
    if left + 1 == right: # 1 element array
        return a[left]

    # sort and scan
    a.sort()
    if right % 2 == 0:
        major_elem = n // 2 + 1
    if right % 2 != 0:
        major_elem = (n+1) // 2
    for i in range((n // 2) + (n % 2)):
        if a[i] == a[i + major_elem - 1]:
            return 1
    return -1


def get_majority_element(a, left, right):

    # base case
    if left == right: # empty array
        return -1
    if left + 1 == right: # 1 element array
        return a[left]

    # recurse on left and right halves
    mid = (right - left) // 2 + left
    elemLeft = get_majority_element(a, left, mid)
    elemRight = get_majority_element(a, mid+1, right)

    if elemLeft == elemRight:
        return elemLeft

    half = (right-left)//2

    if (a.count(elemLeft) > half:
        return elemLeft

    if (a.count(elemRight) > half:
        return elemRight

    return -1

def GetFrequency(arr, elem):
    cnt = collections.Counter(arr)
    freq = cnt[elem]
    return freq

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element_sort(a, 0, n) != -1:
        print(1)
    else:
        print(0)
