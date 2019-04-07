# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python
    a = list(map(int, S.split(",")))
    return sum(a)
