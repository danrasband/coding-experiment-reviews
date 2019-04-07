# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python
    lists = S.split(",")
    total =0
    for num in lists:
        total = total + int (num)
    return total
