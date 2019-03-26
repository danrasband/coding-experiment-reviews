# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    max_ = max(A)
    max_apps = 0
    for i in range(len(A)):
        if A[i] == max_:
            max_apps += 1
    return max_apps
