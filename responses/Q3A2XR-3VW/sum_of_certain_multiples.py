# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(x):
    multiples_3 = [i for i in range(0, x, 3) if i % 5 > 0]
    multiples_5 = [i for i in range(0, x, 5) if i % 3 > 0]
    return sum(multiples_3) + sum(multiples_5)
