#!/user/bin/python

'''Sorting - Quick Sort

Quicksort (partition-exchange sort)

1. choose any element of the array to be the pivot.
2. divide all other elements into two partitions
 * all elements less than the pivot in the left partition
 * all elements greater than the pivot in the right partition
3. use recursion to sort both partitions
4. join the left sorted partition, pivot, and right sorted partition

'''

# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l
    t = l
    i = j
    for i in range(l+1, r+1):
        if a[i] < x:
            a[i], a[j] = a[j], a[i]
            a[i], a[t+1] = a[t+1], a[i]
            j += 1
            t += 1
        elif a[i] == x:
            a[i], a[t+1] = a[t+1], a[i]
            t += 1
    return j, t


def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #m = partition2(a, l, r)
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
