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

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
