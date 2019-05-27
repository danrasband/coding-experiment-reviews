# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    # write your code in Python
    x_string = str(X)
    solution = ""
    
    if x_string[0] == "-":
        solution = "-" + x_string[-1:0:-1]
    else:
        solution = x_string[-1::-1]
        
    return int(solution)
