# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    
    max_total_so_far = 1
    
    if len(B) == 0 or X>len(B):
        return 0
    else:
        for start_i in range(len(B)):
            slice = B[start_i:start_i+X]
            if len(slice) == X:
                
                for val in slice:
                    if val != 0:
                        this_total = 1
                        this_total = this_total * val
                        if this_total > max_total_so_far:
                            max_total_so_far = this_total
    # write your code in Python
    return max_total_so_far