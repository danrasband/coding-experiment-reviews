# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    return sum([i for i in range(x) if (i % 3 == 0 or i % 5 == 0) and not(i % 3 == 0 and i % 5 == 0) ])