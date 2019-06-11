_stack = []


def push(x):
    _stack.append(x)


def pop():
    x = _stack.pop()


def clear():
    _stack.clear()


def is_empty():
    return len(_stack) == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)