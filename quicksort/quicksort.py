def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # recursive case
    comparable = array[0]
    # sub-array of all the elements less than the pivot
    less = [i for i in array[1:] if i <= comparable]
    # sub-array of all the elements greater than the pivot
    greater = [i for i in array[1:] if i > comparable]
    return quicksort(less) + [comparable] + quicksort(greater)

#print(quicksort([100, 15, 2, 3, 50, 18]))
