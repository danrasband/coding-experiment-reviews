# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    # write your code in Python
    sign = 1
    if (X == 0): return 0
    if (X < 0 ): 
        sign = -1
        X = -X
    
    new_num = 0
    
    while (X / 10 != 0):
        new_num = new_num * 10 + X % 10
        X = X // 10
        
    return sign * new_num