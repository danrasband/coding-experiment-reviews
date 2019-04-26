# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python
    for i in range(len(A[0])):
        if A[0][i] in "aeiou":
            test = A[0][:i]
            num = i
            break
        else:
            None

    x = 0
    for word in A:
        if word[:i] == test:
            x = 1
        else:
            x = 0
    if x == 1:
        return test
    else:
        return ""
        pass