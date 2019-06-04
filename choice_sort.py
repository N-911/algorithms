def find_smallest(list):
    """find  smallest element in list"""
    smallest = list[0]
    smallest_index = 0
    for x in range(len(list)):
        if list[x] < smallest:
            smallest = list[x]
            smallest_index = x
        return smallest_index


def choice_sort(list):
    """sort list by choice is smallest element and moving it to the begining"""

    sorted_list = []
    for x in range(len(list)):
        smallest = find_smallest(list)
        sorted_list.append(list.pop(smallest))
    return sorted_list

print(choice_sort([12,3,1,23,4]))