# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    temp = 0
    for i in range(x):
        if i%3==0 or i%5==0 and i not in [3,5]:
            temp += i
    return temp