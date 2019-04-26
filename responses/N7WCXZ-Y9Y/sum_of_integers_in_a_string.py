# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python
    num = list(map(int,S.split(',')))
    
    sum=0
    for it in num:
        sum += int(it)
        
    return sum
    