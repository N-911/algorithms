def generate_bin(m, prefics=''):
    """the generation of all permutations of 0 or 1 numbers in m positions
    """
    if m == 0:
        print(prefics)
    else:
        generate_bin(m-1, prefics + '0')
        generate_bin(m-1, prefics + '1')

# print(generate_bin(4))

def find_number(number, a):
    for x in a:
        if number == x:
            return True
    else:
        return False

def generate_numbers(n, m=-1, prefics=None):
    """the generation of all permutations of n numbers in m positions
    """
    prefics = prefics or []
    m = n if (m == -1 or m > n) else m
    #m = n if m > n else m
    if m == 0:
        print(*prefics)
    else:
        for number in range(1, n+1):
            if find_number(number, prefics):
                continue
            prefics.append(number)
            generate_numbers(n, m-1,prefics)
            prefics.pop()

print(generate_numbers(5, 5))
