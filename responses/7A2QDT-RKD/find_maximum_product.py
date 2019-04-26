# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from functools import reduce
def solution(X, B):
    # write your code in Python
    K = len(B)
    if K == 0 or X > K:
        return 0
    else:
        #choose first X number as initialization
        max_prod = reduce((lambda x, y: x * y), B[0:X])
        for i in range(X, len(B)):
            if B[i] > B[i-X]:
                max_prod = max_prod/B[i-X]*B[i]
        return int(max_prod)
                