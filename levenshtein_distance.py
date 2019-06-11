def levenstein(a, b):
    """
     Levenshtein distance is a string metric for measuring the difference between two sequences.
     Informally, the Levenshtein distance between two words is the minimum number of single-character
     edits (insertions, deletions or substitutions) required to change one word into the other
    """
    f = [[(i + j) if (i*j) == 0 else 0 for j in range(len(b)+1)]
         for i in range((len(a)+1))]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                f[i][j] = f[i-1][j-1]
            else:
                f[i][j] = 1 + min(f[i-1][j], f[i][j-1], f[i-1][j-1])
    for row in f:
        print(*row)
    return f[len(a)][len(b)]


print(levenstein('dedded', 'dedqde'))
