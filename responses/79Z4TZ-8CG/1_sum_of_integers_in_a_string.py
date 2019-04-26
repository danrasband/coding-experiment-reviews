# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import ast

def solution(S):
    # write your code in Python
    
    vals = S.split(',')

    cumm_sum = 0
    
    for val in vals:
        cumm_sum += ast.literal_eval(val)
    
    return cumm_sum