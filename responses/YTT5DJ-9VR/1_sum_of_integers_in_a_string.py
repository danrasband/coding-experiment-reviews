# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    sum = 0
    parts = S.split(',')
    for part in parts:
        if part[0]=='0':
            continue
        elif part[0]=='-':
            sum-=int(part[1:])
        elif part[0]=='+':
            sum+=int(part[1:])
    # write your code in Python
    return sum
    