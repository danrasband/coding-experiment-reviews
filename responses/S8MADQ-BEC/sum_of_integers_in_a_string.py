# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    if not len(A):
        return 0
    
    mx=-2**32
    count=0
    
    for it in A:
        if it>mx:
            count=1
            mx=it
        elif it==mx:
            count+=1
    
    return count