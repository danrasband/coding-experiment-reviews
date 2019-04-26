# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    threes = int(x/3)
    fives = int(x/5)
    result = 0
    if x % 3 != 0:
        threes += 1
    elif x % 5 != 0:
        fives += 1
    for i in range(threes):
        result += i*3
    for i in range(fives):
        result += i*5
    return result