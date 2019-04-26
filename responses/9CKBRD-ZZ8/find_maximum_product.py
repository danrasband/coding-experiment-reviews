# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import defaultdict

def solution(A):
    
    prefix_dict = defaultdict(int)
    
    for string in A:
        for i in range(1,len(string)):
            prefix_dict[string[:i]] = prefix_dict[string[:i]] + 1
    
    highest_k = ""
    highest_v = 1
    
    for k, v in prefix_dict.items():
        if v > highest_v:
            highest_k = k
            highest_v = v
        elif v == highest_v:
            if len(k) > len(highest_k):
                highest_k = k
                highest_v = v 
    
    if highest_v <= 1:
        highest_k = ""
        
        
    return highest_k
    