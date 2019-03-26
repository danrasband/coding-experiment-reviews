# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, B):
    if X > len(B) or len(B) == 0:
        return 0
    return max([pr(1, B[i: X + i]) for i in range(len(B) - X + 1)])


def pr(x, l):
    return pr(x * l.pop(), l) if l else x
