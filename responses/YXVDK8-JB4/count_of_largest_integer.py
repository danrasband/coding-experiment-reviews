# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python

    A.sort()

    counter = 0

    for i in range(0, len(A)):
        if A[i] == A[i-1]:
            counter += 1

    return counter
