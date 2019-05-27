# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    if len(A) == 0:
        return 0
    else:
        max_int = A[0]
        for x in A:
            if (x > max_int):
                max_int = x
        N = 0
        for x in A:
            if x == max_int:
                N = N + 1
        return N
            