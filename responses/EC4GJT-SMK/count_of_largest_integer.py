# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    highest = A[0]
    count = 0
    for item in A:
        if item == highest:
            count += 1
        elif item > highest:
            highest = item
            count = 1
        else:
            pass
    return count
