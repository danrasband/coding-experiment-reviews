# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    if len(B) == 0 or X > len(B):
        return 0
    else:
        out = 1
        for i in B[-X:]:
            out *= i
        return out
