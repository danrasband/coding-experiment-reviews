# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python
    splitList = S.split(",")
    sumVal = 0
    for strVal in splitList:
        sumVal += int(strVal)
    
    return sumVal