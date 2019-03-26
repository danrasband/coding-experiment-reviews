# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    X = str(X)

    if '-' in X:
        X = X.replace('-', '')
        X = X[::-1]
        X = '-' + X
    else:
        X = X[::-1]
        X = X

    return int(X)
