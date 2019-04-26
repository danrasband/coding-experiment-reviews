# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    d=[]
    for i,j in range(len(A)):
        if A[i][j]==A[i+1][j]:
            d.append(A[i][j])
    return d.join()