# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    d=[]
    e=0
    for i in range(1,x):
        if i%3==0 or i%5==0:
            d.append(i)
    return sum(d)