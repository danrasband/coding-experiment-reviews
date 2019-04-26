# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    count = x
    sum = 0
    while count > 0:
        count -= 1
        if (count % 3 == 0) or (count % 5 == 0):
            sum += count
    return sum