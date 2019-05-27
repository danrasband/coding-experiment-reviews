# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    import collections
    count = collections.Counter(A)
    a=1
    for key in count:
        if(a==1):
            highestValue = key
        else:
            if(key>highestValue):
                highestValue = key
        a = a +1
    
    return count[highestValue]
    
    # import numpy as np
    # maxValue = max(A)
    # return np.count_nonzero(A==maxValue)
    