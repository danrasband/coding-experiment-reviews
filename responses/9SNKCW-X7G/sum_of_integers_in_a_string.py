# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    if len(A) == 0:
        return 0
    max_int = A[0]
    max_cnt = 1
    for i in range(1, len(A)):
        if A[i] > max_int:
            max_int = A[i]
            max_cnt = 1
        elif A[i] == max_int:
            max_cnt += 1
    return max_cnt
        