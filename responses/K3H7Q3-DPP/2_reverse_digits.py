# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X):
    # write your code in Python
    ans = str(X)
    if ans[0] == "-":
        return int("-" + ans[:0:-1])
    else:
        return int(ans[::-1])
    pass