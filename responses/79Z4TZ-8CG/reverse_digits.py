# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    # write your code in Python
    
    from collections import deque
    
    int_string = str(X)
    
    build_list = deque()
    
    for char in int_string.strip():
        if char not in {'-'}:
            build_list.appendleft(char)
            
    if int_string.startswith('-'):
        build_list.appendleft("-")
    
    reconstituted_string = "".join(build_list)
    
    return int(reconstituted_string)