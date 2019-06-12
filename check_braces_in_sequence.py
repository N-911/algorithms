import stack_module


def is_braces_sequence_correct(s: str):
    """
    проверяeт корректность скобочной последовательности
    из круглых и квадратных скобок () []

    >>> is_braces_sequence_correct('(([])[])')
    True
    >>> is_braces_sequence_correct('([')
    False
    >>> is_braces_sequence_correct(']])')
    False
    """

    for brace in s:
        if brace not in "() []":
            continue                                # if char is not brace
        if brace in '([':
            stack_module.push(brace)                # opening brace
        else:
            assert brace in ")]",  "Ожидалась закрывающая скобка" + str(brace)
            if stack_module.is_empty():
                return False
            left = stack_module.pop()
            assert left in "([", "Ожидалась открывающая скобка" + str(brace)
            if left == "(":
                right = ")"
            elif left == "[":
                right = "]"
            if right != brace:
                return False
    return stack_module.is_empty()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print('*'*50)
    print("braces_seuqence is correct: ", is_braces_sequence_correct('()()'))
