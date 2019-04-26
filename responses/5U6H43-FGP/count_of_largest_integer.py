# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import re

def solution(S):
    array = re.findall('[-+]\d+', S)
    
    _sum = 0
    for each in array:
        each = int(each)
        _sum += each   
        
    return _sum