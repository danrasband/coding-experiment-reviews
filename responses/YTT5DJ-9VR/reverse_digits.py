# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    i = 0
    sum = 0
    while (i<x):
        sum+=6*(i+3) + 2*5 + 4 + 3*3 + 2 + 2
        i+=15
    
    i-=1
        
    #print(sum)
    
    while(i>=x):
        if i%5==0 or i%3==0:
            sum-=i
        i-=1
    
    return sum