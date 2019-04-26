# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    # write your code in Python
    if X > 0:
        X = str(X)[::-1]
    else:
        #X = str(X)[0:1] + str(X)[2:-1:-1]
        X = str(X)[0] + str(X)[-1:0:-1]
#    print(X)
    return(int(X))