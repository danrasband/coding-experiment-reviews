# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from functools import reduce

def solution(X, B):
    if (X > len(B)) or (len(B) == 0):
        return 0
    B.sort(reverse=True)
    nums = B[:X]
    return reduce(lambda x, y: x*y, nums)
    
    