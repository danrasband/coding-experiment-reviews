# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    a = sorted(A)
    return a.count(a[-1])