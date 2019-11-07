#!/user/bin/python

'''Compute the Edit Distance Between Two Strings

The edit-distance between two strings is the minimum number of operations
(insertions, deletions, and substitutions of symbols) to transform one string
into another


'''

# Uses python3
def edit_distance(s, t):
    #D[i,0] = i
    #D[0,j] = j
    m = len(s)
    n = len(t)
    d = []

    for i in range(len(s) + 1):
        d.append([i])
    del d[0][0]

    for j in range(len(t) + 1):
        d[0].append(j)

    for j in range(1, len(t)+1):
        for i in range(1, len(s)+1):
            insertion = d[i][j-1] + 1
            deletion = d[i-1][j] + 1
            match = d[i-1][j-1]
            mismatch = d[i-1][j-1] + 1
            if s[i-1] == t[j-1]:
                d[i].insert(j, match)
            else:
                minimum = min(insertion, deletion, mismatch)
                d[i].insert(j, minimum)
    editDist = d[-1][-1]
    return editDist

if __name__ == "__main__":
    print(edit_distance(input(), input()))
