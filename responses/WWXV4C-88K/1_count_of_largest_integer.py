# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python
    arr = S.split(",")
    res = 0
    for ele in arr:
        if len(ele) == 1:
            res += int(ele)
        else:
            if ele[0] == "-":
                res -= int(ele[1:])
            else:
                res += int(ele[1:])
    return res