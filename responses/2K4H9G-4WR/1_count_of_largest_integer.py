# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    return A.count(max(set(A))) if len(A)>0 else 0