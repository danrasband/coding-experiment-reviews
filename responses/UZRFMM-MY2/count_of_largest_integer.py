# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    max_num = max(A)
    return A.count(max_num)
