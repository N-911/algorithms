def factorial_recurcion(n):
    if n <= 1:
        return 1
    return factorial_recurcion(n-1) * n


print(factorial_recurcion(40))


def factorial_list(n):
    fact_list = [1]+[0] * n
    for i in range(1, n+1):
        fact_list[i] = fact_list[i-1] * i
    return fact_list[n]


print(factorial_list(40))
