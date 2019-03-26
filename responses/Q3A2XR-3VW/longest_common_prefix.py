# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    min_len = min([len(a) for a in A])
    prefix_len = -1
    for j in range(min_len):
        prefix = A[0][:j+1]
        for i in range(1, len(A)):
            if A[i][:j+1] != prefix:
                prefix_len = j
                break
        if prefix_len >= 0:
            break
    return A[0][:prefix_len]
