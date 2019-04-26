# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    X = str(X)
    return (int(X[:0:-1]) * -1) if X.startswith("-") else int(X[::-1])