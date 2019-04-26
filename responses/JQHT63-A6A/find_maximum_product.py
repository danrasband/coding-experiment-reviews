# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    # write your code in Python
    ans = 1
    if X > len(B) | len(B) == 0:
        return 0
    else:
        for i in range(X):
            ans *= B[::-1][i]
        return ans
    pass