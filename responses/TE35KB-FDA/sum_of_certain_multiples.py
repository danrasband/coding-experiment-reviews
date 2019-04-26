# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    n = int(str(X).lstrip('-')[::-1])
    return n if X > 0 else -n