# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python
    arr_S = S.split(',')
    total = 0
    for i in arr_S:
        total += int(i)
        
    return total