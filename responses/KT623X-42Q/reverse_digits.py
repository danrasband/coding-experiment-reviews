# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    # write your code in Python
    a = X
    r = 0
    if a < -1:
        a = a *-1

    while a > 0:
        b = a % 10
        r = r * 10 + b
        a = a // 10
    if X < 0:
        r = r *-1
    return r
