# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A)==0:
        return 0
    max = 0
    for i in range(len(A)):
        if A[i]>A[max]:
            max =i
    cnt = 0
    for i in A:
        if i==A[max]:
            cnt+=1
    return cnt
    pass