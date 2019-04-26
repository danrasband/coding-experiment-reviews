# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    prefix = A[0]
    for i in A:
        for j in range(len(prefix), -1, -1):
            if i.startswith(prefix[:j]):
                prefix = prefix[:j]
                break
    return prefix