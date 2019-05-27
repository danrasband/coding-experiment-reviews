# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python
    csum=0
    for ele in list(S.split(",")):
        csum = csum + int(ele)
    return csum