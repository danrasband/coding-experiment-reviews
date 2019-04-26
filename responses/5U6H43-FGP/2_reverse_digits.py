# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    
    _sum = 0
    for each in range(1, x):
        if each % 3 == 0 or each % 5 == 0:
            _sum += each
    
    return _sum