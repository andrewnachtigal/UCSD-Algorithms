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

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(j, mn, mx):
 if not j in tree:
  return True

 if tree[j][0] < mn or tree[j][0] > mx:
  return False

 return IsBinarySearchTree(tree[j][1], mn, tree[j][0] - 1) and \
IsBinarySearchTree(tree[j][2], tree[j][0] + 1, mx)

def main():
  nodes = int(sys.stdin.readline().strip())
  global tree
  tree, int_max, int_min = {}, 2147483647, -2147483648
  for i in range(nodes):
    tree[i] = (list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(0, int_min, int_max):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target = main).start()
