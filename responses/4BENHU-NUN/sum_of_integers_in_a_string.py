# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    y=0
    x = S.split(',')
    for i in x:
        y += int(i)
    return (y)

