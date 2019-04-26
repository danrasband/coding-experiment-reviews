# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    start = 1
    array = list()
    
    while(start < x):
        divisibleBy3 = start % 3
        divisibleBy5 = start % 5
        divisibleBy15 = start % 15
        # print("For start", start, divisibleBy3, divisibleBy5, divisibleBy15)
        if((divisibleBy3==0 or divisibleBy5 ==0) and divisibleBy15 !=0):
            array.append(start)
        start = start +1
    
    return sum(array)
    # write your code in Python
    # pass