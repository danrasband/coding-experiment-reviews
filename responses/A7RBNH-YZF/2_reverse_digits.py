# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    # write your code in Python
    
    total = 0
    max_3 = ((x-1) // 3) * 3
    max_5 = ((x-1) // 5) * 5
    max_15 = ((x-1) // 15) * 115
    
    if x < 5:
        return 0
    if x < 6:
        return 3
        
    total = ((3 + max_3) * (max_3/6)) + ((5 + max_5) * (max_5/10)) - ((15 + max_15) * (max_15/30))
    print((5 + max_5) * (max_5/10))
    
    
    return int(total)