def generate_bin(m, prefics=''):
    if m == 0:
        print(prefics)
    else:
        generate_bin(m-1, prefics + '0')
        generate_bin(m-1, prefics + '1')

# print(generate_bin(4))


def generate_numbers(m, n, prefics=''):
    if m == 0:
        print(prefics)
    else:
        for x in range(n):
            generate_numbers(m-1, n, prefics+str(x))


print(generate_numbers(2, 3))
