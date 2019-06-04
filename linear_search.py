import random


def binary_search(array, number):
    for i in range(len(array)):
        if array[i] == number:
            return print('Position ', i)
    else:
        return print('number is not found')


list_test = random.sample(range(1000), 1000)
print(binary_search(list_test, 55))
