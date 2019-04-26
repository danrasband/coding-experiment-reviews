# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python
    l = S.split(',')
    r = 0
    for a in l:
        r =r + int(a)
        
    return r
        