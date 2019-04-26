# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    f = A[0]
    r = ''
    for i in range(100):
        for a in A:
            if f[:i] != a[:i]:
                return r
        r = f[:i]
    return r    