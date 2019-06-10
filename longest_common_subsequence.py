def lcs(a, b):
    """The longest common subsequence (LCS) problem is the problem of finding
    the longest subsequence common to all sequences in a set of sequences
    (often just two sequences). It differs from the longest common substring problem:
    unlike substrings, subsequences are not required to occupy consecutive positions
    within the original sequences"""
    m = len(a)
    n = len(b)
    f = [[0] * (m+1) for _ in range(n+1)]
    for i in range(m+1):
        for j in range(n+1):
            if a[i-1] == b[j-1]:
                f[i][j] = 1 + f[i-1][j-1]
            else:
                f[i][j] = max(f[i-1][j], f[i][j-1])
    return f[-1][-1]


w = 'ASKSMKCKMS'
e = 'ASDSMKCKAO'
print(lcs(w, e))
