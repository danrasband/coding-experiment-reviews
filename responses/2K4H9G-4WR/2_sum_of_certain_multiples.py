# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    r = range(0,x)
    sum = 0
    for item in r:
        dev3 = item % 3
        dev5 = item % 5
        if not dev3 or not dev5:
            if not dev3 and not dev5:
                pass
            else:
                sum += item
    return sum