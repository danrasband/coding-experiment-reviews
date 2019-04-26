# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    result = S.split(",")
    totalSum = sum(int(i) for i in result)
    return (totalSum)
    
