def equal_string(A,B):
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[1] != B[i]:
            return False

    return True
