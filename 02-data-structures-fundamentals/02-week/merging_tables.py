#!/usr/bin/python3

'''Merging Tables

Simulate a sequence of merge operations with tables in a database.

Given 𝑛 tables stored in some database. Tables are numbered from 1 to 𝑛. All
tables share the same set of columns. Each table contains either several rows
with real data or a symbolic link to another table. Initially, all tables
contain data, and 𝑖-th table has 𝑟𝑖 rows. Perform 𝑚 of the following operations:

1. Consider table number 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖. Traverse the path of symbolic links to get
    to the data. That is,
        while 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 contains a symbolic link instead of real data do
            𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 ← symlink(𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖)

2. Consider the table number 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 and traverse the path of symbolic links from
    it in the same manner as for 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖.

3. Now, 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 and 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 are the numbers of two tables with real data. If
    𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 ̸= 𝑠𝑜𝑢𝑟𝑐𝑒𝑖, copy all the rows from table 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 to table 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖,
    then clear the table 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 and instead of real data put a symbolic link to
    𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 into it.

4. Print the maximum size among all 𝑛 tables (recall that size is the number of
    rows in the table). If the table contains only a symbolic link, its size is
    considered to be 0.
'''

"""naive solution

class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        return True

    def get_parent(self, table):
        # find parent and compress path
        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)

if __name__ == "__main__":
    main()
"""

import sys

class disJointSet(object):

    def __init__(self, n, lines):
        self.n = n
        self.lines = [0] * lines
        self.rank = [0] * (n + 1)
        self.parent = list(range(0, n + 1))
        self.max = max(self.lines)

    def get_parent(self, x):

        parent_list = []

        # find root
        root = x
        while root != self.parent[root]:
            parent_list.append(self.parent[root])
            root = self.parent[root]

        # compress path
        for i in parent_list:
            self.parent[i] = root

        return root

    def merge(self, destination, source):
        source_root = self.get_parent(source)
        destination_root = self.get_parent(destination)

        if source_root == destination_root:
            return

        if self.rank[source_root] >= self.rank[destination_root]:
            self.parent[source_root] = destination_root

        else:
            self.parent[destination_root] = source_root
            if self.rank[source_root] == self.rank[destination]:
                self.rank[source_root] += 1

        self.lines[destination_root] += self.lines[source_root]
        self.lines[source_root] = 0

        if self.max < self.lines[destination_root]:
            self.max = self.lines[destination_root]

    def get_max_lines(self):
        return self.max

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lines = list(map(int, sys.stdin.readline().split()))

    disjoint_set = disJointSet(n, lines)

    for i in range(m):
        destination, source = map(int, sys.stdin.readline().split())
        disjoint_set.merge(destination, source)
        print(disjoint_set.get_max_lines())
