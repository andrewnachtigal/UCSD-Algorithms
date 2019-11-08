#!/user/bin/python

'''Longest Common Subsequence of Two Sequences

Compute the length of a longest common subsequence of two sequences. A
subsequence is a sequence that appears in the same relative order, but not
necessarily contiguous order in both strings.

i.e.
x: ABCBDAB
y: BDCABA

LC subsequences:
1. BDAB
2. BCAB
3. BCBA

Bottom Up Dynamic Programming - Iterative LCS:

    int lcs_length(char * A, char * B)
    {
	allocate storage for array L;
	for (i = m; i >= 0; i--)
	    for (j = n; j >= 0; j--)
	    {
		if (A[i] == '\0' || B[j] == '\0') L[i,j] = 0;
		else if (A[i] == B[j]) L[i,j] = 1 + L[i+1, j+1];
		else L[i,j] = max(L[i+1, j], L[i, j+1]);
	    }
	return L[0,0];
    }

'''

import sys

def lcs2(a, b):
    # generate matrix of longest common substrings
    len_array = [[0 for i in range(len(b)+1)] for j in range(len(a)+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                len_array[i+1][j+1] = len_array[i][j] + 1
            else:
                len_array[i+1][j+1] = max(len_array[i+1][j], len_array[i][j+1])

    result = ''
    j = len(b)
    for i in range(1, len(a)+1):
        if len_array[i][j] != len_array[i-1][j]:
            result += a[i-1]

    return result
    #write your code here
    #return min(len(a), len(b))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
