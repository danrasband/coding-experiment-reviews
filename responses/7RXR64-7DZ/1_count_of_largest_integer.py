# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    c=max(A)
    d=0
    for i in A:
        if i==c:
            d+=1
    return d