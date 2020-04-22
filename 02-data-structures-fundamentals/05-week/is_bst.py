#!/usr/bin/env python3

"""Check whether binary search tree

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
threading.stack_size(2**25)  # new thread will get stack of such size

def checkNode(tree, index, left, right):
    """Recursive validation for given node of binary search tree
    """
    if not left < tree[index][0] < right:
        return False

    if tree[index][1] > -1:
        if not checkNode(tree, tree[index][1], left, tree[index][0]):
            return False

    if tree[index][2] > -1:
        if not checkNode(tree, tree[index][2], tree[index][0], right):
            return False

    return True

def IsBST(tree):
    """validation for given tree for BST
    """
    key = tree[0][0]
    bound = pow(2, 31)
    if tree[0][1] > -1:
        if not checkNode(tree, tree[0][1], -bound, key):
            return False
    if tree[0][2] > -1:
        if not checkNode(tree, tree[0][2], key, bound -1):
            return False

    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []

    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))

        if len(tree) < 2:
            print("CORRECT")
        else:
            if IsBST(tree):
                print("CORRECT")
            else:
                print("INCORRECT")

threading.Thread(target=main).start()
