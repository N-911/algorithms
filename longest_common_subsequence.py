def lcs(a, b):
    """The longest common subsequence (LCS) problem is the problem of finding
    the longest subsequence common to all sequences in a set of sequences
    (often just two sequences). It differs from the longest common substring problem:
    unlike substrings, subsequences are not required to occupy consecutive positions
    within the original sequences"""
    m = len(a)
    n = len(b)
    f = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                f[i][j] = 0
            elif a[i-1] == b[j-1]:
                f[i][j] = 1 + f[i-1][j-1]
            else:
                f[i][j] = max(f[i-1][j], f[i][j-1])
    for row in f:
        print(*row)
    print("- " * (n+1))
    return f[-1][-1]


print(lcs("Smskms", "mcscmsa"))
