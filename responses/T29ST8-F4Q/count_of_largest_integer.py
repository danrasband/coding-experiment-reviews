# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    S = S.split(',')
    for i in range(len(S)):
        S[i] = int(S[i])
    return sum(S)