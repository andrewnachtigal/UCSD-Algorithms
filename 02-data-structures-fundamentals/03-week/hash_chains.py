#!/usr/bin/env python3

'''Hashing with Chains

Implement a hash table with lists chaining. Given the number of buckets m and
the polynomial hash function

h(𝑆) = ∑︁ 𝑆[𝑖]𝑥𝑖 mod 𝑝 mod 𝑚,

where 𝑆[𝑖] is the ASCII code of the 𝑖-th symbol of 𝑆, 𝑝 = 1 000 000 007
and 𝑥 = 263.

Support the following types of queries:

∙ add string — insert string into the table. If there is already such string in
    the hash table, then just ignore the query.
∙ del string — remove string from the table. If there is no such string in the
    hash table, then just ignore the query.
∙ find string — output “yes" or “no" (without quotes) depending on whether the
    table contains string or not.
∙ check 𝑖 — output the content of the 𝑖-th list in the table. Use spaces to
    separate the elements of the list. If 𝑖-th list is empty, output a blank
    line.

'''

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.el-ms = [ [] for _ in range(0, bucket_count)]

    def _hash_func(self, s):
        '''Hash function.'''
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    """def add(self, string):
        '''Insert string into the table or ignore.'''
        hashed = self._hash_func(string)
        bucket = self.bucket[hashed]
        if string not in bucket:
            self.buckets[hashed] = [string] + bucket

    def delete(self, string):
        '''Remove string from the table or ignore.'''
        hashed = self._hash_func(string)
        bucket = self.bucket[hashed]
        for i in range(len(bucket)):
            if bucket[i] == string:
                bucket.pop(i)
                break

    def find(self, string):
        '''Output yes or no depending on whether the table contains string.'''
        hashed = self._hash_func(string)
        if string in self.buckets[hashed]:
            return "yes"
        return "no"

    def check(self, i):
        '''Output the content of the 𝑖-th list in the table. If 𝑖-th list is
            empty, output a blank line.'''
        return self.buckets[i]"""

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            """use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)"""
            self.write_chain(reversed(self.elems[query.ind]))

        else:
            hash_ = self._hash_func(query.s)
            try:
                ind = self.elems[hash_].index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind!=-1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems[hash_].append(query.s)
            else:
                if ind != -1:
                    self.elems[hash_].pop(ind)

        """
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)"""

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
