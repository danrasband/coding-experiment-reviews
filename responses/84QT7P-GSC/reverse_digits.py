# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    # write your code in Python
    rev_x = ""
    str_x = str(X)
   # print(str_x)
    if X >= 0 :
        rev_x = str_x[::-1]
    else :
        rev_x = str_x[0] + str_x[-1::(len(X)-1)]
   # print(rev_x)
