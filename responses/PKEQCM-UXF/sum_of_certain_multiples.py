# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    # write your code in Python
    sum_ = 0
    for i in range(1, x):
        if i%3 == 0 and i%5 != 0:
            sum_ += i
        elif i%3 != 0 and i%5 == 0:
            sum_ += i
    return sum_
