# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 3, 5, 6, 9 = 23 

def solution(x):
    y =[]
    for i in range(x):
        if (i%3==0 or i%5==0) and ((i%3==0 and i%5==0)==False):
            y.append(i)
    z=sum(y)
    return(z)
    