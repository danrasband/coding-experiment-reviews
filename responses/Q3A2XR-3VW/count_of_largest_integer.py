# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    sorted_A = sorted(A)
    max_a = sorted_A[-1]
    c = 0
    for a in reversed(sorted_A):
        if a == max_a:
            c += 1
        else:
            break
    return c
