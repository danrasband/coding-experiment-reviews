# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    neg = False
    if X < 0:
        neg = True
        X = X * -1
    X = str(X)
    
    