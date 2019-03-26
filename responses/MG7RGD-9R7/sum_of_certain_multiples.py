# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    # write your code in Python

    if x%3==0:
        m3 = x//3-1
    else:
        m3 = x//3
    if x%5==0:
        m5 = x//5-1
    else:
        m5 = x//5
    if x%15==0:
        m15 = x//15-1
    else:
        m15 = x//15

    sum3 = (3+3*m3)*m3/2
    sum5 = (5+5*m5)*m5/2
    sum15 = (15+15*m15)*m15/2

    return int(sum3+sum5-2*m15)

    pass
