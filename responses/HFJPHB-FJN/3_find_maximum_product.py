# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    # write your code in Python
    if len(B) == 0 : return 0
    if X > len(B) : return 0
    
    B.sort()

    prod = 1
    for i in B[len(B) - X:]:
        prod *= i
        
    return prod
    
    