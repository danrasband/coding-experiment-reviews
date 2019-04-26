# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    # write your code in Python
    neg = True if X < 0 else False
    X = str(X).strip('-')[::-1]
    
    try:
        X = int(X)
        
    except SyntaxError:
        while X[0] == 0:
            X = X[1:]
        X = int(X)
    
    return X * -1 if neg else X