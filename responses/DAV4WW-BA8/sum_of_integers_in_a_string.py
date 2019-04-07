# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    nums = S.split(',')
    return sum([eval(num) for num in nums])
