# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    y = [int(y) for y in S.split(",")]
    ans = 0
    for i in y:
        ans += i
    return ans