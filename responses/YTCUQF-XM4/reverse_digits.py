# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    ans = 0
    for i in range(x):
        if i % 3 == 0:
            ans += i
        elif i % 5 == 0:
            ans += i
    return ans