def fibonacci_recursion(number: int) -> int:
    """ recursion algorimt
     return fibonacci number

    """
    assert number >= 0
    if number <= 1:
        return number
    return fibonacci_recursion(number-1) + fibonacci_recursion(number-2)


print('recursion algoritm fibonacci: ', fibonacci_recursion(100))


def fibonacci_dynamic(number: int):
    """
    dynamic programming algoritm
    """
    assert number >= 0
    fib_list = [0, 1] + [0] * (number-1)
    for i in range(2, number+1):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
    return fib_list[number]

print('dynamic algoritm fibonacci: ', fibonacci_dynamic(100))


F = [None] * 10_000
def fib_combine(number: int) -> int:
    """recursion with caching"""
    assert (number >= 0 and number < 10_000)
    if F[number] is not None:
        return F[number]
    elif number <=1:
        F[number] = number
        return F[number]
    else:
        F[number] =  fib_combine(number-1) + fib_combine(number -2)
        return F[number]

print ('combine algoritm: fibonacci: ',  fib_combine(100))
