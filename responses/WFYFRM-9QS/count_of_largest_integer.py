# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    if A:
        cntDict = {}
        maxNum = A[0]
        count = 0
        for num in A:
            if num > maxNum:
                maxNum = num
                count = 1
            elif num == maxNum:
                count +=1
        return count
    else:
        return 0