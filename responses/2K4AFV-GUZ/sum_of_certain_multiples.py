# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    # write your code in Python
    negative = True if X < 0 else False
    str_X = str(-X) if negative else str(X)
    
    reverse_str_X = ''
    for i in range(len(str_X)-1, -1, -1): 
        reverse_str_X += str_X[i]
    
    return -int(reverse_str_X) if negative else int(reverse_str_X)