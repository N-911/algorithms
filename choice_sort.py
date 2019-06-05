# Finds the smallest value in an array
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index


# Sort array
def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        # Finds the smallest element in the array and adds it to the new array
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr


print(selection_sort([55, 3, 16, 2, 10]))
