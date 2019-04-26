# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    if len(B) == 0 or X > len(B):
        return 0
    max_p = 0
    p = 0
    for i in range(len(B)):
        p = B[i]
        if p > max_p:
            max_p = p
    return max_p