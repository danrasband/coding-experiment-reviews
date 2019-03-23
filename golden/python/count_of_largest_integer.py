def solution(A):
    if len(A) == 0:
        return 0

    max_integer = A[0]
    count = 0

    for i in A:
        if max_integer < i:
            max_integer = i
            count = 1
        elif max_integer == i:
            count += 1

    return count
