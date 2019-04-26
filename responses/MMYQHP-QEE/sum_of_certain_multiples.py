# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    x = str(X)
    result = x[::-1]
    if result[-1] == '-':
        result = '-' + result[:-1]
    return int(result)