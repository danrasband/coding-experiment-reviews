# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python
    S = "+1,0,-1"
    x = []
    y = 0
    for i in range(len(S)):
        if S[i] == '+':
            y = i+1
        elif S[i] == '-':
            y = i
        elif S[i] == ',':
            x.append(S[y:i])
            y = i+1
        else:
            None
    ans = 0
    for item in x:
        ans += item
    return ans
    # ran out of time sorry!
    
    pass