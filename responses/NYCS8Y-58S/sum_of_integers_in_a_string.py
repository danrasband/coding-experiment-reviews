# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    S_array = S.split(',')
    total = 0
    for i in S_array:
        total = total + int(i)
    return total