def kuznechik_1_2(n):
    """the problem of the number of ways to reach point n from point 1,
if the grasshopper can jump +1 and  +2"""

    m = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        m[i] = m[i-1] + m[i-2]
    return m[n]

#print(kuznechik_1_2(3))

def kuznechik_1_3(n, allowed: list):
    """the problem of the number of ways to reach point n from point 1,
if the grasshopper can jump +1, +2 and +3."""

    m = [0, 1, int(allowed[2])] + [0] * (n-2)
    for i in range(3, n+1):
        if allowed[i]:
            m[i] = m[i-1] + m[i-2] + m[i-3]
    return m[n]

#print(kuznechik_1_3 (3, [True,True,False,True]))


def min_cost(n, price: list):
    c = [[0], price[1], price[1]+price[2]] + [0] * (n-2)
    way = []
    for i in range(3, n+1):
        c[i] = price[i] + min(price[i-1], price[i-2])
        way.append((i-1 if price1[i-1] < price1[i-2] else i-2))
    return c[n], way

price1 = [1,1,2,2,3,1,4,3,4,5,2,1,1]

print("min_cost: ",min_cost(9, price1))



