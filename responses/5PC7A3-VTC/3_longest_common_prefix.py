# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    if len(A) == 0:
        return ""
    if len(A) == 1:
        return A[0]
    
    A = sorted(A, key= len)
    
    res = 0
    
    for i in range(len(A[0])):
        for ele in A:
            if ele[i] != A[0][i]:
                return A[0][:res]
        res += 1
    
    return A[0][:res]