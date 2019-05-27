# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    A.sort(reverse = True)
    largestnumber = A[0]
    count = 0
    for i in A:
        if i == largestnumber:
            count += 1
    return count
