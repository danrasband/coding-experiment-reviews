# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def isMultipleOfThree(num):
    return num % 3 == 0

def isMultipleOfFive(num):
    return num % 5 == 0

def isMultipleOfThreeAndFive(num):
    return num % 3 == 0 and num % 5 == 0

def solution(x):
    # write your code in Python
    sum = 0
    for i in range(3,x):
        if (isMultipleOfThree(i) or isMultipleOfFive(i) and not isMultipleOfThreeAndFive(i)):
            sum += i
    return sum
