# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    # write your code in Python
    sum1 = sum(range(0,x,3))
    sum2 = sum(range(0,x,5))
    sum3 = sum(range(0,x,15))

    return sum1 + sum2 -sum3
