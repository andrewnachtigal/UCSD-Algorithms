#!/usr/bin/python3

"""Rope string

Implement Rope - data structure that can store a string and efficiently cut a
part (substring) of the string and insert it in a different position.


"""

import sys

class Rope:
	def __init__(self, s):
		self.s = s
	def result(self):
		return self.s
	def process(self, i, j, k):
                # Implement rope


rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
print(rope.result())
