# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    maxnum = A[0]
    maxcount = 1
    for i in range(len(A)-1):
        if A[i+1] < maxnum:
            continue
        elif A[i+1] == maxnum:
            maxcount+=1
        else:
            maxnum = A[i+1]
            maxcount = 1
    return maxcount

    pass
