m = [3,4,4,6,7]             #weight of elements
v = [4,2,4,5,5]             #costs  elements
# k = 12
N = len (m)             #количество прежметов
M = max(m)                 #  масса максимальная

# i - max  elements
# k - max weight bacpack


F = [[0] * (N+1) for i in range(M + 1)]
def bacpack(m, v):
    for i in range(1, N + 1):
        for k in range(1, M +1 ):
            if m[i] <= k:
                F[k][i] = max(v[i]+F[k-m[i]][i-1], F[k][i-1])
            else:
                F[k][i] = F[k][i-1]

    return F[M][N]


print(bacpack(m, v))

# print(F)