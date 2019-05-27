# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    
    highest_int = -99999999999999999
    highest_count = 0
    
    if len(A) == 0:
        return 0
    else:
        for integer in A:
            if integer > highest_int:
                highest_int = integer
                highest_count = 1
            elif integer == highest_int:
                highest_count += 1
    
    return highest_count
