# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python
    mySum = 0
    if type(S) == str:
        for elem in S.split(','):
            mySum += int(elem)

    return mySum 