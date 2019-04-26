# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    # write your code in Python
    sum = 0
    for i in range(1,x):
        if isMultiple(i,3) == 1:
            sum += i
            if isMultiple(i,5) == 1:
                sum -= i
        elif isMultiple(i,5) == 1:
            sum += i
    return sum        
            


def isMultiple(num, divisor):
    if num%divisor == 0:
        return 1
    else:
        return 0