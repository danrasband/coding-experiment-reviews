# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    min_len = len(A[0])
    for i in range(len(A)-1):
        str_len = len(A[i+1])
        if str_len >= min_len:
            continue
        else:
            min_len = str_len
    prefix = []
    for i in range(str_len):
        letter = A[0][i]
        for j in range(len(A)-1):
            if


    pass
