# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python
    int_list = S.split(",")
    sum = 0
    for elem in int_list:
        sum += int(elem)
    return sum
