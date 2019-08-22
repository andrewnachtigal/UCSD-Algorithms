#!/user/bin/python

'''Maximum Number of Prizes
represent a given positive integer 𝑛 as a sum of as many pairwise distinct
positive integers as possible. That is, to find the maximum 𝑘 such that 𝑛 can
be written as 𝑎1+𝑎2+···+𝑎𝑘 where 𝑎1,...,𝑎𝑘 are positive integers and 𝑎𝑖 ̸=𝑎𝑗
for all 1≤𝑖<𝑗≤𝑘.


'''

import sys

def optimal_summands(n):
    summands = []
    #write your code here
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
