# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys

def solution(A):
    # write your code in Python
    maxInt = -sys.maxsize
    maxCount = 0
    for i in A:
        if i > maxInt:
            maxInt = i
            maxCount = 1
        elif i == maxInt:
            maxCount += 1
    return maxCount
    