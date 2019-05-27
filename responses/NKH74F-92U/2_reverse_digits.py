# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    if X >= 0:
        return int(str(X)[::-1])
    else:
        return -int(str(-X)[::-1])
    