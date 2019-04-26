# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    # write your code in Python
    x = x-1
    max_3 = int(x/3) * 3
    max_5 = int(x/5) * 5
    max_15 = int(x/15) * 15
    
    sum_3 = (max_3+3) *((max_3-3)/3+1) /2
    sum_5 = (max_5+5) *((max_5-5)/5+1) /2
    sum_15 = (max_15+15) *((max_15-15)/15+1) /2
    #print(sum_3, sum_5, sum_15)
    return int(max(sum_3, 0) + max(sum_5, 0) - max(sum_15, 0)*2)