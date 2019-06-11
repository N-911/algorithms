def lis(A):
    f = [0] * (len(A))
    for i in range(0, (len(A))):
        m = 0
        for j in range(0, i):
            if A[i] > A[j] and f[j] > m:
                m = f[j]
        f[i] = m + 1
    print(*f)
    maximum = 0
    for i in f:
        maximum = max(maximum, f[i-1])
    return maximum


print("LIS: ", lis('12837718268925544868458182'))
