#!/user/bin/python

'''Find the Closest Pair of Points

Given n points on a plane, find the smallest distance bewteen a pair of two
points. The distance between points (x1, y1) is sqrt((x1-x2)^2 + (y1-y2)^2)


'''

#Uses python3
import sys
import math

def minimum_distance(x, y):
    #write your code here
    return 10 ** 18

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
