# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python
    l = [int(x[1:]) if x[0] == '+' else int(x) for x in S.split(',')]
    return sum(l)