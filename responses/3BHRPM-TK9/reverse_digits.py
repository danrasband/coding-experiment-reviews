# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    # write your code in Python
    reverse = int(str(abs(X))[::-1])
    if X < 0:
        return -reverse
    return reverse
