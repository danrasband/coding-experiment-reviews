# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#
def solution(X):
    if(X<0):
        X = -1* X
        reveresedString = str(X)[::-1]
        output = -1 * int(reveresedString)
    else:
        output = int(str(X)[::-1])
    
    return output
    
#If input is expected to be int, how can it be negative. Input has to be int, not a string