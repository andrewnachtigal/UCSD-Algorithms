#!/usr/bin/python3

"""Check whether binary search tree - general case

Test whether a binary search tree data structure is implemented correctly.

Given a binary search tree with integers as its key, test whether it is a
correct binary search tree. Check whether the given binary tree structure
satisfies the following condition:

For any node of the left subtree its key must be strictly less than 𝑥, and for
any node in its right subtree its key must be strictly greater than 𝑥.
"""

import sys
import threading

sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

max = None
prev = -1

def IsBST(tree):
    if len(tree) in (0, 1):
        return True

def inOrderWalk(tree, i):
    global max
    global prev
    if i == -1:
        return True

    last = 1
    if not inOrderWalk(tree, tree[i][1]):
        return False

    if max is None or max < tree[i][0]:
        max = tree[i][0]
    elif max == tree[i][0] and last == 1:
        max = tree[i][0]
    else:
        return False

    last = 2
    if not inOrderWalk(tree, tree[i][2]):
        return False

    return True

    if inOrderWalk(tree, 0):
        return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  #tree, int_max, int_min = {}, 2147483647, -2147483648
  for i in range(nodes):
      tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBST(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target = main).start()
