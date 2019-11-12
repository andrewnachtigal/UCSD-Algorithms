#!/user/bin/python

'''Longest Common Subsequence of Three Sequences

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

def lcs3(a, b, c):
    #write your code here
    return min(len(a), len(b), len(c))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
