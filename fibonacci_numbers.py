def fibonacci_recursion(number):
    """return fibonacci number"""
    if number <= 1:
        return number
    return fibonacci_recursion(number-1) + fibonacci_recursion(number-2)


print(fibonacci_recursion(10))


def fibonacci_list(number):
    fib_list = [0, 1] + [0] * (number-1)
    for i in range(2, number+1):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
    return fib_list[number]


print(fibonacci_list(3))
