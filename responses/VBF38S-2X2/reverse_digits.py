# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    # write your code in Python
    a = int(x % 3)
   # print(a)
    if a == 0:
        e = x - 3
    else:    
        e = x - a
    s = 3
    
    r = int((e * (s + e))/6)
   # print(r)
    
    a = int(x % 5)
    if a == 0:
        e = x - 5
    else:    
        e = x - a
    s = 5
    
    r = r + int((e * (s + e))/10)
    return r
    
    
    