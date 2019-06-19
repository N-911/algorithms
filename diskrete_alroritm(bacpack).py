m = [3,4,4,6,7]             #weight of elements
v = [4,2,4,5,5]             #costs  elements
k1 = 12
N = len (m)             #количество прежметов
M = 15                 #  масса максимальная

# i - max  elements
# k - max weight bacpack

def bacpack(m, v):
    N = len (m)                #количество прежметов
    M = max(m)                 #  масса максимальная
    F = [[0] * (N) for i in range(M)]
    for i in range(0, N):
        for k in range(0, M):
            if m[i] <= k:
                F[k][i] = max(v[i]+F[k-m[i]][i-1], F[k][i-1])
            else:
                F[k][i] = F[k][i-1]
    for g in F:
        print (g)
    return F[M-1][N-1]
#     return F[M][N]
bacpack(m, v)


print(bacpack(m, v))
# print ([[0] * (4) for i in range(2)])
# print(F)