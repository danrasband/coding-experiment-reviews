# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    S = S.split(',')
    result = 0
    for num in S:
        if '+' in num:
            num = num.replace('+','')
        result += int(num)
    return result
