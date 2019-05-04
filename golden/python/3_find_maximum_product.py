from functools import reduce

def solution(X, B):
    N = len(B)
    if N == 0:
        return 0
    if N < X:
        return 0
    if N == 1:
        return B[0]

    max = 0
    for i in range(X, N + 1):
        window = B[i-X:i]
        prod = reduce((lambda a, b: a * b), window, 1)
        if max < prod:
            max = prod

    return max
