import random


def merge_sort(a: list):
    if len(a) <= 1:
        return
    middle = len(a)//2
    left = [a[i] for i in range(0, middle)]
    right = [a[i] for i in range(middle, len(a))]
    merge_sort(left)
    merge_sort(right)
    c = merge(left, right)
    for x in range(len(a)):
        a[x] = c[x]
    return a


def merge(left: list, right: list):
    c = [0] * (len(left) + len(right))
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            c[k] = left[i]
            i += 1
            k += 1
        else:
            c[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        c[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        c[k] = right[j]
        j += 1
        k += 1
    return c


s = list(range(20))
random.shuffle(s)
print(s)
print(merge_sort(s))
