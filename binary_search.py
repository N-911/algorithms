import random


def binary_search(array, number):
    """return position number in sorted!!!! array"""
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        if array[middle] == number:      # fix search index in left boundary
            return middle
        elif array[middle] < number:
            left = middle+1
        elif array[middle] > number:
            right = middle-1
    return None



print(binary_search([1,2, 2, 3, 7, 8], 2))
