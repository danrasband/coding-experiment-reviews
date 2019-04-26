# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    ans = 0
    from statistics import mode
    test = max(list(A), key = A.count)
    for i in range(len(A)):
        if A[i] == test:
            ans += 1
        else:
            None
    return ans
    pass