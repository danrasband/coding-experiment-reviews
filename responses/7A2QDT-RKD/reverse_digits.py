# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    # write your code in Python
    neg = 1
    if X < 0:
        X = -X
        neg = -1
    rev=0
    while(X>0):
        dig=X%10
        rev=rev*10+dig
        X=X//10

    return rev * neg
