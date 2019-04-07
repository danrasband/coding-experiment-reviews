# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python

    max_substring_len = len(A[0])
    for i in range(1,len(A)):
        if len(A[i]) < max_substring_len:
            max_substring_len = len(A[i])


    for i in range(1,len(A)):
        for j in range(max_substring_len):
            if A[0][j] != A[i][j]:
                max_substring_len -= 1
                if (max_substring_len == 0) : return ""

    return A[0][0:max_substring_len]
