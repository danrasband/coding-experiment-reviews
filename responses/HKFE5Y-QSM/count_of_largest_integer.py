# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    if not A:
        return 0
        
    return A.count(max(A))
    