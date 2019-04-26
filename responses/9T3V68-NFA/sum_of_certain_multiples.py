# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    value = str(X)[::-1]
    if value.count('-'):
        return -int(value.strip('-').lstrip('0'))
    
    return int(value.lstrip('0'))