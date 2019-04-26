# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    if len(S) == 0:
        return 0
    
    return sum([int(x) for x in S.split(',')])