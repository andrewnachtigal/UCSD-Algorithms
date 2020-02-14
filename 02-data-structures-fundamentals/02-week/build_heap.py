#!/usr/bin/python3

'''Convert Array to Heap

Convert an array of integers into a heap by applying a certain number of swaps
to the array. Swap exchanges elements 𝑎𝑖 and 𝑎𝑗 of the array 𝑎 for some 𝑖 and 𝑗.
Use only 𝑂(𝑛) swaps and use a min-heap.

A binary heap is a binary tree following the properties:
1) shape: complete binary tree - all levels are completely filled except last
2) heap: value stored in each node is greater than or equal to it's children

In-place Heap Sort
In-place: Implies that only additional O(1) extra data structure items are
required to solve the problem.

'''

class BuildMinHeap:
    '''
    Create list of swaps for a min-heap.
    '''
    def __init__(self):
        self._swaps = []
        self._data = []

    def read_data(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def write_response(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def left_child_index(self, index):
        left_child_index = 2 * index + 1
        if left_child_index >= len(self._data):
            return -1
        return left_child_index

    def right_child_index(self, index):
        right_child_index = 2 * index + 2
        if right_child_index >= len(self._data):
            return -1
        return right_child_index

    def shift_down(self, i):
        min_index = i
        left = self.left_child_index(i)
        right = self.right_child_index(i)

        if left != -1 and self._data[left] < self._data[min_index]:
            min_index = left

        if right != -1 and self._data[right] < self._data[min_index]:
            min_index = right

        if i != min_index:
            self._swaps.append((i, min_index))
            self._data[i], self._data[min_index] = self._data[min_index], self._data[i]
            self.shift_down(min_index)

    def generate_swaps(self):
        for i in range(len(self._data) // 2, -1, -1):
            self.shift_down(i)

    def solve(self):
        self.read_data()
        self.generate_swaps()
        self.write_response()


if __name__ == "__main__":
    build_min_heap = BuildMinHeap()
    build_min_heap.solve()
