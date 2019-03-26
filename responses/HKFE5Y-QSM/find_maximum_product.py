# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    if not B:
        return 0

    if X > len(B):
        return 0


    max_value = 0
    index = 0
    value = 1

    for n in B:
        if index < X:
            value *= n
        else:

    # write your code in Python
    pass
