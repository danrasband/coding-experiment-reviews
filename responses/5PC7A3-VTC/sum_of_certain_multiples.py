# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    # write your code in Python
    res = 0
    for ele in range(x):
       if ele % 3 == 0 or ele % 5 == 0 and ele % 15 != 0:
           res += ele

    return res
