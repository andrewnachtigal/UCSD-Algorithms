#!/user/bin/python

'''Tree Height

Task:
Read description of tree from input
Implement tree data structure
Store tree and compute height
    height of rooted tree = maximum depth of a node, or maximum distance from
    a leaf to the root.

Input
    number of nodes n
    n integer numbers from -1 to n - 1 parents of nodes

allocate 𝑛𝑜𝑑𝑒𝑠[𝑛]:
    for 𝑖 ← 0 to 𝑛 − 1:
        𝑛𝑜𝑑𝑒𝑠[𝑖] =new 𝑁𝑜𝑑𝑒

for 𝑐h𝑖𝑙𝑑_𝑖𝑛𝑑𝑒𝑥 ← 0 to 𝑛 − 1:
    read 𝑝𝑎𝑟𝑒𝑛𝑡_𝑖𝑛𝑑𝑒𝑥
    if 𝑝𝑎𝑟𝑒𝑛𝑡_𝑖𝑛𝑑𝑒𝑥 == −1:
        𝑟𝑜𝑜𝑡 ← 𝑐h𝑖𝑙𝑑_𝑖𝑛𝑑𝑒𝑥
    else:
        𝑛𝑜𝑑𝑒𝑠[𝑝𝑎𝑟𝑒𝑛𝑡_𝑖𝑛𝑑𝑒𝑥].𝑎𝑑𝑑𝐶h𝑖𝑙𝑑(𝑛𝑜𝑑𝑒𝑠[𝑐h𝑖𝑙𝑑_𝑖𝑛𝑑𝑒𝑥])
'''

import sys
import threading


def compute_height_naive(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height

class ComputeTreeHeight:
    def __init__(self):
        self.n = 0
        self.parent = []
        self.cache = []

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.cache = [0]*self.n

    def compute_depth(self, node_id):
        parent = self.parent[node_id]
        if parent == -1:
            return 1

        if self.cache[node_id]:
            return self.cache[node_id]

        self.cache[node_id] = 1 + self.compute_depth(self.parent[node_id])
        return self.cache[node_id]

    def compute_height(self):
        return max([self.compute_depth(i) for i in range(self.n)])


def main():
    '''
    n = int(input())
    parents = list(map(int, input().split()))
    '''
    tree = ComputeTreeHeight()
    tree.read()
    print(tree.compute_height())


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
